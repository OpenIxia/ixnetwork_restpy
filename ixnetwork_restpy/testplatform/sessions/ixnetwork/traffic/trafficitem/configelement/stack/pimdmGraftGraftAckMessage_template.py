from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimdmGraftGraftAckMessage(Base):
    __slots__ = ()
    _SDM_NAME = "pimdmGraftGraftAckMessage"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimdmGraftGraftAckMessage.header.version-1",
        "HeaderType": "pimdmGraftGraftAckMessage.header.type-2",
        "HeaderReserved": "pimdmGraftGraftAckMessage.header.reserved-3",
        "HeaderChecksum": "pimdmGraftGraftAckMessage.header.checksum-4",
        "UpstreamNeighborAddressAddrFamily": "pimdmGraftGraftAckMessage.header.upstreamNeighborAddress.addrFamily-5",
        "UpstreamNeighborAddressEncodingType": "pimdmGraftGraftAckMessage.header.upstreamNeighborAddress.encodingType-6",
        "UnicastAddrAddrIPv4": "pimdmGraftGraftAckMessage.header.upstreamNeighborAddress.unicastAddr.addrIPv4-7",
        "UnicastAddrAddrIPv6": "pimdmGraftGraftAckMessage.header.upstreamNeighborAddress.unicastAddr.addrIPv6-8",
        "HeaderReserved": "pimdmGraftGraftAckMessage.header.reserved-9",
        "HeaderNumGroups": "pimdmGraftGraftAckMessage.header.numGroups-10",
        "HeaderHoldTime": "pimdmGraftGraftAckMessage.header.holdTime-11",
        "MulticastGroupAddressAddrFamily": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.addrFamily-12",
        "MulticastGroupAddressEncodingType": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.encodingType-13",
        "MulticastGroupAddressB": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.b-14",
        "MulticastGroupAddressReserved": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.reserved-15",
        "MulticastGroupAddressZ": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.z-16",
        "MulticastGroupAddressMaskLength": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.maskLength-17",
        "GrpAddrFieldGroupMCastAddrIP4": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.grpAddrField.groupMCastAddrIP4-18",
        "GrpAddrFieldGroupMCastAddrIP6": "pimdmGraftGraftAckMessage.header.nextFields.multicastGroupAddress.grpAddrField.groupMCastAddrIP6-19",
        "NextFieldsNumOfJoinedSources": "pimdmGraftGraftAckMessage.header.nextFields.numOfJoinedSources-20",
        "JoinedSourceAddressAddrFamily": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.addrFamily-21",
        "JoinedSourceAddressEncodingType": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.encodingType-22",
        "JoinedSourceAddressReserved": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.reserved-23",
        "JoinedSourceAddressS": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.s-24",
        "JoinedSourceAddressW": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.w-25",
        "JoinedSourceAddressR": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.r-26",
        "JoinedSourceAddressMaskLength": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.maskLength-27",
        "JoinedSrcAddrFieldJoinSrcAddrIP4": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.joinedSrcAddrField.joinSrcAddrIP4-28",
        "JoinedSrcAddrFieldJoinSrcAddrIP6": "pimdmGraftGraftAckMessage.header.nextFields.joinedSourceAddress.joinedSrcAddrField.joinSrcAddrIP6-29",
    }

    def __init__(self, parent, list_op=False):
        super(PimdmGraftGraftAckMessage, self).__init__(parent, list_op)

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
        Default Value: 6
        Value Format: decimal
        Available enum values: Graft, 6, Graft-Ack, 7
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
        Default Value: 0x0
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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
