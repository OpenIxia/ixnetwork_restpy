from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LlcBridgedEthernet(Base):
    __slots__ = ()
    _SDM_NAME = "llcBridgedEthernet"
    _SDM_ATT_MAP = {
        "HeaderLlcHeader": "llcBridgedEthernet.header.llcHeader-1",
        "HeaderOui": "llcBridgedEthernet.header.oui-2",
        "HeaderPid": "llcBridgedEthernet.header.pid-3",
        "HeaderPad": "llcBridgedEthernet.header.pad-4",
    }

    def __init__(self, parent, list_op=False):
        super(LlcBridgedEthernet, self).__init__(parent, list_op)

    @property
    def HeaderLlcHeader(self):
        """
        Display Name: Logical Link Control(LLC) Header
        Default Value: 0xaaaa03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLlcHeader"])
        )

    @property
    def HeaderOui(self):
        """
        Display Name: Organizationally Unique Identifier (OUI)
        Default Value: 0x0080c2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderOui"]))

    @property
    def HeaderPid(self):
        """
        Display Name: PID
        Default Value: 0001
        Value Format: decimal
        Available enum values: With FCS, 1, Without FCS, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderPid"]))

    @property
    def HeaderPad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderPad"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
