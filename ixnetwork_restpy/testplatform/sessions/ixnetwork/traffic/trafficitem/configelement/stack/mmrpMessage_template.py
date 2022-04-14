from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MmrpMessage(Base):
    __slots__ = ()
    _SDM_NAME = "mmrpMessage"
    _SDM_ATT_MAP = {
        "MmrpHeaderProtoVersion": "mmrpMessage.header.mmrpHeader.protoVersion-1",
        "MmrpServiceReqVectorAttributeType": "mmrpMessage.header.attributeType.mmrpServiceReqVector.attributeType-2",
        "MmrpServiceReqVectorAttributeLength": "mmrpMessage.header.attributeType.mmrpServiceReqVector.attributeLength-3",
        "MmrpMacVectorAttributeType": "mmrpMessage.header.attributeType.mmrpMacVector.attributeType-4",
        "MmrpMacVectorAttributeLength": "mmrpMessage.header.attributeType.mmrpMacVector.attributeLength-5",
    }

    def __init__(self, parent, list_op=False):
        super(MmrpMessage, self).__init__(parent, list_op)

    @property
    def MmrpHeaderProtoVersion(self):
        """
        Display Name: Protocol Version
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MmrpHeaderProtoVersion"])
        )

    @property
    def MmrpServiceReqVectorAttributeType(self):
        """
        Display Name: Attribute Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MmrpServiceReqVectorAttributeType"]),
        )

    @property
    def MmrpServiceReqVectorAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MmrpServiceReqVectorAttributeLength"]
            ),
        )

    @property
    def MmrpMacVectorAttributeType(self):
        """
        Display Name: Attribute Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MmrpMacVectorAttributeType"])
        )

    @property
    def MmrpMacVectorAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x06
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MmrpMacVectorAttributeLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
