from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTag(Base):
    __slots__ = ()
    _SDM_NAME = "rTag"
    _SDM_ATT_MAP = {
        "RTagRTagReserved": "rTag.rTag.RTagReserved-1",
        "RTagRTagSeqNum": "rTag.rTag.RTagSeqNum-2",
        "RTagRtagEtherType": "rTag.rTag.rtagEtherType-3",
    }

    def __init__(self, parent, list_op=False):
        super(RTag, self).__init__(parent, list_op)

    @property
    def RTagRTagReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RTagRTagReserved"])
        )

    @property
    def RTagRTagSeqNum(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RTagRTagSeqNum"])
        )

    @property
    def RTagRtagEtherType(self):
        """
        Display Name: Ethernet-Type
        Default Value: 0xffff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RTagRtagEtherType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
