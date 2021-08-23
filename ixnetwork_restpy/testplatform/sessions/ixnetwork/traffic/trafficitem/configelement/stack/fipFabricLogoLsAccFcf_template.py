from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipFabricLogoLsAccFcf(Base):
    __slots__ = ()
    _SDM_NAME = 'fipFabricLogoLsAccFcf'
    _SDM_ATT_MAP = {
        'HeaderFipVersion': 'fipFabricLogoLsAccFcf.header.fipVersion-1',
        'HeaderFipReserved': 'fipFabricLogoLsAccFcf.header.fipReserved-2',
        'FipOperationCodeFipVirtualLinkInstantiation': 'fipFabricLogoLsAccFcf.header.fipOperation.fipOperationCode.fipVirtualLinkInstantiation-3',
        'FipOperationFipOperationReserved1': 'fipFabricLogoLsAccFcf.header.fipOperation.fipOperationReserved1-4',
        'FipSubcodeFipSubcode02h': 'fipFabricLogoLsAccFcf.header.fipOperation.fipSubcode.fipSubcode02h-5',
        'FipOperationFipDescriptorListLength': 'fipFabricLogoLsAccFcf.header.fipOperation.fipDescriptorListLength-6',
        'FipOperationFipFp': 'fipFabricLogoLsAccFcf.header.fipOperation.fipFp-7',
        'FipOperationFipSp': 'fipFabricLogoLsAccFcf.header.fipOperation.fipSp-8',
        'FipOperationFipReserved2': 'fipFabricLogoLsAccFcf.header.fipOperation.fipReserved2-9',
        'FipOperationFipABit': 'fipFabricLogoLsAccFcf.header.fipOperation.fipABit-10',
        'FipOperationFipSBit': 'fipFabricLogoLsAccFcf.header.fipOperation.fipSBit-11',
        'FipOperationFipFBit': 'fipFabricLogoLsAccFcf.header.fipOperation.fipFBit-12',
        'FipLogoDescriptorFipLogoDescriptorType': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoDescriptorType-13',
        'FipLogoDescriptorFipLogoDescriptorLength': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoDescriptorLength-14',
        'FipLogoDescriptorFipLogoDescriptorReserved': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoDescriptorReserved-15',
        'ExtendedLinkServicesExtendedLinkServiceInfo': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelRCtl.extendedLinkServices.extendedLinkServiceInfo-16',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelDId': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelDId-17',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelCsCtlPriority': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelCsCtlPriority-18',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelSId': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelSId-19',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelType': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelType-20',
        'FCtlExchangeContext': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.exchangeContext-21',
        'FCtlSequenceContext': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.sequenceContext-22',
        'FCtlFirstSequence': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.firstSequence-23',
        'FCtlLastSequence': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.lastSequence-24',
        'FCtlEndSequence': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.endSequence-25',
        'FCtlEndConnection': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.endConnection-26',
        'FCtlCsCtlPriority': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.csCtlPriority-27',
        'FCtlSequenceInitiative': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.sequenceInitiative-28',
        'FCtlFcXidReassigned': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.fcXidReassigned-29',
        'FCtlFcInvalidateXid': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.fcInvalidateXid-30',
        'FCtlAckForm': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.ackForm-31',
        'FCtlFcDataCompression': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.fcDataCompression-32',
        'FCtlFcDataEncryption': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.fcDataEncryption-33',
        'FCtlRetransmittedSequence': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.retransmittedSequence-34',
        'FCtlUnidirectionalTransmit': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.unidirectionalTransmit-35',
        'FCtlContinueSeqCondition': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.continueSeqCondition-36',
        'FCtlAbortSeqCondition': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.abortSeqCondition-37',
        'FCtlRelativeOffsetPresent': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.relativeOffsetPresent-38',
        'FCtlExchangeReassembly': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.exchangeReassembly-39',
        'FCtlFillBytes': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelFCtl.fCtl.fillBytes-40',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelSeqId': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelSeqId-41',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelDfCtl': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelDfCtl-42',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelSeqCnt': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelSeqCnt-43',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelOxId': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelOxId-44',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelRxId': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelRxId-45',
        'FipLogoFibreChannelFipLogoDescriptorFibreChannelParameter': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoFibreChannel.fipLogoDescriptorFibreChannelParameter-46',
        'FipLogoDescriptorFcElsCommandCodeFipLogoDescriptorFcElsCommandCodeLsAcc': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoDescriptorFcEls.fipLogoDescriptorFcElsAcceptReject.fipLogoDescriptorFcElsCommandCode.fipLogoDescriptorFcElsCommandCodeLsAcc-47',
        'FipLogoDescriptorFcElsAcceptRejectFipLogoDescriptorFcElsAcceptRejectReserved': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipLogoDescriptor.fipLogoDescriptorFcEls.fipLogoDescriptorFcElsAcceptReject.fipLogoDescriptorFcElsAcceptRejectReserved-48',
        'FipMacAddressDescriptorFipMacAddressDescriptorType': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-49',
        'FipMacAddressDescriptorFipMacAddressDescriptorLength': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-50',
        'FipMacAddressDescriptorFipMacAddressDescriptorValue': 'fipFabricLogoLsAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-51',
    }

    def __init__(self, parent, list_op=False):
        super(FipFabricLogoLsAccFcf, self).__init__(parent, list_op)

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
        Default Value: 10
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
    def FipLogoDescriptorFipLogoDescriptorType(self):
        """
        Display Name: LOGO Descriptor Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoDescriptorFipLogoDescriptorType']))

    @property
    def FipLogoDescriptorFipLogoDescriptorLength(self):
        """
        Display Name: LOGO Descriptor Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoDescriptorFipLogoDescriptorLength']))

    @property
    def FipLogoDescriptorFipLogoDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoDescriptorFipLogoDescriptorReserved']))

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
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelDId(self):
        """
        Display Name: D_ID
        Default Value: 0x000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelDId']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelCsCtlPriority']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelSId(self):
        """
        Display Name: S_ID
        Default Value: 0xFFFFFE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelSId']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelType']))

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
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelSeqId']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelDfCtl']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelSeqCnt']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelOxId']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelRxId']))

    @property
    def FipLogoFibreChannelFipLogoDescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoFibreChannelFipLogoDescriptorFibreChannelParameter']))

    @property
    def FipLogoDescriptorFcElsCommandCodeFipLogoDescriptorFcElsCommandCodeLsAcc(self):
        """
        Display Name: LS_ACC
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoDescriptorFcElsCommandCodeFipLogoDescriptorFcElsCommandCodeLsAcc']))

    @property
    def FipLogoDescriptorFcElsAcceptRejectFipLogoDescriptorFcElsAcceptRejectReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FipLogoDescriptorFcElsAcceptRejectFipLogoDescriptorFcElsAcceptRejectReserved']))

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
