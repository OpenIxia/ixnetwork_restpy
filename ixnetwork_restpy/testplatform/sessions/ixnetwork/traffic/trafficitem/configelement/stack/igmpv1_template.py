from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Igmpv1(Base):
    __slots__ = ()
    _SDM_NAME = "igmpv1"
    _SDM_ATT_MAP = {
        "Version": "igmpv1.header.version-1",
        "Type": "igmpv1.header.type-2",
        "Unused": "igmpv1.header.unused-3",
        "Checksum": "igmpv1.header.checksum-4",
        "GroupAddress": "igmpv1.header.groupAddress-5",
    }

    def __init__(self, parent, list_op=False):
        super(Igmpv1, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Type(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        Available enum values: Host Membership Query, 1, Host Membership Report, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Unused"]))

    @property
    def Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Checksum"]))

    @property
    def GroupAddress(self):
        """
        Display Name: Group address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GroupAddress"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))


from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Igmpv1(Base):
    __slots__ = ()
    _SDM_NAME = "igmpv1"
    _SDM_ATT_MAP = {
        "Version": "igmpv1.header.version-1",
        "Type": "igmpv1.header.type-2",
        "Unused": "igmpv1.header.unused-3",
        "Checksum": "igmpv1.header.checksum-4",
        "GroupAddress": "igmpv1.header.groupAddress-5",
    }

    def __init__(self, parent, list_op=False):
        super(Igmpv1, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Type(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        Available enum values: Host Membership Query, 1, Host Membership Report, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Unused"]))

    @property
    def Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Checksum"]))

    @property
    def GroupAddress(self):
        """
        Display Name: Group address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GroupAddress"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
