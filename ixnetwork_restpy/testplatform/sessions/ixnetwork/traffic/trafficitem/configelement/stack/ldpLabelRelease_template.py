from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpLabelRelease(Base):
    __slots__ = ()
    _SDM_NAME = "ldpLabelRelease"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpLabelRelease.header.version-1",
        "HeaderPduLengthinOctets": "ldpLabelRelease.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpLabelRelease.header.lsrID-3",
        "HeaderLabelSpace": "ldpLabelRelease.header.labelSpace-4",
        "HeaderUBit": "ldpLabelRelease.header.uBit-5",
        "HeaderType": "ldpLabelRelease.header.type-6",
        "HeaderLength": "ldpLabelRelease.header.length-7",
        "HeaderMessageID": "ldpLabelRelease.header.messageID-8",
        "FecTLVUBit": "ldpLabelRelease.header.fecTLV.uBit-9",
        "FecTLVFBit": "ldpLabelRelease.header.fecTLV.fBit-10",
        "FecTLVType": "ldpLabelRelease.header.fecTLV.type-11",
        "FecTLVLength": "ldpLabelRelease.header.fecTLV.length-12",
        "WildcardType": "ldpLabelRelease.header.fecTLV.fecElement.wildcard.type-13",
        "PrefixType": "ldpLabelRelease.header.fecTLV.fecElement.prefix.type-14",
        "Ipv4PrefixAddressFamily": "ldpLabelRelease.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.addressFamily-15",
        "Ipv4PrefixPrelen": "ldpLabelRelease.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prelen-16",
        "Ipv4PrefixPrefix": "ldpLabelRelease.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prefix-17",
        "Ipv6PrefixAddressFamily": "ldpLabelRelease.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.addressFamily-18",
        "Ipv6PrefixPrelen": "ldpLabelRelease.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prelen-19",
        "Ipv6PrefixPrefix": "ldpLabelRelease.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prefix-20",
        "HostAddressType": "ldpLabelRelease.header.fecTLV.fecElement.hostAddress.type-21",
        "Ipv4HostAddressAddressFamily": "ldpLabelRelease.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.addressFamily-22",
        "Ipv4HostAddressHostAddressLength": "ldpLabelRelease.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddressLength-23",
        "Ipv4HostAddressHostAddress": "ldpLabelRelease.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddress-24",
        "Ipv6HostAddressAddressFamily": "ldpLabelRelease.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.addressFamily-25",
        "Ipv6HostAddressHostAddressLength": "ldpLabelRelease.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddressLength-26",
        "Ipv6HostAddressHostAddress": "ldpLabelRelease.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddress-27",
        "TclP2mpTclType": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclType-28",
        "TclIpv4P2mpAddressTclP2mpAddressFamily": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressFamily-29",
        "TclIpv4P2mpAddressTclP2mpAddressLength": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressLength-30",
        "TclIpv4P2mpAddressTclRootAddress": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclRootAddress-31",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressFamily": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressFamily-32",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressLength": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressLength-33",
        "TclIpv6P2mpAddressTclIpv6RootAddress": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclIpv6RootAddress-34",
        "TclP2mpTclOpaqueLength": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclOpaqueLength-35",
        "TclGenericLSPIdentifierTLVTclType": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclType-36",
        "TclGenericLSPIdentifierTLVTclLength": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclLength-37",
        "TclGenericLSPIdentifierTLVTclValue": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclValue-38",
        "TclEditTLVTclType": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclType-39",
        "TclEditTLVTclLength": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclLength-40",
        "TclEditTLVTclValue": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclValue-41",
        "TclP2mpTypedWcardTclTypeTypedWcard": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeTypedWcard-42",
        "TclP2mpTypedWcardTclTypeWcard": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeWcard-43",
        "TclP2mpTypedWcardTclTypeLen": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeLen-44",
        "TclP2mpTypedWcardTclTypeAfi": "ldpLabelRelease.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeAfi-45",
        "GenericLabelTLVUBit": "ldpLabelRelease.header.optionalParameter.labelTLV.genericLabelTLV.uBit-46",
        "GenericLabelTLVFBit": "ldpLabelRelease.header.optionalParameter.labelTLV.genericLabelTLV.fBit-47",
        "GenericLabelTLVType": "ldpLabelRelease.header.optionalParameter.labelTLV.genericLabelTLV.type-48",
        "GenericLabelTLVLength": "ldpLabelRelease.header.optionalParameter.labelTLV.genericLabelTLV.length-49",
        "GenericLabelTLVLabel": "ldpLabelRelease.header.optionalParameter.labelTLV.genericLabelTLV.label-50",
        "AtmLabelTLVUBit": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.uBit-51",
        "AtmLabelTLVFBit": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.fBit-52",
        "AtmLabelTLVType": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.type-53",
        "AtmLabelTLVLength": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.length-54",
        "AtmLabelTLVReserved": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.reserved-55",
        "AtmLabelTLVVBits": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.vBits-56",
        "AtmLabelTLVVpi": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.vpi-57",
        "AtmLabelTLVVci": "ldpLabelRelease.header.optionalParameter.labelTLV.atmLabelTLV.vci-58",
        "FrameRelayLabelTLVUBit": "ldpLabelRelease.header.optionalParameter.labelTLV.frameRelayLabelTLV.uBit-59",
        "FrameRelayLabelTLVFBit": "ldpLabelRelease.header.optionalParameter.labelTLV.frameRelayLabelTLV.fBit-60",
        "FrameRelayLabelTLVType": "ldpLabelRelease.header.optionalParameter.labelTLV.frameRelayLabelTLV.type-61",
        "FrameRelayLabelTLVLength": "ldpLabelRelease.header.optionalParameter.labelTLV.frameRelayLabelTLV.length-62",
        "FrameRelayLabelTLVReserved": "ldpLabelRelease.header.optionalParameter.labelTLV.frameRelayLabelTLV.reserved-63",
        "FrameRelayLabelTLVDlciLength": "ldpLabelRelease.header.optionalParameter.labelTLV.frameRelayLabelTLV.dlciLength-64",
        "FrameRelayLabelTLVDlci": "ldpLabelRelease.header.optionalParameter.labelTLV.frameRelayLabelTLV.dlci-65",
        "VendorPrivateUBit": "ldpLabelRelease.header.optionalParameter.vendorPrivate.uBit-66",
        "VendorPrivateType": "ldpLabelRelease.header.optionalParameter.vendorPrivate.type-67",
        "VendorPrivateLength": "ldpLabelRelease.header.optionalParameter.vendorPrivate.length-68",
        "VendorPrivateMessageID": "ldpLabelRelease.header.optionalParameter.vendorPrivate.messageID-69",
        "VendorPrivateVendorID": "ldpLabelRelease.header.optionalParameter.vendorPrivate.vendorID-70",
    }

    def __init__(self, parent, list_op=False):
        super(LdpLabelRelease, self).__init__(parent, list_op)

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
        Default Value: 0x0403
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
    def TclP2mpTclType(self):
        """
        Display Name: Type
        Default Value: 0x06
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTclType"])
        )

    @property
    def TclIpv4P2mpAddressTclP2mpAddressFamily(self):
        """
        Display Name: Address Family
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv4P2mpAddressTclP2mpAddressFamily"]
            ),
        )

    @property
    def TclIpv4P2mpAddressTclP2mpAddressLength(self):
        """
        Display Name: Address length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv4P2mpAddressTclP2mpAddressLength"]
            ),
        )

    @property
    def TclIpv4P2mpAddressTclRootAddress(self):
        """
        Display Name: Root Node Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclIpv4P2mpAddressTclRootAddress"]),
        )

    @property
    def TclIpv6P2mpAddressTclP2mpIpv6AddressFamily(self):
        """
        Display Name: Address Family
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv6P2mpAddressTclP2mpIpv6AddressFamily"]
            ),
        )

    @property
    def TclIpv6P2mpAddressTclP2mpIpv6AddressLength(self):
        """
        Display Name: Address length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv6P2mpAddressTclP2mpIpv6AddressLength"]
            ),
        )

    @property
    def TclIpv6P2mpAddressTclIpv6RootAddress(self):
        """
        Display Name: Root Node Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclIpv6P2mpAddressTclIpv6RootAddress"]
            ),
        )

    @property
    def TclP2mpTclOpaqueLength(self):
        """
        Display Name: Opaque Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTclOpaqueLength"])
        )

    @property
    def TclGenericLSPIdentifierTLVTclType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclGenericLSPIdentifierTLVTclType"]),
        )

    @property
    def TclGenericLSPIdentifierTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclGenericLSPIdentifierTLVTclLength"]
            ),
        )

    @property
    def TclGenericLSPIdentifierTLVTclValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclGenericLSPIdentifierTLVTclValue"]
            ),
        )

    @property
    def TclEditTLVTclType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclEditTLVTclType"])
        )

    @property
    def TclEditTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclEditTLVTclLength"])
        )

    @property
    def TclEditTLVTclValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclEditTLVTclValue"])
        )

    @property
    def TclP2mpTypedWcardTclTypeTypedWcard(self):
        """
        Display Name: Typed Wcard
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeTypedWcard"]
            ),
        )

    @property
    def TclP2mpTypedWcardTclTypeWcard(self):
        """
        Display Name: Type
        Default Value: 0x06
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeWcard"]),
        )

    @property
    def TclP2mpTypedWcardTclTypeLen(self):
        """
        Display Name: Len
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeLen"])
        )

    @property
    def TclP2mpTypedWcardTclTypeAfi(self):
        """
        Display Name: AFI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclP2mpTypedWcardTclTypeAfi"])
        )

    @property
    def GenericLabelTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVUBit"])
        )

    @property
    def GenericLabelTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVFBit"])
        )

    @property
    def GenericLabelTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0200
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVType"])
        )

    @property
    def GenericLabelTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVLength"])
        )

    @property
    def GenericLabelTLVLabel(self):
        """
        Display Name: Label
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericLabelTLVLabel"])
        )

    @property
    def AtmLabelTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVUBit"])
        )

    @property
    def AtmLabelTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVFBit"])
        )

    @property
    def AtmLabelTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0201
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVType"])
        )

    @property
    def AtmLabelTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVLength"])
        )

    @property
    def AtmLabelTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVReserved"])
        )

    @property
    def AtmLabelTLVVBits(self):
        """
        Display Name: V bits
        Default Value: 0
        Value Format: decimal
        Available enum values: VPI and VCI significant, 0, Only VPI significant, 1, Only VCI significant, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVVBits"])
        )

    @property
    def AtmLabelTLVVpi(self):
        """
        Display Name: VPI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVVpi"])
        )

    @property
    def AtmLabelTLVVci(self):
        """
        Display Name: VCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmLabelTLVVci"])
        )

    @property
    def FrameRelayLabelTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVUBit"])
        )

    @property
    def FrameRelayLabelTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVFBit"])
        )

    @property
    def FrameRelayLabelTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0202
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVType"])
        )

    @property
    def FrameRelayLabelTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVLength"])
        )

    @property
    def FrameRelayLabelTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVReserved"])
        )

    @property
    def FrameRelayLabelTLVDlciLength(self):
        """
        Display Name: DLCI length
        Default Value: 0
        Value Format: decimal
        Available enum values: 10 bits, 0, 23 bits, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVDlciLength"])
        )

    @property
    def FrameRelayLabelTLVDlci(self):
        """
        Display Name: DLCI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FrameRelayLabelTLVDlci"])
        )

    @property
    def VendorPrivateUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorPrivateUBit"])
        )

    @property
    def VendorPrivateType(self):
        """
        Display Name: Type
        Default Value: 0x3E00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorPrivateType"])
        )

    @property
    def VendorPrivateLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorPrivateLength"])
        )

    @property
    def VendorPrivateMessageID(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorPrivateMessageID"])
        )

    @property
    def VendorPrivateVendorID(self):
        """
        Display Name: Vendor ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorPrivateVendorID"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
