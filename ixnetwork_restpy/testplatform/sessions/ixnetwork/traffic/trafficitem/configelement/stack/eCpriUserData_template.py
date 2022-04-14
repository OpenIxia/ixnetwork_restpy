from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriUserData(Base):
    __slots__ = ()
    _SDM_NAME = "eCpriUserData"
    _SDM_ATT_MAP = {
        "HeaderLength": "eCpriUserData.header.length-1",
        "HeaderData": "eCpriUserData.header.data-2",
    }

    def __init__(self, parent, list_op=False):
        super(ECpriUserData, self).__init__(parent, list_op)

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
