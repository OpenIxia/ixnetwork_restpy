from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimBootstrapMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimBootstrapMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimBootstrapMessage.header.version-1",
        "HeaderType": "pimBootstrapMessage.header.type-2",
        "HeaderReserved": "pimBootstrapMessage.header.reserved-3",
        "HeaderChecksum": "pimBootstrapMessage.header.checksum-4",
        "HeaderFragmentTag": "pimBootstrapMessage.header.fragmentTag-5",
        "HeaderHashMaskLen": "pimBootstrapMessage.header.hashMaskLen-6",
        "HeaderBsrpriority": "pimBootstrapMessage.header.bsrpriority-7",
        "EncodedUnicastBSRAddressAddrFamily": "pimBootstrapMessage.header.encodedUnicastBSRAddress.addrFamily-8",
        "EncodedUnicastBSRAddressEncodingType": "pimBootstrapMessage.header.encodedUnicastBSRAddress.encodingType-9",
        "UnicastAddrAddrIPv4": "pimBootstrapMessage.header.encodedUnicastBSRAddress.unicastAddr.addrIPv4-10",
        "UnicastAddrAddrIPv6": "pimBootstrapMessage.header.encodedUnicastBSRAddress.unicastAddr.addrIPv6-11",
        "EncodedGroupAddressAddrFamily": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.addrFamily-12",
        "EncodedGroupAddressEncodingType": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.encodingType-13",
        "EncodedGroupAddressB": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.b-14",
        "EncodedGroupAddressReserved": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.reserved-15",
        "EncodedGroupAddressZ": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.z-16",
        "EncodedGroupAddressMaskLength": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.maskLength-17",
        "GroupMulticastAddrGrpMcastAddrIPv4": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.groupMulticastAddr.grpMcastAddrIPv4-18",
        "GroupMulticastAddrGrpMcastAddrIPv6": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedGroupAddress.groupMulticastAddr.grpMcastAddrIPv6-19",
        "EncodedGroupAddressFieldsRpcount": "pimBootstrapMessage.header.encodedGroupAddressFields.rpcount-20",
        "EncodedGroupAddressFieldsFragRPCount": "pimBootstrapMessage.header.encodedGroupAddressFields.fragRPCount-21",
        "EncodedGroupAddressFieldsReserved1": "pimBootstrapMessage.header.encodedGroupAddressFields.reserved1-22",
        "EncodedUnicastRPAddressAddrFamily": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedUnicastRPAddressFields.encodedUnicastRPAddress.addrFamily-23",
        "EncodedUnicastRPAddressEncodingType": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedUnicastRPAddressFields.encodedUnicastRPAddress.encodingType-24",
        "RpAddrAddrIPv4": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedUnicastRPAddressFields.encodedUnicastRPAddress.rpAddr.addrIPv4-25",
        "RpAddrAddrIPv6": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedUnicastRPAddressFields.encodedUnicastRPAddress.rpAddr.addrIPv6-26",
        "EncodedUnicastRPAddressFieldsRpholdTime": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedUnicastRPAddressFields.rpholdTime-27",
        "EncodedUnicastRPAddressFieldsRppriority": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedUnicastRPAddressFields.rppriority-28",
        "EncodedUnicastRPAddressFieldsReserved2": "pimBootstrapMessage.header.encodedGroupAddressFields.encodedUnicastRPAddressFields.reserved2-29",
    }

    def __init__(self, parent, list_op=False):
        super(PimBootstrapMessage, self).__init__(parent, list_op)

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
        Default Value: 4
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
    def HeaderFragmentTag(self):
        """
        Display Name: Fragment Tag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFragmentTag"])
        )

    @property
    def HeaderHashMaskLen(self):
        """
        Display Name: Hash Mask Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHashMaskLen"])
        )

    @property
    def HeaderBsrpriority(self):
        """
        Display Name: BSR-priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBsrpriority"])
        )

    @property
    def EncodedUnicastBSRAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IP, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUnicastBSRAddressAddrFamily"]
            ),
        )

    @property
    def EncodedUnicastBSRAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUnicastBSRAddressEncodingType"]
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
        Default Value: 0:0:0:0:0:0:0:0
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
        Default Value: 0:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GroupMulticastAddrGrpMcastAddrIPv6"]
            ),
        )

    @property
    def EncodedGroupAddressFieldsRpcount(self):
        """
        Display Name: RP-Count
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EncodedGroupAddressFieldsRpcount"]),
        )

    @property
    def EncodedGroupAddressFieldsFragRPCount(self):
        """
        Display Name: Frag RP-Count
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedGroupAddressFieldsFragRPCount"]
            ),
        )

    @property
    def EncodedGroupAddressFieldsReserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedGroupAddressFieldsReserved1"]
            ),
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
    def RpAddrAddrIPv4(self):
        """
        Display Name: Addr IPv4
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RpAddrAddrIPv4"])
        )

    @property
    def RpAddrAddrIPv6(self):
        """
        Display Name: Addr IPv6
        Default Value: 0:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RpAddrAddrIPv6"])
        )

    @property
    def EncodedUnicastRPAddressFieldsRpholdTime(self):
        """
        Display Name: RP-HoldTime
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUnicastRPAddressFieldsRpholdTime"]
            ),
        )

    @property
    def EncodedUnicastRPAddressFieldsRppriority(self):
        """
        Display Name: RP-Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUnicastRPAddressFieldsRppriority"]
            ),
        )

    @property
    def EncodedUnicastRPAddressFieldsReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUnicastRPAddressFieldsReserved2"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
