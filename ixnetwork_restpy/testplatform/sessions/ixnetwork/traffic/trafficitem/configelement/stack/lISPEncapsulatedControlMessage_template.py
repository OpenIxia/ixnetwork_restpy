from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISPEncapsulatedControlMessage(Base):
    __slots__ = ()
    _SDM_NAME = "lISPEncapsulatedControlMessage"
    _SDM_ATT_MAP = {
        "HeaderType": "lISPEncapsulatedControlMessage.header.type-1",
        "HeaderReserved": "lISPEncapsulatedControlMessage.header.reserved-2",
    }

    def __init__(self, parent, list_op=False):
        super(LISPEncapsulatedControlMessage, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
