from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Tcp(Base):
    __slots__ = ()
    _SDM_NAME = "tcp"
    _SDM_ATT_MAP = {
        "SrcPort": "tcp.header.srcPort-1",
        "DstPort": "tcp.header.dstPort-2",
        "SequenceNumber": "tcp.header.sequenceNumber-3",
        "AcknowledgementNumber": "tcp.header.acknowledgementNumber-4",
        "DataOffset": "tcp.header.dataOffset-5",
        "Reserved": "tcp.header.reserved-6",
        "EcnNsBit": "tcp.header.ecn.nsBit-7",
        "EcnCwrBit": "tcp.header.ecn.cwrBit-8",
        "EcnEcnEchoBit": "tcp.header.ecn.ecnEchoBit-9",
        "ControlBitsUrgBit": "tcp.header.controlBits.urgBit-10",
        "ControlBitsAckBit": "tcp.header.controlBits.ackBit-11",
        "ControlBitsPshBit": "tcp.header.controlBits.pshBit-12",
        "ControlBitsRstBit": "tcp.header.controlBits.rstBit-13",
        "ControlBitsSynBit": "tcp.header.controlBits.synBit-14",
        "ControlBitsFinBit": "tcp.header.controlBits.finBit-15",
        "Window": "tcp.header.window-16",
        "Checksum": "tcp.header.checksum-17",
        "UrgentPtr": "tcp.header.urgentPtr-18",
        "UserDefinedKind": "tcp.header.options.option.type.userDefined.kind-19",
        "UserDefinedLength": "tcp.header.options.option.type.userDefined.length-20",
        "UserDefinedData": "tcp.header.options.option.type.userDefined.data-21",
        "EndOfOptionListKind": "tcp.header.options.option.type.endOfOptionList.kind-22",
        "NoOperationKind": "tcp.header.options.option.type.noOperation.kind-23",
        "MaximumSegmentSizeKind": "tcp.header.options.option.type.maximumSegmentSize.kind-24",
        "MaximumSegmentSizeLength": "tcp.header.options.option.type.maximumSegmentSize.length-25",
        "MaximumSegmentSizeData": "tcp.header.options.option.type.maximumSegmentSize.data-26",
        "WsoptKind": "tcp.header.options.option.type.wsopt.kind-27",
        "WsoptLength": "tcp.header.options.option.type.wsopt.length-28",
        "WsoptData": "tcp.header.options.option.type.wsopt.data-29",
        "SackPermittedKind": "tcp.header.options.option.type.sackPermitted.kind-30",
        "SackPermittedLength": "tcp.header.options.option.type.sackPermitted.length-31",
        "SackKind": "tcp.header.options.option.type.sack.kind-32",
        "SackLength": "tcp.header.options.option.type.sack.length-33",
        "SackData": "tcp.header.options.option.type.sack.data-34",
        "EchoKind": "tcp.header.options.option.type.echo.kind-35",
        "EchoLength": "tcp.header.options.option.type.echo.length-36",
        "EchoData": "tcp.header.options.option.type.echo.data-37",
        "EchoReplyKind": "tcp.header.options.option.type.echoReply.kind-38",
        "EchoReplyLength": "tcp.header.options.option.type.echoReply.length-39",
        "EchoReplyData": "tcp.header.options.option.type.echoReply.data-40",
        "TsoptKind": "tcp.header.options.option.type.tsopt.kind-41",
        "TsoptLength": "tcp.header.options.option.type.tsopt.length-42",
        "TsoptData": "tcp.header.options.option.type.tsopt.data-43",
        "PartialOrderConnectionPermittedKind": "tcp.header.options.option.type.partialOrderConnectionPermitted.kind-44",
        "PartialOrderConnectionPermittedLength": "tcp.header.options.option.type.partialOrderConnectionPermitted.length-45",
        "PartialOrderServiceProfileKind": "tcp.header.options.option.type.partialOrderServiceProfile.kind-46",
        "PartialOrderServiceProfileLength": "tcp.header.options.option.type.partialOrderServiceProfile.length-47",
        "PartialOrderServiceProfileData": "tcp.header.options.option.type.partialOrderServiceProfile.data-48",
        "CcKind": "tcp.header.options.option.type.cc.kind-49",
        "CcNewKind": "tcp.header.options.option.type.ccNew.kind-50",
        "CcEchoKind": "tcp.header.options.option.type.ccEcho.kind-51",
        "AlternateChecksumRequestKind": "tcp.header.options.option.type.alternateChecksumRequest.kind-52",
        "AlternateChecksumRequestLength": "tcp.header.options.option.type.alternateChecksumRequest.length-53",
        "AlternateChecksumRequestData": "tcp.header.options.option.type.alternateChecksumRequest.data-54",
        "AlternateChecksumDataKind": "tcp.header.options.option.type.alternateChecksumData.kind-55",
        "AlternateChecksumDataLength": "tcp.header.options.option.type.alternateChecksumData.length-56",
        "AlternateChecksumDataData": "tcp.header.options.option.type.alternateChecksumData.data-57",
        "SkeeterKind": "tcp.header.options.option.type.skeeter.kind-58",
        "BubbaKind": "tcp.header.options.option.type.bubba.kind-59",
        "TrailerChecksumKind": "tcp.header.options.option.type.trailerChecksum.kind-60",
        "TrailerChecksumLength": "tcp.header.options.option.type.trailerChecksum.length-61",
        "TrailerChecksumData": "tcp.header.options.option.type.trailerChecksum.data-62",
        "Md5SignatureKind": "tcp.header.options.option.type.md5Signature.kind-63",
        "Md5SignatureLength": "tcp.header.options.option.type.md5Signature.length-64",
        "Md5SignatureData": "tcp.header.options.option.type.md5Signature.data-65",
        "ScpsCapabilitiesKind": "tcp.header.options.option.type.scpsCapabilities.kind-66",
        "SelectiveNegativeAckKind": "tcp.header.options.option.type.selectiveNegativeAck.kind-67",
        "RecordBoundariesKind": "tcp.header.options.option.type.recordBoundaries.kind-68",
        "CorruptionExperiencedKind": "tcp.header.options.option.type.corruptionExperienced.kind-69",
        "SnapKind": "tcp.header.options.option.type.snap.kind-70",
        "Unassigned1Kind": "tcp.header.options.option.type.unassigned1.kind-71",
        "CompressionFilterKind": "tcp.header.options.option.type.compressionFilter.kind-72",
        "QuickStartResponseKind": "tcp.header.options.option.type.quickStartResponse.kind-73",
        "QuickStartResponseLength": "tcp.header.options.option.type.quickStartResponse.length-74",
        "QuickStartResponseData": "tcp.header.options.option.type.quickStartResponse.data-75",
        "Unassigned2Kind": "tcp.header.options.option.type.unassigned2.kind-76",
        "Rfc3692StypeExperiment1Kind": "tcp.header.options.option.type.rfc3692StypeExperiment1.kind-77",
        "Rfc3692StypeExperiment1Length": "tcp.header.options.option.type.rfc3692StypeExperiment1.length-78",
        "Rfc3692StypeExperiment1Data": "tcp.header.options.option.type.rfc3692StypeExperiment1.data-79",
        "Rfc3692StypeExperiment2Kind": "tcp.header.options.option.type.rfc3692StypeExperiment2.kind-80",
        "Rfc3692StypeExperiment2Length": "tcp.header.options.option.type.rfc3692StypeExperiment2.length-81",
        "Rfc3692StypeExperiment2Data": "tcp.header.options.option.type.rfc3692StypeExperiment2.data-82",
        "OptionsPad": "tcp.header.options.pad-83",
    }

    def __init__(self, parent, list_op=False):
        super(Tcp, self).__init__(parent, list_op)

    @property
    def SrcPort(self):
        """
        Display Name: TCP-Source-Port
        Default Value: 60
        Value Format: decimal
        Available enum values: Unassigned, 60, MSDP, 639, LDP, 646
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcPort"]))

    @property
    def DstPort(self):
        """
        Display Name: TCP-Dest-Port
        Default Value: 60
        Value Format: decimal
        Available enum values: Unassigned, 60, MSDP, 639, LDP, 646
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DstPort"]))

    @property
    def SequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceNumber"])
        )

    @property
    def AcknowledgementNumber(self):
        """
        Display Name: Acknowledgement Number
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcknowledgementNumber"])
        )

    @property
    def DataOffset(self):
        """
        Display Name: Data Offset
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataOffset"]))

    @property
    def Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved"]))

    @property
    def EcnNsBit(self):
        """
        Display Name: NS
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EcnNsBit"]))

    @property
    def EcnCwrBit(self):
        """
        Display Name: CWR
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EcnCwrBit"]))

    @property
    def EcnEcnEchoBit(self):
        """
        Display Name: ECN-Echo
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EcnEcnEchoBit"]))

    @property
    def ControlBitsUrgBit(self):
        """
        Display Name: URG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlBitsUrgBit"])
        )

    @property
    def ControlBitsAckBit(self):
        """
        Display Name: ACK
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlBitsAckBit"])
        )

    @property
    def ControlBitsPshBit(self):
        """
        Display Name: PSH
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlBitsPshBit"])
        )

    @property
    def ControlBitsRstBit(self):
        """
        Display Name: RST
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlBitsRstBit"])
        )

    @property
    def ControlBitsSynBit(self):
        """
        Display Name: SYN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlBitsSynBit"])
        )

    @property
    def ControlBitsFinBit(self):
        """
        Display Name: FIN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlBitsFinBit"])
        )

    @property
    def Window(self):
        """
        Display Name: Window
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Window"]))

    @property
    def Checksum(self):
        """
        Display Name: TCP-Checksum
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Checksum"]))

    @property
    def UrgentPtr(self):
        """
        Display Name: Urgent Pointer
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UrgentPtr"]))

    @property
    def UserDefinedKind(self):
        """
        Display Name: Options Kind
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedKind"])
        )

    @property
    def UserDefinedLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedLength"])
        )

    @property
    def UserDefinedData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedData"])
        )

    @property
    def EndOfOptionListKind(self):
        """
        Display Name: Options Kind
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndOfOptionListKind"])
        )

    @property
    def NoOperationKind(self):
        """
        Display Name: Options Kind
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NoOperationKind"])
        )

    @property
    def MaximumSegmentSizeKind(self):
        """
        Display Name: Options Kind
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumSegmentSizeKind"])
        )

    @property
    def MaximumSegmentSizeLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumSegmentSizeLength"])
        )

    @property
    def MaximumSegmentSizeData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaximumSegmentSizeData"])
        )

    @property
    def WsoptKind(self):
        """
        Display Name: Options Kind
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["WsoptKind"]))

    @property
    def WsoptLength(self):
        """
        Display Name: Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["WsoptLength"]))

    @property
    def WsoptData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["WsoptData"]))

    @property
    def SackPermittedKind(self):
        """
        Display Name: Options Kind
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SackPermittedKind"])
        )

    @property
    def SackPermittedLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SackPermittedLength"])
        )

    @property
    def SackKind(self):
        """
        Display Name: Options Kind
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SackKind"]))

    @property
    def SackLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SackLength"]))

    @property
    def SackData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SackData"]))

    @property
    def EchoKind(self):
        """
        Display Name: Options Kind
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EchoKind"]))

    @property
    def EchoLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EchoLength"]))

    @property
    def EchoData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EchoData"]))

    @property
    def EchoReplyKind(self):
        """
        Display Name: Options Kind
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EchoReplyKind"]))

    @property
    def EchoReplyLength(self):
        """
        Display Name: Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoReplyLength"])
        )

    @property
    def EchoReplyData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EchoReplyData"]))

    @property
    def TsoptKind(self):
        """
        Display Name: Options Kind
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TsoptKind"]))

    @property
    def TsoptLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TsoptLength"]))

    @property
    def TsoptData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TsoptData"]))

    @property
    def PartialOrderConnectionPermittedKind(self):
        """
        Display Name: Options Kind
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PartialOrderConnectionPermittedKind"]
            ),
        )

    @property
    def PartialOrderConnectionPermittedLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PartialOrderConnectionPermittedLength"]
            ),
        )

    @property
    def PartialOrderServiceProfileKind(self):
        """
        Display Name: Options Kind
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PartialOrderServiceProfileKind"]),
        )

    @property
    def PartialOrderServiceProfileLength(self):
        """
        Display Name: Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PartialOrderServiceProfileLength"]),
        )

    @property
    def PartialOrderServiceProfileData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PartialOrderServiceProfileData"]),
        )

    @property
    def CcKind(self):
        """
        Display Name: Options Kind
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CcKind"]))

    @property
    def CcNewKind(self):
        """
        Display Name: Options Kind
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CcNewKind"]))

    @property
    def CcEchoKind(self):
        """
        Display Name: Options Kind
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CcEchoKind"]))

    @property
    def AlternateChecksumRequestKind(self):
        """
        Display Name: Options Kind
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateChecksumRequestKind"])
        )

    @property
    def AlternateChecksumRequestLength(self):
        """
        Display Name: Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AlternateChecksumRequestLength"]),
        )

    @property
    def AlternateChecksumRequestData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateChecksumRequestData"])
        )

    @property
    def AlternateChecksumDataKind(self):
        """
        Display Name: Options Kind
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateChecksumDataKind"])
        )

    @property
    def AlternateChecksumDataLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateChecksumDataLength"])
        )

    @property
    def AlternateChecksumDataData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateChecksumDataData"])
        )

    @property
    def SkeeterKind(self):
        """
        Display Name: Options Kind
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SkeeterKind"]))

    @property
    def BubbaKind(self):
        """
        Display Name: Options Kind
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BubbaKind"]))

    @property
    def TrailerChecksumKind(self):
        """
        Display Name: Options Kind
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TrailerChecksumKind"])
        )

    @property
    def TrailerChecksumLength(self):
        """
        Display Name: Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TrailerChecksumLength"])
        )

    @property
    def TrailerChecksumData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TrailerChecksumData"])
        )

    @property
    def Md5SignatureKind(self):
        """
        Display Name: Options Kind
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md5SignatureKind"])
        )

    @property
    def Md5SignatureLength(self):
        """
        Display Name: Length
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md5SignatureLength"])
        )

    @property
    def Md5SignatureData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md5SignatureData"])
        )

    @property
    def ScpsCapabilitiesKind(self):
        """
        Display Name: Options Kind
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ScpsCapabilitiesKind"])
        )

    @property
    def SelectiveNegativeAckKind(self):
        """
        Display Name: Options Kind
        Default Value: 21
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SelectiveNegativeAckKind"])
        )

    @property
    def RecordBoundariesKind(self):
        """
        Display Name: Options Kind
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RecordBoundariesKind"])
        )

    @property
    def CorruptionExperiencedKind(self):
        """
        Display Name: Options Kind
        Default Value: 23
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CorruptionExperiencedKind"])
        )

    @property
    def SnapKind(self):
        """
        Display Name: Options Kind
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SnapKind"]))

    @property
    def Unassigned1Kind(self):
        """
        Display Name: Options Kind
        Default Value: 25
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Unassigned1Kind"])
        )

    @property
    def CompressionFilterKind(self):
        """
        Display Name: Options Kind
        Default Value: 26
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CompressionFilterKind"])
        )

    @property
    def QuickStartResponseKind(self):
        """
        Display Name: Options Kind
        Default Value: 27
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QuickStartResponseKind"])
        )

    @property
    def QuickStartResponseLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QuickStartResponseLength"])
        )

    @property
    def QuickStartResponseData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["QuickStartResponseData"])
        )

    @property
    def Unassigned2Kind(self):
        """
        Display Name: Options Kind
        Default Value: 28
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Unassigned2Kind"])
        )

    @property
    def Rfc3692StypeExperiment1Kind(self):
        """
        Display Name: Options Kind
        Default Value: 253
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Rfc3692StypeExperiment1Kind"])
        )

    @property
    def Rfc3692StypeExperiment1Length(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Rfc3692StypeExperiment1Length"]),
        )

    @property
    def Rfc3692StypeExperiment1Data(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Rfc3692StypeExperiment1Data"])
        )

    @property
    def Rfc3692StypeExperiment2Kind(self):
        """
        Display Name: Options Kind
        Default Value: 254
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Rfc3692StypeExperiment2Kind"])
        )

    @property
    def Rfc3692StypeExperiment2Length(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Rfc3692StypeExperiment2Length"]),
        )

    @property
    def Rfc3692StypeExperiment2Data(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Rfc3692StypeExperiment2Data"])
        )

    @property
    def OptionsPad(self):
        """
        Display Name: Pad
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionsPad"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
