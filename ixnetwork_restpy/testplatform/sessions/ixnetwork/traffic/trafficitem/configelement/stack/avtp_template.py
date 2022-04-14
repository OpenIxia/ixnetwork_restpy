from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Avtp(Base):
    __slots__ = ()
    _SDM_NAME = "avtp"
    _SDM_ATT_MAP = {
        "AvtpCommonHeaderControlDataIndicator": "avtp.header.avtpCommonHeader.controlDataIndicator-1",
        "AvtpCommonHeaderSubtype": "avtp.header.avtpCommonHeader.subtype-2",
        "AvtpCommonHeaderStreamIdValid": "avtp.header.avtpCommonHeader.streamIdValid-3",
        "AvtpCommonHeaderVersion": "avtp.header.avtpCommonHeader.version-4",
        "AvtpTypeSpecificHeaderMediaClockRestart": "avtp.header.avtpTypeSpecificHeader.mediaClockRestart-5",
        "AvtpTypeSpecificHeaderReservedField": "avtp.header.avtpTypeSpecificHeader.reservedField-6",
        "AvtpTypeSpecificHeaderGatewayInfoValid": "avtp.header.avtpTypeSpecificHeader.gatewayInfoValid-7",
        "AvtpTypeSpecificHeaderAvtpTimeStampValid": "avtp.header.avtpTypeSpecificHeader.avtpTimeStampValid-8",
        "AvtpTypeSpecificHeaderSequenceNumber": "avtp.header.avtpTypeSpecificHeader.sequenceNumber-9",
        "AvtpTypeSpecificHeaderReservedField2": "avtp.header.avtpTypeSpecificHeader.reservedField2-10",
        "AvtpTypeSpecificHeaderTimeStampUncertain": "avtp.header.avtpTypeSpecificHeader.timeStampUncertain-11",
        "SrpStreamIdStreamId": "avtp.header.srpStreamId.streamId-12",
        "SrpStreamIdStream_name": "avtp.header.srpStreamId.stream_name-13",
        "SrpStreamIdAvtpTimestamp": "avtp.header.srpStreamId.avtpTimestamp-14",
        "SrpStreamIdGatewayInfo": "avtp.header.srpStreamId.gatewayInfo-15",
        "SrpStreamIdStreamDataLength": "avtp.header.srpStreamId.streamDataLength-16",
        "ProtocolSpecificHeaderTag": "avtp.header.packetInformation.protocolSpecificHeader.Tag-17",
        "ProtocolSpecificHeaderChannel": "avtp.header.packetInformation.protocolSpecificHeader.Channel-18",
        "ProtocolSpecificHeaderTCode": "avtp.header.packetInformation.protocolSpecificHeader.tCode-19",
        "ProtocolSpecificHeaderSyField": "avtp.header.packetInformation.protocolSpecificHeader.syField-20",
    }

    def __init__(self, parent, list_op=False):
        super(Avtp, self).__init__(parent, list_op)

    @property
    def AvtpCommonHeaderControlDataIndicator(self):
        """
        Display Name: CD
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpCommonHeaderControlDataIndicator"]
            ),
        )

    @property
    def AvtpCommonHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AvtpCommonHeaderSubtype"])
        )

    @property
    def AvtpCommonHeaderStreamIdValid(self):
        """
        Display Name: SV
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AvtpCommonHeaderStreamIdValid"]),
        )

    @property
    def AvtpCommonHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AvtpCommonHeaderVersion"])
        )

    @property
    def AvtpTypeSpecificHeaderMediaClockRestart(self):
        """
        Display Name: Mr
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpTypeSpecificHeaderMediaClockRestart"]
            ),
        )

    @property
    def AvtpTypeSpecificHeaderReservedField(self):
        """
        Display Name: R
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpTypeSpecificHeaderReservedField"]
            ),
        )

    @property
    def AvtpTypeSpecificHeaderGatewayInfoValid(self):
        """
        Display Name: GV
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpTypeSpecificHeaderGatewayInfoValid"]
            ),
        )

    @property
    def AvtpTypeSpecificHeaderAvtpTimeStampValid(self):
        """
        Display Name: TV
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpTypeSpecificHeaderAvtpTimeStampValid"]
            ),
        )

    @property
    def AvtpTypeSpecificHeaderSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpTypeSpecificHeaderSequenceNumber"]
            ),
        )

    @property
    def AvtpTypeSpecificHeaderReservedField2(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpTypeSpecificHeaderReservedField2"]
            ),
        )

    @property
    def AvtpTypeSpecificHeaderTimeStampUncertain(self):
        """
        Display Name: TU
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpTypeSpecificHeaderTimeStampUncertain"]
            ),
        )

    @property
    def SrpStreamIdStreamId(self):
        """
        Display Name: Stream ID
        Default Value: 0x2222222222220001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrpStreamIdStreamId"])
        )

    @property
    def SrpStreamIdStream_name(self):
        """
        Display Name: Stream Name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrpStreamIdStream_name"])
        )

    @property
    def SrpStreamIdAvtpTimestamp(self):
        """
        Display Name: AVTP Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrpStreamIdAvtpTimestamp"])
        )

    @property
    def SrpStreamIdGatewayInfo(self):
        """
        Display Name: Gateway Info
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrpStreamIdGatewayInfo"])
        )

    @property
    def SrpStreamIdStreamDataLength(self):
        """
        Display Name: Stream Data Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrpStreamIdStreamDataLength"])
        )

    @property
    def ProtocolSpecificHeaderTag(self):
        """
        Display Name: Tag
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolSpecificHeaderTag"])
        )

    @property
    def ProtocolSpecificHeaderChannel(self):
        """
        Display Name: Channel
        Default Value: 31
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ProtocolSpecificHeaderChannel"]),
        )

    @property
    def ProtocolSpecificHeaderTCode(self):
        """
        Display Name: Type Code
        Default Value: 0xA
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolSpecificHeaderTCode"])
        )

    @property
    def ProtocolSpecificHeaderSyField(self):
        """
        Display Name: Sy Field
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ProtocolSpecificHeaderSyField"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
