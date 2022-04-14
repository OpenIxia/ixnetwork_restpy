from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoEGPNL(Base):
    __slots__ = ()
    _SDM_NAME = "fCoEGPNL"
    _SDM_ATT_MAP = {
        "FcoeHeaderVersion": "fCoEGPNL.header.fcoeHeader.version-1",
        "FcoeHeaderReserved": "fCoEGPNL.header.fcoeHeader.reserved-2",
        "FcoeHeaderESOF": "fCoEGPNL.header.fcoeHeader.eSOF-3",
        "DeviceDataFramesDeviceDataInfo": "fCoEGPNL.header.fcHeader.rCTL.deviceDataFrames.deviceDataInfo-4",
        "RCTLReserved": "fCoEGPNL.header.fcHeader.rCTL.reserved-5",
        "ExtendedLinkServicesInfo": "fCoEGPNL.header.fcHeader.rCTL.extendedLinkServices.info-6",
        "Fc4LinkDataInfo": "fCoEGPNL.header.fcHeader.rCTL.fc4LinkData.info-7",
        "VideoDataInfo": "fCoEGPNL.header.fcHeader.rCTL.videoData.info-8",
        "ExtendedHeaderInfo": "fCoEGPNL.header.fcHeader.rCTL.extendedHeader.info-9",
        "BasicLinkServicesInfo": "fCoEGPNL.header.fcHeader.rCTL.basicLinkServices.info-10",
        "LinkControlFramesInfo": "fCoEGPNL.header.fcHeader.rCTL.linkControlFrames.info-11",
        "ExtendedRoutingInfo": "fCoEGPNL.header.fcHeader.rCTL.extendedRouting.info-12",
        "FcHeaderDstId": "fCoEGPNL.header.fcHeader.dstId-13",
        "FcHeaderCsCTLPriority": "fCoEGPNL.header.fcHeader.csCTLPriority-14",
        "FcHeaderSrcId": "fCoEGPNL.header.fcHeader.srcId-15",
        "FcHeaderType": "fCoEGPNL.header.fcHeader.type-16",
        "FCTLCustom": "fCoEGPNL.header.fcHeader.fCTL.custom-17",
        "BuildFCTLExchangeContext": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.exchangeContext-18",
        "BuildFCTLSequenceContext": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.sequenceContext-19",
        "BuildFCTLFirstSequence": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.firstSequence-20",
        "BuildFCTLLastSequence": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.lastSequence-21",
        "BuildFCTLEndSequence": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.endSequence-22",
        "BuildFCTLEndConnection": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.endConnection-23",
        "BuildFCTLCsCTLPriority": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.csCTLPriority-24",
        "BuildFCTLSequenceInitiative": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.sequenceInitiative-25",
        "BuildFCTLFcXIDReassigned": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.fcXIDReassigned-26",
        "BuildFCTLFcInvalidateXID": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.fcInvalidateXID-27",
        "BuildFCTLAckForm": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.ackForm-28",
        "BuildFCTLFcDataCompression": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.fcDataCompression-29",
        "BuildFCTLFcDataEncryption": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.fcDataEncryption-30",
        "BuildFCTLRetransmittedSequence": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.retransmittedSequence-31",
        "BuildFCTLUnidirectionalTransmit": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.unidirectionalTransmit-32",
        "BuildFCTLContinueSeqCondition": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.continueSeqCondition-33",
        "BuildFCTLAbortSeqCondition": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.abortSeqCondition-34",
        "BuildFCTLRelativeOffsetPresent": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.relativeOffsetPresent-35",
        "BuildFCTLExchangeReassembly": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.exchangeReassembly-36",
        "BuildFCTLFillBytes": "fCoEGPNL.header.fcHeader.fCTL.buildFCTL.fillBytes-37",
        "FcHeaderSeqID": "fCoEGPNL.header.fcHeader.seqID-38",
        "FcHeaderDfCTL": "fCoEGPNL.header.fcHeader.dfCTL-39",
        "FcHeaderSeqCNT": "fCoEGPNL.header.fcHeader.seqCNT-40",
        "FcHeaderOxID": "fCoEGPNL.header.fcHeader.oxID-41",
        "FcHeaderRxID": "fCoEGPNL.header.fcHeader.rxID-42",
        "FcHeaderParameter": "fCoEGPNL.header.fcHeader.parameter-43",
        "FcCTRevision": "fCoEGPNL.header.fcCT.revision-44",
        "FcCTInId": "fCoEGPNL.header.fcCT.inId-45",
        "FcCTGsType": "fCoEGPNL.header.fcCT.gsType-46",
        "FcCTGsSubtype": "fCoEGPNL.header.fcCT.gsSubtype-47",
        "FcCTOptions": "fCoEGPNL.header.fcCT.options-48",
        "FcCTReserved": "fCoEGPNL.header.fcCT.reserved-49",
        "FCSOpcode": "fCoEGPNL.header.FCS.opcode-50",
        "FCSMaxsize": "fCoEGPNL.header.FCS.maxsize-51",
        "FCSReserved": "fCoEGPNL.header.FCS.reserved-52",
        "FcCRCAutoCRC": "fCoEGPNL.header.fcCRC.autoCRC-53",
        "FcCRCGenerateBadCRC": "fCoEGPNL.header.fcCRC.generateBadCRC-54",
        "FcTrailerEEOF": "fCoEGPNL.header.fcTrailer.eEOF-55",
        "FcTrailerReserved": "fCoEGPNL.header.fcTrailer.reserved-56",
    }

    def __init__(self, parent, list_op=False):
        super(FCoEGPNL, self).__init__(parent, list_op)

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
        Default Value: 418
        Value Format: decimal
        Available enum values: GTIN, 256, GIEL, 257, GIET, 273, GDID, 274, GMID, 275, GFN, 276, GIELN, 277, GMAL, 278, GIEIL, 279, GPL, 280, GPT, 289, GPPN, 290, GAPNL, 292, GPS, 294, GPSC, 295, GATIN, 296, GSES, 304, GIEAG, 320, GPAG, 321, GPLNL, 401, GPLT, 402, GPLML, 403, GPAB, 407, GNPL, 417, GPNL, 418, GPFCP, 420, GPLI, 421, GNID, 433, RIELN, 533, RPL, 640, RPLN, 657, RPLT, 658, RPLM, 659, RPAB, 664, RPFCP, 666, RPLI, 667, DPL, 896, DPLN, 913, DPLM, 914, DPLML, 915, DPLI, 916, DPAB, 917, DPALL, 927, FTR, 1024, FPNG, 1025
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
    def FcTrailerEEOF(self):
        """
        Display Name: E-EOF
        Default Value: 65
        Value Format: decimal
        Available enum values: EOFn - Normal, 65, EOFt - Terminate, 66, EOFrt - Remove Terminate, 68, EOFni - Normal Invalid, 73, EOFrti - Remove Terminate Invalid, 79, EOFa - Abort, 80
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcTrailerEEOF"]))

    @property
    def FcTrailerReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcTrailerReserved"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
