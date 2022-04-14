from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Icmpv9(Base):
    __slots__ = ()
    _SDM_NAME = "icmpv9"
    _SDM_ATT_MAP = {
        "Icmp9Type": "icmpv9.icmp9.type-1",
        "Icmp9Code": "icmpv9.icmp9.code-2",
        "Icmp9Checksum": "icmpv9.icmp9.checksum-3",
        "Icmp9NumAddr": "icmpv9.icmp9.numAddr-4",
        "Icmp9EntrySize": "icmpv9.icmp9.entrySize-5",
        "Icmp9Lifetime": "icmpv9.icmp9.lifetime-6",
        "AddressEntriesAddress": "icmpv9.icmp9.addressEntries.address-7",
        "AddressEntriesPreference": "icmpv9.icmp9.addressEntries.preference-8",
        "OptionPad1": "icmpv9.icmp9.tlv.option.pad1-9",
        "MobilityAgentExtensionType": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.type-10",
        "MobilityAgentExtensionLength": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.length-11",
        "MobilityAgentExtensionSequence": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.sequence-12",
        "MobilityAgentExtensionLifetime": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.lifetime-13",
        "MobilityAgentExtensionRBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.rBit-14",
        "MobilityAgentExtensionBBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.bBit-15",
        "MobilityAgentExtensionHBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.hBit-16",
        "MobilityAgentExtensionFBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.fBit-17",
        "MobilityAgentExtensionMBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.mBit-18",
        "MobilityAgentExtensionGBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.gBit-19",
        "OptionMobilityAgentExtensionRBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.rBit-20",
        "MobilityAgentExtensionTBit": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.tBit-21",
        "MobilityAgentExtensionReserved": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.reserved-22",
        "CareOfAddressEntriesAddress": "icmpv9.icmp9.tlv.option.mobilityAgentExtension.careOfAddressEntries.address-23",
        "PrefixLengthsType": "icmpv9.icmp9.tlv.option.prefixLengths.type-24",
        "PrefixLengthsLength": "icmpv9.icmp9.tlv.option.prefixLengths.length-25",
        "PrefixLengthsPrefixLength": "icmpv9.icmp9.tlv.option.prefixLengths.prefixLength-26",
    }

    def __init__(self, parent, list_op=False):
        super(Icmpv9, self).__init__(parent, list_op)

    @property
    def Icmp9Type(self):
        """
        Display Name: Type
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Icmp9Type"]))

    @property
    def Icmp9Code(self):
        """
        Display Name: Code
        Default Value: 16
        Value Format: decimal
        Available enum values: Handles common traffic, 0, Handles no common traffic, 16
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Icmp9Code"]))

    @property
    def Icmp9Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Icmp9Checksum"]))

    @property
    def Icmp9NumAddr(self):
        """
        Display Name: Num Addr
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Icmp9NumAddr"]))

    @property
    def Icmp9EntrySize(self):
        """
        Display Name: Add Entry Size
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Icmp9EntrySize"])
        )

    @property
    def Icmp9Lifetime(self):
        """
        Display Name: LifeTime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Icmp9Lifetime"]))

    @property
    def AddressEntriesAddress(self):
        """
        Display Name: Router Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressEntriesAddress"])
        )

    @property
    def AddressEntriesPreference(self):
        """
        Display Name: Router Preference
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressEntriesPreference"])
        )

    @property
    def OptionPad1(self):
        """
        Display Name: Pad1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionPad1"]))

    @property
    def MobilityAgentExtensionType(self):
        """
        Display Name: Type
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionType"])
        )

    @property
    def MobilityAgentExtensionLength(self):
        """
        Display Name: Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionLength"])
        )

    @property
    def MobilityAgentExtensionSequence(self):
        """
        Display Name: Seq #
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionSequence"]),
        )

    @property
    def MobilityAgentExtensionLifetime(self):
        """
        Display Name: LifeTime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionLifetime"]),
        )

    @property
    def MobilityAgentExtensionRBit(self):
        """
        Display Name: R Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionRBit"])
        )

    @property
    def MobilityAgentExtensionBBit(self):
        """
        Display Name: B Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionBBit"])
        )

    @property
    def MobilityAgentExtensionHBit(self):
        """
        Display Name: H Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionHBit"])
        )

    @property
    def MobilityAgentExtensionFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionFBit"])
        )

    @property
    def MobilityAgentExtensionMBit(self):
        """
        Display Name: M Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionMBit"])
        )

    @property
    def MobilityAgentExtensionGBit(self):
        """
        Display Name: G Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionGBit"])
        )

    @property
    def OptionMobilityAgentExtensionRBit(self):
        """
        Display Name: r Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OptionMobilityAgentExtensionRBit"]),
        )

    @property
    def MobilityAgentExtensionTBit(self):
        """
        Display Name: T Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionTBit"])
        )

    @property
    def MobilityAgentExtensionReserved(self):
        """
        Display Name: Reserved
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobilityAgentExtensionReserved"]),
        )

    @property
    def CareOfAddressEntriesAddress(self):
        """
        Display Name: Care-of Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CareOfAddressEntriesAddress"])
        )

    @property
    def PrefixLengthsType(self):
        """
        Display Name: Type
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrefixLengthsType"])
        )

    @property
    def PrefixLengthsLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrefixLengthsLength"])
        )

    @property
    def PrefixLengthsPrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrefixLengthsPrefixLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
