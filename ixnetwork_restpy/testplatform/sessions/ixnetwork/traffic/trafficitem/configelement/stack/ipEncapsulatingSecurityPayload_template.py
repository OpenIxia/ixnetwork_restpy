from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IpEncapsulatingSecurityPayload(Base):
    __slots__ = ()
    _SDM_NAME = "ipEncapsulatingSecurityPayload"
    _SDM_ATT_MAP = {
        "HeaderSpi": "ipEncapsulatingSecurityPayload.header.spi-1",
        "HeaderSn": "ipEncapsulatingSecurityPayload.header.sn-2",
    }

    def __init__(self, parent, list_op=False):
        super(IpEncapsulatingSecurityPayload, self).__init__(parent, list_op)

    @property
    def HeaderSpi(self):
        """
        Display Name: Security Paramaters Index
        Default Value: 0x1ff
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSpi"]))

    @property
    def HeaderSn(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSn"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
