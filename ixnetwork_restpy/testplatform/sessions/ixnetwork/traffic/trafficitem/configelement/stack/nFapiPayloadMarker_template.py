from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NFapiPayloadMarker(Base):
    __slots__ = ()
    _SDM_NAME = "nFapiPayloadMarker"
    _SDM_ATT_MAP = {
        "HeaderMarker": "nFapiPayloadMarker.header.marker-1",
        "HeaderSequenceNumber": "nFapiPayloadMarker.header.sequenceNumber-2",
        "HeaderSegmentNumber": "nFapiPayloadMarker.header.segmentNumber-3",
    }

    def __init__(self, parent, list_op=False):
        super(NFapiPayloadMarker, self).__init__(parent, list_op)

    @property
    def HeaderMarker(self):
        """
        Display Name: Payload Marker
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderMarker"]))

    @property
    def HeaderSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSequenceNumber"])
        )

    @property
    def HeaderSegmentNumber(self):
        """
        Display Name: Segment Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSegmentNumber"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
