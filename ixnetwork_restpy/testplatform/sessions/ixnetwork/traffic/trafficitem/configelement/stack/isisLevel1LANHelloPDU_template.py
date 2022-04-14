from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisLevel1LANHelloPDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisLevel1LANHelloPDU"
    _SDM_ATT_MAP = {
        "CommonHeaderIntradomainRoutingProtocolDiscriminator": "isisLevel1LANHelloPDU.isisHeader.commonHeader.intradomainRoutingProtocolDiscriminator-1",
        "CommonHeaderLengthIndicator": "isisLevel1LANHelloPDU.isisHeader.commonHeader.lengthIndicator-2",
        "CommonHeaderVersionProtocolIDExtension": "isisLevel1LANHelloPDU.isisHeader.commonHeader.versionProtocolIDExtension-3",
        "CommonHeaderIdLength": "isisLevel1LANHelloPDU.isisHeader.commonHeader.idLength-4",
        "CommonHeaderReservedBit": "isisLevel1LANHelloPDU.isisHeader.commonHeader.reservedBit-5",
        "CommonHeaderPduType": "isisLevel1LANHelloPDU.isisHeader.commonHeader.pduType-6",
        "CommonHeaderVersion": "isisLevel1LANHelloPDU.isisHeader.commonHeader.version-7",
        "CommonHeaderReserved": "isisLevel1LANHelloPDU.isisHeader.commonHeader.reserved-8",
        "CommonHeaderMaximumAreaAddresses": "isisLevel1LANHelloPDU.isisHeader.commonHeader.maximumAreaAddresses-9",
        "FixedHeaderReservedCircuitType": "isisLevel1LANHelloPDU.isisHeader.fixedHeader.reservedCircuitType-10",
        "FixedHeaderSourceID": "isisLevel1LANHelloPDU.isisHeader.fixedHeader.sourceID-11",
        "FixedHeaderHoldingTime": "isisLevel1LANHelloPDU.isisHeader.fixedHeader.holdingTime-12",
        "FixedHeaderPduLength": "isisLevel1LANHelloPDU.isisHeader.fixedHeader.pduLength-13",
        "FixedHeaderReservedBit": "isisLevel1LANHelloPDU.isisHeader.fixedHeader.reservedBit-14",
        "FixedHeaderPriority": "isisLevel1LANHelloPDU.isisHeader.fixedHeader.priority-15",
        "FixedHeaderLanID": "isisLevel1LANHelloPDU.isisHeader.fixedHeader.lanID-16",
        "Tlv1AreaAddressesTlvCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvCode-17",
        "Tlv1AreaAddressesTlvLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.tlvLength-18",
        "ValueFieldsAddressLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.addressLength-19",
        "ValueFieldsAreaAddress": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv1AreaAddresses.valueFields.areaAddress-20",
        "Tlv6ISNeighborswith6OctetMACAddressTlvCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv6ISNeighborswith6OctetMACAddress.tlvCode-21",
        "Tlv6ISNeighborswith6OctetMACAddressTlvLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv6ISNeighborswith6OctetMACAddress.tlvLength-22",
        "Tlv6ISNeighborswith6OctetMACAddressLanAddress": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv6ISNeighborswith6OctetMACAddress.lanAddress-23",
        "Tlv7ISNeighborswithVariableLengthSNPAAddressTlvCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.tlvCode-24",
        "Tlv7ISNeighborswithVariableLengthSNPAAddressTlvLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.tlvLength-25",
        "ValueFieldsLanAddressLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.valueFields.lanAddressLength-26",
        "ValueFieldsLanAddress": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv7ISNeighborswithVariableLengthSNPAAddress.valueFields.lanAddress-27",
        "Tlv8PaddingTlvCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.tlvCode-28",
        "Tlv8PaddingTlvLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.tlvLength-29",
        "ValueFieldsPadding": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv8Padding.valueFields.padding-30",
        "Tlv10AuthenticationInformationTlvCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvCode-31",
        "Tlv10AuthenticationInformationTlvLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.tlvLength-32",
        "ValueFieldsAuthenticationType": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticationType-33",
        "ValueFieldsAuthenticatorLengthoctets": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticatorLengthoctets-34",
        "ValueFieldsAuthenticator": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv10AuthenticationInformation.valueFields.authenticator-35",
        "Tlv129ProtocolsSupportedCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.code-36",
        "Tlv129ProtocolsSupportedLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.length-37",
        "NlpidEntriesEntryLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.entryLength-38",
        "NlpidEntriesEntryID": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv129ProtocolsSupported.nlpidEntries.entryID-39",
        "Tlv132IPInterfaceAddressCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.code-40",
        "Tlv132IPInterfaceAddressLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.length-41",
        "IpAddressEntriesIpAddress": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv132IPInterfaceAddress.ipAddressEntries.ipAddress-42",
        "Tlv143MTAwarePortCapType": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.type-43",
        "Tlv143MTAwarePortCapLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.length-44",
        "Tlv143MTAwarePortCapResvBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.resvBit-45",
        "Tlv143MTAwarePortCapTopologyID": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.topologyID-46",
        "SubTLVHeaderTypeNoSubTLVs": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.noSubTLVs-47",
        "SpecialVLANsandFlagsSubTLVCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.subTLVCode-48",
        "SpecialVLANsandFlagsSubTLVLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.subTLVLength-49",
        "SpecialVLANsandFlagsPortID": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.portID-50",
        "SpecialVLANsandFlagsSenderNickname": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.senderNickname-51",
        "SpecialVLANsandFlagsAppointedForwarder": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.appointedForwarder-52",
        "SpecialVLANsandFlagsAccessPort": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.accessPort-53",
        "SpecialVLANsandFlagsVlanMapping": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.vlanMapping-54",
        "SpecialVLANsandFlagsBypassPseudonode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.bypassPseudonode-55",
        "SpecialVLANsandFlagsOuterVLAN": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.outerVLAN-56",
        "SpecialVLANsandFlagsTrunkPort": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.trunkPort-57",
        "SpecialVLANsandFlagsResvBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.resvBit-58",
        "SpecialVLANsandFlagsDesigVLAN": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.specialVLANsandFlags.desigVLAN-59",
        "EnabledVLANsSubTLVCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.enabledVLANs.subTLVCode-60",
        "EnabledVLANsSubTLVLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.enabledVLANs.subTLVLength-61",
        "EnabledVLANsResvBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.enabledVLANs.resvBit-62",
        "EnabledVLANsStartVLANID": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.enabledVLANs.startVLANID-63",
        "VlanBitMapDefault": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.enabledVLANs.vlanBitMap.-64",
        "AppointedForwardersSubTLVCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.appointedForwarders.subTLVCode-65",
        "AppointedForwardersSubTLVLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.appointedForwarders.subTLVLength-66",
        "AppointmentInformationAppointeeNickname": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.appointedForwarders.appointmentInformationEntries.appointmentInformation.appointeeNickname-67",
        "AppointmentInformationResvBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.appointedForwarders.appointmentInformationEntries.appointmentInformation.resvBit-68",
        "AppointmentInformationStartVLAN": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.appointedForwarders.appointmentInformationEntries.appointmentInformation.startVLAN-69",
        "AppointmentInformationResvBit2": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.appointedForwarders.appointmentInformationEntries.appointmentInformation.resvBit2-70",
        "AppointmentInformationEndVLAN": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv143MTAwarePortCap.subTLVHeader.subTLVHeaderType.appointedForwarders.appointmentInformationEntries.appointmentInformation.endVLAN-71",
        "Tlv145TRILLNeighborType": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.type-72",
        "Tlv145TRILLNeighborLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.length-73",
        "Tlv145TRILLNeighborSBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.sBit-74",
        "Tlv145TRILLNeighborLBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.lBit-75",
        "Tlv145TRILLNeighborResvBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.resvBit-76",
        "NeighborRecordFBit": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.neighborRecordEntries.neighborRecord.fBit-77",
        "NeighborRecordResvBit2": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.neighborRecordEntries.neighborRecord.resvBit2-78",
        "NeighborRecordMtu": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.neighborRecordEntries.neighborRecord.mtu-79",
        "NeighborRecordMac": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv145TRILLNeighbor.neighborRecordEntries.neighborRecord.mac-80",
        "Tlv232IPv6InterfaceAddressCode": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.code-81",
        "Tlv232IPv6InterfaceAddressLength": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.length-82",
        "Tlv232ipv6interfaceaddressIpAddressEntriesIpAddress": "isisLevel1LANHelloPDU.isisHeader.tlvHeader.tlvHeaderType.tlv232IPv6InterfaceAddress.ipAddressEntries.ipAddress-83",
    }

    def __init__(self, parent, list_op=False):
        super(IsisLevel1LANHelloPDU, self).__init__(parent, list_op)

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
        Default Value: 15
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
        Default Value: 1
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
    def Tlv143MTAwarePortCapType(self):
        """
        Display Name: Type
        Default Value: 143
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv143MTAwarePortCapType"])
        )

    @property
    def Tlv143MTAwarePortCapLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv143MTAwarePortCapLength"])
        )

    @property
    def Tlv143MTAwarePortCapResvBit(self):
        """
        Display Name: RESV
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv143MTAwarePortCapResvBit"])
        )

    @property
    def Tlv143MTAwarePortCapTopologyID(self):
        """
        Display Name: Topology-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Tlv143MTAwarePortCapTopologyID"]),
        )

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
    def SpecialVLANsandFlagsSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsSubTLVCode"]),
        )

    @property
    def SpecialVLANsandFlagsSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsSubTLVLength"]),
        )

    @property
    def SpecialVLANsandFlagsPortID(self):
        """
        Display Name: Port ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsPortID"])
        )

    @property
    def SpecialVLANsandFlagsSenderNickname(self):
        """
        Display Name: Sender Nickname
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SpecialVLANsandFlagsSenderNickname"]
            ),
        )

    @property
    def SpecialVLANsandFlagsAppointedForwarder(self):
        """
        Display Name: Appointed Forwarder
        Default Value: 0
        Value Format: decimal
        Available enum values: Appointed Forwarder bit not set, 0, Appointed Forwarder bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SpecialVLANsandFlagsAppointedForwarder"]
            ),
        )

    @property
    def SpecialVLANsandFlagsAccessPort(self):
        """
        Display Name: Access Port
        Default Value: 0
        Value Format: decimal
        Available enum values: Access Port bit not set, 0, Access Port bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsAccessPort"]),
        )

    @property
    def SpecialVLANsandFlagsVlanMapping(self):
        """
        Display Name: VLAN Mapping
        Default Value: 0
        Value Format: decimal
        Available enum values: VLAN Mapping bit not set, 0, VLAN Mapping bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsVlanMapping"]),
        )

    @property
    def SpecialVLANsandFlagsBypassPseudonode(self):
        """
        Display Name: Bypass pseudonode
        Default Value: 0
        Value Format: decimal
        Available enum values: Bypass pseudonode bit not set, 0, Bypass pseudonode bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SpecialVLANsandFlagsBypassPseudonode"]
            ),
        )

    @property
    def SpecialVLANsandFlagsOuterVLAN(self):
        """
        Display Name: Outer.VLAN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsOuterVLAN"]),
        )

    @property
    def SpecialVLANsandFlagsTrunkPort(self):
        """
        Display Name: Trunk port
        Default Value: 0
        Value Format: decimal
        Available enum values: Trunk port bit not set, 0, Trunk port bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsTrunkPort"]),
        )

    @property
    def SpecialVLANsandFlagsResvBit(self):
        """
        Display Name: RESV
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsResvBit"])
        )

    @property
    def SpecialVLANsandFlagsDesigVLAN(self):
        """
        Display Name: Desig.VLAN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SpecialVLANsandFlagsDesigVLAN"]),
        )

    @property
    def EnabledVLANsSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnabledVLANsSubTLVCode"])
        )

    @property
    def EnabledVLANsSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnabledVLANsSubTLVLength"])
        )

    @property
    def EnabledVLANsResvBit(self):
        """
        Display Name: RESV
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnabledVLANsResvBit"])
        )

    @property
    def EnabledVLANsStartVLANID(self):
        """
        Display Name: Start VLAN ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnabledVLANsStartVLANID"])
        )

    @property
    def VlanBitMapDefault(self):
        """
        Display Name: BitMap
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VlanBitMapDefault"])
        )

    @property
    def AppointedForwardersSubTLVCode(self):
        """
        Display Name: Sub-TLV code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AppointedForwardersSubTLVCode"]),
        )

    @property
    def AppointedForwardersSubTLVLength(self):
        """
        Display Name: Sub-TLV length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AppointedForwardersSubTLVLength"]),
        )

    @property
    def AppointmentInformationAppointeeNickname(self):
        """
        Display Name: Appointee Nickname
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AppointmentInformationAppointeeNickname"]
            ),
        )

    @property
    def AppointmentInformationResvBit(self):
        """
        Display Name: RESV
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AppointmentInformationResvBit"]),
        )

    @property
    def AppointmentInformationStartVLAN(self):
        """
        Display Name: Start.VLAN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AppointmentInformationStartVLAN"]),
        )

    @property
    def AppointmentInformationResvBit2(self):
        """
        Display Name: RESV2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AppointmentInformationResvBit2"]),
        )

    @property
    def AppointmentInformationEndVLAN(self):
        """
        Display Name: End.VLAN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AppointmentInformationEndVLAN"]),
        )

    @property
    def Tlv145TRILLNeighborType(self):
        """
        Display Name: Type
        Default Value: 145
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv145TRILLNeighborType"])
        )

    @property
    def Tlv145TRILLNeighborLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv145TRILLNeighborLength"])
        )

    @property
    def Tlv145TRILLNeighborSBit(self):
        """
        Display Name: Smallest flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Smallest Flag bit not set, 0, Smallest Flag bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv145TRILLNeighborSBit"])
        )

    @property
    def Tlv145TRILLNeighborLBit(self):
        """
        Display Name: Largest flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Largest Flag bit not set, 0, Largest Flag bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv145TRILLNeighborLBit"])
        )

    @property
    def Tlv145TRILLNeighborResvBit(self):
        """
        Display Name: RESV
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv145TRILLNeighborResvBit"])
        )

    @property
    def NeighborRecordFBit(self):
        """
        Display Name: Failed
        Default Value: 0
        Value Format: decimal
        Available enum values: Failed bit not set, 0, Failed bit set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NeighborRecordFBit"])
        )

    @property
    def NeighborRecordResvBit2(self):
        """
        Display Name: RESV2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NeighborRecordResvBit2"])
        )

    @property
    def NeighborRecordMtu(self):
        """
        Display Name: MTU
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NeighborRecordMtu"])
        )

    @property
    def NeighborRecordMac(self):
        """
        Display Name: MAC Address
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NeighborRecordMac"])
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
