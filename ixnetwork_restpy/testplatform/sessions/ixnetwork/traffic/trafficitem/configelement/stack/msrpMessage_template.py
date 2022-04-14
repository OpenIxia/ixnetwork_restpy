from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MsrpMessage(Base):
    __slots__ = ()
    _SDM_NAME = "msrpMessage"
    _SDM_ATT_MAP = {
        "MsrpHeaderProtoVersion": "msrpMessage.header.msrpHeader.protoVersion-1",
        "MsrpTalkerAdvertiseAttributeLength": "msrpMessage.header.attributeType.msrpTalkerAdvertise.attributeLength-2",
        "MsrpTalkerAdvertiseAttributeLength": "msrpMessage.header.attributeType.msrpTalkerAdvertise.attributeLength-3",
        "MsrpTalkerFailedAttributeLength": "msrpMessage.header.attributeType.msrpTalkerFailed.attributeLength-4",
        "MsrpTalkerFailedAttributeLength": "msrpMessage.header.attributeType.msrpTalkerFailed.attributeLength-5",
        "MsrpListenerAttributeLength": "msrpMessage.header.attributeType.msrpListener.attributeLength-6",
        "MsrpListenerAttributeLength": "msrpMessage.header.attributeType.msrpListener.attributeLength-7",
        "MsrpDomainAttributeLength": "msrpMessage.header.attributeType.msrpDomain.attributeLength-8",
        "MsrpDomainAttributeLength": "msrpMessage.header.attributeType.msrpDomain.attributeLength-9",
        "MsrpCustomAttributeAttributeLength": "msrpMessage.header.attributeType.msrpCustomAttribute.attributeLength-10",
        "MsrpCustomAttributeAttributeLength": "msrpMessage.header.attributeType.msrpCustomAttribute.attributeLength-11",
        "HeaderAttributeListLength": "msrpMessage.header.attributeListLength-12",
    }

    def __init__(self, parent, list_op=False):
        super(MsrpMessage, self).__init__(parent, list_op)

    @property
    def MsrpHeaderProtoVersion(self):
        """
        Display Name: Protocol Version
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MsrpHeaderProtoVersion"])
        )

    @property
    def MsrpTalkerAdvertiseAttributeLength(self):
        """
        Display Name: Attribute Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrpTalkerAdvertiseAttributeLength"]
            ),
        )

    @property
    def MsrpTalkerAdvertiseAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x19
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrpTalkerAdvertiseAttributeLength"]
            ),
        )

    @property
    def MsrpTalkerFailedAttributeLength(self):
        """
        Display Name: Attribute Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MsrpTalkerFailedAttributeLength"]),
        )

    @property
    def MsrpTalkerFailedAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x22
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MsrpTalkerFailedAttributeLength"]),
        )

    @property
    def MsrpListenerAttributeLength(self):
        """
        Display Name: Attribute Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MsrpListenerAttributeLength"])
        )

    @property
    def MsrpListenerAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MsrpListenerAttributeLength"])
        )

    @property
    def MsrpDomainAttributeLength(self):
        """
        Display Name: Attribute Type
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MsrpDomainAttributeLength"])
        )

    @property
    def MsrpDomainAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x4
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MsrpDomainAttributeLength"])
        )

    @property
    def MsrpCustomAttributeAttributeLength(self):
        """
        Display Name: Attribute Type
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrpCustomAttributeAttributeLength"]
            ),
        )

    @property
    def MsrpCustomAttributeAttributeLength(self):
        """
        Display Name: Attribute Length
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrpCustomAttributeAttributeLength"]
            ),
        )

    @property
    def HeaderAttributeListLength(self):
        """
        Display Name: Attribute List Length
        Default Value: 0x1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAttributeListLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
