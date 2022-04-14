from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriMsgType5(Base):
    __slots__ = ()
    _SDM_NAME = "eCpriMsgType5"
    _SDM_ATT_MAP = {
        "HeaderMid": "eCpriMsgType5.header.mid-1",
        "HeaderAtype": "eCpriMsgType5.header.atype-2",
        "HeaderTimestamp": "eCpriMsgType5.header.timestamp-3",
        "HeaderCompvalue": "eCpriMsgType5.header.compvalue-4",
        "HeaderLength": "eCpriMsgType5.header.header.length-5",
        "HeaderData": "eCpriMsgType5.header.header.data-6",
    }

    def __init__(self, parent, list_op=False):
        super(ECpriMsgType5, self).__init__(parent, list_op)

    @property
    def HeaderMid(self):
        """
        Display Name: mid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderMid"]))

    @property
    def HeaderAtype(self):
        """
        Display Name: atype
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderAtype"]))

    @property
    def HeaderTimestamp(self):
        """
        Display Name: timestamp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTimestamp"])
        )

    @property
    def HeaderCompvalue(self):
        """
        Display Name: compvalue
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCompvalue"])
        )

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
