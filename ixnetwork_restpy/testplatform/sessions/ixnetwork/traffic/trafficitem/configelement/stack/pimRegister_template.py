from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PimRegister(Base):
    __slots__ = ()
    _SDM_NAME = "pimRegister"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pimRegister.header.version-1",
        "HeaderMessageType": "pimRegister.header.messageType-2",
        "HeaderReserved": "pimRegister.header.reserved-3",
        "HeaderChecksum": "pimRegister.header.checksum-4",
        "HeaderBorderBit": "pimRegister.header.borderBit-5",
        "HeaderNullRegisterBit": "pimRegister.header.nullRegisterBit-6",
        "HeaderReserved2": "pimRegister.header.reserved2-7",
    }

    def __init__(self, parent, list_op=False):
        super(PimRegister, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderMessageType(self):
        """
        Display Name: Message type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageType"])
        )

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderChecksum"])
        )

    @property
    def HeaderBorderBit(self):
        """
        Display Name: Border Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBorderBit"])
        )

    @property
    def HeaderNullRegisterBit(self):
        """
        Display Name: Null Register Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNullRegisterBit"])
        )

    @property
    def HeaderReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved2"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
