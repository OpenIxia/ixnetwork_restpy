from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpAddressWithdraw(Base):
    __slots__ = ()
    _SDM_NAME = "ldpAddressWithdraw"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpAddressWithdraw.header.version-1",
        "HeaderPduLengthinOctets": "ldpAddressWithdraw.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpAddressWithdraw.header.lsrID-3",
        "HeaderLabelSpace": "ldpAddressWithdraw.header.labelSpace-4",
        "HeaderUBit": "ldpAddressWithdraw.header.uBit-5",
        "HeaderType": "ldpAddressWithdraw.header.type-6",
        "HeaderLength": "ldpAddressWithdraw.header.length-7",
        "HeaderMessageID": "ldpAddressWithdraw.header.messageID-8",
        "FecTLVUBit": "ldpAddressWithdraw.header.fecTLV.uBit-9",
        "FecTLVFBit": "ldpAddressWithdraw.header.fecTLV.fBit-10",
        "FecTLVType": "ldpAddressWithdraw.header.fecTLV.type-11",
        "FecTLVLength": "ldpAddressWithdraw.header.fecTLV.length-12",
        "WildcardType": "ldpAddressWithdraw.header.fecTLV.fecElement.wildcard.type-13",
        "PrefixType": "ldpAddressWithdraw.header.fecTLV.fecElement.prefix.type-14",
        "Ipv4PrefixAddressFamily": "ldpAddressWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.addressFamily-15",
        "Ipv4PrefixPrelen": "ldpAddressWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prelen-16",
        "Ipv4PrefixPrefix": "ldpAddressWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prefix-17",
        "Ipv6PrefixAddressFamily": "ldpAddressWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.addressFamily-18",
        "Ipv6PrefixPrelen": "ldpAddressWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prelen-19",
        "Ipv6PrefixPrefix": "ldpAddressWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prefix-20",
        "HostAddressType": "ldpAddressWithdraw.header.fecTLV.fecElement.hostAddress.type-21",
        "Ipv4HostAddressAddressFamily": "ldpAddressWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.addressFamily-22",
        "Ipv4HostAddressHostAddressLength": "ldpAddressWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddressLength-23",
        "Ipv4HostAddressHostAddress": "ldpAddressWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddress-24",
        "Ipv6HostAddressAddressFamily": "ldpAddressWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.addressFamily-25",
        "Ipv6HostAddressHostAddressLength": "ldpAddressWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddressLength-26",
        "Ipv6HostAddressHostAddress": "ldpAddressWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddress-27",
        "AddressListTLVUBit": "ldpAddressWithdraw.header.addressListTLV.uBit-28",
        "AddressListTLVFBit": "ldpAddressWithdraw.header.addressListTLV.fBit-29",
        "AddressListTLVType": "ldpAddressWithdraw.header.addressListTLV.type-30",
        "AddressListTLVLength": "ldpAddressWithdraw.header.addressListTLV.length-31",
        "Ipv4AddressesAddressFamilyIPv4": "ldpAddressWithdraw.header.addressListTLV.addressFamily.ipv4Addresses.addressFamilyIPv4-32",
        "Ipv4AddressesIpv4Address": "ldpAddressWithdraw.header.addressListTLV.addressFamily.ipv4Addresses.ipv4Address-33",
        "Ipv6AddressesAddressFamilyIPv6": "ldpAddressWithdraw.header.addressListTLV.addressFamily.ipv6Addresses.addressFamilyIPv6-34",
        "Ipv6AddressesIpv6Address": "ldpAddressWithdraw.header.addressListTLV.addressFamily.ipv6Addresses.ipv6Address-35",
    }

    def __init__(self, parent, list_op=False):
        super(LdpAddressWithdraw, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderPduLengthinOctets(self):
        """
        Display Name: PDU length(in octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPduLengthinOctets"])
        )

    @property
    def HeaderLsrID(self):
        """
        Display Name: LSR ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLsrID"]))

    @property
    def HeaderLabelSpace(self):
        """
        Display Name: Label space
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLabelSpace"])
        )

    @property
    def HeaderUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderUBit"]))

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x0301
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderMessageID(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageID"])
        )

    @property
    def FecTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVUBit"]))

    @property
    def FecTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVFBit"]))

    @property
    def FecTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVType"]))

    @property
    def FecTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FecTLVLength"]))

    @property
    def WildcardType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["WildcardType"]))

    @property
    def PrefixType(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrefixType"]))

    @property
    def Ipv4PrefixAddressFamily(self):
        """
        Display Name: Address family
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4PrefixAddressFamily"])
        )

    @property
    def Ipv4PrefixPrelen(self):
        """
        Display Name: Prelen
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4PrefixPrelen"])
        )

    @property
    def Ipv4PrefixPrefix(self):
        """
        Display Name: Prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4PrefixPrefix"])
        )

    @property
    def Ipv6PrefixAddressFamily(self):
        """
        Display Name: Address family
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6PrefixAddressFamily"])
        )

    @property
    def Ipv6PrefixPrelen(self):
        """
        Display Name: Prelen
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6PrefixPrelen"])
        )

    @property
    def Ipv6PrefixPrefix(self):
        """
        Display Name: Prefix
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6PrefixPrefix"])
        )

    @property
    def HostAddressType(self):
        """
        Display Name: Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HostAddressType"])
        )

    @property
    def Ipv4HostAddressAddressFamily(self):
        """
        Display Name: Address family
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4HostAddressAddressFamily"])
        )

    @property
    def Ipv4HostAddressHostAddressLength(self):
        """
        Display Name: Host address length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4HostAddressHostAddressLength"]),
        )

    @property
    def Ipv4HostAddressHostAddress(self):
        """
        Display Name: Host address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4HostAddressHostAddress"])
        )

    @property
    def Ipv6HostAddressAddressFamily(self):
        """
        Display Name: Address family
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6HostAddressAddressFamily"])
        )

    @property
    def Ipv6HostAddressHostAddressLength(self):
        """
        Display Name: Host address length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6HostAddressHostAddressLength"]),
        )

    @property
    def Ipv6HostAddressHostAddress(self):
        """
        Display Name: Host address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6HostAddressHostAddress"])
        )

    @property
    def AddressListTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressListTLVUBit"])
        )

    @property
    def AddressListTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressListTLVFBit"])
        )

    @property
    def AddressListTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0101
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressListTLVType"])
        )

    @property
    def AddressListTLVLength(self):
        """
        Display Name: Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressListTLVLength"])
        )

    @property
    def Ipv4AddressesAddressFamilyIPv4(self):
        """
        Display Name: Address family (IPv4)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4AddressesAddressFamilyIPv4"]),
        )

    @property
    def Ipv4AddressesIpv4Address(self):
        """
        Display Name: IPv4 address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4AddressesIpv4Address"])
        )

    @property
    def Ipv6AddressesAddressFamilyIPv6(self):
        """
        Display Name: Address family (IPv6)
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6AddressesAddressFamilyIPv6"]),
        )

    @property
    def Ipv6AddressesIpv6Address(self):
        """
        Display Name: IPv6 address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6AddressesIpv6Address"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
