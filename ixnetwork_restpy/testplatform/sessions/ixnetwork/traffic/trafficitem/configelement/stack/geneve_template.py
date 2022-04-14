from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Geneve(Base):
    __slots__ = ()
    _SDM_NAME = "geneve"
    _SDM_ATT_MAP = {
        "Version": "geneve.header.version-1",
        "Optionslen": "geneve.header.optionslen-2",
        "Flags": "geneve.header.flags-3",
        "Protocol": "geneve.header.protocol-4",
        "Vni": "geneve.header.vni-5",
        "Reserved8": "geneve.header.reserved8-6",
        "Length": "geneve.header.length-7",
        "Options": "geneve.header.options-8",
    }

    def __init__(self, parent, list_op=False):
        super(Geneve, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Optionslen(self):
        """
        Display Name: Options Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Optionslen"]))

    @property
    def Flags(self):
        """
        Display Name: Flags
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Flags"]))

    @property
    def Protocol(self):
        """
        Display Name: Protocol Type
        Default Value: 0x6558
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Protocol"]))

    @property
    def Vni(self):
        """
        Display Name: VNI
        Default Value: 1000
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Vni"]))

    @property
    def Reserved8(self):
        """
        Display Name: Reserved8
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved8"]))

    @property
    def Length(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Length"]))

    @property
    def Options(self):
        """
        Display Name: Tunnel Options
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Options"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
