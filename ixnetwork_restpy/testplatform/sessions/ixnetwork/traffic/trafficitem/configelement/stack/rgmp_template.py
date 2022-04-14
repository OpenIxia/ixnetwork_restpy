from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Rgmp(Base):
    __slots__ = ()
    _SDM_NAME = "rgmp"
    _SDM_ATT_MAP = {
        "HeaderType": "rgmp.header.type-1",
        "HeaderReserved": "rgmp.header.reserved-2",
        "HeaderChecksum": "rgmp.header.checksum-3",
        "HeaderMulticastAddress": "rgmp.header.multicastAddress-4",
    }

    def __init__(self, parent, list_op=False):
        super(Rgmp, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 252
        Value Format: decimal
        Available enum values: Leave a Group, 252, Join a Group, 253, Bye, 254, Hello, 255
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
    def HeaderMulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: 224.0.0.25
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMulticastAddress"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
