from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoEEFPRequest(Base):
    __slots__ = ()
    _SDM_NAME = "fCoEEFPRequest"
    _SDM_ATT_MAP = {
        "FcoeHeaderVersion": "fCoEEFPRequest.header.fcoeHeader.version-1",
        "FcoeHeaderReserved": "fCoEEFPRequest.header.fcoeHeader.reserved-2",
        "FcoeHeaderESOF": "fCoEEFPRequest.header.fcoeHeader.eSOF-3",
        "FcHeaderRCTL": "fCoEEFPRequest.header.fcHeader.rCTL-4",
        "FcHeaderDstId": "fCoEEFPRequest.header.fcHeader.dstId-5",
        "FcHeaderCsCTLPriority": "fCoEEFPRequest.header.fcHeader.csCTLPriority-6",
        "FcHeaderSrcId": "fCoEEFPRequest.header.fcHeader.srcId-7",
        "FcHeaderType": "fCoEEFPRequest.header.fcHeader.type-8",
        "FCTLCustom": "fCoEEFPRequest.header.fcHeader.fCTL.custom-9",
        "BuildFCTLExchangeContext": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.exchangeContext-10",
        "BuildFCTLSequenceContext": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.sequenceContext-11",
        "BuildFCTLFirstSequence": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.firstSequence-12",
        "BuildFCTLLastSequence": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.lastSequence-13",
        "BuildFCTLEndSequence": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.endSequence-14",
        "BuildFCTLEndConnection": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.endConnection-15",
        "BuildFCTLCsCTLPriority": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.csCTLPriority-16",
        "BuildFCTLSequenceInitiative": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.sequenceInitiative-17",
        "BuildFCTLFcXIDReassigned": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.fcXIDReassigned-18",
        "BuildFCTLFcInvalidateXID": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.fcInvalidateXID-19",
        "BuildFCTLAckForm": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.ackForm-20",
        "BuildFCTLFcDataCompression": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.fcDataCompression-21",
        "BuildFCTLFcDataEncryption": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.fcDataEncryption-22",
        "BuildFCTLRetransmittedSequence": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.retransmittedSequence-23",
        "BuildFCTLUnidirectionalTransmit": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.unidirectionalTransmit-24",
        "BuildFCTLContinueSeqCondition": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.continueSeqCondition-25",
        "BuildFCTLAbortSeqCondition": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.abortSeqCondition-26",
        "BuildFCTLRelativeOffsetPresent": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.relativeOffsetPresent-27",
        "BuildFCTLExchangeReassembly": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.exchangeReassembly-28",
        "BuildFCTLFillBytes": "fCoEEFPRequest.header.fcHeader.fCTL.buildFCTL.fillBytes-29",
        "FcHeaderSeqID": "fCoEEFPRequest.header.fcHeader.seqID-30",
        "FcHeaderDfCTL": "fCoEEFPRequest.header.fcHeader.dfCTL-31",
        "FcHeaderSeqCNT": "fCoEEFPRequest.header.fcHeader.seqCNT-32",
        "FcHeaderOxID": "fCoEEFPRequest.header.fcHeader.oxID-33",
        "FcHeaderRxID": "fCoEEFPRequest.header.fcHeader.rxID-34",
        "FcHeaderParameter": "fCoEEFPRequest.header.fcHeader.parameter-35",
        "HeaderFcCmd": "fCoEEFPRequest.header.fcCmd-36",
        "HeaderReserved1": "fCoEEFPRequest.header.reserved1-37",
        "HeaderReserved2": "fCoEEFPRequest.header.reserved2-38",
        "HeaderLength": "fCoEEFPRequest.header.length-39",
        "HeaderReserved3": "fCoEEFPRequest.header.reserved3-40",
        "HeaderPrincipalSwitchPriority": "fCoEEFPRequest.header.principalSwitchPriority-41",
        "HeaderPrincipalSwitchName": "fCoEEFPRequest.header.principalSwitchName-42",
        "HeaderRecordType": "fCoEEFPRequest.header.recordType-43",
        "HeaderDomainID": "fCoEEFPRequest.header.domainID-44",
        "HeaderReserved4": "fCoEEFPRequest.header.reserved4-45",
        "HeaderReserved5": "fCoEEFPRequest.header.reserved5-46",
        "HeaderSwitchName": "fCoEEFPRequest.header.switchName-47",
    }

    def __init__(self, parent, list_op=False):
        super(FCoEEFPRequest, self).__init__(parent, list_op)

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
    def FcHeaderRCTL(self):
        """
        Display Name: R_CTL
        Default Value: 2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderRCTL"]))

    @property
    def FcHeaderDstId(self):
        """
        Display Name: Destination ID
        Default Value: 0
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDstId"]))

    @property
    def FcHeaderCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderCsCTLPriority"])
        )

    @property
    def FcHeaderSrcId(self):
        """
        Display Name: Source ID
        Default Value: 0
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSrcId"]))

    @property
    def FcHeaderType(self):
        """
        Display Name: Type
        Default Value: 22
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderType"]))

    @property
    def FCTLCustom(self):
        """
        Display Name: Custom
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCTLCustom"]))

    @property
    def BuildFCTLExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLExchangeContext"])
        )

    @property
    def BuildFCTLSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLSequenceContext"])
        )

    @property
    def BuildFCTLFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFirstSequence"])
        )

    @property
    def BuildFCTLLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLLastSequence"])
        )

    @property
    def BuildFCTLEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLEndSequence"])
        )

    @property
    def BuildFCTLEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLEndConnection"])
        )

    @property
    def BuildFCTLCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLCsCTLPriority"])
        )

    @property
    def BuildFCTLSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 0
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLSequenceInitiative"])
        )

    @property
    def BuildFCTLFcXIDReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcXIDReassigned"])
        )

    @property
    def BuildFCTLFcInvalidateXID(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcInvalidateXID"])
        )

    @property
    def BuildFCTLAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLAckForm"])
        )

    @property
    def BuildFCTLFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcDataCompression"])
        )

    @property
    def BuildFCTLFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcDataEncryption"])
        )

    @property
    def BuildFCTLRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLRetransmittedSequence"]),
        )

    @property
    def BuildFCTLUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLUnidirectionalTransmit"]),
        )

    @property
    def BuildFCTLContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLContinueSeqCondition"]),
        )

    @property
    def BuildFCTLAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLAbortSeqCondition"])
        )

    @property
    def BuildFCTLRelativeOffsetPresent(self):
        """
        Display Name: Relative Offset Present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLRelativeOffsetPresent"]),
        )

    @property
    def BuildFCTLExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLExchangeReassembly"])
        )

    @property
    def BuildFCTLFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFillBytes"])
        )

    @property
    def FcHeaderSeqID(self):
        """
        Display Name: SEQ_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqID"]))

    @property
    def FcHeaderDfCTL(self):
        """
        Display Name: DF_CTL
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDfCTL"]))

    @property
    def FcHeaderSeqCNT(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqCNT"])
        )

    @property
    def FcHeaderOxID(self):
        """
        Display Name: OX_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderOxID"]))

    @property
    def FcHeaderRxID(self):
        """
        Display Name: RX_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderRxID"]))

    @property
    def FcHeaderParameter(self):
        """
        Display Name: Parameter
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderParameter"])
        )

    @property
    def HeaderFcCmd(self):
        """
        Display Name: FC Command
        Default Value: 285212672
        Value Format: decimal
        Available enum values: SW_RJT, 16777216, SW_ACC, 33554432, ELP, 268435456, EFP, 285212672, DIA, 301989888, RDI, 318767104, HLO, 335544320, LSU, 352321536, LSA, 369098752, BF, 385875968, RCF, 402653184, SW_RSCN, 452984832, DRLIR, 503316480, DSCN, 536870912, LOOPD, 553648128, MR, 570425344, ACA, 587202560, RCA, 603979776, SFC, 620756992, UFC, 637534208, CEC, 687865856, EACA, 704708608, ESFC, 704774144, EUFC, 704839680, ERCA, 704905216, TCO, 704970752, ESC, 805306368, ESS, 822083584, MRRA, 872415232, STR, 889257984, EVFP, 905969664, FFI, 1342177280
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFcCmd"]))

    @property
    def HeaderReserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0x11
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved1"])
        )

    @property
    def HeaderReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0x10
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved2"])
        )

    @property
    def HeaderLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderReserved3(self):
        """
        Display Name: Reserved3
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved3"])
        )

    @property
    def HeaderPrincipalSwitchPriority(self):
        """
        Display Name: Principal Switch_Priority
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderPrincipalSwitchPriority"]),
        )

    @property
    def HeaderPrincipalSwitchName(self):
        """
        Display Name: Principal Switch_Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPrincipalSwitchName"])
        )

    @property
    def HeaderRecordType(self):
        """
        Display Name: Record_Type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRecordType"])
        )

    @property
    def HeaderDomainID(self):
        """
        Display Name: Domain_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDomainID"])
        )

    @property
    def HeaderReserved4(self):
        """
        Display Name: Reserved4
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved4"])
        )

    @property
    def HeaderReserved5(self):
        """
        Display Name: Reserved5
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved5"])
        )

    @property
    def HeaderSwitchName(self):
        """
        Display Name: Switch_Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSwitchName"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
