from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpLabelWithdraw(Base):
    __slots__ = ()
    _SDM_NAME = "ldpLabelWithdraw"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpLabelWithdraw.header.version-1",
        "HeaderPduLengthinOctets": "ldpLabelWithdraw.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpLabelWithdraw.header.lsrID-3",
        "HeaderLabelSpace": "ldpLabelWithdraw.header.labelSpace-4",
        "HeaderUBit": "ldpLabelWithdraw.header.uBit-5",
        "HeaderType": "ldpLabelWithdraw.header.type-6",
        "HeaderLength": "ldpLabelWithdraw.header.length-7",
        "HeaderMessageID": "ldpLabelWithdraw.header.messageID-8",
        "FecTLVUBit": "ldpLabelWithdraw.header.fecTLV.uBit-9",
        "FecTLVFBit": "ldpLabelWithdraw.header.fecTLV.fBit-10",
        "FecTLVType": "ldpLabelWithdraw.header.fecTLV.type-11",
        "FecTLVLength": "ldpLabelWithdraw.header.fecTLV.length-12",
        "WildcardType": "ldpLabelWithdraw.header.fecTLV.fecElement.wildcard.type-13",
        "PrefixType": "ldpLabelWithdraw.header.fecTLV.fecElement.prefix.type-14",
        "Ipv4PrefixAddressFamily": "ldpLabelWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.addressFamily-15",
        "Ipv4PrefixPrelen": "ldpLabelWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prelen-16",
        "Ipv4PrefixPrefix": "ldpLabelWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prefix-17",
        "Ipv6PrefixAddressFamily": "ldpLabelWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.addressFamily-18",
        "Ipv6PrefixPrelen": "ldpLabelWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prelen-19",
        "Ipv6PrefixPrefix": "ldpLabelWithdraw.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prefix-20",
        "HostAddressType": "ldpLabelWithdraw.header.fecTLV.fecElement.hostAddress.type-21",
        "Ipv4HostAddressAddressFamily": "ldpLabelWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.addressFamily-22",
        "Ipv4HostAddressHostAddressLength": "ldpLabelWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddressLength-23",
        "Ipv4HostAddressHostAddress": "ldpLabelWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddress-24",
        "Ipv6HostAddressAddressFamily": "ldpLabelWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.addressFamily-25",
        "Ipv6HostAddressHostAddressLength": "ldpLabelWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddressLength-26",
        "Ipv6HostAddressHostAddress": "ldpLabelWithdraw.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddress-27",
        "TclP2mpTclType": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclType-28",
        "TclIpv4P2mpAddressTclP2mpAddressFamily": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressFamily-29",
        "TclIpv4P2mpAddressTclP2mpAddressLength": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressLength-30",
        "TclIpv4P2mpAddressTclRootAddress": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclRootAddress-31",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressFamily": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressFamily-32",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressLength": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressLength-33",
        "TclIpv6P2mpAddressTclIpv6RootAddress": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclIpv6RootAddress-34",
        "TclP2mpTclOpaqueLength": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclOpaqueLength-35",
        "TclGenericLSPIdentifierTLVTclType": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclType-36",
        "TclGenericLSPIdentifierTLVTclLength": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclLength-37",
        "TclGenericLSPIdentifierTLVTclValue": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclValue-38",
        "TclEditTLVTclType": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclType-39",
        "TclEditTLVTclLength": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclLength-40",
        "TclEditTLVTclValue": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclValue-41",
        "TclP2mpTypedWcardTclTypeTypedWcard": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeTypedWcard-42",
        "TclP2mpTypedWcardTclTypeWcard": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeWcard-43",
        "TclP2mpTypedWcardTclTypeLen": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeLen-44",
        "TclP2mpTypedWcardTclTypeAfi": "ldpLabelWithdraw.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeAfi-45",
        "GenericLabelTLVUBit": "ldpLabelWithdraw.header.labelTLV.genericLabelTLV.uBit-46",
        "GenericLabelTLVFBit": "ldpLabelWithdraw.header.labelTLV.genericLabelTLV.fBit-47",
        "GenericLabelTLVType": "ldpLabelWithdraw.header.labelTLV.genericLabelTLV.type-48",
        "GenericLabelTLVLength": "ldpLabelWithdraw.header.labelTLV.genericLabelTLV.length-49",
        "GenericLabelTLVLabel": "ldpLabelWithdraw.header.labelTLV.genericLabelTLV.label-50",
        "AtmLabelTLVUBit": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.uBit-51",
        "AtmLabelTLVFBit": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.fBit-52",
        "AtmLabelTLVType": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.type-53",
        "AtmLabelTLVLength": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.length-54",
        "AtmLabelTLVReserved": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.reserved-55",
        "AtmLabelTLVVBits": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.vBits-56",
        "AtmLabelTLVVpi": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.vpi-57",
        "AtmLabelTLVVci": "ldpLabelWithdraw.header.labelTLV.atmLabelTLV.vci-58",
        "FrameRelayLabelTLVUBit": "ldpLabelWithdraw.header.labelTLV.frameRelayLabelTLV.uBit-59",
        "FrameRelayLabelTLVFBit": "ldpLabelWithdraw.header.labelTLV.frameRelayLabelTLV.fBit-60",
        "FrameRelayLabelTLVType": "ldpLabelWithdraw.header.labelTLV.frameRelayLabelTLV.type-61",
        "FrameRelayLabelTLVLength": "ldpLabelWithdraw.header.labelTLV.frameRelayLabelTLV.length-62",
        "FrameRelayLabelTLVReserved": "ldpLabelWithdraw.header.labelTLV.frameRelayLabelTLV.reserved-63",
        "FrameRelayLabelTLVDlciLength": "ldpLabelWithdraw.header.labelTLV.frameRelayLabelTLV.dlciLength-64",
        "FrameRelayLabelTLVDlci": "ldpLabelWithdraw.header.labelTLV.frameRelayLabelTLV.dlci-65",
    }

    def __init__(self, parent, list_op=False):
        super(LdpLabelWithdraw, self).__init__(parent, list_op)

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
        Default Value: 0x0402
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
        Available enum values: VPI and VCI significant, 0, Only VPI significant, 0, Only VCI significant, 2
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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
