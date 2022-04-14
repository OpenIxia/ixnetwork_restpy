from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriFaultNotify(Base):
    __slots__ = ()
    _SDM_NAME = "eCpriFaultNotify"
    _SDM_ATT_MAP = {
        "HeaderElementId": "eCpriFaultNotify.header.elementId-1",
        "HeaderRaiseCease": "eCpriFaultNotify.header.raiseCease-2",
        "HeaderFaultNotifNum": "eCpriFaultNotify.header.faultNotifNum-3",
        "HeaderAddInfo": "eCpriFaultNotify.header.addInfo-4",
    }

    def __init__(self, parent, list_op=False):
        super(ECpriFaultNotify, self).__init__(parent, list_op)

    @property
    def HeaderElementId(self):
        """
        Display Name: elementId
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderElementId"])
        )

    @property
    def HeaderRaiseCease(self):
        """
        Display Name: raiseCease
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRaiseCease"])
        )

    @property
    def HeaderFaultNotifNum(self):
        """
        Display Name: faultNotifNum
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFaultNotifNum"])
        )

    @property
    def HeaderAddInfo(self):
        """
        Display Name: addInfo
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderAddInfo"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
