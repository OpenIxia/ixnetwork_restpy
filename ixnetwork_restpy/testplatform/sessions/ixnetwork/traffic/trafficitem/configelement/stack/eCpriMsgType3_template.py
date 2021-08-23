from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriMsgType3(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType3'
    _SDM_ATT_MAP = {
        'HeaderPcid': 'eCpriMsgType3.header.pcid-1',
        'HeaderSeqid': 'eCpriMsgType3.header.seqid-2',
        'HeaderLength': 'eCpriMsgType3.header.header.length-3',
        'HeaderData': 'eCpriMsgType3.header.header.data-4',
    }

    def __init__(self, parent, list_op=False):
        super(ECpriMsgType3, self).__init__(parent, list_op)

    @property
    def HeaderPcid(self):
        """
        Display Name: pcid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderPcid']))

    @property
    def HeaderSeqid(self):
        """
        Display Name: seqid
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderSeqid']))

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderLength']))

    @property
    def HeaderData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderData']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
