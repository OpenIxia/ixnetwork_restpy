from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipFlogiLsRjtFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipFlogiLsRjtFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipFlogiLsRjtFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipFlogiLsRjtFcf.header.fipReserved-2",
        "FipOperationCodeFipVirtualLinkInstantiation": "fipFlogiLsRjtFcf.header.fipOperation.fipOperationCode.fipVirtualLinkInstantiation-3",
        "FipOperationFipOperationReserved1": "fipFlogiLsRjtFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipFlogiLsRjtFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipFlogiLsRjtFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipFlogiLsRjtFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipFlogiLsRjtFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipFlogiLsRjtFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipFlogiLsRjtFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipFlogiLsRjtFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipFlogiLsRjtFcf.header.fipOperation.fipFBit-12",
        "FipFlogiDescriptorFipFlogiDescriptorType": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorType-13",
        "FipFlogiDescriptorFipFlogiDescriptorLength": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorLength-14",
        "FipFlogiDescriptorFipFlogiDescriptorReserved": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorReserved-15",
        "ExtendedLinkServicesExtendedLinkServiceInfo": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelRCtl.extendedLinkServices.extendedLinkServiceInfo-16",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDId": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelDId-17",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelCsCtlPriority": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelCsCtlPriority-18",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSId": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelSId-19",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelType": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelType-20",
        "FCtlExchangeContext": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.exchangeContext-21",
        "FCtlSequenceContext": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.sequenceContext-22",
        "FCtlFirstSequence": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.firstSequence-23",
        "FCtlLastSequence": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.lastSequence-24",
        "FCtlEndSequence": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.endSequence-25",
        "FCtlEndConnection": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.endConnection-26",
        "FCtlCsCtlPriority": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.csCtlPriority-27",
        "FCtlSequenceInitiative": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.sequenceInitiative-28",
        "FCtlFcXidReassigned": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcXidReassigned-29",
        "FCtlFcInvalidateXid": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcInvalidateXid-30",
        "FCtlAckForm": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.ackForm-31",
        "FCtlFcDataCompression": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcDataCompression-32",
        "FCtlFcDataEncryption": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fcDataEncryption-33",
        "FCtlRetransmittedSequence": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.retransmittedSequence-34",
        "FCtlUnidirectionalTransmit": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.unidirectionalTransmit-35",
        "FCtlContinueSeqCondition": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.continueSeqCondition-36",
        "FCtlAbortSeqCondition": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.abortSeqCondition-37",
        "FCtlRelativeOffsetPresent": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.relativeOffsetPresent-38",
        "FCtlExchangeReassembly": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.exchangeReassembly-39",
        "FCtlFillBytes": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelFCtl.fCtl.fillBytes-40",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqId": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelSeqId-41",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDfCtl": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelDfCtl-42",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqCnt": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelSeqCnt-43",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelOxId": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelOxId-44",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelRxId": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelRxId-45",
        "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelParameter": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiFibreChannel.fipFlogiDescriptorFibreChannelParameter-46",
        "FipFlogiDescriptorFcElsCommandCodeFipFlogiDescriptorFcElsCommandCodeLsRjt": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsCommandCode.fipFlogiDescriptorFcElsCommandCodeLsRjt-47",
        "FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsAcceptRejectReserved": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsAcceptRejectReserved-48",
        "FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsLsRjtReasonCodes": "fipFlogiLsRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipFlogiDescriptor.fipFlogiDescriptorFcEls.fipFlogiDescriptorFcElsAcceptReject.fipFlogiDescriptorFcElsLsRjtReasonCodes-49",
    }

    def __init__(self, parent, list_op=False):
        super(FipFlogiLsRjtFcf, self).__init__(parent, list_op)

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
        Default Value: 9
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
    def FipFlogiDescriptorFipFlogiDescriptorType(self):
        """
        Display Name: FLOGI Descriptor Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFlogiDescriptorFipFlogiDescriptorType"]
            ),
        )

    @property
    def FipFlogiDescriptorFipFlogiDescriptorLength(self):
        """
        Display Name: FLOGI Descriptor Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFlogiDescriptorFipFlogiDescriptorLength"]
            ),
        )

    @property
    def FipFlogiDescriptorFipFlogiDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipFlogiDescriptorFipFlogiDescriptorReserved"]
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
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDId(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDId"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelCsCtlPriority(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelCsCtlPriority"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSId(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSId"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelType(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelType"
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
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqId(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqId"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDfCtl(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelDfCtl"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqCnt(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelSeqCnt"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelOxId(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelOxId"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelRxId(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelRxId"
                ]
            ),
        )

    @property
    def FipFlogiFibreChannelFipFlogiDescriptorFibreChannelParameter(self):
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
                    "FipFlogiFibreChannelFipFlogiDescriptorFibreChannelParameter"
                ]
            ),
        )

    @property
    def FipFlogiDescriptorFcElsCommandCodeFipFlogiDescriptorFcElsCommandCodeLsRjt(self):
        """
        Display Name: LS_RJT
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipFlogiDescriptorFcElsCommandCodeFipFlogiDescriptorFcElsCommandCodeLsRjt"
                ]
            ),
        )

    @property
    def FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsAcceptRejectReserved(
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
                    "FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsAcceptRejectReserved"
                ]
            ),
        )

    @property
    def FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsLsRjtReasonCodes(
        self,
    ):
        """
        Display Name: LS_RJT Reason Codes
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipFlogiDescriptorFcElsAcceptRejectFipFlogiDescriptorFcElsLsRjtReasonCodes"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
