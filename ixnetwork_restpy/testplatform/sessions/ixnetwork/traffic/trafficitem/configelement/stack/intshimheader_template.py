from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Intshimheader(Base):
    __slots__ = ()
    _SDM_NAME = "intshimheader"
    _SDM_ATT_MAP = {
        "ShimheaderType": "intshimheader.shimheader.type-1",
        "ShimheaderReserved8": "intshimheader.shimheader.reserved8-2",
        "ShimheaderLength": "intshimheader.shimheader.length-3",
        "ShimheaderDscp": "intshimheader.shimheader.dscp-4",
        "ShimheaderReserved2": "intshimheader.shimheader.reserved2-5",
    }

    def __init__(self, parent, list_op=False):
        super(Intshimheader, self).__init__(parent, list_op)

    @property
    def ShimheaderType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Hop-by-Hop, 1, Destination, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimheaderType"])
        )

    @property
    def ShimheaderReserved8(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimheaderReserved8"])
        )

    @property
    def ShimheaderLength(self):
        """
        Display Name: Length (x4 bytes)
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimheaderLength"])
        )

    @property
    def ShimheaderDscp(self):
        """
        Display Name: DSCP
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimheaderDscp"])
        )

    @property
    def ShimheaderReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimheaderReserved2"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
