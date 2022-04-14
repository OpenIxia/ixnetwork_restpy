from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MrpFourPackedEvent(Base):
    __slots__ = ()
    _SDM_NAME = "mrpFourPackedEvent"
    _SDM_ATT_MAP = {
        "HeaderFourPackedAttributeEvent": "mrpFourPackedEvent.header.fourPackedAttributeEvent-1",
    }

    def __init__(self, parent, list_op=False):
        super(MrpFourPackedEvent, self).__init__(parent, list_op)

    @property
    def HeaderFourPackedAttributeEvent(self):
        """
        Display Name: Four Packed Attribute Event
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderFourPackedAttributeEvent"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
