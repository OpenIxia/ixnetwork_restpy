from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Gtpu(Base):
    __slots__ = ()
    _SDM_NAME = "gtpu"
    _SDM_ATT_MAP = {
        "Version": "gtpu.header.version-1",
        "Pt": "gtpu.header.pt-2",
        "Reserved": "gtpu.header.reserved-3",
        "E": "gtpu.header.e-4",
        "S": "gtpu.header.s-5",
        "N": "gtpu.header.n-6",
        "Type": "gtpu.header.type-7",
        "TotalLength": "gtpu.header.totalLength-8",
        "Teid": "gtpu.header.teid-9",
    }

    def __init__(self, parent, list_op=False):
        super(Gtpu, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        Available enum values: GTPv1, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Pt(self):
        """
        Display Name: PT
        Default Value: 1
        Value Format: decimal
        Available enum values: GTP', 0, GTP, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Pt"]))

    @property
    def Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved"]))

    @property
    def E(self):
        """
        Display Name: E
        Default Value: 0
        Value Format: decimal
        Available enum values: Extension Header Not Present, 0, Extension Header Present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["E"]))

    @property
    def S(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: decimal
        Available enum values: Sequence Number Not Present, 0, Sequence Number Present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["S"]))

    @property
    def N(self):
        """
        Display Name: N
        Default Value: 0
        Value Format: decimal
        Available enum values: N-PDU Field Not Present, 0, N-PDU Field Present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["N"]))

    @property
    def Type(self):
        """
        Display Name: Type
        Default Value: 255
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def TotalLength(self):
        """
        Display Name: Total Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TotalLength"]))

    @property
    def Teid(self):
        """
        Display Name: TEID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Teid"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
