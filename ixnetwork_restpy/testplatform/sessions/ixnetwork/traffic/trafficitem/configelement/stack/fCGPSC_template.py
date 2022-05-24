from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCGPSC(Base):
    __slots__ = ()
    _SDM_NAME = "fCGPSC"
    _SDM_ATT_MAP = {
        "FcHeaderSof": "fCGPSC.header.fcHeader.sof-1",
        "DeviceDataFramesDeviceDataInfo": "fCGPSC.header.fcHeader.rCTL.deviceDataFrames.deviceDataInfo-2",
        "RCTLReserved": "fCGPSC.header.fcHeader.rCTL.reserved-3",
        "ExtendedLinkServicesInfo": "fCGPSC.header.fcHeader.rCTL.extendedLinkServices.info-4",
        "Fc4LinkDataInfo": "fCGPSC.header.fcHeader.rCTL.fc4LinkData.info-5",
        "VideoDataInfo": "fCGPSC.header.fcHeader.rCTL.videoData.info-6",
        "ExtendedHeaderInfo": "fCGPSC.header.fcHeader.rCTL.extendedHeader.info-7",
        "BasicLinkServicesInfo": "fCGPSC.header.fcHeader.rCTL.basicLinkServices.info-8",
        "LinkControlFramesInfo": "fCGPSC.header.fcHeader.rCTL.linkControlFrames.info-9",
        "ExtendedRoutingInfo": "fCGPSC.header.fcHeader.rCTL.extendedRouting.info-10",
        "FcHeaderDstId": "fCGPSC.header.fcHeader.dstId-11",
        "FcHeaderCsCTLPriority": "fCGPSC.header.fcHeader.csCTLPriority-12",
        "FcHeaderSrcId": "fCGPSC.header.fcHeader.srcId-13",
        "FcHeaderType": "fCGPSC.header.fcHeader.type-14",
        "FCTLCustom": "fCGPSC.header.fcHeader.fCTL.custom-15",
        "BuildFCTLExchangeContext": "fCGPSC.header.fcHeader.fCTL.buildFCTL.exchangeContext-16",
        "BuildFCTLSequenceContext": "fCGPSC.header.fcHeader.fCTL.buildFCTL.sequenceContext-17",
        "BuildFCTLFirstSequence": "fCGPSC.header.fcHeader.fCTL.buildFCTL.firstSequence-18",
        "BuildFCTLLastSequence": "fCGPSC.header.fcHeader.fCTL.buildFCTL.lastSequence-19",
        "BuildFCTLEndSequence": "fCGPSC.header.fcHeader.fCTL.buildFCTL.endSequence-20",
        "BuildFCTLEndConnection": "fCGPSC.header.fcHeader.fCTL.buildFCTL.endConnection-21",
        "BuildFCTLCsCTLPriority": "fCGPSC.header.fcHeader.fCTL.buildFCTL.csCTLPriority-22",
        "BuildFCTLSequenceInitiative": "fCGPSC.header.fcHeader.fCTL.buildFCTL.sequenceInitiative-23",
        "BuildFCTLFcXIDReassigned": "fCGPSC.header.fcHeader.fCTL.buildFCTL.fcXIDReassigned-24",
        "BuildFCTLFcInvalidateXID": "fCGPSC.header.fcHeader.fCTL.buildFCTL.fcInvalidateXID-25",
        "BuildFCTLAckForm": "fCGPSC.header.fcHeader.fCTL.buildFCTL.ackForm-26",
        "BuildFCTLFcDataCompression": "fCGPSC.header.fcHeader.fCTL.buildFCTL.fcDataCompression-27",
        "BuildFCTLFcDataEncryption": "fCGPSC.header.fcHeader.fCTL.buildFCTL.fcDataEncryption-28",
        "BuildFCTLRetransmittedSequence": "fCGPSC.header.fcHeader.fCTL.buildFCTL.retransmittedSequence-29",
        "BuildFCTLUnidirectionalTransmit": "fCGPSC.header.fcHeader.fCTL.buildFCTL.unidirectionalTransmit-30",
        "BuildFCTLContinueSeqCondition": "fCGPSC.header.fcHeader.fCTL.buildFCTL.continueSeqCondition-31",
        "BuildFCTLAbortSeqCondition": "fCGPSC.header.fcHeader.fCTL.buildFCTL.abortSeqCondition-32",
        "BuildFCTLRelativeOffsetPresent": "fCGPSC.header.fcHeader.fCTL.buildFCTL.relativeOffsetPresent-33",
        "BuildFCTLExchangeReassembly": "fCGPSC.header.fcHeader.fCTL.buildFCTL.exchangeReassembly-34",
        "BuildFCTLFillBytes": "fCGPSC.header.fcHeader.fCTL.buildFCTL.fillBytes-35",
        "FcHeaderSeqID": "fCGPSC.header.fcHeader.seqID-36",
        "FcHeaderDfCTL": "fCGPSC.header.fcHeader.dfCTL-37",
        "FcHeaderSeqCNT": "fCGPSC.header.fcHeader.seqCNT-38",
        "FcHeaderOxID": "fCGPSC.header.fcHeader.oxID-39",
        "FcHeaderRxID": "fCGPSC.header.fcHeader.rxID-40",
        "FcHeaderParameter": "fCGPSC.header.fcHeader.parameter-41",
        "FcCTRevision": "fCGPSC.header.fcCT.revision-42",
        "FcCTInId": "fCGPSC.header.fcCT.inId-43",
        "FcCTGsType": "fCGPSC.header.fcCT.gsType-44",
        "FcCTGsSubtype": "fCGPSC.header.fcCT.gsSubtype-45",
        "FcCTOptions": "fCGPSC.header.fcCT.options-46",
        "FcCTReserved": "fCGPSC.header.fcCT.reserved-47",
        "FCSOpcode": "fCGPSC.header.FCS.opcode-48",
        "FCSMaxsize": "fCGPSC.header.FCS.maxsize-49",
        "FCSReserved": "fCGPSC.header.FCS.reserved-50",
        "FCSPortName": "fCGPSC.header.FCS.portName-51",
        "FcCRCAutoCRC": "fCGPSC.header.fcCRC.autoCRC-52",
        "FcCRCGenerateBadCRC": "fCGPSC.header.fcCRC.generateBadCRC-53",
        "FcTrailerEof": "fCGPSC.header.fcTrailer.eof-54",
    }

    def __init__(self, parent, list_op=False):
        super(FCGPSC, self).__init__(parent, list_op)

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
        Default Value: 250
        Value Format: decimal
        Available enum values: Event Service, 244, Key Distribution Service, 247, Alias Service, 248, Management Service, 250, Time Service, 251, Directory Service, 252
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTGsType"]))

    @property
    def FcCTGsSubtype(self):
        """
        Display Name: GS_Subtype
        Default Value: 0x01
        Value Format: hex
        Available enum values: Fabric Configuration Server, 1, Unzoned Name Server, 2, Fabric Zone Server, 3, Lock Server, 4, Performance Server, 5, Security Policy Server, 6, Security Information Server, 7
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
    def FCSOpcode(self):
        """
        Display Name: Command/Response Code
        Default Value: 295
        Value Format: decimal
        Available enum values: GTIN, 256, GIEL, 257, GIET, 273, GDID, 274, GMID, 275, GFN, 276, GIELN, 277, GMAL, 278, GIEIL, 279, GPL, 280, GPT, 289, GPPN, 290, GAPNL, 292, GPS, 294, GPSC, 295, GSES, 304, GIEAG, 320, GPAG, 321, GPLNL, 401, GPLT, 402, GPLML, 403, GPAB, 407, GNPL, 417, GPNL, 418, GPFCP, 420, GPLI, 421, GNID, 433, RIELN, 533, RPL, 640, RPLN, 657, RPLT, 658, RPLM, 659, RPAB, 664, RPFCP, 666, RPLI, 667, DPL, 896, DPLN, 913, DPLM, 914, DPLML, 915, DPLI, 916, DPAB, 917, DPALL, 927, FTR, 1024, FPNG, 1025
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCSOpcode"]))

    @property
    def FCSMaxsize(self):
        """
        Display Name: Maximum/Residual Size
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCSMaxsize"]))

    @property
    def FCSReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCSReserved"]))

    @property
    def FCSPortName(self):
        """
        Display Name: Port Name
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCSPortName"]))

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
