from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IntShimHeaderVxlangpe(Base):
    __slots__ = ()
    _SDM_NAME = "intShimHeaderVxlangpe"
    _SDM_ATT_MAP = {
        "ShimHeaderType": "intShimHeaderVxlangpe.shimHeader.type-1",
        "ShimHeaderReserved": "intShimHeaderVxlangpe.shimHeader.reserved-2",
        "ShimHeaderLength": "intShimHeaderVxlangpe.shimHeader.length-3",
        "ShimHeaderGFlag": "intShimHeaderVxlangpe.shimHeader.gFlag-4",
        "ShimHeaderReserved7": "intShimHeaderVxlangpe.shimHeader.reserved7-5",
        "ShimHeaderNextProtocol": "intShimHeaderVxlangpe.shimHeader.nextProtocol-6",
    }

    def __init__(self, parent, list_op=False):
        super(IntShimHeaderVxlangpe, self).__init__(parent, list_op)

    @property
    def ShimHeaderType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        Available enum values: INT-MD, 1, INT-Destination, 2, INT-MX, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimHeaderType"])
        )

    @property
    def ShimHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimHeaderReserved"])
        )

    @property
    def ShimHeaderLength(self):
        """
        Display Name: Length (x4 bytes)
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimHeaderLength"])
        )

    @property
    def ShimHeaderGFlag(self):
        """
        Display Name: G Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Original packet used VXLAN GPE encapsulation, 0, Original packet used VXLAN encapsulation, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimHeaderGFlag"])
        )

    @property
    def ShimHeaderReserved7(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimHeaderReserved7"])
        )

    @property
    def ShimHeaderNextProtocol(self):
        """
        Display Name: Next Protocol
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ShimHeaderNextProtocol"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
