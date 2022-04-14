from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Msdp(Base):
    __slots__ = ()
    _SDM_NAME = "msdp"
    _SDM_ATT_MAP = {
        "Ipv4SourceActiveType": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.type-1",
        "Ipv4SourceActiveLength": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.length-2",
        "Ipv4SourceActiveEntryCount": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.entryCount-3",
        "Ipv4SourceActiveRpAddress": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.rpAddress-4",
        "EntryReserved": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.entry.reserved-5",
        "EntrySourcePrefixLength": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.entry.sourcePrefixLength-6",
        "EntryGroupAddress": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.entry.groupAddress-7",
        "EntrySourceAddress": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActive.entry.sourceAddress-8",
        "Ipv4SourceActiveRequestType": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActiveRequest.type-9",
        "Ipv4SourceActiveRequestLength": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActiveRequest.length-10",
        "Ipv4SourceActiveRequestGprefixLen": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActiveRequest.gprefixLen-11",
        "Ipv4SourceActiveRequestGroupAddressPrefix": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActiveRequest.groupAddressPrefix-12",
        "Ipv4SourceActiveResponseType": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActiveResponse.type-13",
        "Ipv4SourceActiveResponseLength": "msdp.msdpMessage.msdpMessegeType.ipv4SourceActiveResponse.length-14",
        "KeepaliveType": "msdp.msdpMessage.msdpMessegeType.keepalive.type-15",
        "KeepaliveLength": "msdp.msdpMessage.msdpMessegeType.keepalive.length-16",
    }

    def __init__(self, parent, list_op=False):
        super(Msdp, self).__init__(parent, list_op)

    @property
    def Ipv4SourceActiveType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveType"])
        )

    @property
    def Ipv4SourceActiveLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveLength"])
        )

    @property
    def Ipv4SourceActiveEntryCount(self):
        """
        Display Name: Entry count
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveEntryCount"])
        )

    @property
    def Ipv4SourceActiveRpAddress(self):
        """
        Display Name: RP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveRpAddress"])
        )

    @property
    def EntryReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EntryReserved"]))

    @property
    def EntrySourcePrefixLength(self):
        """
        Display Name: Source prefix length
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EntrySourcePrefixLength"])
        )

    @property
    def EntryGroupAddress(self):
        """
        Display Name: Group address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EntryGroupAddress"])
        )

    @property
    def EntrySourceAddress(self):
        """
        Display Name: Source address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EntrySourceAddress"])
        )

    @property
    def Ipv4SourceActiveRequestType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveRequestType"])
        )

    @property
    def Ipv4SourceActiveRequestLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveRequestLength"]),
        )

    @property
    def Ipv4SourceActiveRequestGprefixLen(self):
        """
        Display Name: Gprefix Len
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveRequestGprefixLen"]),
        )

    @property
    def Ipv4SourceActiveRequestGroupAddressPrefix(self):
        """
        Display Name: Group address prefix
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4SourceActiveRequestGroupAddressPrefix"]
            ),
        )

    @property
    def Ipv4SourceActiveResponseType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveResponseType"])
        )

    @property
    def Ipv4SourceActiveResponseLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceActiveResponseLength"]),
        )

    @property
    def KeepaliveType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeepaliveType"]))

    @property
    def KeepaliveLength(self):
        """
        Display Name: Length
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeepaliveLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
