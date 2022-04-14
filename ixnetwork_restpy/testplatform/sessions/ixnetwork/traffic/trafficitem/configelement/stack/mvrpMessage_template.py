from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MvrpMessage(Base):
    __slots__ = ()
    _SDM_NAME = "mvrpMessage"
    _SDM_ATT_MAP = {
        "MvrpHeaderProtoVersion": "mvrpMessage.header.mvrpHeader.protoVersion-1",
        "MvrpVidVectorAttributeType": "mvrpMessage.header.attributeType.mvrpVidVector.attributeType-2",
        "MvrpVidVectorAttributeLength": "mvrpMessage.header.attributeType.mvrpVidVector.attributeLength-3",
    }

    def __init__(self, parent, list_op=False):
        super(MvrpMessage, self).__init__(parent, list_op)

    @property
    def MvrpHeaderProtoVersion(self):
        """
        Display Name: Protocol Version
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MvrpHeaderProtoVersion"])
        )

    @property
    def MvrpVidVectorAttributeType(self):
        """
        Display Name: Attribute Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MvrpVidVectorAttributeType"])
        )

    @property
    def MvrpVidVectorAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MvrpVidVectorAttributeLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
