from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Igmpv2(Base):
    __slots__ = ()
    _SDM_NAME = "igmpv2"
    _SDM_ATT_MAP = {
        "Type": "igmpv2.header.type-1",
        "MaximumResponseTimeunits110Second": "igmpv2.header.maximumResponseTimeunits110Second-2",
        "Checksum": "igmpv2.header.checksum-3",
        "GroupAddress": "igmpv2.header.groupAddress-4",
    }

    def __init__(self, parent, list_op=False):
        super(Igmpv2, self).__init__(parent, list_op)

    @property
    def Type(self):
        """
        Display Name: Type
        Default Value: 17
        Value Format: decimal
        Available enum values: Membership Query, 17, Version 1 Membership Report, 18, Version 2 Membership Report, 22, Leave Group, 23
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def MaximumResponseTimeunits110Second(self):
        """
        Display Name: Maximum response time (units 1/10 second)
        Default Value: 100
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MaximumResponseTimeunits110Second"]),
        )

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


class Igmpv2(Base):
    __slots__ = ()
    _SDM_NAME = "igmpv2"
    _SDM_ATT_MAP = {
        "Type": "igmpv2.header.type-1",
        "MaximumResponseTimeunits110Second": "igmpv2.header.maximumResponseTimeunits110Second-2",
        "Checksum": "igmpv2.header.checksum-3",
        "GroupAddress": "igmpv2.header.groupAddress-4",
    }

    def __init__(self, parent, list_op=False):
        super(Igmpv2, self).__init__(parent, list_op)

    @property
    def Type(self):
        """
        Display Name: Type
        Default Value: 17
        Value Format: decimal
        Available enum values: Membership Query, 17, Version 1 Membership Report, 18, Version 2 Membership Report, 22, Leave Group, 23
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Type"]))

    @property
    def MaximumResponseTimeunits110Second(self):
        """
        Display Name: Maximum response time (units 1/10 second)
        Default Value: 100
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MaximumResponseTimeunits110Second"]),
        )

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
