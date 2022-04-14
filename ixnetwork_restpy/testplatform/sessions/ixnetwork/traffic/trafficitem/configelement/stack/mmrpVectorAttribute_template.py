from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MmrpVectorAttribute(Base):
    __slots__ = ()
    _SDM_NAME = "mmrpVectorAttribute"
    _SDM_ATT_MAP = {
        "VectorHeaderLeaveAllEvent": "mmrpVectorAttribute.header.vectorHeader.leaveAllEvent-1",
        "VectorHeaderNoOfValues": "mmrpVectorAttribute.header.vectorHeader.noOfValues-2",
        "MmrpServiceRequiremenVectorFirstValueFirstValue": "mmrpVectorAttribute.header.selectFirstValueType.mmrpServiceRequiremenVectorFirstValue.firstValue-3",
        "MmrpMacVectorFirstValueFirstValue": "mmrpVectorAttribute.header.selectFirstValueType.mmrpMacVectorFirstValue.firstValue-4",
    }

    def __init__(self, parent, list_op=False):
        super(MmrpVectorAttribute, self).__init__(parent, list_op)

    @property
    def VectorHeaderLeaveAllEvent(self):
        """
        Display Name: Leave All Event
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VectorHeaderLeaveAllEvent"])
        )

    @property
    def VectorHeaderNoOfValues(self):
        """
        Display Name: No Of Values
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VectorHeaderNoOfValues"])
        )

    @property
    def MmrpServiceRequiremenVectorFirstValueFirstValue(self):
        """
        Display Name: First Value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MmrpServiceRequiremenVectorFirstValueFirstValue"]
            ),
        )

    @property
    def MmrpMacVectorFirstValueFirstValue(self):
        """
        Display Name: First Value
        Default Value: 0x91E0F000FE00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MmrpMacVectorFirstValueFirstValue"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
