from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisL1McastLinkStatePDU(Base):
    __slots__ = ()
    _SDM_NAME = "isisL1McastLinkStatePDU"
    _SDM_ATT_MAP = {
        "CommonHeaderL1ProtocolDiscriminator": "isisL1McastLinkStatePDU.header.commonHeaderL1.protocolDiscriminator-1",
        "CommonHeaderL1LengthIndicator": "isisL1McastLinkStatePDU.header.commonHeaderL1.lengthIndicator-2",
        "CommonHeaderL1VersionProtocolID": "isisL1McastLinkStatePDU.header.commonHeaderL1.versionProtocolID-3",
        "CommonHeaderL1IdLength": "isisL1McastLinkStatePDU.header.commonHeaderL1.idLength-4",
        "CommonHeaderL1Reserved1": "isisL1McastLinkStatePDU.header.commonHeaderL1.reserved1-5",
        "CommonHeaderL1PduTypeL1Link": "isisL1McastLinkStatePDU.header.commonHeaderL1.pduTypeL1Link-6",
        "CommonHeaderL1Version": "isisL1McastLinkStatePDU.header.commonHeaderL1.version-7",
        "CommonHeaderL1Reserved2": "isisL1McastLinkStatePDU.header.commonHeaderL1.reserved2-8",
        "CommonHeaderL1MaxAreaAddresses": "isisL1McastLinkStatePDU.header.commonHeaderL1.maxAreaAddresses-9",
        "FixedHeaderL1LSPPduLength": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.pduLength-10",
        "FixedHeaderL1LSPRemainingLifetime": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.remainingLifetime-11",
        "LspIDPseudonodeID": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.lspID.pseudonodeID-12",
        "LspIDLspNumber": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.lspID.lspNumber-13",
        "FixedHeaderL1LSPSequenceNumber": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.sequenceNumber-14",
        "FixedHeaderL1LSPChecksum": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.checksum-15",
        "FixedHeaderL1LSPPartitionRepair": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.partitionRepair-16",
        "FixedHeaderL1LSPAttached": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.attached-17",
        "FixedHeaderL1LSPLspDBOverload": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.lspDBOverload-18",
        "FixedHeaderL1LSPIsType": "isisL1McastLinkStatePDU.header.fixedHeaderL1LSP.isType-19",
        "Tlv1Code": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv1.code-20",
        "Tlv1Length": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv1.length-21",
        "ValueAddressLength": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv1.value.addressLength-22",
        "ValueAreaAddress": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv1.value.areaAddress-23",
        "Tlv2Code": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.code-24",
        "Tlv2Length": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.length-25",
        "ValueVirtualFlag": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.virtualFlag-26",
        "Tlv2Reserved1": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.reserved1-27",
        "Tlv2InternalMetric1": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.internalMetric1-28",
        "Tlv2DefaultMetric1": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.defaultMetric1-29",
        "Tlv2Supported1": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.supported1-30",
        "Tlv2InternalMetric2": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.internalMetric2-31",
        "Tlv2DelayMetric2": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.delayMetric2-32",
        "Tlv2Supported2": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.supported2-33",
        "Tlv2InternalMetric3": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.internalMetric3-34",
        "Tlv2ExpenseMetric3": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.expenseMetric3-35",
        "Tlv2Supported3": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.supported3-36",
        "Tlv2InternalMetric4": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.internalMetric4-37",
        "Tlv2ExpenseMetric4": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.expenseMetric4-38",
        "Tlv2Supported4": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.supported4-39",
        "Tlv2InternalMetric5": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.internalMetric5-40",
        "Tlv2ErrorMetric5": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.errorMetric5-41",
        "NeighborIDId": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.neighborID.id-42",
        "NeighborIDPad": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv2.value.tlv2.neighborID.pad-43",
        "Tlv3Code": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv3.code-44",
        "Tlv3Length": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv3.length-45",
        "ValueReserved": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv3.value.reserved-46",
        "ValueNeighborID": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv3.value.neighborID-47",
        "Tlv10Code": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv10.code-48",
        "Tlv10Length": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv10.length-49",
        "ValueAuthenticationType": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv10.value.authenticationType-50",
        "ValueAuthenticationValue": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv10.value.authenticationValue-51",
        "Tlv142Code": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.code-52",
        "Tlv142Length": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.length-53",
        "TlvHeaderSubTLVs": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.subTLVs-54",
        "GroupMACAddressType": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.type-55",
        "GroupMACAddressLength": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.length-56",
        "GroupMACAddressVlanID": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.vlanID-57",
        "GroupMACAddressNumberOfGroupRecords": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.numberOfGroupRecords-58",
        "GroupRecordReserved": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.groupRecord.reserved-59",
        "GroupRecordNumberOfSources": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.groupRecord.numberOfSources-60",
        "GroupRecordGroupAddress": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.groupRecord.groupAddress-61",
        "SrcAddressValue": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupMACAddress.groupRecord.srcAddress.value-62",
        "GroupIPv4AddressType": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.type-63",
        "GroupIPv4AddressLength": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.length-64",
        "GroupIPv4AddressVlanID": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.vlanID-65",
        "GroupIPv4AddressNumberOfGroupRecords": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.numberOfGroupRecords-66",
        "Groupipv4addressGroupRecordReserved": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.reserved-67",
        "Groupipv4addressGroupRecordNumberOfSources": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.numberOfSources-68",
        "Groupipv4addressGroupRecordGroupAddress": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.groupAddress-69",
        "SourceAddressValue": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.sourceAddress.value-70",
        "TlvheaderGroupIPv4AddressType": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.type-71",
        "TlvheaderGroupIPv4AddressLength": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.length-72",
        "TlvheaderGroupIPv4AddressVlanID": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.vlanID-73",
        "TlvheaderGroupIPv4AddressNumberOfGroupRecords": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.numberOfGroupRecords-74",
        "TlvheaderGroupipv4addressGroupRecordReserved": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.reserved-75",
        "TlvheaderGroupipv4addressGroupRecordNumberOfSources": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.numberOfSources-76",
        "TlvheaderGroupipv4addressGroupRecordGroupAddress": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.groupAddress-77",
        "GrouprecordSourceAddressValue": "isisL1McastLinkStatePDU.header.variableHeaderL1LSP.tlvHeader.tlv142.subTLVHeader.tlvHeader.groupIPv4Address.groupRecord.sourceAddress.value-78",
    }

    def __init__(self, parent, list_op=False):
        super(IsisL1McastLinkStatePDU, self).__init__(parent, list_op)

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
    def CommonHeaderL1PduTypeL1Link(self):
        """
        Display Name: PDU type
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHeaderL1PduTypeL1Link"])
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
    def FixedHeaderL1LSPPduLength(self):
        """
        Display Name: PDU length
        Default Value: 1497
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPPduLength"])
        )

    @property
    def FixedHeaderL1LSPRemainingLifetime(self):
        """
        Display Name: Remaining lifetime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPRemainingLifetime"]),
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
    def FixedHeaderL1LSPSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPSequenceNumber"]),
        )

    @property
    def FixedHeaderL1LSPChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPChecksum"])
        )

    @property
    def FixedHeaderL1LSPPartitionRepair(self):
        """
        Display Name: Partition repair bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not supported, 0, Supported, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPPartitionRepair"]),
        )

    @property
    def FixedHeaderL1LSPAttached(self):
        """
        Display Name: Attached
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPAttached"])
        )

    @property
    def FixedHeaderL1LSPLspDBOverload(self):
        """
        Display Name: LSP database overload
        Default Value: 0
        Value Format: decimal
        Available enum values: No overload, 0, Overload, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPLspDBOverload"]),
        )

    @property
    def FixedHeaderL1LSPIsType(self):
        """
        Display Name: IS type
        Default Value: 1
        Value Format: decimal
        Available enum values: Level 1 IS, 1, Level 2 IS, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FixedHeaderL1LSPIsType"])
        )

    @property
    def Tlv1Code(self):
        """
        Display Name: TLV code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv1Code"]))

    @property
    def Tlv1Length(self):
        """
        Display Name: TLV length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv1Length"]))

    @property
    def ValueAddressLength(self):
        """
        Display Name: Address length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueAddressLength"])
        )

    @property
    def ValueAreaAddress(self):
        """
        Display Name: Area address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueAreaAddress"])
        )

    @property
    def Tlv2Code(self):
        """
        Display Name: TLV code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv2Code"]))

    @property
    def Tlv2Length(self):
        """
        Display Name: TLV length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv2Length"]))

    @property
    def ValueVirtualFlag(self):
        """
        Display Name: Virtual flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Level 2 path to repair area partition, 0, Level 2 path to repair area partition, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueVirtualFlag"])
        )

    @property
    def Tlv2Reserved1(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv2Reserved1"]))

    @property
    def Tlv2InternalMetric1(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2InternalMetric1"])
        )

    @property
    def Tlv2DefaultMetric1(self):
        """
        Display Name: Default metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2DefaultMetric1"])
        )

    @property
    def Tlv2Supported1(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2Supported1"])
        )

    @property
    def Tlv2InternalMetric2(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2InternalMetric2"])
        )

    @property
    def Tlv2DelayMetric2(self):
        """
        Display Name: Delay metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2DelayMetric2"])
        )

    @property
    def Tlv2Supported2(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2Supported2"])
        )

    @property
    def Tlv2InternalMetric3(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2InternalMetric3"])
        )

    @property
    def Tlv2ExpenseMetric3(self):
        """
        Display Name: Expense metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2ExpenseMetric3"])
        )

    @property
    def Tlv2Supported3(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2Supported3"])
        )

    @property
    def Tlv2InternalMetric4(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2InternalMetric4"])
        )

    @property
    def Tlv2ExpenseMetric4(self):
        """
        Display Name: Expense metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2ExpenseMetric4"])
        )

    @property
    def Tlv2Supported4(self):
        """
        Display Name: Supported bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Metric unsupported, 1, Metric supported, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2Supported4"])
        )

    @property
    def Tlv2InternalMetric5(self):
        """
        Display Name: Internal metric
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2InternalMetric5"])
        )

    @property
    def Tlv2ErrorMetric5(self):
        """
        Display Name: Error metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Tlv2ErrorMetric5"])
        )

    @property
    def NeighborIDId(self):
        """
        Display Name: Neighbor ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NeighborIDId"]))

    @property
    def NeighborIDPad(self):
        """
        Display Name: Padding - 8 bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NeighborIDPad"]))

    @property
    def Tlv3Code(self):
        """
        Display Name: TLV code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv3Code"]))

    @property
    def Tlv3Length(self):
        """
        Display Name: TLV length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv3Length"]))

    @property
    def ValueReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueReserved"]))

    @property
    def ValueNeighborID(self):
        """
        Display Name: Neighbor ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ValueNeighborID"])
        )

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
        Default Value: 4
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

    @property
    def Tlv142Code(self):
        """
        Display Name: TLV Type
        Default Value: 142
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv142Code"]))

    @property
    def Tlv142Length(self):
        """
        Display Name: TLV Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Tlv142Length"]))

    @property
    def TlvHeaderSubTLVs(self):
        """
        Display Name: No sub-TLVs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TlvHeaderSubTLVs"])
        )

    @property
    def GroupMACAddressType(self):
        """
        Display Name: TYPE
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressType"])
        )

    @property
    def GroupMACAddressLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressLength"])
        )

    @property
    def GroupMACAddressVlanID(self):
        """
        Display Name: Vlan-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupMACAddressVlanID"])
        )

    @property
    def GroupMACAddressNumberOfGroupRecords(self):
        """
        Display Name: Num Group Records
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GroupMACAddressNumberOfGroupRecords"]
            ),
        )

    @property
    def GroupRecordReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordReserved"])
        )

    @property
    def GroupRecordNumberOfSources(self):
        """
        Display Name: Num of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordNumberOfSources"])
        )

    @property
    def GroupRecordGroupAddress(self):
        """
        Display Name: Group Address
        Default Value: 0:0:0:0:0:0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupRecordGroupAddress"])
        )

    @property
    def SrcAddressValue(self):
        """
        Display Name: Source Address Value 1
        Default Value: 0:0:0:0:0:0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcAddressValue"])
        )

    @property
    def GroupIPv4AddressType(self):
        """
        Display Name: TYPE
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv4AddressType"])
        )

    @property
    def GroupIPv4AddressLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv4AddressLength"])
        )

    @property
    def GroupIPv4AddressVlanID(self):
        """
        Display Name: Vlan-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupIPv4AddressVlanID"])
        )

    @property
    def GroupIPv4AddressNumberOfGroupRecords(self):
        """
        Display Name: Num Group Records
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GroupIPv4AddressNumberOfGroupRecords"]
            ),
        )

    @property
    def Groupipv4addressGroupRecordReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Groupipv4addressGroupRecordReserved"]
            ),
        )

    @property
    def Groupipv4addressGroupRecordNumberOfSources(self):
        """
        Display Name: Num of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Groupipv4addressGroupRecordNumberOfSources"]
            ),
        )

    @property
    def Groupipv4addressGroupRecordGroupAddress(self):
        """
        Display Name: Group Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Groupipv4addressGroupRecordGroupAddress"]
            ),
        )

    @property
    def SourceAddressValue(self):
        """
        Display Name: Source Address Value 1
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceAddressValue"])
        )

    @property
    def TlvheaderGroupIPv4AddressType(self):
        """
        Display Name: TYPE
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TlvheaderGroupIPv4AddressType"]),
        )

    @property
    def TlvheaderGroupIPv4AddressLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TlvheaderGroupIPv4AddressLength"]),
        )

    @property
    def TlvheaderGroupIPv4AddressVlanID(self):
        """
        Display Name: Vlan-ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TlvheaderGroupIPv4AddressVlanID"]),
        )

    @property
    def TlvheaderGroupIPv4AddressNumberOfGroupRecords(self):
        """
        Display Name: Num Group Records
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderGroupIPv4AddressNumberOfGroupRecords"]
            ),
        )

    @property
    def TlvheaderGroupipv4addressGroupRecordReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderGroupipv4addressGroupRecordReserved"]
            ),
        )

    @property
    def TlvheaderGroupipv4addressGroupRecordNumberOfSources(self):
        """
        Display Name: Num of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderGroupipv4addressGroupRecordNumberOfSources"]
            ),
        )

    @property
    def TlvheaderGroupipv4addressGroupRecordGroupAddress(self):
        """
        Display Name: Group Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TlvheaderGroupipv4addressGroupRecordGroupAddress"]
            ),
        )

    @property
    def GrouprecordSourceAddressValue(self):
        """
        Display Name: Source Address Value 1
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GrouprecordSourceAddressValue"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
