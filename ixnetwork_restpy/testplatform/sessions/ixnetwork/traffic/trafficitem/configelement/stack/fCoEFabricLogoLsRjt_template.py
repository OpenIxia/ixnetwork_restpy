from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoEFabricLogoLsRjt(Base):
    __slots__ = ()
    _SDM_NAME = "fCoEFabricLogoLsRjt"
    _SDM_ATT_MAP = {
        "FcoeHeaderVersion": "fCoEFabricLogoLsRjt.header.fcoeHeader.version-1",
        "FcoeHeaderReserved": "fCoEFabricLogoLsRjt.header.fcoeHeader.reserved-2",
        "FcoeHeaderESOF": "fCoEFabricLogoLsRjt.header.fcoeHeader.eSOF-3",
        "ExtendedLinkServicesExtendedLinkServiceInfo": "fCoEFabricLogoLsRjt.header.fcHeader.RCtl.extendedLinkServices.extendedLinkServiceInfo-4",
        "FcHeaderDId": "fCoEFabricLogoLsRjt.header.fcHeader.DId-5",
        "FcHeaderCsCtlPriority": "fCoEFabricLogoLsRjt.header.fcHeader.CsCtlPriority-6",
        "FcHeaderSId": "fCoEFabricLogoLsRjt.header.fcHeader.SId-7",
        "FcHeaderType": "fCoEFabricLogoLsRjt.header.fcHeader.Type-8",
        "FCtlExchangeContext": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.exchangeContext-9",
        "FCtlSequenceContext": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.sequenceContext-10",
        "FCtlFirstSequence": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.firstSequence-11",
        "FCtlLastSequence": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.lastSequence-12",
        "FCtlEndSequence": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.endSequence-13",
        "FCtlEndConnection": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.endConnection-14",
        "FCtlCsCtlPriority": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.csCtlPriority-15",
        "FCtlSequenceInitiative": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.sequenceInitiative-16",
        "FCtlFcXidReassigned": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.fcXidReassigned-17",
        "FCtlFcInvalidateXid": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.fcInvalidateXid-18",
        "FCtlAckForm": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.ackForm-19",
        "FCtlFcDataCompression": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.fcDataCompression-20",
        "FCtlFcDataEncryption": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.fcDataEncryption-21",
        "FCtlRetransmittedSequence": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.retransmittedSequence-22",
        "FCtlUnidirectionalTransmit": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.unidirectionalTransmit-23",
        "FCtlContinueSeqCondition": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.continueSeqCondition-24",
        "FCtlAbortSeqCondition": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.abortSeqCondition-25",
        "FCtlRelativeOffsetPresent": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.relativeOffsetPresent-26",
        "FCtlExchangeReassembly": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.exchangeReassembly-27",
        "FCtlFillBytes": "fCoEFabricLogoLsRjt.header.fcHeader.FCtl.fCtl.fillBytes-28",
        "FcHeaderSeqId": "fCoEFabricLogoLsRjt.header.fcHeader.SeqId-29",
        "FcHeaderDfCtl": "fCoEFabricLogoLsRjt.header.fcHeader.DfCtl-30",
        "FcHeaderSeqCnt": "fCoEFabricLogoLsRjt.header.fcHeader.SeqCnt-31",
        "FcHeaderOxId": "fCoEFabricLogoLsRjt.header.fcHeader.OxId-32",
        "FcHeaderRxId": "fCoEFabricLogoLsRjt.header.fcHeader.RxId-33",
        "FcHeaderParameter": "fCoEFabricLogoLsRjt.header.fcHeader.Parameter-34",
        "FcElsCommandCodeFcElsCommandCodeLsRjt": "fCoEFabricLogoLsRjt.header.FcEls.FcElsAcceptReject.FcElsCommandCode.FcElsCommandCodeLsRjt-35",
        "FcElsAcceptRejectFcElsAcceptRejectReserved": "fCoEFabricLogoLsRjt.header.FcEls.FcElsAcceptReject.FcElsAcceptRejectReserved-36",
        "FcElsAcceptRejectFcElsLsRjtReasonCodes": "fCoEFabricLogoLsRjt.header.FcEls.FcElsAcceptReject.FcElsLsRjtReasonCodes-37",
    }

    def __init__(self, parent, list_op=False):
        super(FCoEFabricLogoLsRjt, self).__init__(parent, list_op)

    @property
    def FcoeHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderVersion"])
        )

    @property
    def FcoeHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderReserved"])
        )

    @property
    def FcoeHeaderESOF(self):
        """
        Display Name: E-SOF
        Default Value: 54
        Value Format: decimal
        Available enum values: SOFf - Fabric, 40, SOFi4 - Initiate Class 4, 41, SOFi2 - Initiate Class 2, 45, SOFi3 - Initiate Class 3, 46, SOFn4 - Normal Class 4, 49, SOFn2 - Normal Class 2, 53, SOFn3 - Normal Class 3, 54, SOFc4 - Connect Class 4, 57, SOFn1 - Normal Class 1 or 6, 250
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderESOF"])
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
    def FcHeaderDId(self):
        """
        Display Name: D_ID
        Default Value: 0x000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDId"]))

    @property
    def FcHeaderCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderCsCtlPriority"])
        )

    @property
    def FcHeaderSId(self):
        """
        Display Name: S_ID
        Default Value: 0xFFFFFE
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSId"]))

    @property
    def FcHeaderType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderType"]))

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
    def FcHeaderSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqId"]))

    @property
    def FcHeaderDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDfCtl"]))

    @property
    def FcHeaderSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqCnt"])
        )

    @property
    def FcHeaderOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderOxId"]))

    @property
    def FcHeaderRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderRxId"]))

    @property
    def FcHeaderParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderParameter"])
        )

    @property
    def FcElsCommandCodeFcElsCommandCodeLsRjt(self):
        """
        Display Name: LS_RJT
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsCommandCodeFcElsCommandCodeLsRjt"]
            ),
        )

    @property
    def FcElsAcceptRejectFcElsAcceptRejectReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsAcceptRejectFcElsAcceptRejectReserved"]
            ),
        )

    @property
    def FcElsAcceptRejectFcElsLsRjtReasonCodes(self):
        """
        Display Name: LS_RJT Reason Codes
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsAcceptRejectFcElsLsRjtReasonCodes"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
