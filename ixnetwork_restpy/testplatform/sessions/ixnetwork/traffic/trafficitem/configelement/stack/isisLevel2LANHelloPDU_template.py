from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisLevel2LANHelloPDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisLevel2LANHelloPDU"
    _SDM_ATT_MAP = {
        "CommonHeaderIntradomainRoutingProtocolDiscriminator": "isisLevel2LANHelloPDU.isisHeader.commonHeader.intradomainRoutingProtocolDiscriminator-1",
        "CommonHeaderLengthIndicator": "isisLevel2LANHelloPDU.isisHeader.commonHeader.lengthIndicator-2",
        "CommonHeaderVersionProtocolIDExtension": "isisLevel2LANHelloPDU.isisHeader.commonHeader.versionProtocolIDExtension-3",
        "CommonHeaderIdLength": "isisLevel2LANHelloPDU.isisHeader.commonHeader.idLength-4",
        "CommonHeaderReservedBit": "isisLevel2LANHelloPDU.isisHeader.commonHeader.reservedBit-5",
        "CommonHeaderPduType": "isisLevel2LANHelloPDU.isisHeader.commonHeader.pduType-6",
        "CommonHeaderVersion": "isisLevel2LANHelloPDU.isisHeader.commonHeader.version-7",
        "CommonHeaderReserved": "isisLevel2LANHelloPDU.isisHeader.commonHeader.reserved-8",
        "CommonHeaderMaximumAreaAddresses": "isisLevel2LANHelloPDU.isisHeader.commonHeader.maximumAreaAddresses-9",
        "FixedHeaderReservedCircuitType": "isisLevel2LANHelloPDU.isisHeader.fixedHeader.reservedCircuitType-10",
        "FixedHeaderSourceID": "isisLevel2LANHelloPDU.isisHeader.fixedHeader.sourceID-11",
        "FixedHeaderHoldingTime": "isisLevel2LANHelloPDU.isisHeader.fixedHeader.holdingTime-12",
        "FixedHeaderPduLength": "isisLevel2LANHelloPDU.isisHeader.fixedHeader.pduLength-13",
        "FixedHeaderReservedBit": "isisLevel2LANHelloPDU.isisHeader.fixedHeader.reservedBit-14",
        "FixedHeaderPriority": "isisLevel2LANHelloPDU.isisHeader.fixedHeader.priority-15",
        "FixedHeaderLanID": "isisLevel2LANHelloPDU.isisHeader.fixedHeader.lanID-16",
        "Tlv1AreaAddressesTlvCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvCode-17",
        "Tlv1AreaAddressesTlvLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvLength-18",
        "ValueFieldsAddressLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.addressLength-19",
        "ValueFieldsAreaAddress": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.areaAddress-20",
        "Tlv6ISNeighborswith6OctetMACAddressTlvCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv6ISNeighborswith6OctetMACAddress.tlvCode-21",
        "Tlv6ISNeighborswith6OctetMACAddressTlvLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv6ISNeighborswith6OctetMACAddress.tlvLength-22",
        "Tlv6ISNeighborswith6OctetMACAddressLanAddress": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv6ISNeighborswith6OctetMACAddress.lanAddress-23",
        "Tlv7ISNeighborswithVariableLengthSNPAAddressTlvCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.tlvCode-24",
        "Tlv7ISNeighborswithVariableLengthSNPAAddressTlvLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.tlvLength-25",
        "ValueFieldsLanAddressLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.valueFields.lanAddressLength-26",
        "ValueFieldsLanAddress": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.valueFields.lanAddress-27",
        "Tlv8PaddingTlvCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.tlvCode-28",
        "Tlv8PaddingTlvLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.tlvLength-29",
        "ValueFieldsPadding": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.valueFields.padding-30",
        "Tlv10AuthenticationInformationTlvCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvCode-31",
        "Tlv10AuthenticationInformationTlvLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvLength-32",
        "ValueFieldsAuthenticationType": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationType-33",
        "ValueFieldsAuthenticatorLengthoctets": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticatorLengthoctets-34",
        "ValueFieldsAuthenticator": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticator-35",
        "Tlv129ProtocolsSupportedCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.code-36",
        "Tlv129ProtocolsSupportedLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.length-37",
        "NlpidEntriesEntryLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.entryLength-38",
        "NlpidEntriesEntryID": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.entryID-39",
        "Tlv132IPInterfaceAddressCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.code-40",
        "Tlv132IPInterfaceAddressLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.length-41",
        "IpAddressEntriesIpAddress": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.ipAddressEntries.ipAddress-42",
        "Tlv232IPv6InterfaceAddressCode": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.code-43",
        "Tlv232IPv6InterfaceAddressLength": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.length-44",
        "Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress": "isisLevel2LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.ipAddressEntries.ipAddress-45",
    }

    def __init__(self, parent, list_op=False):
        super(IsisLevel2LANHelloPDU, self).__init__(parent, list_op)

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
        Default Value: 16
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
    def FixedHeaderReservedCircuitType(self):
        """
        Display Name: Reserved/Circuit type
        Default Value: 2
        Value Format: decimal
        Available enum values: Reserved value, 0, Level 1 only, 1, Level 2 only, 2, Both level 1 and 2, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FixedHeaderReservedCircuitType"]),
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
    def FixedHeaderHoldingTime(self):
        """
        Display Name: Holding time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderHoldingTime"])
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
    def FixedHeaderReservedBit(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Must be Zero, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderReservedBit"])
        )

    @property
    def FixedHeaderPriority(self):
        """
        Display Name: Priority
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderPriority"])
        )

    @property
    def FixedHeaderLanID(self):
        """
        Display Name: LAN ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderLanID"])
        )

    @property
    def Tlv1AreaAddressesTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv1AreaAddressesTlvCode"])
        )

    @property
    def Tlv1AreaAddressesTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv1AreaAddressesTlvLength"])
        )

    @property
    def ValueFieldsAddressLength(self):
        """
        Display Name: Address length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAddressLength"])
        )

    @property
    def ValueFieldsAreaAddress(self):
        """
        Display Name: Area address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAreaAddress"])
        )

    @property
    def Tlv6ISNeighborswith6OctetMACAddressTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv6ISNeighborswith6OctetMACAddressTlvCode"]
            ),
        )

    @property
    def Tlv6ISNeighborswith6OctetMACAddressTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv6ISNeighborswith6OctetMACAddressTlvLength"]
            ),
        )

    @property
    def Tlv6ISNeighborswith6OctetMACAddressLanAddress(self):
        """
        Display Name: LAN address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv6ISNeighborswith6OctetMACAddressLanAddress"]
            ),
        )

    @property
    def Tlv7ISNeighborswithVariableLengthSNPAAddressTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv7ISNeighborswithVariableLengthSNPAAddressTlvCode"]
            ),
        )

    @property
    def Tlv7ISNeighborswithVariableLengthSNPAAddressTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv7ISNeighborswithVariableLengthSNPAAddressTlvLength"
                ]
            ),
        )

    @property
    def ValueFieldsLanAddressLength(self):
        """
        Display Name: LAN address length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsLanAddressLength"])
        )

    @property
    def ValueFieldsLanAddress(self):
        """
        Display Name: LAN address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsLanAddress"])
        )

    @property
    def Tlv8PaddingTlvCode(self):
        """
        Display Name: TLV code
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv8PaddingTlvCode"])
        )

    @property
    def Tlv8PaddingTlvLength(self):
        """
        Display Name: TLV length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv8PaddingTlvLength"])
        )

    @property
    def ValueFieldsPadding(self):
        """
        Display Name: Padding
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsPadding"])
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
    def ValueFieldsAuthenticatorLengthoctets(self):
        """
        Display Name: Authenticator Length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ValueFieldsAuthenticatorLengthoctets"]
            ),
        )

    @property
    def ValueFieldsAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueFieldsAuthenticator"])
        )

    @property
    def Tlv129ProtocolsSupportedCode(self):
        """
        Display Name: Code
        Default Value: 129
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv129ProtocolsSupportedCode"])
        )

    @property
    def Tlv129ProtocolsSupportedLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv129ProtocolsSupportedLength"]),
        )

    @property
    def NlpidEntriesEntryLength(self):
        """
        Display Name: Entry Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NlpidEntriesEntryLength"])
        )

    @property
    def NlpidEntriesEntryID(self):
        """
        Display Name: Entry ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NlpidEntriesEntryID"])
        )

    @property
    def Tlv132IPInterfaceAddressCode(self):
        """
        Display Name: Code
        Default Value: 132
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv132IPInterfaceAddressCode"])
        )

    @property
    def Tlv132IPInterfaceAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv132IPInterfaceAddressLength"]),
        )

    @property
    def IpAddressEntriesIpAddress(self):
        """
        Display Name: IP Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpAddressEntriesIpAddress"])
        )

    @property
    def Tlv232IPv6InterfaceAddressCode(self):
        """
        Display Name: Code
        Default Value: 232
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv232IPv6InterfaceAddressCode"]),
        )

    @property
    def Tlv232IPv6InterfaceAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv232IPv6InterfaceAddressLength"]),
        )

    @property
    def Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress(self):
        """
        Display Name: IP Address
        Default Value: 0:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
