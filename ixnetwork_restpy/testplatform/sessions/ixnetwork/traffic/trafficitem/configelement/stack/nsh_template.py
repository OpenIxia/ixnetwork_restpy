from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Nsh(Base):
    __slots__ = ()
    _SDM_NAME = "nsh"
    _SDM_ATT_MAP = {
        "Network_service_headerVersion": "nsh.network_service_header.version-1",
        "Network_service_headerZeroBit": "nsh.network_service_header.zeroBit-2",
        "Network_service_headerC_bit": "nsh.network_service_header.c_bit-3",
        "Network_service_headerTtl": "nsh.network_service_header.ttl-4",
        "Network_service_headerLength": "nsh.network_service_header.length-5",
        "Md_type_1MdType1": "nsh.network_service_header.mdType.md_type_1.mdType1-6",
        "Md_type_1NextProtocol": "nsh.network_service_header.mdType.md_type_1.nextProtocol-7",
        "Md_type_1Spi": "nsh.network_service_header.mdType.md_type_1.spi-8",
        "Md_type_1Si": "nsh.network_service_header.mdType.md_type_1.si-9",
        "Md_type_1Fixed_context": "nsh.network_service_header.mdType.md_type_1.fixed_context-10",
        "Md_type_2MdType2": "nsh.network_service_header.mdType.md_type_2.mdType2-11",
        "Md_type_2NextProtocol": "nsh.network_service_header.mdType.md_type_2.nextProtocol-12",
        "Md_type_2Spi": "nsh.network_service_header.mdType.md_type_2.spi-13",
        "Md_type_2Si": "nsh.network_service_header.mdType.md_type_2.si-14",
        "Var_len_metadataTlvClass": "nsh.network_service_header.mdType.md_type_2.var_len_metadata.tlvClass-15",
        "Var_len_metadataType": "nsh.network_service_header.mdType.md_type_2.var_len_metadata.type-16",
        "Var_len_metadataUnassigned": "nsh.network_service_header.mdType.md_type_2.var_len_metadata.unassigned-17",
        "Var_len_metadataLength": "nsh.network_service_header.mdType.md_type_2.var_len_metadata.length-18",
        "Var_len_metadataMetadata": "nsh.network_service_header.mdType.md_type_2.var_len_metadata.metadata-19",
        "Var_len_metadataPadding": "nsh.network_service_header.mdType.md_type_2.var_len_metadata.padding-20",
        "Network_service_headerPadding": "nsh.network_service_header.padding-21",
    }

    def __init__(self, parent, list_op=False):
        super(Nsh, self).__init__(parent, list_op)

    @property
    def Network_service_headerVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Network_service_headerVersion"]),
        )

    @property
    def Network_service_headerZeroBit(self):
        """
        Display Name: 0 bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Network_service_headerZeroBit"]),
        )

    @property
    def Network_service_headerC_bit(self):
        """
        Display Name: C bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Network_service_headerC_bit"])
        )

    @property
    def Network_service_headerTtl(self):
        """
        Display Name: TTL
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Network_service_headerTtl"])
        )

    @property
    def Network_service_headerLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Network_service_headerLength"])
        )

    @property
    def Md_type_1MdType1(self):
        """
        Display Name: MD Type 1
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md_type_1MdType1"])
        )

    @property
    def Md_type_1NextProtocol(self):
        """
        Display Name: Next Protocol
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md_type_1NextProtocol"])
        )

    @property
    def Md_type_1Spi(self):
        """
        Display Name: SPI
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Md_type_1Spi"]))

    @property
    def Md_type_1Si(self):
        """
        Display Name: SI
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Md_type_1Si"]))

    @property
    def Md_type_1Fixed_context(self):
        """
        Display Name: Fixed Context
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md_type_1Fixed_context"])
        )

    @property
    def Md_type_2MdType2(self):
        """
        Display Name: MD Type 2
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md_type_2MdType2"])
        )

    @property
    def Md_type_2NextProtocol(self):
        """
        Display Name: Next Protocol
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Md_type_2NextProtocol"])
        )

    @property
    def Md_type_2Spi(self):
        """
        Display Name: SPI
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Md_type_2Spi"]))

    @property
    def Md_type_2Si(self):
        """
        Display Name: SI
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Md_type_2Si"]))

    @property
    def Var_len_metadataTlvClass(self):
        """
        Display Name: TLV Class
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Var_len_metadataTlvClass"])
        )

    @property
    def Var_len_metadataType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Var_len_metadataType"])
        )

    @property
    def Var_len_metadataUnassigned(self):
        """
        Display Name: Unassigned
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Var_len_metadataUnassigned"])
        )

    @property
    def Var_len_metadataLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Var_len_metadataLength"])
        )

    @property
    def Var_len_metadataMetadata(self):
        """
        Display Name: Metadata
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Var_len_metadataMetadata"])
        )

    @property
    def Var_len_metadataPadding(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Var_len_metadataPadding"])
        )

    @property
    def Network_service_headerPadding(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Network_service_headerPadding"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
