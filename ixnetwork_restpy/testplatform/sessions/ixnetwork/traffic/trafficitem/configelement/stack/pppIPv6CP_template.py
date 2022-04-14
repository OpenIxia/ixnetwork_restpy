from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PppIPv6CP(Base):
    __slots__ = ()
    _SDM_NAME = "pppIPv6CP"
    _SDM_ATT_MAP = {
        "HeaderCode": "pppIPv6CP.header.code-1",
        "HeaderIdentifier": "pppIPv6CP.header.identifier-2",
        "HeaderLength": "pppIPv6CP.header.length-3",
        "OptionsType": "pppIPv6CP.header.data.options.type-4",
        "FieldsForInterfaceIdentifierLength": "pppIPv6CP.header.data.options.nextFields.fieldsForInterfaceIdentifier.length-5",
        "FieldsForInterfaceIdentifierIdentifier": "pppIPv6CP.header.data.options.nextFields.fieldsForInterfaceIdentifier.identifier-6",
        "FieldsForIPv6CompressionLength": "pppIPv6CP.header.data.options.nextFields.fieldsForIPv6Compression.length-7",
        "FieldsForIPv6CompressionCompressionProtocol": "pppIPv6CP.header.data.options.nextFields.fieldsForIPv6Compression.compressionProtocol-8",
        "NextfieldsFieldsForIPv6CompressionLength": "pppIPv6CP.header.data.options.nextFields.fieldsForIPv6Compression.length-9",
        "FieldsForIPv6CompressionData": "pppIPv6CP.header.data.options.nextFields.fieldsForIPv6Compression.data-10",
        "DataInLCPLength": "pppIPv6CP.header.data.dataInLCP.length-11",
        "DataInLCPData": "pppIPv6CP.header.data.dataInLCP.data-12",
    }

    def __init__(self, parent, list_op=False):
        super(PppIPv6CP, self).__init__(parent, list_op)

    @property
    def HeaderCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        Available enum values: Configure-Request, 1, Configure-Ack, 2, Configure-Nak, 3, Configure-Reject, 4, Terminate-Request, 5, Terminate-Ack, 6, Code-Reject, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCode"]))

    @property
    def HeaderIdentifier(self):
        """
        Display Name: Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderIdentifier"])
        )

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def OptionsType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Interface-Identifier, 1, IPv6-Compression-Protocol, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionsType"]))

    @property
    def FieldsForInterfaceIdentifierLength(self):
        """
        Display Name: Length for Interface-Identifier
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FieldsForInterfaceIdentifierLength"]
            ),
        )

    @property
    def FieldsForInterfaceIdentifierIdentifier(self):
        """
        Display Name: Interface Identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FieldsForInterfaceIdentifierIdentifier"]
            ),
        )

    @property
    def FieldsForIPv6CompressionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FieldsForIPv6CompressionLength"]),
        )

    @property
    def FieldsForIPv6CompressionCompressionProtocol(self):
        """
        Display Name:  IPv6-Compression-Protocol
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FieldsForIPv6CompressionCompressionProtocol"]
            ),
        )

    @property
    def NextfieldsFieldsForIPv6CompressionLength(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextfieldsFieldsForIPv6CompressionLength"]
            ),
        )

    @property
    def FieldsForIPv6CompressionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldsForIPv6CompressionData"])
        )

    @property
    def DataInLCPLength(self):
        """
        Display Name: Length of data field
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataInLCPLength"])
        )

    @property
    def DataInLCPData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataInLCPData"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
