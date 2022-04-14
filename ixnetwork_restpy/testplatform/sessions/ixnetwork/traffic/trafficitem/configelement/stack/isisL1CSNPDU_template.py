from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisL1CSNPDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisL1CSNPDU"
    _SDM_ATT_MAP = {
        "CommonHeaderIntradomainRoutingProtocolDiscriminator": "isisL1CSNPDU.isisHeader.commonHeader.intradomainRoutingProtocolDiscriminator-1",
        "CommonHeaderLengthIndicator": "isisL1CSNPDU.isisHeader.commonHeader.lengthIndicator-2",
        "CommonHeaderVersionProtocolIDExtension": "isisL1CSNPDU.isisHeader.commonHeader.versionProtocolIDExtension-3",
        "CommonHeaderIdLength": "isisL1CSNPDU.isisHeader.commonHeader.idLength-4",
        "CommonHeaderReservedBit": "isisL1CSNPDU.isisHeader.commonHeader.reservedBit-5",
        "CommonHeaderPduType": "isisL1CSNPDU.isisHeader.commonHeader.pduType-6",
        "CommonHeaderVersion": "isisL1CSNPDU.isisHeader.commonHeader.version-7",
        "CommonHeaderReserved": "isisL1CSNPDU.isisHeader.commonHeader.reserved-8",
        "CommonHeaderMaximumAreaAddresses": "isisL1CSNPDU.isisHeader.commonHeader.maximumAreaAddresses-9",
        "FixedHeaderPduLength": "isisL1CSNPDU.isisHeader.fixedHeader.pduLength-10",
        "FixedHeaderSourceID": "isisL1CSNPDU.isisHeader.fixedHeader.sourceID-11",
        "FixedHeaderStartLSPID": "isisL1CSNPDU.isisHeader.fixedHeader.startLSPID-12",
        "FixedHeaderEndLSPID": "isisL1CSNPDU.isisHeader.fixedHeader.endLSPID-13",
        "Tlv9LSPEntriesTlvCode": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv9LSPEntries.tlvCode-14",
        "Tlv9LSPEntriesTlvLength": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv9LSPEntries.tlvLength-15",
        "ValueFieldsRemainingLifetime": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv9LSPEntries.valueFields.remainingLifetime-16",
        "LspIDPseudonodeID": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv9LSPEntries.valueFields.lspID.pseudonodeID-17",
        "LspIDLspNumber": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv9LSPEntries.valueFields.lspID.lspNumber-18",
        "ValueFieldsSequenceNumber": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv9LSPEntries.valueFields.sequenceNumber-19",
        "ValueFieldsChecksum": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv9LSPEntries.valueFields.checksum-20",
        "Tlv10AuthenticationInformationTlvCode": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvCode-21",
        "Tlv10AuthenticationInformationTlvLength": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvLength-22",
        "ValueFieldsAuthenticationType": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationType-23",
        "ValueFieldsAuthenticationValue": "isisL1CSNPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationValue-24",
    }

    def __init__(self, parent, list_op=False):
        super(IsisL1CSNPDU, self).__init__(parent, list_op)

    @property
    def CommonHeaderIntradomainRoutingProtocolDiscriminator(self):
        """
        Display Name: Intradomain routing protocol discriminator
        Default Value: 0x83
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonHeaderIntradomainRoutingProtocolDiscriminator"]
            ),
        )

    @property
    def CommonHeaderLengthIndicator(self):
        """
        Display Name: Length indicator
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderLengthIndicator"])
        )

    @property
    def CommonHeaderVersionProtocolIDExtension(self):
        """
        Display Name: Version/Protocol ID extension
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CommonHeaderVersionProtocolIDExtension"]
            ),
        )

    @property
    def CommonHeaderIdLength(self):
        """
        Display Name: ID length
        Default Value: 0
        Value Format: decimal
        Available enum values: One, 1, Two, 2, Three, 3, Four, 4, Five, 5, Six, 6, Seven, 7, Eight, 8, 6 Octet ID field, 0, Null ID field, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderIdLength"])
        )

    @property
    def CommonHeaderReservedBit(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderReservedBit"])
        )

    @property
    def CommonHeaderPduType(self):
        """
        Display Name: PDU type
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderPduType"])
        )

    @property
    def CommonHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderVersion"])
        )

    @property
    def CommonHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderReserved"])
        )

    @property
    def CommonHeaderMaximumAreaAddresses(self):
        """
        Display Name: Maximum area addresses
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHeaderMaximumAreaAddresses"]),
        )

    @property
    def FixedHeaderPduLength(self):
        """
        Display Name: PDU length
        Default Value: 1497
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderPduLength"])
        )

    @property
    def FixedHeaderSourceID(self):
        """
        Display Name: Source ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderSourceID"])
        )

    @property
    def FixedHeaderStartLSPID(self):
        """
        Display Name: Start LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderStartLSPID"])
        )

    @property
    def FixedHeaderEndLSPID(self):
        """
        Display Name: End LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderEndLSPID"])
        )

    @property
    def Tlv9LSPEntriesTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv9LSPEntriesTlvCode"])
        )

    @property
    def Tlv9LSPEntriesTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv9LSPEntriesTlvLength"])
        )

    @property
    def ValueFieldsRemainingLifetime(self):
        """
        Display Name: Remaining lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsRemainingLifetime"])
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
    def ValueFieldsSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsSequenceNumber"])
        )

    @property
    def ValueFieldsChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsChecksum"])
        )

    @property
    def Tlv10AuthenticationInformationTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv10AuthenticationInformationTlvCode"]
            ),
        )

    @property
    def Tlv10AuthenticationInformationTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv10AuthenticationInformationTlvLength"]
            ),
        )

    @property
    def ValueFieldsAuthenticationType(self):
        """
        Display Name: Authentication type
        Default Value: 1
        Value Format: decimal
        Available enum values: Cleartext password, 1, Routing domain private authentication method, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAuthenticationType"]),
        )

    @property
    def ValueFieldsAuthenticationValue(self):
        """
        Display Name: Authentication value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAuthenticationValue"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
