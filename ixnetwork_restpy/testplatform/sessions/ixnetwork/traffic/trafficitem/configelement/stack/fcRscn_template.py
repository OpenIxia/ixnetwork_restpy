from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FcRscn(Base):
    __slots__ = ()
    _SDM_NAME = "fcRscn"
    _SDM_ATT_MAP = {
        "FcHeaderSof": "fcRscn.header.fcHeader.sof-1",
        "ExtendedLinkServicesExtendedLinkServiceInfo": "fcRscn.header.fcHeader.RCtl.extendedLinkServices.extendedLinkServiceInfo-2",
        "FcHeaderDId": "fcRscn.header.fcHeader.DId-3",
        "FcHeaderCsCtlPriority": "fcRscn.header.fcHeader.CsCtlPriority-4",
        "FcHeaderSId": "fcRscn.header.fcHeader.SId-5",
        "FcHeaderType": "fcRscn.header.fcHeader.Type-6",
        "FCtlExchangeContext": "fcRscn.header.fcHeader.FCtl.fCtl.exchangeContext-7",
        "FCtlSequenceContext": "fcRscn.header.fcHeader.FCtl.fCtl.sequenceContext-8",
        "FCtlFirstSequence": "fcRscn.header.fcHeader.FCtl.fCtl.firstSequence-9",
        "FCtlLastSequence": "fcRscn.header.fcHeader.FCtl.fCtl.lastSequence-10",
        "FCtlEndSequence": "fcRscn.header.fcHeader.FCtl.fCtl.endSequence-11",
        "FCtlEndConnection": "fcRscn.header.fcHeader.FCtl.fCtl.endConnection-12",
        "FCtlCsCtlPriority": "fcRscn.header.fcHeader.FCtl.fCtl.csCtlPriority-13",
        "FCtlSequenceInitiative": "fcRscn.header.fcHeader.FCtl.fCtl.sequenceInitiative-14",
        "FCtlFcXidReassigned": "fcRscn.header.fcHeader.FCtl.fCtl.fcXidReassigned-15",
        "FCtlFcInvalidateXid": "fcRscn.header.fcHeader.FCtl.fCtl.fcInvalidateXid-16",
        "FCtlAckForm": "fcRscn.header.fcHeader.FCtl.fCtl.ackForm-17",
        "FCtlFcDataCompression": "fcRscn.header.fcHeader.FCtl.fCtl.fcDataCompression-18",
        "FCtlFcDataEncryption": "fcRscn.header.fcHeader.FCtl.fCtl.fcDataEncryption-19",
        "FCtlRetransmittedSequence": "fcRscn.header.fcHeader.FCtl.fCtl.retransmittedSequence-20",
        "FCtlUnidirectionalTransmit": "fcRscn.header.fcHeader.FCtl.fCtl.unidirectionalTransmit-21",
        "FCtlContinueSeqCondition": "fcRscn.header.fcHeader.FCtl.fCtl.continueSeqCondition-22",
        "FCtlAbortSeqCondition": "fcRscn.header.fcHeader.FCtl.fCtl.abortSeqCondition-23",
        "FCtlRelativeOffsetPresent": "fcRscn.header.fcHeader.FCtl.fCtl.relativeOffsetPresent-24",
        "FCtlExchangeReassembly": "fcRscn.header.fcHeader.FCtl.fCtl.exchangeReassembly-25",
        "FCtlFillBytes": "fcRscn.header.fcHeader.FCtl.fCtl.fillBytes-26",
        "FcHeaderSeqId": "fcRscn.header.fcHeader.SeqId-27",
        "FcHeaderDfCtl": "fcRscn.header.fcHeader.DfCtl-28",
        "FcHeaderSeqCnt": "fcRscn.header.fcHeader.SeqCnt-29",
        "FcHeaderOxId": "fcRscn.header.fcHeader.OxId-30",
        "FcHeaderRxId": "fcRscn.header.fcHeader.RxId-31",
        "FcHeaderParameter": "fcRscn.header.fcHeader.Parameter-32",
        "FcElsCommandCodeFcElsCommandCodeRscn": "fcRscn.header.FcEls.FcElsRequest.FcElsCommandCode.FcElsCommandCodeRscn-33",
        "FcElsRequestFcElsRequestPageLength": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPageLength-34",
        "FcElsRequestFcElsRequestPayloadLength": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPayloadLength-35",
        "FcElsRequestPortIDPageReserved": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPortIDPage.reserved-36",
        "FcElsRequestPortIDPageRscnEventQualifier": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPortIDPage.rscnEventQualifier-37",
        "FcElsRequestPortIDPageAddressFormat": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPortIDPage.addressFormat-38",
        "FcElsRequestPortIDPageDomain": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPortIDPage.domain-39",
        "FcElsRequestPortIDPageArea": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPortIDPage.area-40",
        "FcElsRequestPortIDPagePort": "fcRscn.header.FcEls.FcElsRequest.FcElsRequestPortIDPage.port-41",
    }

    def __init__(self, parent, list_op=False):
        super(FcRscn, self).__init__(parent, list_op)

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
        Default Value: FF.FF.FE
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
    def FcElsCommandCodeFcElsCommandCodeRscn(self):
        """
        Display Name: RSCN
        Default Value: 0x61
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsCommandCodeFcElsCommandCodeRscn"]
            ),
        )

    @property
    def FcElsRequestFcElsRequestPageLength(self):
        """
        Display Name: Page Length
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestFcElsRequestPageLength"]
            ),
        )

    @property
    def FcElsRequestFcElsRequestPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0x0008
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestFcElsRequestPayloadLength"]
            ),
        )

    @property
    def FcElsRequestPortIDPageReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FcElsRequestPortIDPageReserved"]),
        )

    @property
    def FcElsRequestPortIDPageRscnEventQualifier(self):
        """
        Display Name: RSCN Event Qualifier
        Default Value: 0
        Value Format: decimal
        Available enum values: Event Not Specified, 0, Changed Name Server Object, 1, Changed Port Attribute, 2, Changed Service Object, 3, Reserved1, 4, Reserved2, 5, Reserved3, 6, Reserved4, 7, Changed Switch Configuration, 8, Removed Object, 9, Reserved5, 10, Reserved6, 11, Reserved7, 12, Reserved8, 13, Reserved9, 14, Reserved10, 15
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestPortIDPageRscnEventQualifier"]
            ),
        )

    @property
    def FcElsRequestPortIDPageAddressFormat(self):
        """
        Display Name: Address Format
        Default Value: 0
        Value Format: decimal
        Available enum values: Port Address, 0, Area Address Group, 1, Domain Address Group, 2, Fabric Address Group, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FcElsRequestPortIDPageAddressFormat"]
            ),
        )

    @property
    def FcElsRequestPortIDPageDomain(self):
        """
        Display Name: Domain
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcElsRequestPortIDPageDomain"])
        )

    @property
    def FcElsRequestPortIDPageArea(self):
        """
        Display Name: Area
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcElsRequestPortIDPageArea"])
        )

    @property
    def FcElsRequestPortIDPagePort(self):
        """
        Display Name: Port
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcElsRequestPortIDPagePort"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
