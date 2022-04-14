from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MaapHeader(Base):
    __slots__ = ()
    _SDM_NAME = "maapHeader"
    _SDM_ATT_MAP = {
        "DefaultControlDataIndicator": "maapHeader.header..controlDataIndicator-1",
        "DefaultSubtype": "maapHeader.header..subtype-2",
        "DefaultStreamIdValid": "maapHeader.header..streamIdValid-3",
        "DefaultVersion": "maapHeader.header..version-4",
        "MaapReservedMessageTypeMessageType": "maapHeader.header.selectMessageType.maapReservedMessageType.messageType-5",
        "MaapProbMessageTypeMessageType": "maapHeader.header.selectMessageType.maapProbMessageType.messageType-6",
        "MaapDefendMessageTypeMessageType": "maapHeader.header.selectMessageType.maapDefendMessageType.messageType-7",
        "MaapAnnounceMessageTypeMessageType": "maapHeader.header.selectMessageType.maapAnnounceMessageType.messageType-8",
        "HeaderMaapVersion": "maapHeader.header.maapVersion-9",
        "HeaderMaapVersion": "maapHeader.header.maapVersion-10",
        "HeaderStreamId": "maapHeader.header.streamId-11",
        "HeaderRequestedStartAddress": "maapHeader.header.requestedStartAddress-12",
        "HeaderRequestedCount": "maapHeader.header.requestedCount-13",
        "HeaderConflictStartAddress": "maapHeader.header.conflictStartAddress-14",
        "HeaderConflictCount": "maapHeader.header.conflictCount-15",
    }

    def __init__(self, parent, list_op=False):
        super(MaapHeader, self).__init__(parent, list_op)

    @property
    def DefaultControlDataIndicator(self):
        """
        Display Name: CD
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultControlDataIndicator"])
        )

    @property
    def DefaultSubtype(self):
        """
        Display Name: Subtype
        Default Value: 0x7E
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultSubtype"])
        )

    @property
    def DefaultStreamIdValid(self):
        """
        Display Name: SV
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultStreamIdValid"])
        )

    @property
    def DefaultVersion(self):
        """
        Display Name: Version
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultVersion"])
        )

    @property
    def MaapReservedMessageTypeMessageType(self):
        """
        Display Name: Message Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaapReservedMessageTypeMessageType"]
            ),
        )

    @property
    def MaapProbMessageTypeMessageType(self):
        """
        Display Name: Message Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MaapProbMessageTypeMessageType"]),
        )

    @property
    def MaapDefendMessageTypeMessageType(self):
        """
        Display Name: Message Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MaapDefendMessageTypeMessageType"]),
        )

    @property
    def MaapAnnounceMessageTypeMessageType(self):
        """
        Display Name: Message Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MaapAnnounceMessageTypeMessageType"]
            ),
        )

    @property
    def HeaderMaapVersion(self):
        """
        Display Name: Maap Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMaapVersion"])
        )

    @property
    def HeaderMaapVersion(self):
        """
        Display Name: Maap Data Length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMaapVersion"])
        )

    @property
    def HeaderStreamId(self):
        """
        Display Name: Stream ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderStreamId"])
        )

    @property
    def HeaderRequestedStartAddress(self):
        """
        Display Name: Requested Start Address
        Default Value: 0x91E0F000FE00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRequestedStartAddress"])
        )

    @property
    def HeaderRequestedCount(self):
        """
        Display Name: Requested Count
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRequestedCount"])
        )

    @property
    def HeaderConflictStartAddress(self):
        """
        Display Name: Conflict Start Address
        Default Value: 0x001101000002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderConflictStartAddress"])
        )

    @property
    def HeaderConflictCount(self):
        """
        Display Name: Conflict Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderConflictCount"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
