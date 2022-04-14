from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Vntag(Base):
    __slots__ = ()
    _SDM_NAME = "vntag"
    _SDM_ATT_MAP = {
        "VntagDirection": "vntag.header.vntagHeader.vntagDirection-1",
        "VntagPointer": "vntag.header.vntagHeader.vntagPointer-2",
        "VntagDstVif": "vntag.header.vntagHeader.vntagDstVif-3",
        "VntagLooped": "vntag.header.vntagHeader.vntagLooped-4",
        "Default": "vntag.header.vntagHeader.-5",
        "VntagVersion": "vntag.header.vntagHeader.vntagVersion-6",
        "VntagSrcVif": "vntag.header.vntagHeader.vntagSrcVif-7",
        "ProtocolID": "vntag.header.protocolID-8",
    }

    def __init__(self, parent, list_op=False):
        super(Vntag, self).__init__(parent, list_op)

    @property
    def VntagDirection(self):
        """
        Display Name: Direction
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VntagDirection"])
        )

    @property
    def VntagPointer(self):
        """
        Display Name: Pointer
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VntagPointer"]))

    @property
    def VntagDstVif(self):
        """
        Display Name: Destination VIF
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VntagDstVif"]))

    @property
    def VntagLooped(self):
        """
        Display Name: Looped
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VntagLooped"]))

    @property
    def Default(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Default"]))

    @property
    def VntagVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VntagVersion"]))

    @property
    def VntagSrcVif(self):
        """
        Display Name: Source VIF
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VntagSrcVif"]))

    @property
    def ProtocolID(self):
        """
        Display Name: Protocol-ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProtocolID"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
