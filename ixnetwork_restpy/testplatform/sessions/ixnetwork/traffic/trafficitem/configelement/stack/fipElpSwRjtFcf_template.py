from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipElpSwRjtFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipElpSwRjtFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipElpSwRjtFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipElpSwRjtFcf.header.fipReserved-2",
        "FipOperationCodeFipVirtualLinkInstantiation": "fipElpSwRjtFcf.header.fipOperation.fipOperationCode.fipVirtualLinkInstantiation-3",
        "FipOperationFipOperationReserved1": "fipElpSwRjtFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipElpSwRjtFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipElpSwRjtFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipElpSwRjtFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipElpSwRjtFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipElpSwRjtFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipElpSwRjtFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipElpSwRjtFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipElpSwRjtFcf.header.fipOperation.fipFBit-12",
        "FipElpDescriptorFipElpDescriptorType": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorType-13",
        "FipElpDescriptorFipElpDescriptorLength": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorLength-14",
        "FipElpDescriptorFipElpDescriptorReserved": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorReserved-15",
        "FipElpDescriptorFibreChannelRCtlExchangeLinkParametersFipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelRCtl.fipElpDescriptorFibreChannelRCtlExchangeLinkParameters.fipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply-16",
        "FipElpFibreChannelFipElpDescriptorFibreChannelDId": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelDId-17",
        "FipElpFibreChannelFipElpDescriptorFibreChannelCsCtlPriority": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelCsCtlPriority-18",
        "FipElpFibreChannelFipElpDescriptorFibreChannelSId": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelSId-19",
        "FipElpFibreChannelFipElpDescriptorFibreChannelType": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelType-20",
        "FCtlExchangeContext": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.exchangeContext-21",
        "FCtlSequenceContext": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.sequenceContext-22",
        "FCtlFirstSequence": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.firstSequence-23",
        "FCtlLastSequence": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.lastSequence-24",
        "FCtlEndSequence": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.endSequence-25",
        "FCtlEndConnection": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.endConnection-26",
        "FCtlCsCtlPriority": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.csCtlPriority-27",
        "FCtlSequenceInitiative": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.sequenceInitiative-28",
        "FCtlFcXidReassigned": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcXidReassigned-29",
        "FCtlFcInvalidateXid": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcInvalidateXid-30",
        "FCtlAckForm": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.ackForm-31",
        "FCtlFcDataCompression": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcDataCompression-32",
        "FCtlFcDataEncryption": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcDataEncryption-33",
        "FCtlRetransmittedSequence": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.retransmittedSequence-34",
        "FCtlUnidirectionalTransmit": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.unidirectionalTransmit-35",
        "FCtlContinueSeqCondition": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.continueSeqCondition-36",
        "FCtlAbortSeqCondition": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.abortSeqCondition-37",
        "FCtlRelativeOffsetPresent": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.relativeOffsetPresent-38",
        "FCtlExchangeReassembly": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.exchangeReassembly-39",
        "FCtlFillBytes": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fillBytes-40",
        "FipElpFibreChannelFipElpDescriptorFibreChannelSeqId": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelSeqId-41",
        "FipElpFibreChannelFipElpDescriptorFibreChannelDfCtl": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelDfCtl-42",
        "FipElpFibreChannelFipElpDescriptorFibreChannelSeqCnt": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelSeqCnt-43",
        "FipElpFibreChannelFipElpDescriptorFibreChannelOxId": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelOxId-44",
        "FipElpFibreChannelFipElpDescriptorFibreChannelRxId": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelRxId-45",
        "FipElpFibreChannelFipElpDescriptorFibreChannelParameter": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelParameter-46",
        "FipElpDescriptorFcElpCommandCodeFipElpDescriptorFcElpCommandCodeExchangeLinkParametersReject": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommandCode.fipElpDescriptorFcElpCommandCodeExchangeLinkParametersReject-47",
        "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpSwRjtReasonCodes": "fipElpSwRjtFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpSwRjtReasonCodes-48",
    }

    def __init__(self, parent, list_op=False):
        super(FipElpSwRjtFcf, self).__init__(parent, list_op)

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
    def FipElpDescriptorFipElpDescriptorType(self):
        """
        Display Name: ELP Descriptor Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpDescriptorFipElpDescriptorType"]
            ),
        )

    @property
    def FipElpDescriptorFipElpDescriptorLength(self):
        """
        Display Name: ELP Descriptor Length
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpDescriptorFipElpDescriptorLength"]
            ),
        )

    @property
    def FipElpDescriptorFipElpDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpDescriptorFipElpDescriptorReserved"]
            ),
        )

    @property
    def FipElpDescriptorFibreChannelRCtlExchangeLinkParametersFipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply(
        self,
    ):
        """
        Display Name: Request/Reply
        Default Value: 3
        Value Format: decimal
        Available enum values: Request, 2, Reply, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFibreChannelRCtlExchangeLinkParametersFipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply"
                ]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelDId(self):
        """
        Display Name: D_ID
        Default Value: 0xFFFFFD
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelDId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelCsCtlPriority(self):
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
                    "FipElpFibreChannelFipElpDescriptorFibreChannelCsCtlPriority"
                ]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelSId(self):
        """
        Display Name: S_ID
        Default Value: 0xFFFFFD
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelSId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x22
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelType"]
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
    def FCtlCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlCsCtlPriority"])
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
    def FipElpFibreChannelFipElpDescriptorFibreChannelSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelSeqId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelDfCtl"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelSeqCnt(self):
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
                    "FipElpFibreChannelFipElpDescriptorFibreChannelSeqCnt"
                ]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelOxId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelRxId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelParameter(self):
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
                    "FipElpFibreChannelFipElpDescriptorFibreChannelParameter"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommandCodeFipElpDescriptorFcElpCommandCodeExchangeLinkParametersReject(
        self,
    ):
        """
        Display Name: ELP Reject
        Default Value: 0x01000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommandCodeFipElpDescriptorFcElpCommandCodeExchangeLinkParametersReject"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpSwRjtReasonCodes(self):
        """
        Display Name: ELP SW_RJT Reason Codes
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpSwRjtReasonCodes"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
