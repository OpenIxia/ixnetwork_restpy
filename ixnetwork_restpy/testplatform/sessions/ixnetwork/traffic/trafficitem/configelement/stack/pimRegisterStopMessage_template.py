from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimRegisterStopMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimRegisterStopMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimRegisterStopMessage.header.version-1",
        "HeaderType": "pimRegisterStopMessage.header.type-2",
        "HeaderReserved": "pimRegisterStopMessage.header.reserved-3",
        "HeaderChecksum": "pimRegisterStopMessage.header.checksum-4",
        "EncodedGrpAddressGrpAddrFamily": "pimRegisterStopMessage.header.encodedGrpAddress.grpAddrFamily-5",
        "EncodedGrpAddressEncodingType": "pimRegisterStopMessage.header.encodedGrpAddress.encodingType-6",
        "EncodedGrpAddressB": "pimRegisterStopMessage.header.encodedGrpAddress.b-7",
        "EncodedGrpAddressReserved": "pimRegisterStopMessage.header.encodedGrpAddress.reserved-8",
        "EncodedGrpAddressZ": "pimRegisterStopMessage.header.encodedGrpAddress.z-9",
        "EncodedGrpAddressMaskLength": "pimRegisterStopMessage.header.encodedGrpAddress.maskLength-10",
        "GroupMulticastAddrGrpMcastAddrIPv4": "pimRegisterStopMessage.header.encodedGrpAddress.groupMulticastAddr.grpMcastAddrIPv4-11",
        "GroupMulticastAddrGrpMcastAddrIPv6": "pimRegisterStopMessage.header.encodedGrpAddress.groupMulticastAddr.grpMcastAddrIPv6-12",
        "EncodedUcastSrcAddressSrcAddrFamily": "pimRegisterStopMessage.header.encodedUcastSrcAddress.srcAddrFamily-13",
        "EncodedUcastSrcAddressEncodingType": "pimRegisterStopMessage.header.encodedUcastSrcAddress.encodingType-14",
        "SrcAddrOfMcastTrafficSrcAddrIPv4": "pimRegisterStopMessage.header.encodedUcastSrcAddress.srcAddrOfMcastTraffic.srcAddrIPv4-15",
        "SrcAddrOfMcastTrafficSrcAddrIPv6": "pimRegisterStopMessage.header.encodedUcastSrcAddress.srcAddrOfMcastTraffic.srcAddrIPv6-16",
    }

    def __init__(self, parent, list_op=False):
        super(PimRegisterStopMessage, self).__init__(parent, list_op)

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
        Default Value: 2
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
    def EncodedGrpAddressGrpAddrFamily(self):
        """
        Display Name:  Grp Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IP, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EncodedGrpAddressGrpAddrFamily"]),
        )

    @property
    def EncodedGrpAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["EncodedGrpAddressEncodingType"]),
        )

    @property
    def EncodedGrpAddressB(self):
        """
        Display Name: B
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncodedGrpAddressB"])
        )

    @property
    def EncodedGrpAddressReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncodedGrpAddressReserved"])
        )

    @property
    def EncodedGrpAddressZ(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncodedGrpAddressZ"])
        )

    @property
    def EncodedGrpAddressMaskLength(self):
        """
        Display Name: Mask Length
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EncodedGrpAddressMaskLength"])
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

    @property
    def EncodedUcastSrcAddressSrcAddrFamily(self):
        """
        Display Name: Src Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IP, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUcastSrcAddressSrcAddrFamily"]
            ),
        )

    @property
    def EncodedUcastSrcAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["EncodedUcastSrcAddressEncodingType"]
            ),
        )

    @property
    def SrcAddrOfMcastTrafficSrcAddrIPv4(self):
        """
        Display Name: Src Addr IPv4
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcAddrOfMcastTrafficSrcAddrIPv4"]),
        )

    @property
    def SrcAddrOfMcastTrafficSrcAddrIPv6(self):
        """
        Display Name: Src Addr IPv6
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcAddrOfMcastTrafficSrcAddrIPv6"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
