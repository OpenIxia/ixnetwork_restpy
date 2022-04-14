from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriMsgType6(Base):
    __slots__ = ()
    _SDM_NAME = "eCpriMsgType6"
    _SDM_ATT_MAP = {
        "HeaderResetid": "eCpriMsgType6.header.resetid-1",
        "HeaderResetop": "eCpriMsgType6.header.resetop-2",
        "HeaderLength": "eCpriMsgType6.header.header.length-3",
        "HeaderData": "eCpriMsgType6.header.header.data-4",
    }

    def __init__(self, parent, list_op=False):
        super(ECpriMsgType6, self).__init__(parent, list_op)

    @property
    def HeaderResetid(self):
        """
        Display Name: resetid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderResetid"]))

    @property
    def HeaderResetop(self):
        """
        Display Name: resetop
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderResetop"]))

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderData"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
