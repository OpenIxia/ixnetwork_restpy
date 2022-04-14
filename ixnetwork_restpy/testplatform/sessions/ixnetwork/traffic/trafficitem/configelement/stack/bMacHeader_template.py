from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BMacHeader(Base):
    __slots__ = ()
    _SDM_NAME = "bMacHeader"
    _SDM_ATT_MAP = {
        "HeaderBDstAddress": "bMacHeader.header.bDstAddress-1",
        "HeaderBSrcAddress": "bMacHeader.header.bSrcAddress-2",
    }

    def __init__(self, parent, list_op=False):
        super(BMacHeader, self).__init__(parent, list_op)

    @property
    def HeaderBDstAddress(self):
        """
        Display Name: B-Destination Address (Ethernet)
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBDstAddress"])
        )

    @property
    def HeaderBSrcAddress(self):
        """
        Display Name: B-Source Address (Ethernet)
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBSrcAddress"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
