from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ppp(Base):
    __slots__ = ()
    _SDM_NAME = "ppp"
    _SDM_ATT_MAP = {
        "Address": "ppp.header.address-1",
        "Control": "ppp.header.control-2",
        "ProtocolType": "ppp.header.protocolType-3",
    }

    def __init__(self, parent, list_op=False):
        super(Ppp, self).__init__(parent, list_op)

    @property
    def Address(self):
        """
        Display Name: PPP Address
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Address"]))

    @property
    def Control(self):
        """
        Display Name: PPP Control
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Control"]))

    @property
    def ProtocolType(self):
        """
        Display Name: PPP Protocol Type
        Default Value: 0x0021
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProtocolType"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
