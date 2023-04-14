from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Vxlangpe(Base):
    __slots__ = ()
    _SDM_NAME = "vxlangpe"
    _SDM_ATT_MAP = {
        "FlagsReserved11": "vxlangpe.header.flags.reserved11-1",
        "FlagsReserved12": "vxlangpe.header.flags.reserved12-2",
        "FlagsVersion": "vxlangpe.header.flags.version-3",
        "FlagsInstanceBit": "vxlangpe.header.flags.instanceBit-4",
        "FlagsNextProtocolBit": "vxlangpe.header.flags.nextProtocolBit-5",
        "FlagsBumTrafficBit": "vxlangpe.header.flags.bumTrafficBit-6",
        "FlagsOamFlagBit": "vxlangpe.header.flags.oamFlagBit-7",
        "HeaderReserved": "vxlangpe.header.reserved-8",
        "HeaderNextProtocol": "vxlangpe.header.nextProtocol-9",
        "HeaderVni": "vxlangpe.header.vni-10",
        "HeaderReserved8": "vxlangpe.header.reserved8-11",
    }

    def __init__(self, parent, list_op=False):
        super(Vxlangpe, self).__init__(parent, list_op)

    @property
    def FlagsReserved11(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved11"])
        )

    @property
    def FlagsReserved12(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved12"])
        )

    @property
    def FlagsVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsVersion"]))

    @property
    def FlagsInstanceBit(self):
        """
        Display Name: Instance Bit
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsInstanceBit"])
        )

    @property
    def FlagsNextProtocolBit(self):
        """
        Display Name: Next Protocol Bit
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsNextProtocolBit"])
        )

    @property
    def FlagsBumTrafficBit(self):
        """
        Display Name: BUM Traffic Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsBumTrafficBit"])
        )

    @property
    def FlagsOamFlagBit(self):
        """
        Display Name: OAM Flag Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsOamFlagBit"])
        )

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderNextProtocol(self):
        """
        Display Name: Next Protocol
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNextProtocol"])
        )

    @property
    def HeaderVni(self):
        """
        Display Name: VNI
        Default Value: 1000
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVni"]))

    @property
    def HeaderReserved8(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved8"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
