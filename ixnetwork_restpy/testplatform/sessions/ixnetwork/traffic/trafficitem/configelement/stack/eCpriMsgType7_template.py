from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriMsgType7(Base):
    __slots__ = ()
    _SDM_NAME = "eCpriMsgType7"
    _SDM_ATT_MAP = {
        "HeaderEventid": "eCpriMsgType7.header.eventid-1",
        "HeaderEventtype": "eCpriMsgType7.header.eventtype-2",
        "HeaderSeqnum": "eCpriMsgType7.header.seqnum-3",
        "HeaderFaults": "eCpriMsgType7.header.faults-4",
    }

    def __init__(self, parent, list_op=False):
        super(ECpriMsgType7, self).__init__(parent, list_op)

    @property
    def HeaderEventid(self):
        """
        Display Name: eventid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderEventid"]))

    @property
    def HeaderEventtype(self):
        """
        Display Name: eventtype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderEventtype"])
        )

    @property
    def HeaderSeqnum(self):
        """
        Display Name: seqnum
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSeqnum"]))

    @property
    def HeaderFaults(self):
        """
        Display Name: faults
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFaults"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
