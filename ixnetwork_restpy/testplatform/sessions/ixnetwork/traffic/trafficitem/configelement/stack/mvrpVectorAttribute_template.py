from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MvrpVectorAttribute(Base):
    __slots__ = ()
    _SDM_NAME = "mvrpVectorAttribute"
    _SDM_ATT_MAP = {
        "VectorHeaderLeaveAllEvent": "mvrpVectorAttribute.header.vectorHeader.leaveAllEvent-1",
        "VectorHeaderNoOfValues": "mvrpVectorAttribute.header.vectorHeader.noOfValues-2",
        "MvrpVidVectorFirstValueFirstValue": "mvrpVectorAttribute.header.selectFirstValueType.mvrpVidVectorFirstValue.firstValue-3",
    }

    def __init__(self, parent, list_op=False):
        super(MvrpVectorAttribute, self).__init__(parent, list_op)

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
    def MvrpVidVectorFirstValueFirstValue(self):
        """
        Display Name: First Value
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MvrpVidVectorFirstValueFirstValue"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
