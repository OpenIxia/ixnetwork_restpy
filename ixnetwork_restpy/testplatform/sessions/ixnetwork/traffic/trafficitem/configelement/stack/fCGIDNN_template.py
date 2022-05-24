from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCGIDNN(Base):
    __slots__ = ()
    _SDM_NAME = "fCGIDNN"
    _SDM_ATT_MAP = {
        "FcHeaderSof": "fCGIDNN.header.fcHeader.sof-1",
        "DeviceDataFramesDeviceDataInfo": "fCGIDNN.header.fcHeader.rCTL.deviceDataFrames.deviceDataInfo-2",
        "RCTLReserved": "fCGIDNN.header.fcHeader.rCTL.reserved-3",
        "ExtendedLinkServicesInfo": "fCGIDNN.header.fcHeader.rCTL.extendedLinkServices.info-4",
        "Fc4LinkDataInfo": "fCGIDNN.header.fcHeader.rCTL.fc4LinkData.info-5",
        "VideoDataInfo": "fCGIDNN.header.fcHeader.rCTL.videoData.info-6",
        "ExtendedHeaderInfo": "fCGIDNN.header.fcHeader.rCTL.extendedHeader.info-7",
        "BasicLinkServicesInfo": "fCGIDNN.header.fcHeader.rCTL.basicLinkServices.info-8",
        "LinkControlFramesInfo": "fCGIDNN.header.fcHeader.rCTL.linkControlFrames.info-9",
        "ExtendedRoutingInfo": "fCGIDNN.header.fcHeader.rCTL.extendedRouting.info-10",
        "FcHeaderDstId": "fCGIDNN.header.fcHeader.dstId-11",
        "FcHeaderCsCTLPriority": "fCGIDNN.header.fcHeader.csCTLPriority-12",
        "FcHeaderSrcId": "fCGIDNN.header.fcHeader.srcId-13",
        "FcHeaderType": "fCGIDNN.header.fcHeader.type-14",
        "FCTLCustom": "fCGIDNN.header.fcHeader.fCTL.custom-15",
        "BuildFCTLExchangeContext": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.exchangeContext-16",
        "BuildFCTLSequenceContext": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.sequenceContext-17",
        "BuildFCTLFirstSequence": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.firstSequence-18",
        "BuildFCTLLastSequence": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.lastSequence-19",
        "BuildFCTLEndSequence": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.endSequence-20",
        "BuildFCTLEndConnection": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.endConnection-21",
        "BuildFCTLCsCTLPriority": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.csCTLPriority-22",
        "BuildFCTLSequenceInitiative": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.sequenceInitiative-23",
        "BuildFCTLFcXIDReassigned": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.fcXIDReassigned-24",
        "BuildFCTLFcInvalidateXID": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.fcInvalidateXID-25",
        "BuildFCTLAckForm": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.ackForm-26",
        "BuildFCTLFcDataCompression": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.fcDataCompression-27",
        "BuildFCTLFcDataEncryption": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.fcDataEncryption-28",
        "BuildFCTLRetransmittedSequence": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.retransmittedSequence-29",
        "BuildFCTLUnidirectionalTransmit": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.unidirectionalTransmit-30",
        "BuildFCTLContinueSeqCondition": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.continueSeqCondition-31",
        "BuildFCTLAbortSeqCondition": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.abortSeqCondition-32",
        "BuildFCTLRelativeOffsetPresent": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.relativeOffsetPresent-33",
        "BuildFCTLExchangeReassembly": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.exchangeReassembly-34",
        "BuildFCTLFillBytes": "fCGIDNN.header.fcHeader.fCTL.buildFCTL.fillBytes-35",
        "FcHeaderSeqID": "fCGIDNN.header.fcHeader.seqID-36",
        "FcHeaderDfCTL": "fCGIDNN.header.fcHeader.dfCTL-37",
        "FcHeaderSeqCNT": "fCGIDNN.header.fcHeader.seqCNT-38",
        "FcHeaderOxID": "fCGIDNN.header.fcHeader.oxID-39",
        "FcHeaderRxID": "fCGIDNN.header.fcHeader.rxID-40",
        "FcHeaderParameter": "fCGIDNN.header.fcHeader.parameter-41",
        "FcCTRevision": "fCGIDNN.header.fcCT.revision-42",
        "FcCTInId": "fCGIDNN.header.fcCT.inId-43",
        "FcCTGsType": "fCGIDNN.header.fcCT.gsType-44",
        "FcCTGsSubtype": "fCGIDNN.header.fcCT.gsSubtype-45",
        "FcCTOptions": "fCGIDNN.header.fcCT.options-46",
        "FcCTReserved": "fCGIDNN.header.fcCT.reserved-47",
        "DNSOpcode": "fCGIDNN.header.dNS.opcode-48",
        "DNSMaxsize": "fCGIDNN.header.dNS.maxsize-49",
        "DNSReserved": "fCGIDNN.header.dNS.reserved-50",
        "DNSNodeName": "fCGIDNN.header.dNS.nodeName-51",
        "FcCRCAutoCRC": "fCGIDNN.header.fcCRC.autoCRC-52",
        "FcCRCGenerateBadCRC": "fCGIDNN.header.fcCRC.generateBadCRC-53",
        "FcTrailerEof": "fCGIDNN.header.fcTrailer.eof-54",
    }

    def __init__(self, parent, list_op=False):
        super(FCGIDNN, self).__init__(parent, list_op)

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
    def DeviceDataFramesDeviceDataInfo(self):
        """
        Display Name: Information
        Default Value: 0
        Value Format: decimal
        Available enum values: Uncategorized Information, 0, Solicited Data, 1, Unsolicited Control, 2, Solicited Control, 3, Unsolicited Data, 4, Data Descriptor, 5, Unsolicited Command, 6, Command Status, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DeviceDataFramesDeviceDataInfo"]),
        )

    @property
    def RCTLReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RCTLReserved"]))

    @property
    def ExtendedLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 33
        Value Format: decimal
        Available enum values: Solicited Data, 32, Request, 33, Reply, 34
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedLinkServicesInfo"])
        )

    @property
    def Fc4LinkDataInfo(self):
        """
        Display Name: Information
        Default Value: 48
        Value Format: decimal
        Available enum values: Uncategorized Information, 48, Solicited Data, 49, Unsolicited Control, 50, Solicited Control, 51, Unsolicited Data, 52, Data Descriptor, 53, Unsolicited Command, 54, Command Status, 55
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Fc4LinkDataInfo"])
        )

    @property
    def VideoDataInfo(self):
        """
        Display Name: Information
        Default Value: 68
        Value Format: decimal
        Available enum values: Unsolicited Data, 68
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VideoDataInfo"]))

    @property
    def ExtendedHeaderInfo(self):
        """
        Display Name: Information
        Default Value: 80
        Value Format: decimal
        Available enum values: Virtual Fabric Tagging Header, 80, Inter Fabric Routing Header, 81, Encapsulation Header, 82
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedHeaderInfo"])
        )

    @property
    def BasicLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 128
        Value Format: decimal
        Available enum values: No Operation, 128, Abort Sequence, 129, Remove Connection, 130, Basic Accept, 132, Basic Reject, 133, Dedicated Connection Preempted, 134
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BasicLinkServicesInfo"])
        )

    @property
    def LinkControlFramesInfo(self):
        """
        Display Name: Information
        Default Value: 192
        Value Format: decimal
        Available enum values: Acknowledge_1, 128, Acknowledge_0, 129, Nx Port Reject, 130, Fabric Reject, 131, Nx Port Busy, 132, Fabric Busy to Data Frame, 133, Fabric Busy to Link Control Frame, 134, Link Credit Reset, 135, Notify, 136, End, 137
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkControlFramesInfo"])
        )

    @property
    def ExtendedRoutingInfo(self):
        """
        Display Name: Information
        Default Value: 240
        Value Format: decimal
        Available enum values: Vendor Unique, 240
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedRoutingInfo"])
        )

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
        Default Value: 0
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
    def FcCTRevision(self):
        """
        Display Name: Revision
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTRevision"]))

    @property
    def FcCTInId(self):
        """
        Display Name: IN_ID
        Default Value: 0x000000
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTInId"]))

    @property
    def FcCTGsType(self):
        """
        Display Name: GS_Type
        Default Value: 252
        Value Format: decimal
        Available enum values: Event Service, 244, Key Distribution Service, 247, Alias Service, 248, Management Service, 250, Time Service, 251, Directory Service, 252
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTGsType"]))

    @property
    def FcCTGsSubtype(self):
        """
        Display Name: GS_Subtype
        Default Value: 0x02
        Value Format: hex
        Available enum values: X.500 Server (Obsolete), 1, Name Server, 2, IP Address Server (Obsolete), 3, FC-4 specific Servers, 128
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTGsSubtype"]))

    @property
    def FcCTOptions(self):
        """
        Display Name: Options
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTOptions"]))

    @property
    def FcCTReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTReserved"]))

    @property
    def DNSOpcode(self):
        """
        Display Name: Command/Response Code
        Default Value: 305
        Value Format: decimal
        Available enum values: GA_NXT, 256, GID_A, 257, GPN_ID, 274, GNN_ID, 275, GCS_ID, 276, GFT_ID, 279, GSPN_ID, 280, GPT_ID, 282, GIPP_ID, 283, GFPN_ID, 284, GHA_ID, 285, GFD_ID, 286, GFF_ID, 287, GID_PN, 289, GIPP_PN, 299, GID_NN, 305, GPN_NN, 306, GIP_NN, 309, GIPA_NN, 310, GSNN_NN, 313, GNN_IP, 339, GIPA_IP, 342, GID_FT, 369, GPN_FT, 370, GNN_FT, 371, GNN_FF, 384, GPN_FF, 385, GPN_SDFCP, 386, GID_PT, 417, GID_IPP, 433, GPN_IPP, 434, GID_FPN, 449, GPPN_ID, 465, GID_FF, 497, GID_DP, 498, RPN_ID, 530, RNN_ID, 531, RCS_ID, 532, RFT_ID, 535, RSPN_ID, 536, RPT_ID, 538, RIPP_ID, 539, RHA_ID, 541, RFD_ID, 542, RFF_ID, 543, RIP_NN, 565, RIPA_NN, 566, RSNN_NN, 569, DA_ID, 768, SSB, 32761, SSE, 32762
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSOpcode"]))

    @property
    def DNSMaxsize(self):
        """
        Display Name: Maximum/Residual Size
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSMaxsize"]))

    @property
    def DNSReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSReserved"]))

    @property
    def DNSNodeName(self):
        """
        Display Name: Node Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSNodeName"]))

    @property
    def FcCRCAutoCRC(self):
        """
        Display Name: Auto
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCRCAutoCRC"]))

    @property
    def FcCRCGenerateBadCRC(self):
        """
        Display Name: Bad CRC
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcCRCGenerateBadCRC"])
        )

    @property
    def FcTrailerEof(self):
        """
        Display Name: EOF
        Default Value: -1128933931
        Value Format: decimal
        Available enum values: EOFn - Normal, 3166033365, EOFt - Terminate, 3166008693, EOFrt - Remove Terminate, 3166017945, EOFni - Normal Invalid, 3165312469, EOFrti - Remove Terminate Invalid, 3165297049, EOFa - Abort, 3166041589
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcTrailerEof"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
