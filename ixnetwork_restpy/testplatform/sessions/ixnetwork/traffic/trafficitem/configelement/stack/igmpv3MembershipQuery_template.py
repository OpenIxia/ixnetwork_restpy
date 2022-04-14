from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Igmpv3MembershipQuery(Base):
    __slots__ = ()
    _SDM_NAME = "igmpv3MembershipQuery"
    _SDM_ATT_MAP = {
        "HeaderType": "igmpv3MembershipQuery.header.type-1",
        "HeaderMaximumResponseCodeunits110Second": "igmpv3MembershipQuery.header.maximumResponseCodeunits110Second-2",
        "HeaderChecksum": "igmpv3MembershipQuery.header.checksum-3",
        "HeaderGroupAddress": "igmpv3MembershipQuery.header.groupAddress-4",
        "HeaderReserved": "igmpv3MembershipQuery.header.reserved-5",
        "HeaderSuppressRoutersideProcessingSflag": "igmpv3MembershipQuery.header.suppressRoutersideProcessingSflag-6",
        "HeaderQrv": "igmpv3MembershipQuery.header.qrv-7",
        "HeaderQqic": "igmpv3MembershipQuery.header.qqic-8",
        "HeaderNumberOfSources": "igmpv3MembershipQuery.header.numberOfSources-9",
        "MulticastSourcesMulticastSource": "igmpv3MembershipQuery.header.multicastSources.multicastSource-10",
    }

    def __init__(self, parent, list_op=False):
        super(Igmpv3MembershipQuery, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0x11
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderMaximumResponseCodeunits110Second(self):
        """
        Display Name: Maximum response code (units 1/10 second)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HeaderMaximumResponseCodeunits110Second"]
            ),
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
    def HeaderGroupAddress(self):
        """
        Display Name: Group address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderGroupAddress"])
        )

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderSuppressRoutersideProcessingSflag(self):
        """
        Display Name: Suppress router-side processing (S-flag)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HeaderSuppressRoutersideProcessingSflag"]
            ),
        )

    @property
    def HeaderQrv(self):
        """
        Display Name: Querier's Robustness Variable
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderQrv"]))

    @property
    def HeaderQqic(self):
        """
        Display Name: Querier's Query Interval Code
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderQqic"]))

    @property
    def HeaderNumberOfSources(self):
        """
        Display Name: Number of sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNumberOfSources"])
        )

    @property
    def MulticastSourcesMulticastSource(self):
        """
        Display Name: Multicast source
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastSourcesMulticastSource"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
