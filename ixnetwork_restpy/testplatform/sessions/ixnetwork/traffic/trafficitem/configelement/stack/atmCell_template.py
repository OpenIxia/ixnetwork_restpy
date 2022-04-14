from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AtmCell(Base):
    __slots__ = ()
    _SDM_NAME = "atmCell"
    _SDM_ATT_MAP = {
        "AtmCellVpi": "atmCell.atmCell.vpi-1",
        "AtmCellVci": "atmCell.atmCell.vci-2",
        "AtmCellPti": "atmCell.atmCell.pti-3",
        "AtmCellCellRelayCbit": "atmCell.atmCell.cellRelayCbit-4",
        "AtmCellCellData": "atmCell.atmCell.cellData-5",
    }

    def __init__(self, parent, list_op=False):
        super(AtmCell, self).__init__(parent, list_op)

    @property
    def AtmCellVpi(self):
        """
        Display Name: VPI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AtmCellVpi"]))

    @property
    def AtmCellVci(self):
        """
        Display Name: VCI
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AtmCellVci"]))

    @property
    def AtmCellPti(self):
        """
        Display Name: PTI
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AtmCellPti"]))

    @property
    def AtmCellCellRelayCbit(self):
        """
        Display Name: Cell Relay Cbit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmCellCellRelayCbit"])
        )

    @property
    def AtmCellCellData(self):
        """
        Display Name: Cell Data
        Default Value: 0xAAAA030000000800450000200000000040FF5BDC0A00000214000002DDDDDDDDDDDDDDDDDDDDDDDD00000028BF1E07A2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AtmCellCellData"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
