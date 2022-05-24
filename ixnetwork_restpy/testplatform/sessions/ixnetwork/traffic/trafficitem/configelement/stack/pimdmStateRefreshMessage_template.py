from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimdmStateRefreshMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimdmStateRefreshMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimdmStateRefreshMessage.header.version-1",
        "HeaderType": "pimdmStateRefreshMessage.header.type-2",
        "HeaderReserved": "pimdmStateRefreshMessage.header.reserved-3",
        "HeaderChecksum": "pimdmStateRefreshMessage.header.checksum-4",
        "MulticastGroupAddressAddrFamily": "pimdmStateRefreshMessage.header.multicastGroupAddress.addrFamily-5",
        "MulticastGroupAddressEncodingType": "pimdmStateRefreshMessage.header.multicastGroupAddress.encodingType-6",
        "MulticastGroupAddressB": "pimdmStateRefreshMessage.header.multicastGroupAddress.b-7",
        "MulticastGroupAddressReserved": "pimdmStateRefreshMessage.header.multicastGroupAddress.reserved-8",
        "MulticastGroupAddressZ": "pimdmStateRefreshMessage.header.multicastGroupAddress.z-9",
        "MulticastGroupAddressMaskLength": "pimdmStateRefreshMessage.header.multicastGroupAddress.maskLength-10",
        "GrpAddrFieldGroupMCastAddrIP4": "pimdmStateRefreshMessage.header.multicastGroupAddress.grpAddrField.groupMCastAddrIP4-11",
        "GrpAddrFieldGroupMCastAddrIP6": "pimdmStateRefreshMessage.header.multicastGroupAddress.grpAddrField.groupMCastAddrIP6-12",
        "SourceAddressAddrFamily": "pimdmStateRefreshMessage.header.sourceAddress.addrFamily-13",
        "SourceAddressEncodingType": "pimdmStateRefreshMessage.header.sourceAddress.encodingType-14",
        "UnicastAddrAddrIPv4": "pimdmStateRefreshMessage.header.sourceAddress.unicastAddr.addrIPv4-15",
        "UnicastAddrAddrIPv6": "pimdmStateRefreshMessage.header.sourceAddress.unicastAddr.addrIPv6-16",
        "OriginatorAddressAddrFamily": "pimdmStateRefreshMessage.header.originatorAddress.addrFamily-17",
        "OriginatorAddressEncodingType": "pimdmStateRefreshMessage.header.originatorAddress.encodingType-18",
        "UnicastAddrAddrIPv4": "pimdmStateRefreshMessage.header.originatorAddress.unicastAddr.addrIPv4-19",
        "UnicastAddrAddrIPv6": "pimdmStateRefreshMessage.header.originatorAddress.unicastAddr.addrIPv6-20",
        "HeaderR": "pimdmStateRefreshMessage.header.r-21",
        "HeaderMetricPreference": "pimdmStateRefreshMessage.header.metricPreference-22",
        "HeaderMetric": "pimdmStateRefreshMessage.header.metric-23",
        "HeaderMasklength": "pimdmStateRefreshMessage.header.masklength-24",
        "HeaderTtl": "pimdmStateRefreshMessage.header.ttl-25",
        "HeaderP": "pimdmStateRefreshMessage.header.p-26",
        "HeaderN": "pimdmStateRefreshMessage.header.n-27",
        "HeaderO": "pimdmStateRefreshMessage.header.o-28",
        "HeaderReserved": "pimdmStateRefreshMessage.header.reserved-29",
        "HeaderIntervalinSec": "pimdmStateRefreshMessage.header.intervalinSec-30",
    }

    def __init__(self, parent, list_op=False):
        super(PimdmStateRefreshMessage, self).__init__(parent, list_op)

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
        Default Value: 9
        Value Format: decimal
        Available enum values: State Refresh, 9
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
    def MulticastGroupAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IPv4, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastGroupAddressAddrFamily"]),
        )

    @property
    def MulticastGroupAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastGroupAddressEncodingType"]),
        )

    @property
    def MulticastGroupAddressB(self):
        """
        Display Name: B
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastGroupAddressB"])
        )

    @property
    def MulticastGroupAddressReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastGroupAddressReserved"]),
        )

    @property
    def MulticastGroupAddressZ(self):
        """
        Display Name: Z
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastGroupAddressZ"])
        )

    @property
    def MulticastGroupAddressMaskLength(self):
        """
        Display Name: Mask Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastGroupAddressMaskLength"]),
        )

    @property
    def GrpAddrFieldGroupMCastAddrIP4(self):
        """
        Display Name: Group MCast Addr IP4
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GrpAddrFieldGroupMCastAddrIP4"]),
        )

    @property
    def GrpAddrFieldGroupMCastAddrIP6(self):
        """
        Display Name: Group MCast Addr IP6
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["GrpAddrFieldGroupMCastAddrIP6"]),
        )

    @property
    def SourceAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IPv4, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceAddressAddrFamily"])
        )

    @property
    def SourceAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SourceAddressEncodingType"])
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
    def OriginatorAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IPv4, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OriginatorAddressAddrFamily"])
        )

    @property
    def OriginatorAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OriginatorAddressEncodingType"]),
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
    def HeaderR(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderR"]))

    @property
    def HeaderMetricPreference(self):
        """
        Display Name: Metric Preference
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMetricPreference"])
        )

    @property
    def HeaderMetric(self):
        """
        Display Name: Metric
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderMetric"]))

    @property
    def HeaderMasklength(self):
        """
        Display Name: Masklength
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMasklength"])
        )

    @property
    def HeaderTtl(self):
        """
        Display Name: TTL
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderTtl"]))

    @property
    def HeaderP(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderP"]))

    @property
    def HeaderN(self):
        """
        Display Name: N
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderN"]))

    @property
    def HeaderO(self):
        """
        Display Name: O
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderO"]))

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
    def HeaderIntervalinSec(self):
        """
        Display Name: Interval(in sec)
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderIntervalinSec"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
