from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RealTimeTransportControlProtocol1733(Base):
    __slots__ = ()
    _SDM_NAME = "realTimeTransportControlProtocol1733"
    _SDM_ATT_MAP = {
        "RtcpHeaderVersion": "realTimeTransportControlProtocol1733.rtcpHeader.version-1",
        "RtcpHeaderPaddingBit": "realTimeTransportControlProtocol1733.rtcpHeader.paddingBit-2",
        "RtcpHeaderSubtype": "realTimeTransportControlProtocol1733.rtcpHeader.subtype-3",
        "RtcpHeaderPacketType": "realTimeTransportControlProtocol1733.rtcpHeader.packetType-4",
        "RtcpHeaderMessageLength": "realTimeTransportControlProtocol1733.rtcpHeader.messageLength-5",
        "RtcpHeaderSsrc/csrc": "realTimeTransportControlProtocol1733.rtcpHeader.ssrc/csrc-6",
        "RtcpHeaderName": "realTimeTransportControlProtocol1733.rtcpHeader.name-7",
        "RtcpHeaderGmTimeBaseIndicator": "realTimeTransportControlProtocol1733.rtcpHeader.gmTimeBaseIndicator-8",
        "RtcpHeaderGmIdentity": "realTimeTransportControlProtocol1733.rtcpHeader.gmIdentity-9",
        "RtcpHeaderStream_id": "realTimeTransportControlProtocol1733.rtcpHeader.stream_id-10",
        "RtcpHeaderAsTimestamp": "realTimeTransportControlProtocol1733.rtcpHeader.asTimestamp-11",
        "RtcpHeaderRtpTimestamp": "realTimeTransportControlProtocol1733.rtcpHeader.rtpTimestamp-12",
    }

    def __init__(self, parent, list_op=False):
        super(RealTimeTransportControlProtocol1733, self).__init__(parent, list_op)

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
    def RtcpHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderSubtype"])
        )

    @property
    def RtcpHeaderPacketType(self):
        """
        Display Name: Packet Type
        Default Value: 208
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderPacketType"])
        )

    @property
    def RtcpHeaderMessageLength(self):
        """
        Display Name: Message Length
        Default Value: 0x9
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderMessageLength"])
        )

    @property
    def RtcpHeaderSsrccsrc(self):
        """
        Display Name: SSRC/CSRC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderSsrc/csrc"])
        )

    @property
    def RtcpHeaderName(self):
        """
        Display Name: Name
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderName"])
        )

    @property
    def RtcpHeaderGmTimeBaseIndicator(self):
        """
        Display Name: gm Time Base Indicator
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderGmTimeBaseIndicator"]),
        )

    @property
    def RtcpHeaderGmIdentity(self):
        """
        Display Name: gm Identity
        Default Value: 0x00
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderGmIdentity"])
        )

    @property
    def RtcpHeaderStream_id(self):
        """
        Display Name: Stream Id
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderStream_id"])
        )

    @property
    def RtcpHeaderAsTimestamp(self):
        """
        Display Name: As Timestamp
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderAsTimestamp"])
        )

    @property
    def RtcpHeaderRtpTimestamp(self):
        """
        Display Name: RTP Timestamp
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtcpHeaderRtpTimestamp"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
