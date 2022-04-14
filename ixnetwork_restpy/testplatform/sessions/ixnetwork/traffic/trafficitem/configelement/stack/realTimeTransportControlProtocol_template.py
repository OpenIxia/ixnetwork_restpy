from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RealTimeTransportControlProtocol(Base):
    __slots__ = ()
    _SDM_NAME = "realTimeTransportControlProtocol"
    _SDM_ATT_MAP = {
        "RtcpHeaderVersion": "realTimeTransportControlProtocol.header.rtcpHeader.version-1",
        "RtcpHeaderPaddingBit": "realTimeTransportControlProtocol.header.rtcpHeader.paddingBit-2",
        "RtcpHeaderReceptionReportCount": "realTimeTransportControlProtocol.header.rtcpHeader.receptionReportCount-3",
        "RtcpHeaderPacketType": "realTimeTransportControlProtocol.header.rtcpHeader.packetType-4",
        "RtcpHeaderMessageLength": "realTimeTransportControlProtocol.header.rtcpHeader.messageLength-5",
        "RtcpHeaderSsrcOfReportSender": "realTimeTransportControlProtocol.header.rtcpHeader.ssrcOfReportSender-6",
        "SenderReportHeaderNtpTimestamp": "realTimeTransportControlProtocol.header.senderReportHeader.ntpTimestamp-7",
        "SenderReportHeaderRtpTimestamp": "realTimeTransportControlProtocol.header.senderReportHeader.rtpTimestamp-8",
        "SenderReportHeaderSenderPacketCount": "realTimeTransportControlProtocol.header.senderReportHeader.senderPacketCount-9",
        "SenderReportHeaderSenderPacketCount": "realTimeTransportControlProtocol.header.senderReportHeader.senderPacketCount-10",
        "SenderReportHeaderSenderByteCount": "realTimeTransportControlProtocol.header.senderReportHeader.senderByteCount-11",
        "SenderReportHeaderSenderPacketCount": "realTimeTransportControlProtocol.header.senderReportHeader.senderPacketCount-12",
        "SenderReportHeaderSenderPacketCount": "realTimeTransportControlProtocol.header.senderReportHeader.senderPacketCount-13",
        "ReceiverReportHeaderSsrcOfSource": "realTimeTransportControlProtocol.header.receiverReportHeader.ssrcOfSource-14",
        "ReceiverReportHeaderFractionLost": "realTimeTransportControlProtocol.header.receiverReportHeader.fractionLost-15",
        "ReceiverReportHeaderNumberOfPacketLost": "realTimeTransportControlProtocol.header.receiverReportHeader.NumberOfPacketLost-16",
        "ReceiverReportHeaderExtendedHighestSequenceNumber": "realTimeTransportControlProtocol.header.receiverReportHeader.extendedHighestSequenceNumber-17",
        "ReceiverReportHeaderInterarrivalJitter": "realTimeTransportControlProtocol.header.receiverReportHeader.interarrivalJitter-18",
        "ReceiverReportHeaderLastSr": "realTimeTransportControlProtocol.header.receiverReportHeader.lastSr-19",
        "ReceiverReportHeaderDelaySincelastSr": "realTimeTransportControlProtocol.header.receiverReportHeader.delaySincelastSr-20",
        "ReceiverReportHeaderSenderPacketCount": "realTimeTransportControlProtocol.header.receiverReportHeader.senderPacketCount-21",
        "SourceDescriptionPacketSsrcOfFirstCsrc": "realTimeTransportControlProtocol.header.sourceDescriptionPacket.ssrcOfFirstCsrc-22",
        "SourceDescriptionPacketSdesType": "realTimeTransportControlProtocol.header.sourceDescriptionPacket.sdesType-23",
        "SourceDescriptionPacketSdesLength": "realTimeTransportControlProtocol.header.sourceDescriptionPacket.sdesLength-24",
        "SourceDescriptionPacketSdesItem": "realTimeTransportControlProtocol.header.sourceDescriptionPacket.sdesItem-25",
        "ByePacketSsrc/csrcOfSender": "realTimeTransportControlProtocol.header.byePacket.ssrc/csrcOfSender-26",
        "ByePacketLength": "realTimeTransportControlProtocol.header.byePacket.length-27",
        "ByePacketReasonForLeaving": "realTimeTransportControlProtocol.header.byePacket.reasonForLeaving-28",
        "ApplicationDefinedPacketSsrc/csrcOfSender": "realTimeTransportControlProtocol.header.applicationDefinedPacket.ssrc/csrcOfSender-29",
        "ApplicationDefinedPacketName": "realTimeTransportControlProtocol.header.applicationDefinedPacket.name-30",
        "ApplicationDefinedPacketApplicationDependentData": "realTimeTransportControlProtocol.header.applicationDefinedPacket.applicationDependentData-31",
    }

    def __init__(self, parent, list_op=False):
        super(RealTimeTransportControlProtocol, self).__init__(parent, list_op)

    @property
    def RtcpHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0x2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderVersion"])
        )

    @property
    def RtcpHeaderPaddingBit(self):
        """
        Display Name: Padding
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderPaddingBit"])
        )

    @property
    def RtcpHeaderReceptionReportCount(self):
        """
        Display Name: RR Count
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderReceptionReportCount"]),
        )

    @property
    def RtcpHeaderPacketType(self):
        """
        Display Name: Packet Type
        Default Value: 200
        Value Format: decimal
        Available enum values: SR, sender report., 200, RR, receiver report., 201, SDES, source description., 202, BYE, goodbye., 203, APP, application defined., 204
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderPacketType"])
        )

    @property
    def RtcpHeaderMessageLength(self):
        """
        Display Name: Message Length
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderMessageLength"])
        )

    @property
    def RtcpHeaderSsrcOfReportSender(self):
        """
        Display Name: SSRC Of Report Sender
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderSsrcOfReportSender"])
        )

    @property
    def SenderReportHeaderNtpTimestamp(self):
        """
        Display Name: NTP Timestamp
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SenderReportHeaderNtpTimestamp"]),
        )

    @property
    def SenderReportHeaderRtpTimestamp(self):
        """
        Display Name: RTP Timestamp
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SenderReportHeaderRtpTimestamp"]),
        )

    @property
    def SenderReportHeaderSenderPacketCount(self):
        """
        Display Name: Sender's Packet Count
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SenderReportHeaderSenderPacketCount"]
            ),
        )

    @property
    def SenderReportHeaderSenderPacketCount(self):
        """
        Display Name: Reception Report Block 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SenderReportHeaderSenderPacketCount"]
            ),
        )

    @property
    def SenderReportHeaderSenderByteCount(self):
        """
        Display Name: Sender's Byte Count
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SenderReportHeaderSenderByteCount"]),
        )

    @property
    def SenderReportHeaderSenderPacketCount(self):
        """
        Display Name: Sender's Packet Count
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SenderReportHeaderSenderPacketCount"]
            ),
        )

    @property
    def SenderReportHeaderSenderPacketCount(self):
        """
        Display Name: Reception Report Block 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SenderReportHeaderSenderPacketCount"]
            ),
        )

    @property
    def ReceiverReportHeaderSsrcOfSource(self):
        """
        Display Name: SSRC Of Source
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReceiverReportHeaderSsrcOfSource"]),
        )

    @property
    def ReceiverReportHeaderFractionLost(self):
        """
        Display Name: Fraction Lost
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReceiverReportHeaderFractionLost"]),
        )

    @property
    def ReceiverReportHeaderNumberOfPacketLost(self):
        """
        Display Name: Number Of Packet Lost
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReceiverReportHeaderNumberOfPacketLost"]
            ),
        )

    @property
    def ReceiverReportHeaderExtendedHighestSequenceNumber(self):
        """
        Display Name: Extended Highest Sequence Number
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReceiverReportHeaderExtendedHighestSequenceNumber"]
            ),
        )

    @property
    def ReceiverReportHeaderInterarrivalJitter(self):
        """
        Display Name: Interarrival Jitter
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReceiverReportHeaderInterarrivalJitter"]
            ),
        )

    @property
    def ReceiverReportHeaderLastSr(self):
        """
        Display Name: Last SR
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReceiverReportHeaderLastSr"])
        )

    @property
    def ReceiverReportHeaderDelaySincelastSr(self):
        """
        Display Name: Delay Since Last SR
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReceiverReportHeaderDelaySincelastSr"]
            ),
        )

    @property
    def ReceiverReportHeaderSenderPacketCount(self):
        """
        Display Name: Reception Report Block 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReceiverReportHeaderSenderPacketCount"]
            ),
        )

    @property
    def SourceDescriptionPacketSsrcOfFirstCsrc(self):
        """
        Display Name: SSRC Of First CSRC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SourceDescriptionPacketSsrcOfFirstCsrc"]
            ),
        )

    @property
    def SourceDescriptionPacketSdesType(self):
        """
        Display Name: SDES Type
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SourceDescriptionPacketSdesType"]),
        )

    @property
    def SourceDescriptionPacketSdesLength(self):
        """
        Display Name: SDES Length
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SourceDescriptionPacketSdesLength"]),
        )

    @property
    def SourceDescriptionPacketSdesItem(self):
        """
        Display Name: SDES Item
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SourceDescriptionPacketSdesItem"]),
        )

    @property
    def ByePacketSsrccsrcOfSender(self):
        """
        Display Name: SSRC/CSRC Of Sender
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ByePacketSsrc/csrcOfSender"])
        )

    @property
    def ByePacketLength(self):
        """
        Display Name: Length
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ByePacketLength"])
        )

    @property
    def ByePacketReasonForLeaving(self):
        """
        Display Name: Reason For Leaving
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ByePacketReasonForLeaving"])
        )

    @property
    def ApplicationDefinedPacketSsrccsrcOfSender(self):
        """
        Display Name: SSRC/CSRC Of Sender
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ApplicationDefinedPacketSsrc/csrcOfSender"]
            ),
        )

    @property
    def ApplicationDefinedPacketName(self):
        """
        Display Name: Name
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ApplicationDefinedPacketName"])
        )

    @property
    def ApplicationDefinedPacketApplicationDependentData(self):
        """
        Display Name: Application Dependent Data
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ApplicationDefinedPacketApplicationDependentData"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
