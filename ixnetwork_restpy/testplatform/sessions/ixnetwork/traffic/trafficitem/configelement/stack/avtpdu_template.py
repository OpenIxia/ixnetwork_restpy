from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Avtpdu(Base):
    __slots__ = ()
    _SDM_NAME = "avtpdu"
    _SDM_ATT_MAP = {
        "AvtpduCommonStreamHeaderSubtype": "avtpdu.header.avtpduCommonStreamHeader.subtype-1",
        "AvtpduCommonStreamHeaderStreamIdValid": "avtpdu.header.avtpduCommonStreamHeader.streamIdValid-2",
        "AvtpduCommonStreamHeaderVersion": "avtpdu.header.avtpduCommonStreamHeader.version-3",
        "AvtpduTypeSpecificHeaderMediaClockRestart": "avtpdu.header.avtpduTypeSpecificHeader.mediaClockRestart-4",
        "AvtpduTypeSpecificHeaderRsv": "avtpdu.header.avtpduTypeSpecificHeader.rsv-5",
        "AvtpduTypeSpecificHeaderAvtpTimeStampValid": "avtpdu.header.avtpduTypeSpecificHeader.avtpTimeStampValid-6",
        "AvtpduTypeSpecificHeaderSequenceNumber": "avtpdu.header.avtpduTypeSpecificHeader.sequenceNumber-7",
        "AvtpduTypeSpecificHeaderReservedField": "avtpdu.header.avtpduTypeSpecificHeader.reservedField-8",
        "AvtpduTypeSpecificHeaderTimeStampUncertain": "avtpdu.header.avtpduTypeSpecificHeader.timeStampUncertain-9",
        "AvtpduStreamIdStreamId": "avtpdu.header.avtpduStreamId.streamId-10",
        "AvtpduStreamIdAvtpTimestamp": "avtpdu.header.avtpduStreamId.avtpTimestamp-11",
        "FormatInformationFormat": "avtpdu.header.selectInitialPart.formatInformation.Format-12",
        "FormatInformationFormatSubtype": "avtpdu.header.selectInitialPart.formatInformation.formatSubtype-13",
        "FormatInformationReservedField3": "avtpdu.header.selectInitialPart.formatInformation.reservedField3-14",
        "SdiSpecificInformationFormat": "avtpdu.header.selectInitialPart.sdiSpecificInformation.Format-15",
        "SdiSpecificInformationISequenceNumber": "avtpdu.header.selectInitialPart.sdiSpecificInformation.iSequenceNumber-16",
        "SdiSpecificInformationPacketInformation": "avtpdu.header.selectInitialPart.sdiSpecificInformation.packetInformation-17",
        "PacketInformationStreamdataLength": "avtpdu.header.packetInformation.streamdataLength-18",
        "TypeIRsv": "avtpdu.header.packetInformation.protocolSpecificHeader.selectInitialPart.typeI.Rsv-19",
        "TypeIM": "avtpdu.header.packetInformation.protocolSpecificHeader.selectInitialPart.typeI.M-20",
        "TypeIIReservedField5": "avtpdu.header.packetInformation.protocolSpecificHeader.selectInitialPart.typeII.reservedField5-21",
        "TypeIIGuardBand": "avtpdu.header.packetInformation.protocolSpecificHeader.selectInitialPart.typeII.guardBand-22",
        "TypeIIRp168Switch": "avtpdu.header.packetInformation.protocolSpecificHeader.selectInitialPart.typeII.rp168Switch-23",
        "TypeIIEndFrame": "avtpdu.header.packetInformation.protocolSpecificHeader.selectInitialPart.typeII.endFrame-24",
        "ProtocolSpecificHeaderEVT": "avtpdu.header.packetInformation.protocolSpecificHeader.EVT-25",
        "ProtocolSpecificHeaderReservedField4": "avtpdu.header.packetInformation.protocolSpecificHeader.reservedField4-26",
    }

    def __init__(self, parent, list_op=False):
        super(Avtpdu, self).__init__(parent, list_op)

    @property
    def AvtpduCommonStreamHeaderSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AvtpduCommonStreamHeaderSubtype"]),
        )

    @property
    def AvtpduCommonStreamHeaderStreamIdValid(self):
        """
        Display Name: SV
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpduCommonStreamHeaderStreamIdValid"]
            ),
        )

    @property
    def AvtpduCommonStreamHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AvtpduCommonStreamHeaderVersion"]),
        )

    @property
    def AvtpduTypeSpecificHeaderMediaClockRestart(self):
        """
        Display Name: Mr
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpduTypeSpecificHeaderMediaClockRestart"]
            ),
        )

    @property
    def AvtpduTypeSpecificHeaderRsv(self):
        """
        Display Name: RSV
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AvtpduTypeSpecificHeaderRsv"])
        )

    @property
    def AvtpduTypeSpecificHeaderAvtpTimeStampValid(self):
        """
        Display Name: TV
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpduTypeSpecificHeaderAvtpTimeStampValid"]
            ),
        )

    @property
    def AvtpduTypeSpecificHeaderSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpduTypeSpecificHeaderSequenceNumber"]
            ),
        )

    @property
    def AvtpduTypeSpecificHeaderReservedField(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpduTypeSpecificHeaderReservedField"]
            ),
        )

    @property
    def AvtpduTypeSpecificHeaderTimeStampUncertain(self):
        """
        Display Name: TU
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AvtpduTypeSpecificHeaderTimeStampUncertain"]
            ),
        )

    @property
    def AvtpduStreamIdStreamId(self):
        """
        Display Name: Stream ID
        Default Value: 0x2222222222220001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AvtpduStreamIdStreamId"])
        )

    @property
    def AvtpduStreamIdAvtpTimestamp(self):
        """
        Display Name: AVTP Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AvtpduStreamIdAvtpTimestamp"])
        )

    @property
    def FormatInformationFormat(self):
        """
        Display Name: Format
        Default Value: 0x2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FormatInformationFormat"])
        )

    @property
    def FormatInformationFormatSubtype(self):
        """
        Display Name: Format Subtype
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FormatInformationFormatSubtype"]),
        )

    @property
    def FormatInformationReservedField3(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FormatInformationReservedField3"]),
        )

    @property
    def SdiSpecificInformationFormat(self):
        """
        Display Name: Format
        Default Value: 0x2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SdiSpecificInformationFormat"])
        )

    @property
    def SdiSpecificInformationISequenceNumber(self):
        """
        Display Name: I Sequence Number
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SdiSpecificInformationISequenceNumber"]
            ),
        )

    @property
    def SdiSpecificInformationPacketInformation(self):
        """
        Display Name: Line Number
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SdiSpecificInformationPacketInformation"]
            ),
        )

    @property
    def PacketInformationStreamdataLength(self):
        """
        Display Name: Stream Data Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PacketInformationStreamdataLength"]),
        )

    @property
    def TypeIRsv(self):
        """
        Display Name: Rsv
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TypeIRsv"]))

    @property
    def TypeIM(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TypeIM"]))

    @property
    def TypeIIReservedField5(self):
        """
        Display Name: r
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeIIReservedField5"])
        )

    @property
    def TypeIIGuardBand(self):
        """
        Display Name: gb
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeIIGuardBand"])
        )

    @property
    def TypeIIRp168Switch(self):
        """
        Display Name: sp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeIIRp168Switch"])
        )

    @property
    def TypeIIEndFrame(self):
        """
        Display Name: ef
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeIIEndFrame"])
        )

    @property
    def ProtocolSpecificHeaderEVT(self):
        """
        Display Name: EVT
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ProtocolSpecificHeaderEVT"])
        )

    @property
    def ProtocolSpecificHeaderReservedField4(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ProtocolSpecificHeaderReservedField4"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
