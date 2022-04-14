from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpLabelAbortRequest(Base):
    __slots__ = ()
    _SDM_NAME = "ldpLabelAbortRequest"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpLabelAbortRequest.header.version-1",
        "HeaderPduLengthinOctets": "ldpLabelAbortRequest.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpLabelAbortRequest.header.lsrID-3",
        "HeaderLabelSpace": "ldpLabelAbortRequest.header.labelSpace-4",
        "HeaderUBit": "ldpLabelAbortRequest.header.uBit-5",
        "HeaderType": "ldpLabelAbortRequest.header.type-6",
        "HeaderLength": "ldpLabelAbortRequest.header.length-7",
        "HeaderMessageID": "ldpLabelAbortRequest.header.messageID-8",
        "FecTLVUBit": "ldpLabelAbortRequest.header.fecTLV.uBit-9",
        "FecTLVFBit": "ldpLabelAbortRequest.header.fecTLV.fBit-10",
        "FecTLVType": "ldpLabelAbortRequest.header.fecTLV.type-11",
        "FecTLVLength": "ldpLabelAbortRequest.header.fecTLV.length-12",
        "WildcardType": "ldpLabelAbortRequest.header.fecTLV.fecElement.wildcard.type-13",
        "PrefixType": "ldpLabelAbortRequest.header.fecTLV.fecElement.prefix.type-14",
        "Ipv4PrefixAddressFamily": "ldpLabelAbortRequest.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.addressFamily-15",
        "Ipv4PrefixPrelen": "ldpLabelAbortRequest.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prelen-16",
        "Ipv4PrefixPrefix": "ldpLabelAbortRequest.header.fecTLV.fecElement.prefix.addressFamily.ipv4Prefix.prefix-17",
        "Ipv6PrefixAddressFamily": "ldpLabelAbortRequest.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.addressFamily-18",
        "Ipv6PrefixPrelen": "ldpLabelAbortRequest.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prelen-19",
        "Ipv6PrefixPrefix": "ldpLabelAbortRequest.header.fecTLV.fecElement.prefix.addressFamily.ipv6Prefix.prefix-20",
        "HostAddressType": "ldpLabelAbortRequest.header.fecTLV.fecElement.hostAddress.type-21",
        "Ipv4HostAddressAddressFamily": "ldpLabelAbortRequest.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.addressFamily-22",
        "Ipv4HostAddressHostAddressLength": "ldpLabelAbortRequest.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddressLength-23",
        "Ipv4HostAddressHostAddress": "ldpLabelAbortRequest.header.fecTLV.fecElement.hostAddress.addressFamily.ipv4HostAddress.hostAddress-24",
        "Ipv6HostAddressAddressFamily": "ldpLabelAbortRequest.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.addressFamily-25",
        "Ipv6HostAddressHostAddressLength": "ldpLabelAbortRequest.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddressLength-26",
        "Ipv6HostAddressHostAddress": "ldpLabelAbortRequest.header.fecTLV.fecElement.hostAddress.addressFamily.ipv6HostAddress.hostAddress-27",
        "LabelRequestMessageIDTLVUBit": "ldpLabelAbortRequest.header.labelRequestMessageIDTLV.uBit-28",
        "LabelRequestMessageIDTLVFBit": "ldpLabelAbortRequest.header.labelRequestMessageIDTLV.fBit-29",
        "LabelRequestMessageIDTLVType": "ldpLabelAbortRequest.header.labelRequestMessageIDTLV.type-30",
        "LabelRequestMessageIDTLVLength": "ldpLabelAbortRequest.header.labelRequestMessageIDTLV.length-31",
        "LabelRequestMessageIDTLVMessageID": "ldpLabelAbortRequest.header.labelRequestMessageIDTLV.messageID-32",
    }

    def __init__(self, parent, list_op=False):
        super(LdpLabelAbortRequest, self).__init__(parent, list_op)

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
        Default Value: 0x0404
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
        Default Value: 0:0:0:0:0:0:0:0
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
        Default Value: 0*
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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
