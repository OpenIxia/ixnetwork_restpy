from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ddp(Base):
    __slots__ = ()
    _SDM_NAME = "ddp"
    _SDM_ATT_MAP = {
        "LongHeaderUnused": "ddp.header.header.longHeader.unused-1",
        "LongHeaderHopCount": "ddp.header.header.longHeader.hopCount-2",
        "LongHeaderLength": "ddp.header.header.longHeader.length-3",
        "ChecksumNoChecksum": "ddp.header.header.longHeader.checksum.noChecksum-4",
        "ChecksumDdpChecksum": "ddp.header.header.longHeader.checksum.ddpChecksum-5",
        "LongHeaderDstNetworkNo": "ddp.header.header.longHeader.dstNetworkNo-6",
        "LongHeaderSrcNetworkNo": "ddp.header.header.longHeader.srcNetworkNo-7",
        "LongHeaderDstNodeId": "ddp.header.header.longHeader.dstNodeId-8",
        "LongHeaderSrcNodeId": "ddp.header.header.longHeader.srcNodeId-9",
        "LongHeaderDstSocketNo": "ddp.header.header.longHeader.dstSocketNo-10",
        "LongHeaderSrcSocketNo": "ddp.header.header.longHeader.srcSocketNo-11",
        "LongHeaderProtocolType": "ddp.header.header.longHeader.protocolType-12",
        "ShortHeaderUnused": "ddp.header.header.shortHeader.unused-13",
        "ShortHeaderLength": "ddp.header.header.shortHeader.length-14",
        "ShortHeaderDstSocketNo": "ddp.header.header.shortHeader.dstSocketNo-15",
        "ShortHeaderSrcSocketNo": "ddp.header.header.shortHeader.srcSocketNo-16",
        "ShortHeaderProtocolType": "ddp.header.header.shortHeader.protocolType-17",
    }

    def __init__(self, parent, list_op=False):
        super(Ddp, self).__init__(parent, list_op)

    @property
    def LongHeaderUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderUnused"])
        )

    @property
    def LongHeaderHopCount(self):
        """
        Display Name: Hop count
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderHopCount"])
        )

    @property
    def LongHeaderLength(self):
        """
        Display Name: Datagram length
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderLength"])
        )

    @property
    def ChecksumNoChecksum(self):
        """
        Display Name: No checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChecksumNoChecksum"])
        )

    @property
    def ChecksumDdpChecksum(self):
        """
        Display Name: DDP checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChecksumDdpChecksum"])
        )

    @property
    def LongHeaderDstNetworkNo(self):
        """
        Display Name: Destination network no
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderDstNetworkNo"])
        )

    @property
    def LongHeaderSrcNetworkNo(self):
        """
        Display Name: Source network no
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderSrcNetworkNo"])
        )

    @property
    def LongHeaderDstNodeId(self):
        """
        Display Name: Destination node id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderDstNodeId"])
        )

    @property
    def LongHeaderSrcNodeId(self):
        """
        Display Name: Source node id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderSrcNodeId"])
        )

    @property
    def LongHeaderDstSocketNo(self):
        """
        Display Name: Destination socket no
        Default Value: 1
        Value Format: decimal
        Available enum values: RTMP socket, 1, NIS socket, 2, Echoer socket, 4, ZIS socket, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderDstSocketNo"])
        )

    @property
    def LongHeaderSrcSocketNo(self):
        """
        Display Name: Source socket no
        Default Value: 1
        Value Format: decimal
        Available enum values: RTMP socket, 1, NIS socket, 2, Echoer socket, 4, ZIS socket, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderSrcSocketNo"])
        )

    @property
    def LongHeaderProtocolType(self):
        """
        Display Name: DDP protocol type
        Default Value: 1
        Value Format: decimal
        Available enum values: RTMP response or data packet, 1, NBP packet, 2, ATP packet, 3, AEP packet, 4, RTMP request packet, 5, ZIP packet, 6, ADSP packet, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LongHeaderProtocolType"])
        )

    @property
    def ShortHeaderUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShortHeaderUnused"])
        )

    @property
    def ShortHeaderLength(self):
        """
        Display Name: Datagram length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShortHeaderLength"])
        )

    @property
    def ShortHeaderDstSocketNo(self):
        """
        Display Name: Destination socket no
        Default Value: 1
        Value Format: decimal
        Available enum values: RTMP socket, 1, NIS socket, 2, Echoer socket, 4, ZIS socket, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShortHeaderDstSocketNo"])
        )

    @property
    def ShortHeaderSrcSocketNo(self):
        """
        Display Name: Source socket no
        Default Value: 1
        Value Format: decimal
        Available enum values: RTMP socket, 1, NIS socket, 2, Echoer socket, 4, ZIS socket, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShortHeaderSrcSocketNo"])
        )

    @property
    def ShortHeaderProtocolType(self):
        """
        Display Name: DDP protocol type
        Default Value: 1
        Value Format: decimal
        Available enum values: RTMP response or data packet, 1, NBP packet, 2, ATP packet, 3, AEP packet, 4, RTMP request packet, 5, ZIP packet, 6, ADSP packet, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShortHeaderProtocolType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
