from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6Pseudo(Base):
    __slots__ = ()
    _SDM_NAME = "ipv6Pseudo"
    _SDM_ATT_MAP = {
        "HeaderSrcAddress": "ipv6Pseudo.header.srcAddress-1",
        "HeaderDstAddress": "ipv6Pseudo.header.dstAddress-2",
        "HeaderUpperLayerPacketLength": "ipv6Pseudo.header.upperLayerPacketLength-3",
        "HeaderZero": "ipv6Pseudo.header.zero-4",
        "HeaderNextHeader": "ipv6Pseudo.header.nextHeader-5",
    }

    def __init__(self, parent, list_op=False):
        super(Ipv6Pseudo, self).__init__(parent, list_op)

    @property
    def HeaderSrcAddress(self):
        """
        Display Name: Source Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcAddress"])
        )

    @property
    def HeaderDstAddress(self):
        """
        Display Name: Destination Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDstAddress"])
        )

    @property
    def HeaderUpperLayerPacketLength(self):
        """
        Display Name: Upper-Layer Packet Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderUpperLayerPacketLength"])
        )

    @property
    def HeaderZero(self):
        """
        Display Name: Zero
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderZero"]))

    @property
    def HeaderNextHeader(self):
        """
        Display Name: Next Header
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNextHeader"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
