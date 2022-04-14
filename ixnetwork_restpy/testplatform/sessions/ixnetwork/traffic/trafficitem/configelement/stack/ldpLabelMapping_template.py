from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpLabelMapping(Base):
    __slots__ = ()
    _SDM_NAME = "ldpLabelMapping"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpLabelMapping.header.version-1",
        "HeaderPduLengthinOctets": "ldpLabelMapping.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpLabelMapping.header.lsrID-3",
        "HeaderLabelSpace": "ldpLabelMapping.header.labelSpace-4",
        "HeaderUBit": "ldpLabelMapping.header.uBit-5",
        "HeaderType": "ldpLabelMapping.header.type-6",
        "HeaderLength": "ldpLabelMapping.header.length-7",
        "HeaderMessageID": "ldpLabelMapping.header.messageID-8",
        "FecTLVUBit": "ldpLabelMapping.header.fecTLV.uBit-9",
        "FecTLVFBit": "ldpLabelMapping.header.fecTLV.fBit-10",
        "FecTLVType": "ldpLabelMapping.header.fecTLV.type-11",
        "FecTLVLength": "ldpLabelMapping.header.fecTLV.length-12",
        "WildcardType": "ldpLabelMapping.header.fecTLV.fecElement.wildcard.type-13",
        "PrefixType": "ldpLabelMapping.header.fecTLV.fecElement.prefix.type-14",
        "Ipv4PrefixAddressFamily": "ldpLabelMapping.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.addressFamily-15",
        "Ipv4PrefixPrelen": "ldpLabelMapping.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prelen-16",
        "Ipv4PrefixPrefix": "ldpLabelMapping.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prefix-17",
        "Ipv6PrefixAddressFamily": "ldpLabelMapping.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.addressFamily-18",
        "Ipv6PrefixPrelen": "ldpLabelMapping.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prelen-19",
        "Ipv6PrefixPrefix": "ldpLabelMapping.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prefix-20",
        "HostAddressType": "ldpLabelMapping.header.fecTLV.fecElement.hostAddress.type-21",
        "Ipv4HostAddressAddressFamily": "ldpLabelMapping.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.addressFamily-22",
        "Ipv4HostAddressHostAddressLength": "ldpLabelMapping.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddressLength-23",
        "Ipv4HostAddressHostAddress": "ldpLabelMapping.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddress-24",
        "Ipv6HostAddressAddressFamily": "ldpLabelMapping.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.addressFamily-25",
        "Ipv6HostAddressHostAddressLength": "ldpLabelMapping.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddressLength-26",
        "Ipv6HostAddressHostAddress": "ldpLabelMapping.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddress-27",
        "TclP2mpTclType": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclType-28",
        "TclIpv4P2mpAddressTclP2mpAddressFamily": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressFamily-29",
        "TclIpv4P2mpAddressTclP2mpAddressLength": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclP2mpAddressLength-30",
        "TclIpv4P2mpAddressTclRootAddress": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv4P2mpAddress.tclRootAddress-31",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressFamily": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressFamily-32",
        "TclIpv6P2mpAddressTclP2mpIpv6AddressLength": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclP2mpIpv6AddressLength-33",
        "TclIpv6P2mpAddressTclIpv6RootAddress": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclAddressFamily.tclIpv6P2mpAddress.tclIpv6RootAddress-34",
        "TclP2mpTclOpaqueLength": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclOpaqueLength-35",
        "TclGenericLSPIdentifierTLVTclType": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclType-36",
        "TclGenericLSPIdentifierTLVTclLength": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclLength-37",
        "TclGenericLSPIdentifierTLVTclValue": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclGenericLSPIdentifierTLV.tclValue-38",
        "TclEditTLVTclType": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclType-39",
        "TclEditTLVTclLength": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclLength-40",
        "TclEditTLVTclValue": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mp.tclOpaqueTlvs.selectTLVType.tclEditTLV.tclValue-41",
        "TclP2mpTypedWcardTclTypeTypedWcard": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeTypedWcard-42",
        "TclP2mpTypedWcardTclTypeWcard": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeWcard-43",
        "TclP2mpTypedWcardTclTypeLen": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeLen-44",
        "TclP2mpTypedWcardTclTypeAfi": "ldpLabelMapping.header.fecTLV.fecElement.tclP2mpTypedWcard.tclTypeAfi-45",
        "GenericLabelTLVUBit": "ldpLabelMapping.header.labelTLV.genericLabelTLV.uBit-46",
        "GenericLabelTLVFBit": "ldpLabelMapping.header.labelTLV.genericLabelTLV.fBit-47",
        "GenericLabelTLVType": "ldpLabelMapping.header.labelTLV.genericLabelTLV.type-48",
        "GenericLabelTLVLength": "ldpLabelMapping.header.labelTLV.genericLabelTLV.length-49",
        "GenericLabelTLVLabel": "ldpLabelMapping.header.labelTLV.genericLabelTLV.label-50",
        "AtmLabelTLVUBit": "ldpLabelMapping.header.labelTLV.atmLabelTLV.uBit-51",
        "AtmLabelTLVFBit": "ldpLabelMapping.header.labelTLV.atmLabelTLV.fBit-52",
        "AtmLabelTLVType": "ldpLabelMapping.header.labelTLV.atmLabelTLV.type-53",
        "AtmLabelTLVLength": "ldpLabelMapping.header.labelTLV.atmLabelTLV.length-54",
        "AtmLabelTLVReserved": "ldpLabelMapping.header.labelTLV.atmLabelTLV.reserved-55",
        "AtmLabelTLVVBits": "ldpLabelMapping.header.labelTLV.atmLabelTLV.vBits-56",
        "AtmLabelTLVVpi": "ldpLabelMapping.header.labelTLV.atmLabelTLV.vpi-57",
        "AtmLabelTLVVci": "ldpLabelMapping.header.labelTLV.atmLabelTLV.vci-58",
        "FrameRelayLabelTLVUBit": "ldpLabelMapping.header.labelTLV.frameRelayLabelTLV.uBit-59",
        "FrameRelayLabelTLVFBit": "ldpLabelMapping.header.labelTLV.frameRelayLabelTLV.fBit-60",
        "FrameRelayLabelTLVType": "ldpLabelMapping.header.labelTLV.frameRelayLabelTLV.type-61",
        "FrameRelayLabelTLVLength": "ldpLabelMapping.header.labelTLV.frameRelayLabelTLV.length-62",
        "FrameRelayLabelTLVReserved": "ldpLabelMapping.header.labelTLV.frameRelayLabelTLV.reserved-63",
        "FrameRelayLabelTLVDlciLength": "ldpLabelMapping.header.labelTLV.frameRelayLabelTLV.dlciLength-64",
        "FrameRelayLabelTLVDlci": "ldpLabelMapping.header.labelTLV.frameRelayLabelTLV.dlci-65",
        "TclOptionalLDPMpStatusTLVUBit": "ldpLabelMapping.header.tclOptionalLDPMpStatusTLV.uBit-66",
        "TclOptionalLDPMpStatusTLVFBit": "ldpLabelMapping.header.tclOptionalLDPMpStatusTLV.fBit-67",
        "TclOptionalLDPMpStatusTLVTclType": "ldpLabelMapping.header.tclOptionalLDPMpStatusTLV.tclType-68",
        "TclOptionalLDPMpStatusTLVTclLength": "ldpLabelMapping.header.tclOptionalLDPMpStatusTLV.tclLength-69",
        "TclCustomTypeTclType": "ldpLabelMapping.header.tclOptionalLDPMpStatusTLV.tclLDPMPStatusValueElements.selectTLVType.tclCustomType.tclType-70",
        "TclCustomTypeTclLength": "ldpLabelMapping.header.tclOptionalLDPMpStatusTLV.tclLDPMPStatusValueElements.selectTLVType.tclCustomType.tclLength-71",
        "TclCustomTypeTclValue": "ldpLabelMapping.header.tclOptionalLDPMpStatusTLV.tclLDPMPStatusValueElements.selectTLVType.tclCustomType.tclValue-72",
        "LabelRequestMessageIDTLVUBit": "ldpLabelMapping.header.optionalParameter.labelRequestMessageIDTLV.uBit-73",
        "LabelRequestMessageIDTLVFBit": "ldpLabelMapping.header.optionalParameter.labelRequestMessageIDTLV.fBit-74",
        "LabelRequestMessageIDTLVType": "ldpLabelMapping.header.optionalParameter.labelRequestMessageIDTLV.type-75",
        "LabelRequestMessageIDTLVLength": "ldpLabelMapping.header.optionalParameter.labelRequestMessageIDTLV.length-76",
        "LabelRequestMessageIDTLVMessageID": "ldpLabelMapping.header.optionalParameter.labelRequestMessageIDTLV.messageID-77",
        "HopCountTLVUBit": "ldpLabelMapping.header.optionalParameter.hopCountTLV.uBit-78",
        "HopCountTLVFBit": "ldpLabelMapping.header.optionalParameter.hopCountTLV.fBit-79",
        "HopCountTLVType": "ldpLabelMapping.header.optionalParameter.hopCountTLV.type-80",
        "HopCountTLVLength": "ldpLabelMapping.header.optionalParameter.hopCountTLV.length-81",
        "HopCountTLVHopCount": "ldpLabelMapping.header.optionalParameter.hopCountTLV.hopCount-82",
        "PathVectorTLVUBit": "ldpLabelMapping.header.optionalParameter.pathVectorTLV.uBit-83",
        "PathVectorTLVFBit": "ldpLabelMapping.header.optionalParameter.pathVectorTLV.fBit-84",
        "PathVectorTLVType": "ldpLabelMapping.header.optionalParameter.pathVectorTLV.type-85",
        "PathVectorTLVLength": "ldpLabelMapping.header.optionalParameter.pathVectorTLV.length-86",
        "PathVectorTLVLsrID": "ldpLabelMapping.header.optionalParameter.pathVectorTLV.lsrID-87",
    }

    def __init__(self, parent, list_op=False):
        super(LdpLabelMapping, self).__init__(parent, list_op)

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
        Default Value: 0x0400
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
        Value Format: hex
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
    def TclOptionalLDPMpStatusTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclOptionalLDPMpStatusTLVUBit"]),
        )

    @property
    def TclOptionalLDPMpStatusTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclOptionalLDPMpStatusTLVFBit"]),
        )

    @property
    def TclOptionalLDPMpStatusTLVTclType(self):
        """
        Display Name: Type
        Default Value: 0x0040
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TclOptionalLDPMpStatusTLVTclType"]),
        )

    @property
    def TclOptionalLDPMpStatusTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TclOptionalLDPMpStatusTLVTclLength"]
            ),
        )

    @property
    def TclCustomTypeTclType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclCustomTypeTclType"])
        )

    @property
    def TclCustomTypeTclLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclCustomTypeTclLength"])
        )

    @property
    def TclCustomTypeTclValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TclCustomTypeTclValue"])
        )

    @property
    def LabelRequestMessageIDTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelRequestMessageIDTLVUBit"])
        )

    @property
    def LabelRequestMessageIDTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelRequestMessageIDTLVFBit"])
        )

    @property
    def LabelRequestMessageIDTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0600
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LabelRequestMessageIDTLVType"])
        )

    @property
    def LabelRequestMessageIDTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LabelRequestMessageIDTLVLength"]),
        )

    @property
    def LabelRequestMessageIDTLVMessageID(self):
        """
        Display Name: Message ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LabelRequestMessageIDTLVMessageID"]),
        )

    @property
    def HopCountTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HopCountTLVUBit"])
        )

    @property
    def HopCountTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HopCountTLVFBit"])
        )

    @property
    def HopCountTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0103
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HopCountTLVType"])
        )

    @property
    def HopCountTLVLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HopCountTLVLength"])
        )

    @property
    def HopCountTLVHopCount(self):
        """
        Display Name: Hop count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HopCountTLVHopCount"])
        )

    @property
    def PathVectorTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathVectorTLVUBit"])
        )

    @property
    def PathVectorTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathVectorTLVFBit"])
        )

    @property
    def PathVectorTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0104
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathVectorTLVType"])
        )

    @property
    def PathVectorTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathVectorTLVLength"])
        )

    @property
    def PathVectorTLVLsrID(self):
        """
        Display Name: LSR ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathVectorTLVLsrID"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
