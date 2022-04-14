from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FcScrRequest(Base):
    __slots__ = ()
    _SDM_NAME = "fcScrRequest"
    _SDM_ATT_MAP = {
        "FcHeaderSof": "fcScrRequest.header.fcHeader.sof-1",
        "ExtendedLinkServicesExtendedLinkServiceInfo": "fcScrRequest.header.fcHeader.RCtl.extendedLinkServices.extendedLinkServiceInfo-2",
        "FcHeaderDId": "fcScrRequest.header.fcHeader.DId-3",
        "FcHeaderCsCtlPriority": "fcScrRequest.header.fcHeader.CsCtlPriority-4",
        "FcHeaderSId": "fcScrRequest.header.fcHeader.SId-5",
        "FcHeaderType": "fcScrRequest.header.fcHeader.Type-6",
        "FCtlExchangeContext": "fcScrRequest.header.fcHeader.FCtl.fCtl.exchangeContext-7",
        "FCtlSequenceContext": "fcScrRequest.header.fcHeader.FCtl.fCtl.sequenceContext-8",
        "FCtlFirstSequence": "fcScrRequest.header.fcHeader.FCtl.fCtl.firstSequence-9",
        "FCtlLastSequence": "fcScrRequest.header.fcHeader.FCtl.fCtl.lastSequence-10",
        "FCtlEndSequence": "fcScrRequest.header.fcHeader.FCtl.fCtl.endSequence-11",
        "FCtlEndConnection": "fcScrRequest.header.fcHeader.FCtl.fCtl.endConnection-12",
        "FCtlCsCtlPriority": "fcScrRequest.header.fcHeader.FCtl.fCtl.csCtlPriority-13",
        "FCtlSequenceInitiative": "fcScrRequest.header.fcHeader.FCtl.fCtl.sequenceInitiative-14",
        "FCtlFcXidReassigned": "fcScrRequest.header.fcHeader.FCtl.fCtl.fcXidReassigned-15",
        "FCtlFcInvalidateXid": "fcScrRequest.header.fcHeader.FCtl.fCtl.fcInvalidateXid-16",
        "FCtlAckForm": "fcScrRequest.header.fcHeader.FCtl.fCtl.ackForm-17",
        "FCtlFcDataCompression": "fcScrRequest.header.fcHeader.FCtl.fCtl.fcDataCompression-18",
        "FCtlFcDataEncryption": "fcScrRequest.header.fcHeader.FCtl.fCtl.fcDataEncryption-19",
        "FCtlRetransmittedSequence": "fcScrRequest.header.fcHeader.FCtl.fCtl.retransmittedSequence-20",
        "FCtlUnidirectionalTransmit": "fcScrRequest.header.fcHeader.FCtl.fCtl.unidirectionalTransmit-21",
        "FCtlContinueSeqCondition": "fcScrRequest.header.fcHeader.FCtl.fCtl.continueSeqCondition-22",
        "FCtlAbortSeqCondition": "fcScrRequest.header.fcHeader.FCtl.fCtl.abortSeqCondition-23",
        "FCtlRelativeOffsetPresent": "fcScrRequest.header.fcHeader.FCtl.fCtl.relativeOffsetPresent-24",
        "FCtlExchangeReassembly": "fcScrRequest.header.fcHeader.FCtl.fCtl.exchangeReassembly-25",
        "FCtlFillBytes": "fcScrRequest.header.fcHeader.FCtl.fCtl.fillBytes-26",
        "FcHeaderSeqId": "fcScrRequest.header.fcHeader.SeqId-27",
        "FcHeaderDfCtl": "fcScrRequest.header.fcHeader.DfCtl-28",
        "FcHeaderSeqCnt": "fcScrRequest.header.fcHeader.SeqCnt-29",
        "FcHeaderOxId": "fcScrRequest.header.fcHeader.OxId-30",
        "FcHeaderRxId": "fcScrRequest.header.fcHeader.RxId-31",
        "FcHeaderParameter": "fcScrRequest.header.fcHeader.Parameter-32",
        "FcElsCommandCodeFcElsCommandCodeScr": "fcScrRequest.header.FcEls.FcElsRequest.FcElsCommandCode.FcElsCommandCodeScr-33",
        "FcElsRequestFcElsRequestReserved": "fcScrRequest.header.FcEls.FcElsRequest.FcElsRequestReserved-34",
        "FcElsRequestRegistrationFunction": "fcScrRequest.header.FcEls.FcElsRequest.RegistrationFunction-35",
    }

    def __init__(self, parent, list_op=False):
        super(FcScrRequest, self).__init__(parent, list_op)

    @property
    def FcHeaderSof(self):
        """
        Display Name: SOF
        Default Value: -1128974794
        Value Format: decimal
        Available enum values: SOFf - Fabric, 3166001232, SOFi4 - Initiate Class 4, 3166001497, SOFi2 - Initiate Class 2, 3166000469, SOFi3 - Initiate Class 3, 3166000726, SOFn4 - Normal Class 4, 3165993273, SOFn2 - Normal Class 2, 3165992245, SOFn3 - Normal Class 3, 3165992502, SOFc4 - Connect Class 4, 3165985049, SOFn1 - Normal Class 1 or 6, 3165992759
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSof"]))

    @property
    def ExtendedLinkServicesExtendedLinkServiceInfo(self):
        """
        Display Name: Information
        Default Value: 34
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
        Default Value: FF.FF.FD
        Value Format: fCID
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
        Default Value: 00.00.00
        Value Format: fCID
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
    def FcHeaderSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x01
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
        Default Value: 0x0001
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
    def FcElsCommandCodeFcElsCommandCodeScr(self):
        """
        Display Name: SCR
        Default Value: 0x62
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsCommandCodeFcElsCommandCodeScr"]
            ),
        )

    @property
    def FcElsRequestFcElsRequestReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FcElsRequestFcElsRequestReserved"]),
        )

    @property
    def FcElsRequestRegistrationFunction(self):
        """
        Display Name: Registration Function
        Default Value: 1
        Value Format: decimal
        Available enum values: Fabric Detected, 1, NX Port Detected, 2, All, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FcElsRequestRegistrationFunction"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
