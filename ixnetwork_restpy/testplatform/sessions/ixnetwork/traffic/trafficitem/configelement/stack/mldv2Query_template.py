from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Mldv2Query(Base):
    __slots__ = ()
    _SDM_NAME = "mldv2Query"
    _SDM_ATT_MAP = {
        "Mldv2ListenerQueryType": "mldv2Query.mldv2ListenerQuery.type-1",
        "Mldv2ListenerQueryCode": "mldv2Query.mldv2ListenerQuery.code-2",
        "Mldv2ListenerQueryMldv2Checksum": "mldv2Query.mldv2ListenerQuery.mldv2Checksum-3",
        "Mldv2ListenerQueryMaximumResponseCode": "mldv2Query.mldv2ListenerQuery.maximumResponseCode-4",
        "Mldv2ListenerQueryReserved": "mldv2Query.mldv2ListenerQuery.reserved-5",
        "Mldv2ListenerQueryMulticastAddress": "mldv2Query.mldv2ListenerQuery.multicastAddress-6",
        "Mldv2ListenerQueryResv": "mldv2Query.mldv2ListenerQuery.resv-7",
        "SFlagValue": "mldv2Query.mldv2ListenerQuery.sFlag.value-8",
        "Mldv2ListenerQueryQrv": "mldv2Query.mldv2ListenerQuery.qrv-9",
        "Mldv2ListenerQueryQqic": "mldv2Query.mldv2ListenerQuery.qqic-10",
        "Mldv2ListenerQueryNumberOfSources": "mldv2Query.mldv2ListenerQuery.numberOfSources-11",
        "SourceAddressEntriesSourceAddress": "mldv2Query.mldv2ListenerQuery.sourceAddressEntries.sourceAddress-12",
    }

    def __init__(self, parent, list_op=False):
        super(Mldv2Query, self).__init__(parent, list_op)

    @property
    def Mldv2ListenerQueryType(self):
        """
        Display Name: Type
        Default Value: 130
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryType"])
        )

    @property
    def Mldv2ListenerQueryCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryCode"])
        )

    @property
    def Mldv2ListenerQueryMldv2Checksum(self):
        """
        Display Name: MLDv2 checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryMldv2Checksum"]),
        )

    @property
    def Mldv2ListenerQueryMaximumResponseCode(self):
        """
        Display Name: Maximum response code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Mldv2ListenerQueryMaximumResponseCode"]
            ),
        )

    @property
    def Mldv2ListenerQueryReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryReserved"])
        )

    @property
    def Mldv2ListenerQueryMulticastAddress(self):
        """
        Display Name: Multicast address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Mldv2ListenerQueryMulticastAddress"]
            ),
        )

    @property
    def Mldv2ListenerQueryResv(self):
        """
        Display Name: Resv
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryResv"])
        )

    @property
    def SFlagValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: decimal
        Available enum values: OFF, 0, ON, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SFlagValue"]))

    @property
    def Mldv2ListenerQueryQrv(self):
        """
        Display Name: QRV
        Default Value: 2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryQrv"])
        )

    @property
    def Mldv2ListenerQueryQqic(self):
        """
        Display Name: QQIC
        Default Value: 125
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryQqic"])
        )

    @property
    def Mldv2ListenerQueryNumberOfSources(self):
        """
        Display Name: Number of Sources
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Mldv2ListenerQueryNumberOfSources"]),
        )

    @property
    def SourceAddressEntriesSourceAddress(self):
        """
        Display Name: Source address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SourceAddressEntriesSourceAddress"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
