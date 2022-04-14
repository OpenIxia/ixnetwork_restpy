from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPNPPP(Base):
    __slots__ = ()
    _SDM_NAME = "l2VPNPPP"
    _SDM_ATT_MAP = {
        "PppHeaderAddress": "l2VPNPPP.pppHeader.address-1",
        "PppHeaderControl": "l2VPNPPP.pppHeader.control-2",
        "PppHeaderProtocolType": "l2VPNPPP.pppHeader.protocolType-3",
    }

    def __init__(self, parent, list_op=False):
        super(L2VPNPPP, self).__init__(parent, list_op)

    @property
    def PppHeaderAddress(self):
        """
        Display Name: Address
        Default Value: 0xFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PppHeaderAddress"])
        )

    @property
    def PppHeaderControl(self):
        """
        Display Name: Control
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PppHeaderControl"])
        )

    @property
    def PppHeaderProtocolType(self):
        """
        Display Name: Protocol Type
        Default Value: 0x0021
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PppHeaderProtocolType"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
