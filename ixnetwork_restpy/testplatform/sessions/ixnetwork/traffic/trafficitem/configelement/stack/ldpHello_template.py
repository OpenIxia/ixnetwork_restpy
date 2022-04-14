from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpHello(Base):
    __slots__ = ()
    _SDM_NAME = "ldpHello"
    _SDM_ATT_MAP = {
        "HeaderVersion": "ldpHello.header.version-1",
        "HeaderPduLengthinOctets": "ldpHello.header.pduLengthinOctets-2",
        "HeaderLsrID": "ldpHello.header.lsrID-3",
        "HeaderLabelSpace": "ldpHello.header.labelSpace-4",
        "HeaderUBit": "ldpHello.header.uBit-5",
        "HeaderType": "ldpHello.header.type-6",
        "HeaderLength": "ldpHello.header.length-7",
        "HeaderMessageID": "ldpHello.header.messageID-8",
        "CommonHelloParametersTLVUBit": "ldpHello.header.commonHelloParametersTLV.uBit-9",
        "CommonHelloParametersTLVFBit": "ldpHello.header.commonHelloParametersTLV.fBit-10",
        "CommonHelloParametersTLVType": "ldpHello.header.commonHelloParametersTLV.type-11",
        "CommonHelloParametersTLVLength": "ldpHello.header.commonHelloParametersTLV.length-12",
        "CommonHelloParametersTLVHoldTime": "ldpHello.header.commonHelloParametersTLV.holdTime-13",
        "CommonHelloParametersTLVTBit": "ldpHello.header.commonHelloParametersTLV.tBit-14",
        "CommonHelloParametersTLVRBit": "ldpHello.header.commonHelloParametersTLV.rBit-15",
        "CommonHelloParametersTLVReserved": "ldpHello.header.commonHelloParametersTLV.reserved-16",
        "Ipv4TransportAddressTLVUBit": "ldpHello.header.optionalParameter.ipv4TransportAddressTLV.uBit-17",
        "Ipv4TransportAddressTLVFBit": "ldpHello.header.optionalParameter.ipv4TransportAddressTLV.fBit-18",
        "Ipv4TransportAddressTLVType": "ldpHello.header.optionalParameter.ipv4TransportAddressTLV.type-19",
        "Ipv4TransportAddressTLVLength": "ldpHello.header.optionalParameter.ipv4TransportAddressTLV.length-20",
        "Ipv4TransportAddressTLVIpv4Address": "ldpHello.header.optionalParameter.ipv4TransportAddressTLV.ipv4Address-21",
        "ConfigurationSequenceNumberTLVUBit": "ldpHello.header.optionalParameter.configurationSequenceNumberTLV.uBit-22",
        "ConfigurationSequenceNumberTLVFBit": "ldpHello.header.optionalParameter.configurationSequenceNumberTLV.fBit-23",
        "ConfigurationSequenceNumberTLVType": "ldpHello.header.optionalParameter.configurationSequenceNumberTLV.type-24",
        "ConfigurationSequenceNumberTLVLength": "ldpHello.header.optionalParameter.configurationSequenceNumberTLV.length-25",
        "ConfigurationSequenceNumberTLVSequenceNumber": "ldpHello.header.optionalParameter.configurationSequenceNumberTLV.sequenceNumber-26",
        "Ipv6TransportAddressTLVUBit": "ldpHello.header.optionalParameter.ipv6TransportAddressTLV.uBit-27",
        "Ipv6TransportAddressTLVFBit": "ldpHello.header.optionalParameter.ipv6TransportAddressTLV.fBit-28",
        "Ipv6TransportAddressTLVType": "ldpHello.header.optionalParameter.ipv6TransportAddressTLV.type-29",
        "Ipv6TransportAddressTLVLength": "ldpHello.header.optionalParameter.ipv6TransportAddressTLV.length-30",
        "Ipv6TransportAddressTLVIpv6Address": "ldpHello.header.optionalParameter.ipv6TransportAddressTLV.ipv6Address-31",
    }

    def __init__(self, parent, list_op=False):
        super(LdpHello, self).__init__(parent, list_op)

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
        Default Value: 0x0100
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
    def CommonHelloParametersTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVUBit"])
        )

    @property
    def CommonHelloParametersTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVFBit"])
        )

    @property
    def CommonHelloParametersTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0400
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVType"])
        )

    @property
    def CommonHelloParametersTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVLength"]),
        )

    @property
    def CommonHelloParametersTLVHoldTime(self):
        """
        Display Name: Hold time
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVHoldTime"]),
        )

    @property
    def CommonHelloParametersTLVTBit(self):
        """
        Display Name: T bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Link hello, 0, Targeted hello, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVTBit"])
        )

    @property
    def CommonHelloParametersTLVRBit(self):
        """
        Display Name: R bit
        Default Value: 0
        Value Format: decimal
        Available enum values: No request, 0, Request periodic targeted hellos, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVRBit"])
        )

    @property
    def CommonHelloParametersTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CommonHelloParametersTLVReserved"]),
        )

    @property
    def Ipv4TransportAddressTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4TransportAddressTLVUBit"])
        )

    @property
    def Ipv4TransportAddressTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4TransportAddressTLVFBit"])
        )

    @property
    def Ipv4TransportAddressTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0401
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4TransportAddressTLVType"])
        )

    @property
    def Ipv4TransportAddressTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4TransportAddressTLVLength"]),
        )

    @property
    def Ipv4TransportAddressTLVIpv4Address(self):
        """
        Display Name: IPv4 address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4TransportAddressTLVIpv4Address"]
            ),
        )

    @property
    def ConfigurationSequenceNumberTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigurationSequenceNumberTLVUBit"]
            ),
        )

    @property
    def ConfigurationSequenceNumberTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigurationSequenceNumberTLVFBit"]
            ),
        )

    @property
    def ConfigurationSequenceNumberTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0402
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigurationSequenceNumberTLVType"]
            ),
        )

    @property
    def ConfigurationSequenceNumberTLVLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigurationSequenceNumberTLVLength"]
            ),
        )

    @property
    def ConfigurationSequenceNumberTLVSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ConfigurationSequenceNumberTLVSequenceNumber"]
            ),
        )

    @property
    def Ipv6TransportAddressTLVUBit(self):
        """
        Display Name: U bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ignore entire message if unknown TLV, 0, Ignore only unknown TLV, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6TransportAddressTLVUBit"])
        )

    @property
    def Ipv6TransportAddressTLVFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not forward, 0, Forward, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6TransportAddressTLVFBit"])
        )

    @property
    def Ipv6TransportAddressTLVType(self):
        """
        Display Name: Type
        Default Value: 0x0403
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6TransportAddressTLVType"])
        )

    @property
    def Ipv6TransportAddressTLVLength(self):
        """
        Display Name: Length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6TransportAddressTLVLength"]),
        )

    @property
    def Ipv6TransportAddressTLVIpv6Address(self):
        """
        Display Name: IPv6 address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6TransportAddressTLVIpv6Address"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
