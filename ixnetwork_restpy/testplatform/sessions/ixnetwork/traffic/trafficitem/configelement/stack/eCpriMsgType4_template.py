from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriMsgType4(Base):
    __slots__ = ()
    _SDM_NAME = "eCpriMsgType4"
    _SDM_ATT_MAP = {
        "HeaderRmaid": "eCpriMsgType4.header.rmaid-1",
        "HeaderRdwr": "eCpriMsgType4.header.rdwr-2",
        "HeaderReqresp": "eCpriMsgType4.header.reqresp-3",
        "HeaderElemid": "eCpriMsgType4.header.elemid-4",
        "HeaderAddress": "eCpriMsgType4.header.address-5",
        "HeaderDefault": "eCpriMsgType4.header.-6",
    }

    def __init__(self, parent, list_op=False):
        super(ECpriMsgType4, self).__init__(parent, list_op)

    @property
    def HeaderRmaid(self):
        """
        Display Name: rmaid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderRmaid"]))

    @property
    def HeaderRdwr(self):
        """
        Display Name: rdwr
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderRdwr"]))

    @property
    def HeaderReqresp(self):
        """
        Display Name: reqresp
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderReqresp"]))

    @property
    def HeaderElemid(self):
        """
        Display Name: elemid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderElemid"]))

    @property
    def HeaderAddress(self):
        """
        Display Name: address
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderAddress"]))

    @property
    def HeaderDefault(self):
        """
        Display Name: memorylength
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDefault"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
