from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisL1McastCSNPDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisL1McastCSNPDU"
    _SDM_ATT_MAP = {
        "CommonHeaderL1ProtocolDiscriminator": "isisL1McastCSNPDU.header.commonHeaderL1.protocolDiscriminator-1",
        "CommonHeaderL1LengthIndicator": "isisL1McastCSNPDU.header.commonHeaderL1.lengthIndicator-2",
        "CommonHeaderL1VersionProtocolID": "isisL1McastCSNPDU.header.commonHeaderL1.versionProtocolID-3",
        "CommonHeaderL1IdLength": "isisL1McastCSNPDU.header.commonHeaderL1.idLength-4",
        "CommonHeaderL1Reserved1": "isisL1McastCSNPDU.header.commonHeaderL1.reserved1-5",
        "CommonHeaderL1PduTypeL1CSNP": "isisL1McastCSNPDU.header.commonHeaderL1.pduTypeL1CSNP-6",
        "CommonHeaderL1Version": "isisL1McastCSNPDU.header.commonHeaderL1.version-7",
        "CommonHeaderL1Reserved2": "isisL1McastCSNPDU.header.commonHeaderL1.reserved2-8",
        "CommonHeaderL1MaxAreaAddresses": "isisL1McastCSNPDU.header.commonHeaderL1.maxAreaAddresses-9",
        "FixedHeaderL1CSNPPduLength": "isisL1McastCSNPDU.header.fixedHeaderL1CSNP.pduLength-10",
        "FixedHeaderL1CSNPSourceID": "isisL1McastCSNPDU.header.fixedHeaderL1CSNP.sourceID-11",
        "FixedHeaderL1CSNPStartLSPID": "isisL1McastCSNPDU.header.fixedHeaderL1CSNP.startLSPID-12",
        "FixedHeaderL1CSNPEndLSPID": "isisL1McastCSNPDU.header.fixedHeaderL1CSNP.endLSPID-13",
        "Tlv9Code": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv9.code-14",
        "Tlv9Length": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv9.length-15",
        "ValueRemainingLlifetime": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv9.value.remainingLlifetime-16",
        "LspIDPseudonodeID": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv9.value.lspID.pseudonodeID-17",
        "LspIDLspNumber": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv9.value.lspID.lspNumber-18",
        "ValueSequenceNumber": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv9.value.sequenceNumber-19",
        "ValueChecksum": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv9.value.checksum-20",
        "Tlv10Code": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv10.code-21",
        "Tlv10Length": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv10.length-22",
        "ValueAuthenticationType": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv10.value.authenticationType-23",
        "ValueAuthenticationValue": "isisL1McastCSNPDU.header.variableHeaderL1CSNP.tlvHeader.tlv10.value.authenticationValue-24",
    }

    def __init__(self, parent, list_op=False):
        super(IsisL1McastCSNPDU, self).__init__(parent, list_op)

    @property
    def CommonHeaderL1ProtocolDiscriminator(self):
        """
        Display Name: Intradomain routing protocol discriminator
        Default Value: 0x83
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonHeaderL1ProtocolDiscriminator"]
            ),
        )

    @property
    def CommonHeaderL1LengthIndicator(self):
        """
        Display Name: Length indicator
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1LengthIndicator"]),
        )

    @property
    def CommonHeaderL1VersionProtocolID(self):
        """
        Display Name: Version/Protocol ID extension
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1VersionProtocolID"]),
        )

    @property
    def CommonHeaderL1IdLength(self):
        """
        Display Name: ID length
        Default Value: 0
        Value Format: decimal
        Available enum values: One, 1, Two, 2, Three, 3, Four, 4, Five, 5, Six, 6, Seven, 7, Eight, 8, 6 Octet ID field, 0, Null ID field, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1IdLength"])
        )

    @property
    def CommonHeaderL1Reserved1(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1Reserved1"])
        )

    @property
    def CommonHeaderL1PduTypeL1CSNP(self):
        """
        Display Name: PDU type
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1PduTypeL1CSNP"])
        )

    @property
    def CommonHeaderL1Version(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1Version"])
        )

    @property
    def CommonHeaderL1Reserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1Reserved2"])
        )

    @property
    def CommonHeaderL1MaxAreaAddresses(self):
        """
        Display Name: Maximum area addresses
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1MaxAreaAddresses"]),
        )

    @property
    def FixedHeaderL1CSNPPduLength(self):
        """
        Display Name: PDU length
        Default Value: 1497
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1CSNPPduLength"])
        )

    @property
    def FixedHeaderL1CSNPSourceID(self):
        """
        Display Name: Source ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1CSNPSourceID"])
        )

    @property
    def FixedHeaderL1CSNPStartLSPID(self):
        """
        Display Name: Start LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1CSNPStartLSPID"])
        )

    @property
    def FixedHeaderL1CSNPEndLSPID(self):
        """
        Display Name: End LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1CSNPEndLSPID"])
        )

    @property
    def Tlv9Code(self):
        """
        Display Name: TLV code
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv9Code"]))

    @property
    def Tlv9Length(self):
        """
        Display Name: TLV length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv9Length"]))

    @property
    def ValueRemainingLlifetime(self):
        """
        Display Name: Remaining lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueRemainingLlifetime"])
        )

    @property
    def LspIDPseudonodeID(self):
        """
        Display Name: Pseudonode ID
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LspIDPseudonodeID"])
        )

    @property
    def LspIDLspNumber(self):
        """
        Display Name: LSP number
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LspIDLspNumber"])
        )

    @property
    def ValueSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueSequenceNumber"])
        )

    @property
    def ValueChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueChecksum"]))

    @property
    def Tlv10Code(self):
        """
        Display Name: TLV code
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv10Code"]))

    @property
    def Tlv10Length(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv10Length"]))

    @property
    def ValueAuthenticationType(self):
        """
        Display Name: Authentication type
        Default Value: 1
        Value Format: decimal
        Available enum values: Cleartext password, 1, Routing domain private authentication method, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueAuthenticationType"])
        )

    @property
    def ValueAuthenticationValue(self):
        """
        Display Name: Authentication value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueAuthenticationValue"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
