from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpAddress(Base):
    __slots__ = ()
    _SDM_NAME = "ldpAddress"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpAddress.header.version-1",
        "HeaderPduLengthinOctets": "ldpAddress.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpAddress.header.lsrID-3",
        "HeaderLabelSpace": "ldpAddress.header.labelSpace-4",
        "HeaderUBit": "ldpAddress.header.uBit-5",
        "HeaderType": "ldpAddress.header.type-6",
        "HeaderLength": "ldpAddress.header.length-7",
        "HeaderMessageID": "ldpAddress.header.messageID-8",
        "AddressListTLVUBit": "ldpAddress.header.addressListTLV.uBit-9",
        "AddressListTLVFBit": "ldpAddress.header.addressListTLV.fBit-10",
        "AddressListTLVType": "ldpAddress.header.addressListTLV.type-11",
        "AddressListTLVLength": "ldpAddress.header.addressListTLV.length-12",
        "Ipv4AddressesAddressFamilyIPv4": "ldpAddress.header.addressListTLV.addressFamily.ipv4Addresses.addressFamilyIPv4-13",
        "Ipv4AddressesIpv4Address": "ldpAddress.header.addressListTLV.addressFamily.ipv4Addresses.ipv4Address-14",
        "Ipv6AddressesAddressFamilyIPv6": "ldpAddress.header.addressListTLV.addressFamily.ipv6Addresses.addressFamilyIPv6-15",
        "Ipv6AddressesIpv6Address": "ldpAddress.header.addressListTLV.addressFamily.ipv6Addresses.ipv6Address-16",
    }

    def __init__(self, parent, list_op=False):
        super(LdpAddress, self).__init__(parent, list_op)

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
        Default Value: 0x0300
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
