from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6Encapsulation(Base):
    __slots__ = ()
    _SDM_NAME = "ipv6Encapsulation"
    _SDM_ATT_MAP = {
        "HeaderSpi": "ipv6Encapsulation.header.spi-1",
        "HeaderSequenceNumber": "ipv6Encapsulation.header.sequenceNumber-2",
    }

    def __init__(self, parent, list_op=False):
        super(Ipv6Encapsulation, self).__init__(parent, list_op)

    @property
    def HeaderSpi(self):
        """
        Display Name: Security Paramaters Index
        Default Value: 0x1ff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSpi"]))

    @property
    def HeaderSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSequenceNumber"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
