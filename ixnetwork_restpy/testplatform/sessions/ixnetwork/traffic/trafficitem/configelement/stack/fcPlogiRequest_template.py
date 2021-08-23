from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FcPlogiRequest(Base):
    __slots__ = ()
    _SDM_NAME = 'fcPlogiRequest'
    _SDM_ATT_MAP = {
        'FcHeaderSof': 'fcPlogiRequest.header.fcHeader.sof-1',
        'ExtendedLinkServicesExtendedLinkServiceInfo': 'fcPlogiRequest.header.fcHeader.RCtl.extendedLinkServices.extendedLinkServiceInfo-2',
        'FcHeaderDId': 'fcPlogiRequest.header.fcHeader.DId-3',
        'FcHeaderCsCtlPriority': 'fcPlogiRequest.header.fcHeader.CsCtlPriority-4',
        'FcHeaderSId': 'fcPlogiRequest.header.fcHeader.SId-5',
        'FcHeaderType': 'fcPlogiRequest.header.fcHeader.Type-6',
        'FCtlExchangeContext': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.exchangeContext-7',
        'FCtlSequenceContext': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.sequenceContext-8',
        'FCtlFirstSequence': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.firstSequence-9',
        'FCtlLastSequence': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.lastSequence-10',
        'FCtlEndSequence': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.endSequence-11',
        'FCtlEndConnection': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.endConnection-12',
        'FCtlCsCtlPriority': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.csCtlPriority-13',
        'FCtlSequenceInitiative': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.sequenceInitiative-14',
        'FCtlFcXidReassigned': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.fcXidReassigned-15',
        'FCtlFcInvalidateXid': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.fcInvalidateXid-16',
        'FCtlAckForm': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.ackForm-17',
        'FCtlFcDataCompression': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.fcDataCompression-18',
        'FCtlFcDataEncryption': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.fcDataEncryption-19',
        'FCtlRetransmittedSequence': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.retransmittedSequence-20',
        'FCtlUnidirectionalTransmit': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.unidirectionalTransmit-21',
        'FCtlContinueSeqCondition': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.continueSeqCondition-22',
        'FCtlAbortSeqCondition': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.abortSeqCondition-23',
        'FCtlRelativeOffsetPresent': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.relativeOffsetPresent-24',
        'FCtlExchangeReassembly': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.exchangeReassembly-25',
        'FCtlFillBytes': 'fcPlogiRequest.header.fcHeader.FCtl.fCtl.fillBytes-26',
        'FcHeaderSeqId': 'fcPlogiRequest.header.fcHeader.SeqId-27',
        'FcHeaderDfCtl': 'fcPlogiRequest.header.fcHeader.DfCtl-28',
        'FcHeaderSeqCnt': 'fcPlogiRequest.header.fcHeader.SeqCnt-29',
        'FcHeaderOxId': 'fcPlogiRequest.header.fcHeader.OxId-30',
        'FcHeaderRxId': 'fcPlogiRequest.header.fcHeader.RxId-31',
        'FcHeaderParameter': 'fcPlogiRequest.header.fcHeader.Parameter-32',
        'FcElsCommandCodeFcElsCommandCodePlogi': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommandCode.FcElsCommandCodePlogi-33',
        'FcElsRequestFcElsRequestReserved': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsRequestReserved-34',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersFc-phVersion': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersFc-phVersion-35',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferCredit': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersBuffer-to-bufferCredit-36',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersCommonFeatures': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersCommonFeatures-37',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersBbScNumber': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersBbScNumber-38',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize-39',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersRATov': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersRATov-40',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersEDTov': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersEDTov-41',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersNPortPortName': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersNPortPortName-42',
        'FcElsCommonServiceParametersFcElsCommonServiceParametersFabricNodeName': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsCommonServiceParameters.FcElsCommonServiceParametersFabricNodeName-43',
        'FcElsRequestFcElsClass1SvcParameters': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass1SvcParameters-44',
        'FcElsRequestFcElsClass2SvcParameters': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass2SvcParameters-45',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersServiceOptions': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersServiceOptions-46',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersInitiatorControl': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersInitiatorControl-47',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersRecipientControl': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersRecipientControl-48',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersClassReceiveSize': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersClassReceiveSize-49',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersTotalConcurrentSequence': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersTotalConcurrentSequence-50',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersEnd-to-endCredit': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersEnd-to-endCredit-51',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersOpenSeqPerExchange': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersOpenSeqPerExchange-52',
        'FcElsClass3SvcParametersFcElsClass3SvcParametersCrTov': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsClass3SvcParameters.FcElsClass3SvcParametersCrTov-53',
        'FcElsRequestClass4SvcParameters': 'fcPlogiRequest.header.FcEls.FcElsRequest.Class4SvcParameters-54',
        'FcElsRequestFcElsVendorVersion': 'fcPlogiRequest.header.FcEls.FcElsRequest.FcElsVendorVersion-55',
    }

    def __init__(self, parent, list_op=False):
        super(FcPlogiRequest, self).__init__(parent, list_op)

    @property
    def FcHeaderSof(self):
        """
        Display Name: SOF
        Default Value: -1128974794
        Value Format: decimal
        Available enum values: SOFf - Fabric, 3166001232, SOFi4 - Initiate Class 4, 3166001497, SOFi2 - Initiate Class 2, 3166000469, SOFi3 - Initiate Class 3, 3166000726, SOFn4 - Normal Class 4, 3165993273, SOFn2 - Normal Class 2, 3165992245, SOFn3 - Normal Class 3, 3165992502, SOFc4 - Connect Class 4, 3165985049, SOFn1 - Normal Class 1 or 6, 3165992759
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSof']))

    @property
    def ExtendedLinkServicesExtendedLinkServiceInfo(self):
        """
        Display Name: Information
        Default Value: 34
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtendedLinkServicesExtendedLinkServiceInfo']))

    @property
    def FcHeaderDId(self):
        """
        Display Name: D_ID
        Default Value: FF.FF.FE
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderDId']))

    @property
    def FcHeaderCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderCsCtlPriority']))

    @property
    def FcHeaderSId(self):
        """
        Display Name: S_ID
        Default Value: 00.00.00
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSId']))

    @property
    def FcHeaderType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderType']))

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
    def FcHeaderSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSeqId']))

    @property
    def FcHeaderDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderDfCtl']))

    @property
    def FcHeaderSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSeqCnt']))

    @property
    def FcHeaderOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderOxId']))

    @property
    def FcHeaderRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderRxId']))

    @property
    def FcHeaderParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderParameter']))

    @property
    def FcElsCommandCodeFcElsCommandCodePlogi(self):
        """
        Display Name: PLOGI
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommandCodeFcElsCommandCodePlogi']))

    @property
    def FcElsRequestFcElsRequestReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsRequestFcElsRequestReserved']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersFcphVersion(self):
        """
        Display Name: FC-PH Version
        Default Value: 0x2020
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersFc-phVersion']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersBuffertobufferCredit(self):
        """
        Display Name: Buffer-to-Buffer Credit
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferCredit']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersCommonFeatures(self):
        """
        Display Name: Common Features
        Default Value: 0x8000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersCommonFeatures']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersBbScNumber(self):
        """
        Display Name: BB_SC_Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersBbScNumber']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersBuffertobufferReceiveDataFieldSize(self):
        """
        Display Name: Buffer-to-Buffer Receive Data Field Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersBuffer-to-bufferReceiveDataFieldSize']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersRATov(self):
        """
        Display Name: R_A_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersRATov']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersEDTov(self):
        """
        Display Name: E_D_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersEDTov']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersNPortPortName(self):
        """
        Display Name: N_Port Port Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersNPortPortName']))

    @property
    def FcElsCommonServiceParametersFcElsCommonServiceParametersFabricNodeName(self):
        """
        Display Name: Fabric/Node Name
        Default Value: 0x1000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommonServiceParametersFcElsCommonServiceParametersFabricNodeName']))

    @property
    def FcElsRequestFcElsClass1SvcParameters(self):
        """
        Display Name: Class 1 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsRequestFcElsClass1SvcParameters']))

    @property
    def FcElsRequestFcElsClass2SvcParameters(self):
        """
        Display Name: Class 2 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsRequestFcElsClass2SvcParameters']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersServiceOptions(self):
        """
        Display Name: Service Options
        Default Value: 0x8800
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersServiceOptions']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersInitiatorControl(self):
        """
        Display Name: Initiator Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersInitiatorControl']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersRecipientControl(self):
        """
        Display Name: Recipient Control
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersRecipientControl']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersClassReceiveSize(self):
        """
        Display Name: Class Receive Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersClassReceiveSize']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersTotalConcurrentSequence(self):
        """
        Display Name: Total Concurrent Sequence
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersTotalConcurrentSequence']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersEndtoendCredit(self):
        """
        Display Name: End-to-End Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersEnd-to-endCredit']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersOpenSeqPerExchange(self):
        """
        Display Name: Open Seq Per Exchange
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersOpenSeqPerExchange']))

    @property
    def FcElsClass3SvcParametersFcElsClass3SvcParametersCrTov(self):
        """
        Display Name: CR_TOV
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsClass3SvcParametersFcElsClass3SvcParametersCrTov']))

    @property
    def FcElsRequestClass4SvcParameters(self):
        """
        Display Name: Class 4 Svc Parameters
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsRequestClass4SvcParameters']))

    @property
    def FcElsRequestFcElsVendorVersion(self):
        """
        Display Name: Vendor Version
        Default Value: 0x00000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsRequestFcElsVendorVersion']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
