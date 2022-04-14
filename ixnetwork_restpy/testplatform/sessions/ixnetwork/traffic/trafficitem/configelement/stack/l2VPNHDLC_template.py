from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPNHDLC(Base):
    __slots__ = ()
    _SDM_NAME = "l2VPNHDLC"
    _SDM_ATT_MAP = {
        "HdlcHeaderAddress": "l2VPNHDLC.hdlcHeader.address-1",
        "HdlcHeaderControl": "l2VPNHDLC.hdlcHeader.control-2",
        "HdlcHeaderProtocolType": "l2VPNHDLC.hdlcHeader.protocolType-3",
    }

    def __init__(self, parent, list_op=False):
        super(L2VPNHDLC, self).__init__(parent, list_op)

    @property
    def HdlcHeaderAddress(self):
        """
        Display Name: Address
        Default Value: 0x0F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HdlcHeaderAddress"])
        )

    @property
    def HdlcHeaderControl(self):
        """
        Display Name: Control
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HdlcHeaderControl"])
        )

    @property
    def HdlcHeaderProtocolType(self):
        """
        Display Name: Protocol Type
        Default Value: 0x0021
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HdlcHeaderProtocolType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
