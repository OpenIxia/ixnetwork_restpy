from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisPointToPointHelloPDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisPointToPointHelloPDU"
    _SDM_ATT_MAP = {
        "CommonHeaderIntradomainRoutingProtocolDiscriminator": "isisPointToPointHelloPDU.isisHeader.commonHeader.intradomainRoutingProtocolDiscriminator-1",
        "CommonHeaderLengthIndicator": "isisPointToPointHelloPDU.isisHeader.commonHeader.lengthIndicator-2",
        "CommonHeaderVersionProtocolIDExtension": "isisPointToPointHelloPDU.isisHeader.commonHeader.versionProtocolIDExtension-3",
        "CommonHeaderIdLength": "isisPointToPointHelloPDU.isisHeader.commonHeader.idLength-4",
        "CommonHeaderReservedBit": "isisPointToPointHelloPDU.isisHeader.commonHeader.reservedBit-5",
        "CommonHeaderPduType": "isisPointToPointHelloPDU.isisHeader.commonHeader.pduType-6",
        "CommonHeaderVersion": "isisPointToPointHelloPDU.isisHeader.commonHeader.version-7",
        "CommonHeaderReserved": "isisPointToPointHelloPDU.isisHeader.commonHeader.reserved-8",
        "CommonHeaderMaximumAreaAddresses": "isisPointToPointHelloPDU.isisHeader.commonHeader.maximumAreaAddresses-9",
        "FixedHeaderReservedCircuitType": "isisPointToPointHelloPDU.isisHeader.fixedHeader.reservedCircuitType-10",
        "FixedHeaderSourceID": "isisPointToPointHelloPDU.isisHeader.fixedHeader.sourceID-11",
        "FixedHeaderHoldingTime": "isisPointToPointHelloPDU.isisHeader.fixedHeader.holdingTime-12",
        "FixedHeaderPduLength": "isisPointToPointHelloPDU.isisHeader.fixedHeader.pduLength-13",
        "FixedHeaderCircuitID": "isisPointToPointHelloPDU.isisHeader.fixedHeader.circuitID-14",
        "Tlv1AreaAddressesTlvCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvCode-15",
        "Tlv1AreaAddressesTlvLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvLength-16",
        "ValueFieldsAddressLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.addressLength-17",
        "ValueFieldsAreaAddress": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.areaAddress-18",
        "Tlv8PaddingTlvCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.tlvCode-19",
        "Tlv8PaddingTlvLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.tlvLength-20",
        "ValueFieldsPadding": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.valueFields.padding-21",
        "Tlv10AuthenticationInformationTlvCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvCode-22",
        "Tlv10AuthenticationInformationTlvLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvLength-23",
        "ValueFieldsAuthenticationType": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationType-24",
        "ValueFieldsAuthenticatorLengthoctets": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticatorLengthoctets-25",
        "ValueFieldsAuthenticator": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticator-26",
        "Tlv129ProtocolsSupportedCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.code-27",
        "Tlv129ProtocolsSupportedLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.length-28",
        "NlpidEntriesEntryLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.entryLength-29",
        "NlpidEntriesEntryID": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.entryID-30",
        "Tlv132IPInterfaceAddressCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.code-31",
        "Tlv132IPInterfaceAddressLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.length-32",
        "IpAddressEntriesIpAddress": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.ipAddressEntries.ipAddress-33",
        "Tlv232IPv6InterfaceAddressCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.code-34",
        "Tlv232IPv6InterfaceAddressLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.length-35",
        "Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.ipAddressEntries.ipAddress-36",
        "Tlv144MTPortCapabilityCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.code-37",
        "Tlv144MTPortCapabilityLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.length-38",
        "ValueRbit": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.rbit-39",
        "ValueMtID": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.mtID-40",
        "SubTLVHeaderTypeNoSubTLVs": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.noSubTLVs-41",
        "BasevidType": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.basevid.type-42",
        "BasevidLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.basevid.length-43",
        "Ectbvid-tupleEct_algo": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.basevid.ectbvid-tuple.ect_algo-44",
        "Ectbvid-tupleBasevid": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.basevid.ectbvid-tuple.basevid-45",
        "Ectbvid-tupleUBit": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.basevid.ectbvid-tuple.UBit-46",
        "Ectbvid-tupleMBit": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.basevid.ectbvid-tuple.MBit-47",
        "Ectbvid-tupleRsvbit": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv144MTPortCapability.value.subTLVHeader.subTLVHeaderType.basevid.ectbvid-tuple.rsvbit-48",
        "Tlv240P2PThreeWayAdjacencyCode": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv240P2PThreeWayAdjacency.code-49",
        "Tlv240P2PThreeWayAdjacencyLength": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv240P2PThreeWayAdjacency.length-50",
        "Tlv240P2PThreeWayAdjacencyAdjacencyThreeWayState": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv240P2PThreeWayAdjacency.adjacencyThreeWayState-51",
        "Tlv240P2PThreeWayAdjacencyExtendedLocalCircuitID": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv240P2PThreeWayAdjacency.extendedLocalCircuitID-52",
        "Tlv240P2PThreeWayAdjacencySystemID": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv240P2PThreeWayAdjacency.systemID-53",
        "Tlv240P2PThreeWayAdjacencyNeighborExtendedLocalCircuitID": "isisPointToPointHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv240P2PThreeWayAdjacency.neighborExtendedLocalCircuitID-54",
    }

    def __init__(self, parent, list_op=False):
        super(IsisPointToPointHelloPDU, self).__init__(parent, list_op)

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
        Default Value: 17
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
        Default Value: 3
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
        Default Value: 30
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
    def FixedHeaderCircuitID(self):
        """
        Display Name: Circuit ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderCircuitID"])
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

    @property
    def Tlv144MTPortCapabilityCode(self):
        """
        Display Name: Code
        Default Value: 143
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv144MTPortCapabilityCode"])
        )

    @property
    def Tlv144MTPortCapabilityLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv144MTPortCapabilityLength"])
        )

    @property
    def ValueRbit(self):
        """
        Display Name: Reserved Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueRbit"]))

    @property
    def ValueMtID(self):
        """
        Display Name: MT ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueMtID"]))

    @property
    def SubTLVHeaderTypeNoSubTLVs(self):
        """
        Display Name: No sub-TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubTLVHeaderTypeNoSubTLVs"])
        )

    @property
    def BasevidType(self):
        """
        Display Name: TYPE
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BasevidType"]))

    @property
    def BasevidLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BasevidLength"]))

    @property
    def EctbvidtupleEct_algo(self):
        """
        Display Name: ECT Algorithm
        Default Value: 8438273
        Value Format: decimal
        Available enum values: ECT_ALGORITHM 1, 8438273, ECT_ALGORITHM 2, 8438274, ECT_ALGORITHM 3, 8438275, ECT_ALGORITHM 4, 8438276, ECT_ALGORITHM 5, 8438277, ECT_ALGORITHM 6, 8438278, ECT_ALGORITHM 7, 8438279, ECT_ALGORITHM 8, 8438280, ECT_ALGORITHM 9, 8438281, ECT_ALGORITHM 10, 8438282, ECT_ALGORITHM 11, 8438283, ECT_ALGORITHM 12, 8438284, ECT_ALGORITHM 13, 8438285, ECT_ALGORITHM 14, 8438286, ECT_ALGORITHM 15, 8438287, ECT_ALGORITHM 16, 8438288
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ectbvid-tupleEct_algo"])
        )

    @property
    def EctbvidtupleBasevid(self):
        """
        Display Name: Base-Vid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ectbvid-tupleBasevid"])
        )

    @property
    def EctbvidtupleUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: U-bit disabled, 0, U-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ectbvid-tupleUBit"])
        )

    @property
    def EctbvidtupleMBit(self):
        """
        Display Name: M bit
        Default Value: 0
        Value Format: decimal
        Available enum values: M-bit disabled, 0, M-bit enabled, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ectbvid-tupleMBit"])
        )

    @property
    def EctbvidtupleRsvbit(self):
        """
        Display Name: Reserved Bits
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ectbvid-tupleRsvbit"])
        )

    @property
    def Tlv240P2PThreeWayAdjacencyCode(self):
        """
        Display Name: Code
        Default Value: 240
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv240P2PThreeWayAdjacencyCode"]),
        )

    @property
    def Tlv240P2PThreeWayAdjacencyLength(self):
        """
        Display Name: Length
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv240P2PThreeWayAdjacencyLength"]),
        )

    @property
    def Tlv240P2PThreeWayAdjacencyAdjacencyThreeWayState(self):
        """
        Display Name: Adjacency Three-Way State
        Default Value: 1
        Value Format: decimal
        Available enum values: Up, 0, Initializing, 1, Down, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv240P2PThreeWayAdjacencyAdjacencyThreeWayState"]
            ),
        )

    @property
    def Tlv240P2PThreeWayAdjacencyExtendedLocalCircuitID(self):
        """
        Display Name: Extended Local Circuit ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv240P2PThreeWayAdjacencyExtendedLocalCircuitID"]
            ),
        )

    @property
    def Tlv240P2PThreeWayAdjacencySystemID(self):
        """
        Display Name: System ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Tlv240P2PThreeWayAdjacencySystemID"]
            ),
        )

    @property
    def Tlv240P2PThreeWayAdjacencyNeighborExtendedLocalCircuitID(self):
        """
        Display Name: Neighbor Extended Local Circuit ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Tlv240P2PThreeWayAdjacencyNeighborExtendedLocalCircuitID"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
