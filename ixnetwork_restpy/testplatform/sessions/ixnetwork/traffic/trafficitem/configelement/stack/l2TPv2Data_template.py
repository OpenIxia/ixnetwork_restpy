from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2TPv2Data(Base):
    __slots__ = ()
    _SDM_NAME = "l2TPv2Data"
    _SDM_ATT_MAP = {
        "DataHeaderType": "l2TPv2Data.dataHeader.type-1",
        "DataHeaderLength": "l2TPv2Data.dataHeader.length-2",
        "DataHeaderReserved2": "l2TPv2Data.dataHeader.reserved2-3",
        "DataHeaderSequence": "l2TPv2Data.dataHeader.sequence-4",
        "DataHeaderReserved1": "l2TPv2Data.dataHeader.reserved1-5",
        "DataHeaderOffset": "l2TPv2Data.dataHeader.offset-6",
        "DataHeaderPriority": "l2TPv2Data.dataHeader.priority-7",
        "DataHeaderReserved4": "l2TPv2Data.dataHeader.reserved4-8",
        "DataHeaderVersion": "l2TPv2Data.dataHeader.version-9",
        "DataHeaderControlLength": "l2TPv2Data.dataHeader.controlLength-10",
        "TunnelSessionIdCombinedIds": "l2TPv2Data.dataHeader.tunnelSessionId.combinedIds-11",
        "SeparateIdsTunnelId": "l2TPv2Data.dataHeader.tunnelSessionId.separateIds.tunnelId-12",
        "SeparateIdsSessionId": "l2TPv2Data.dataHeader.tunnelSessionId.separateIds.sessionId-13",
        "SequenceNs": "l2TPv2Data.dataHeader.sequence.ns-14",
        "SequenceNr": "l2TPv2Data.dataHeader.sequence.nr-15",
        "OffsetOffsetSize": "l2TPv2Data.dataHeader.offset.offsetSize-16",
        "OffsetData": "l2TPv2Data.dataHeader.offset.data-17",
    }

    def __init__(self, parent, list_op=False):
        super(L2TPv2Data, self).__init__(parent, list_op)

    @property
    def DataHeaderType(self):
        """
        Display Name: Type bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Data message, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderType"])
        )

    @property
    def DataHeaderLength(self):
        """
        Display Name: Length bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Length field not present, 0, Length field present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderLength"])
        )

    @property
    def DataHeaderReserved2(self):
        """
        Display Name: Reserved bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderReserved2"])
        )

    @property
    def DataHeaderSequence(self):
        """
        Display Name: Sequence bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Ns and Nr fields not present, 0, Ns and Nr fields present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderSequence"])
        )

    @property
    def DataHeaderReserved1(self):
        """
        Display Name: Reserved bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderReserved1"])
        )

    @property
    def DataHeaderOffset(self):
        """
        Display Name: Offset bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Offset fields not present, 0, Offset fields present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderOffset"])
        )

    @property
    def DataHeaderPriority(self):
        """
        Display Name: Priority bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Normal priority, 0, Requires preferential treatment, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderPriority"])
        )

    @property
    def DataHeaderReserved4(self):
        """
        Display Name: Reserved bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderReserved4"])
        )

    @property
    def DataHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderVersion"])
        )

    @property
    def DataHeaderControlLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataHeaderControlLength"])
        )

    @property
    def TunnelSessionIdCombinedIds(self):
        """
        Display Name: Concatenated IDs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TunnelSessionIdCombinedIds"])
        )

    @property
    def SeparateIdsTunnelId(self):
        """
        Display Name: Tunnel ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SeparateIdsTunnelId"])
        )

    @property
    def SeparateIdsSessionId(self):
        """
        Display Name: Session ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SeparateIdsSessionId"])
        )

    @property
    def SequenceNs(self):
        """
        Display Name: Sequence number for this message
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SequenceNs"]))

    @property
    def SequenceNr(self):
        """
        Display Name: Sequence number expected next message
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SequenceNr"]))

    @property
    def OffsetOffsetSize(self):
        """
        Display Name: Offset size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OffsetOffsetSize"])
        )

    @property
    def OffsetData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OffsetData"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
