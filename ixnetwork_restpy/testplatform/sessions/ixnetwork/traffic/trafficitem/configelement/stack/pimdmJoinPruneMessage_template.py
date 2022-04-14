from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimdmJoinPruneMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimdmJoinPruneMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimdmJoinPruneMessage.header.version-1",
        "HeaderType": "pimdmJoinPruneMessage.header.type-2",
        "HeaderReserved": "pimdmJoinPruneMessage.header.reserved-3",
        "HeaderChecksum": "pimdmJoinPruneMessage.header.checksum-4",
        "UpstreamNeighborAddressAddrFamily": "pimdmJoinPruneMessage.header.upstreamNeighborAddress.addrFamily-5",
        "UpstreamNeighborAddressEncodingType": "pimdmJoinPruneMessage.header.upstreamNeighborAddress.encodingType-6",
        "UnicastAddrAddrIPv4": "pimdmJoinPruneMessage.header.upstreamNeighborAddress.unicastAddr.addrIPv4-7",
        "UnicastAddrAddrIPv6": "pimdmJoinPruneMessage.header.upstreamNeighborAddress.unicastAddr.addrIPv6-8",
        "HeaderReserved": "pimdmJoinPruneMessage.header.reserved-9",
        "HeaderNumGroups": "pimdmJoinPruneMessage.header.numGroups-10",
        "HeaderHoldTime": "pimdmJoinPruneMessage.header.holdTime-11",
        "MulticastGroupAddressAddrFamily": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.addrFamily-12",
        "MulticastGroupAddressEncodingType": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.encodingType-13",
        "MulticastGroupAddressB": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.b-14",
        "MulticastGroupAddressReserved": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.reserved-15",
        "MulticastGroupAddressZ": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.z-16",
        "MulticastGroupAddressMaskLength": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.maskLength-17",
        "GrpAddrFieldGroupMCastAddrIP4": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.grpAddrField.groupMCastAddrIP4-18",
        "GrpAddrFieldGroupMCastAddrIP6": "pimdmJoinPruneMessage.header.nextFields.multicastGroupAddress.grpAddrField.groupMCastAddrIP6-19",
        "NextFieldsNumOfJoinedSources": "pimdmJoinPruneMessage.header.nextFields.numOfJoinedSources-20",
        "NextFieldsNumOfPrunedSources": "pimdmJoinPruneMessage.header.nextFields.numOfPrunedSources-21",
        "JoinedSourceAddressAddrFamily": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.addrFamily-22",
        "JoinedSourceAddressEncodingType": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.encodingType-23",
        "JoinedSourceAddressReserved": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.reserved-24",
        "JoinedSourceAddressS": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.s-25",
        "JoinedSourceAddressW": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.w-26",
        "JoinedSourceAddressR": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.r-27",
        "JoinedSourceAddressMaskLength": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.maskLength-28",
        "JoinedSrcAddrFieldJoinSrcAddrIP4": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.joinedSrcAddrField.joinSrcAddrIP4-29",
        "JoinedSrcAddrFieldJoinSrcAddrIP6": "pimdmJoinPruneMessage.header.nextFields.joinedSourceAddress.joinedSrcAddrField.joinSrcAddrIP6-30",
        "PrunedSourceAddressAddrFamily": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.addrFamily-31",
        "PrunedSourceAddressEncodingType": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.encodingType-32",
        "PrunedSourceAddressReserved": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.reserved-33",
        "PrunedSourceAddressS": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.s-34",
        "PrunedSourceAddressW": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.w-35",
        "PrunedSourceAddressR": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.r-36",
        "PrunedSourceAddressMaskLength": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.maskLength-37",
        "PrunedSrcAddrFieldPruneSrcAddrIP4": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.prunedSrcAddrField.pruneSrcAddrIP4-38",
        "PrunedSrcAddrFieldPruneSrcAddrIP6": "pimdmJoinPruneMessage.header.nextFields.prunedSourceAddress.prunedSrcAddrField.pruneSrcAddrIP6-39",
    }

    def __init__(self, parent, list_op=False):
        super(PimdmJoinPruneMessage, self).__init__(parent, list_op)

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
        Default Value: 3
        Value Format: decimal
        Available enum values: Join/Prune, 3
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
    def UpstreamNeighborAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IPv4, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["UpstreamNeighborAddressAddrFamily"]),
        )

    @property
    def UpstreamNeighborAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UpstreamNeighborAddressEncodingType"]
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
    def HeaderNumGroups(self):
        """
        Display Name: Num groups
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNumGroups"])
        )

    @property
    def HeaderHoldTime(self):
        """
        Display Name: HoldTime
        Default Value: 0xb4
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHoldTime"])
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
    def NextFieldsNumOfJoinedSources(self):
        """
        Display Name: Num of joined sources
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextFieldsNumOfJoinedSources"])
        )

    @property
    def NextFieldsNumOfPrunedSources(self):
        """
        Display Name: Num of pruned sources
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextFieldsNumOfPrunedSources"])
        )

    @property
    def JoinedSourceAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IPv4, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["JoinedSourceAddressAddrFamily"]),
        )

    @property
    def JoinedSourceAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["JoinedSourceAddressEncodingType"]),
        )

    @property
    def JoinedSourceAddressReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JoinedSourceAddressReserved"])
        )

    @property
    def JoinedSourceAddressS(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JoinedSourceAddressS"])
        )

    @property
    def JoinedSourceAddressW(self):
        """
        Display Name: W
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JoinedSourceAddressW"])
        )

    @property
    def JoinedSourceAddressR(self):
        """
        Display Name: R
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["JoinedSourceAddressR"])
        )

    @property
    def JoinedSourceAddressMaskLength(self):
        """
        Display Name: Mask Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["JoinedSourceAddressMaskLength"]),
        )

    @property
    def JoinedSrcAddrFieldJoinSrcAddrIP4(self):
        """
        Display Name: Join Src Addr IP4
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["JoinedSrcAddrFieldJoinSrcAddrIP4"]),
        )

    @property
    def JoinedSrcAddrFieldJoinSrcAddrIP6(self):
        """
        Display Name: Join Src Addr IP6
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["JoinedSrcAddrFieldJoinSrcAddrIP6"]),
        )

    @property
    def PrunedSourceAddressAddrFamily(self):
        """
        Display Name: Addr Family
        Default Value: 1
        Value Format: decimal
        Available enum values: IPv4, 1, IPv6, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrunedSourceAddressAddrFamily"]),
        )

    @property
    def PrunedSourceAddressEncodingType(self):
        """
        Display Name: Encoding Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrunedSourceAddressEncodingType"]),
        )

    @property
    def PrunedSourceAddressReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrunedSourceAddressReserved"])
        )

    @property
    def PrunedSourceAddressS(self):
        """
        Display Name: S
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrunedSourceAddressS"])
        )

    @property
    def PrunedSourceAddressW(self):
        """
        Display Name: W
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrunedSourceAddressW"])
        )

    @property
    def PrunedSourceAddressR(self):
        """
        Display Name: R
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrunedSourceAddressR"])
        )

    @property
    def PrunedSourceAddressMaskLength(self):
        """
        Display Name: Mask Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrunedSourceAddressMaskLength"]),
        )

    @property
    def PrunedSrcAddrFieldPruneSrcAddrIP4(self):
        """
        Display Name: Prune Src Addr IP4
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrunedSrcAddrFieldPruneSrcAddrIP4"]),
        )

    @property
    def PrunedSrcAddrFieldPruneSrcAddrIP6(self):
        """
        Display Name: Prune Src Addr IP6
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["PrunedSrcAddrFieldPruneSrcAddrIP6"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
