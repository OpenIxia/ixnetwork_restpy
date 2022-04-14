from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimCandidateRPAdvMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimCandidateRPAdvMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimCandidateRPAdvMessage.header.version-1",
        "HeaderType": "pimCandidateRPAdvMessage.header.type-2",
        "HeaderReserved": "pimCandidateRPAdvMessage.header.reserved-3",
        "HeaderChecksum": "pimCandidateRPAdvMessage.header.checksum-4",
        "HeaderPrefixCnt": "pimCandidateRPAdvMessage.header.prefixCnt-5",
        "HeaderPriority": "pimCandidateRPAdvMessage.header.priority-6",
        "HeaderHoldTime": "pimCandidateRPAdvMessage.header.holdTime-7",
        "EncodedUnicastRPAddressAddrFamily": "pimCandidateRPAdvMessage.header.encodedUnicastRPAddress.addrFamily-8",
        "EncodedUnicastRPAddressEncodingType": "pimCandidateRPAdvMessage.header.encodedUnicastRPAddress.encodingType-9",
        "UnicastAddrAddrIPv4": "pimCandidateRPAdvMessage.header.encodedUnicastRPAddress.unicastAddr.addrIPv4-10",
        "UnicastAddrAddrIPv6": "pimCandidateRPAdvMessage.header.encodedUnicastRPAddress.unicastAddr.addrIPv6-11",
        "EncodedGroupAddressAddrFamily": "pimCandidateRPAdvMessage.header.encodedGroupAddress.addrFamily-12",
        "EncodedGroupAddressEncodingType": "pimCandidateRPAdvMessage.header.encodedGroupAddress.encodingType-13",
        "EncodedGroupAddressB": "pimCandidateRPAdvMessage.header.encodedGroupAddress.b-14",
        "EncodedGroupAddressReserved": "pimCandidateRPAdvMessage.header.encodedGroupAddress.reserved-15",
        "EncodedGroupAddressZ": "pimCandidateRPAdvMessage.header.encodedGroupAddress.z-16",
        "EncodedGroupAddressMaskLength": "pimCandidateRPAdvMessage.header.encodedGroupAddress.maskLength-17",
        "GroupMulticastAddrGrpMcastAddrIPv4": "pimCandidateRPAdvMessage.header.encodedGroupAddress.groupMulticastAddr.grpMcastAddrIPv4-18",
        "GroupMulticastAddrGrpMcastAddrIPv6": "pimCandidateRPAdvMessage.header.encodedGroupAddress.groupMulticastAddr.grpMcastAddrIPv6-19",
    }

    def __init__(self, parent, list_op=False):
        super(PimCandidateRPAdvMessage, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderChecksum"])
        )

    @property
    def HeaderPrefixCnt(self):
        """
        Display Name: Prefix-Cnt
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPrefixCnt"])
        )

    @property
    def HeaderPriority(self):
        """
        Display Name: Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPriority"])
        )

    @property
    def HeaderHoldTime(self):
        """
        Display Name: HoldTime
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHoldTime"])
        )

    @property
    def EncodedUnicastRPAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IP, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EncodedUnicastRPAddressAddrFamily"]),
        )

    @property
    def EncodedUnicastRPAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUnicastRPAddressEncodingType"]
            ),
        )

    @property
    def UnicastAddrAddrIPv4(self):
        """
        Display Name: Addr IPv4
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnicastAddrAddrIPv4"])
        )

    @property
    def UnicastAddrAddrIPv6(self):
        """
        Display Name: Addr IPv6
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnicastAddrAddrIPv6"])
        )

    @property
    def EncodedGroupAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IP, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EncodedGroupAddressAddrFamily"]),
        )

    @property
    def EncodedGroupAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EncodedGroupAddressEncodingType"]),
        )

    @property
    def EncodedGroupAddressB(self):
        """
        Display Name: B
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncodedGroupAddressB"])
        )

    @property
    def EncodedGroupAddressReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncodedGroupAddressReserved"])
        )

    @property
    def EncodedGroupAddressZ(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncodedGroupAddressZ"])
        )

    @property
    def EncodedGroupAddressMaskLength(self):
        """
        Display Name: Mask Length
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EncodedGroupAddressMaskLength"]),
        )

    @property
    def GroupMulticastAddrGrpMcastAddrIPv4(self):
        """
        Display Name: Grp Mcast Addr IPv4
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GroupMulticastAddrGrpMcastAddrIPv4"]
            ),
        )

    @property
    def GroupMulticastAddrGrpMcastAddrIPv6(self):
        """
        Display Name: Grp Mcast Addr IPv6
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GroupMulticastAddrGrpMcastAddrIPv6"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
