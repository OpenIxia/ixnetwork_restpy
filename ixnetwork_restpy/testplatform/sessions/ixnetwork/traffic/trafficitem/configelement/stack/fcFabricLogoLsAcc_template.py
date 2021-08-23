from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FcFabricLogoLsAcc(Base):
    __slots__ = ()
    _SDM_NAME = 'fcFabricLogoLsAcc'
    _SDM_ATT_MAP = {
        'FcHeaderSof': 'fcFabricLogoLsAcc.header.fcHeader.sof-1',
        'ExtendedLinkServicesExtendedLinkServiceInfo': 'fcFabricLogoLsAcc.header.fcHeader.RCtl.extendedLinkServices.extendedLinkServiceInfo-2',
        'FcHeaderDId': 'fcFabricLogoLsAcc.header.fcHeader.DId-3',
        'FcHeaderCsCtlPriority': 'fcFabricLogoLsAcc.header.fcHeader.CsCtlPriority-4',
        'FcHeaderSId': 'fcFabricLogoLsAcc.header.fcHeader.SId-5',
        'FcHeaderType': 'fcFabricLogoLsAcc.header.fcHeader.Type-6',
        'FCtlExchangeContext': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.exchangeContext-7',
        'FCtlSequenceContext': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.sequenceContext-8',
        'FCtlFirstSequence': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.firstSequence-9',
        'FCtlLastSequence': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.lastSequence-10',
        'FCtlEndSequence': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.endSequence-11',
        'FCtlEndConnection': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.endConnection-12',
        'FCtlCsCtlPriority': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.csCtlPriority-13',
        'FCtlSequenceInitiative': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.sequenceInitiative-14',
        'FCtlFcXidReassigned': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.fcXidReassigned-15',
        'FCtlFcInvalidateXid': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.fcInvalidateXid-16',
        'FCtlAckForm': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.ackForm-17',
        'FCtlFcDataCompression': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.fcDataCompression-18',
        'FCtlFcDataEncryption': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.fcDataEncryption-19',
        'FCtlRetransmittedSequence': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.retransmittedSequence-20',
        'FCtlUnidirectionalTransmit': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.unidirectionalTransmit-21',
        'FCtlContinueSeqCondition': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.continueSeqCondition-22',
        'FCtlAbortSeqCondition': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.abortSeqCondition-23',
        'FCtlRelativeOffsetPresent': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.relativeOffsetPresent-24',
        'FCtlExchangeReassembly': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.exchangeReassembly-25',
        'FCtlFillBytes': 'fcFabricLogoLsAcc.header.fcHeader.FCtl.fCtl.fillBytes-26',
        'FcHeaderSeqId': 'fcFabricLogoLsAcc.header.fcHeader.SeqId-27',
        'FcHeaderDfCtl': 'fcFabricLogoLsAcc.header.fcHeader.DfCtl-28',
        'FcHeaderSeqCnt': 'fcFabricLogoLsAcc.header.fcHeader.SeqCnt-29',
        'FcHeaderOxId': 'fcFabricLogoLsAcc.header.fcHeader.OxId-30',
        'FcHeaderRxId': 'fcFabricLogoLsAcc.header.fcHeader.RxId-31',
        'FcHeaderParameter': 'fcFabricLogoLsAcc.header.fcHeader.Parameter-32',
        'FcElsCommandCodeFcElsCommandCodeLsAcc': 'fcFabricLogoLsAcc.header.FcEls.FcElsAcceptReject.FcElsCommandCode.FcElsCommandCodeLsAcc-33',
        'FcElsAcceptRejectFcElsAcceptRejectReserved': 'fcFabricLogoLsAcc.header.FcEls.FcElsAcceptReject.FcElsAcceptRejectReserved-34',
    }

    def __init__(self, parent, list_op=False):
        super(FcFabricLogoLsAcc, self).__init__(parent, list_op)

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
        Default Value: 35
        Value Format: decimal
        Available enum values: Solicited Data, 33, Request, 34, Reply, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtendedLinkServicesExtendedLinkServiceInfo']))

    @property
    def FcHeaderDId(self):
        """
        Display Name: D_ID
        Default Value: 0x000001
        Value Format: hex
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
        Default Value: 0xFFFFFE
        Value Format: hex
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
        Default Value: 0
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
        Default Value: 0
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
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCtlCsCtlPriority']))

    @property
    def FCtlSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 0
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
        Display Name: ACK_Form
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
        Default Value: 0x00
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
        Default Value: 0x0000
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
    def FcElsCommandCodeFcElsCommandCodeLsAcc(self):
        """
        Display Name: LS_ACC
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsCommandCodeFcElsCommandCodeLsAcc']))

    @property
    def FcElsAcceptRejectFcElsAcceptRejectReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcElsAcceptRejectFcElsAcceptRejectReserved']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
