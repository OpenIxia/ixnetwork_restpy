from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoEELPRequest(Base):
    __slots__ = ()
    _SDM_NAME = "fCoEELPRequest"
    _SDM_ATT_MAP = {
        "FcoeHeaderVersion": "fCoEELPRequest.header.fcoeHeader.version-1",
        "FcoeHeaderReserved": "fCoEELPRequest.header.fcoeHeader.reserved-2",
        "FcoeHeaderESOF": "fCoEELPRequest.header.fcoeHeader.eSOF-3",
        "FcHeaderRCTL": "fCoEELPRequest.header.fcHeader.rCTL-4",
        "FcHeaderDstId": "fCoEELPRequest.header.fcHeader.dstId-5",
        "FcHeaderCsCTLPriority": "fCoEELPRequest.header.fcHeader.csCTLPriority-6",
        "FcHeaderSrcId": "fCoEELPRequest.header.fcHeader.srcId-7",
        "FcHeaderType": "fCoEELPRequest.header.fcHeader.type-8",
        "FCTLCustom": "fCoEELPRequest.header.fcHeader.fCTL.custom-9",
        "BuildFCTLExchangeContext": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.exchangeContext-10",
        "BuildFCTLSequenceContext": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.sequenceContext-11",
        "BuildFCTLFirstSequence": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.firstSequence-12",
        "BuildFCTLLastSequence": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.lastSequence-13",
        "BuildFCTLEndSequence": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.endSequence-14",
        "BuildFCTLEndConnection": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.endConnection-15",
        "BuildFCTLCsCTLPriority": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.csCTLPriority-16",
        "BuildFCTLSequenceInitiative": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.sequenceInitiative-17",
        "BuildFCTLFcXIDReassigned": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.fcXIDReassigned-18",
        "BuildFCTLFcInvalidateXID": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.fcInvalidateXID-19",
        "BuildFCTLAckForm": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.ackForm-20",
        "BuildFCTLFcDataCompression": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.fcDataCompression-21",
        "BuildFCTLFcDataEncryption": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.fcDataEncryption-22",
        "BuildFCTLRetransmittedSequence": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.retransmittedSequence-23",
        "BuildFCTLUnidirectionalTransmit": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.unidirectionalTransmit-24",
        "BuildFCTLContinueSeqCondition": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.continueSeqCondition-25",
        "BuildFCTLAbortSeqCondition": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.abortSeqCondition-26",
        "BuildFCTLRelativeOffsetPresent": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.relativeOffsetPresent-27",
        "BuildFCTLExchangeReassembly": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.exchangeReassembly-28",
        "BuildFCTLFillBytes": "fCoEELPRequest.header.fcHeader.fCTL.buildFCTL.fillBytes-29",
        "FcHeaderSeqID": "fCoEELPRequest.header.fcHeader.seqID-30",
        "FcHeaderDfCTL": "fCoEELPRequest.header.fcHeader.dfCTL-31",
        "FcHeaderSeqCNT": "fCoEELPRequest.header.fcHeader.seqCNT-32",
        "FcHeaderOxID": "fCoEELPRequest.header.fcHeader.oxID-33",
        "FcHeaderRxID": "fCoEELPRequest.header.fcHeader.rxID-34",
        "FcHeaderParameter": "fCoEELPRequest.header.fcHeader.parameter-35",
        "HeaderFcCmd": "fCoEELPRequest.header.fcCmd-36",
        "HeaderReserved1": "fCoEELPRequest.header.reserved1-37",
        "HeaderRevision": "fCoEELPRequest.header.revision-38",
        "HeaderFlags": "fCoEELPRequest.header.flags-39",
        "HeaderBbScN": "fCoEELPRequest.header.bbScN-40",
        "HeaderRATov": "fCoEELPRequest.header.rATov-41",
        "HeaderEDTov": "fCoEELPRequest.header.eDTov-42",
        "HeaderReqInterconnectPortName": "fCoEELPRequest.header.reqInterconnectPortName-43",
        "HeaderReqSwitchName": "fCoEELPRequest.header.reqSwitchName-44",
        "HeaderServiceParams": "fCoEELPRequest.header.serviceParams-45",
        "HeaderClass1PortParams": "fCoEELPRequest.header.class1PortParams-46",
        "HeaderClass2PortParams": "fCoEELPRequest.header.class2PortParams-47",
        "HeaderClass3PortParams": "fCoEELPRequest.header.class3PortParams-48",
        "HeaderReserved2": "fCoEELPRequest.header.reserved2-49",
        "HeaderIslFlowControlMode": "fCoEELPRequest.header.islFlowControlMode-50",
        "HeaderFlowControlParamLength": "fCoEELPRequest.header.flowControlParamLength-51",
        "HeaderFlowControlParams": "fCoEELPRequest.header.flowControlParams-52",
    }

    def __init__(self, parent, list_op=False):
        super(FCoEELPRequest, self).__init__(parent, list_op)

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
        Default Value: 268435456
        Value Format: decimal
        Available enum values: SW_RJT, 16777216, SW_ACC, 33554432, ELP, 268435456, EFP, 285212672, DIA, 301989888, RDI, 318767104, HLO, 335544320, LSU, 352321536, LSA, 369098752, BF, 385875968, RCF, 402653184, SW_RSCN, 452984832, DRLIR, 503316480, DSCN, 536870912, LOOPD, 553648128, MR, 570425344, ACA, 587202560, RCA, 603979776, SFC, 620756992, UFC, 637534208, CEC, 687865856, EACA, 704708608, ESFC, 704774144, EUFC, 704839680, ERCA, 704905216, TCO, 704970752, ESC, 805306368, ESS, 822083584, MRRA, 872415232, STR, 889257984, EVFP, 905969664, FFI, 1342177280
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFcCmd"]))

    @property
    def HeaderReserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0x10000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved1"])
        )

    @property
    def HeaderRevision(self):
        """
        Display Name: Revision
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRevision"])
        )

    @property
    def HeaderFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFlags"]))

    @property
    def HeaderBbScN(self):
        """
        Display Name: BB_SC_N
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderBbScN"]))

    @property
    def HeaderRATov(self):
        """
        Display Name: R_A_TOV
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderRATov"]))

    @property
    def HeaderEDTov(self):
        """
        Display Name: E_D_TOV
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderEDTov"]))

    @property
    def HeaderReqInterconnectPortName(self):
        """
        Display Name: Requester Interconnect_Port_Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderReqInterconnectPortName"]),
        )

    @property
    def HeaderReqSwitchName(self):
        """
        Display Name: Requester Switch_Name
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReqSwitchName"])
        )

    @property
    def HeaderServiceParams(self):
        """
        Display Name: Fabric Controller Class F Service Parameters
        Default Value: 0xF00F0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderServiceParams"])
        )

    @property
    def HeaderClass1PortParams(self):
        """
        Display Name: Class 1 Interconnect_Port Parameters
        Default Value: 0x00000F00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderClass1PortParams"])
        )

    @property
    def HeaderClass2PortParams(self):
        """
        Display Name: Class 2 Interconnect_Port Parameters
        Default Value: 0x00000F00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderClass2PortParams"])
        )

    @property
    def HeaderClass3PortParams(self):
        """
        Display Name: Class 3 Interconnect_Port Parameters
        Default Value: 0x00000F00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderClass3PortParams"])
        )

    @property
    def HeaderReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0x10000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved2"])
        )

    @property
    def HeaderIslFlowControlMode(self):
        """
        Display Name: ISL Flow Control Mode
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderIslFlowControlMode"])
        )

    @property
    def HeaderFlowControlParamLength(self):
        """
        Display Name: Flow Control Parameter Length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFlowControlParamLength"])
        )

    @property
    def HeaderFlowControlParams(self):
        """
        Display Name: Flow Control Parameters
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFlowControlParams"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
