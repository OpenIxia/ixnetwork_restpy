from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class H264(Base):
    __slots__ = ()
    _SDM_NAME = "h264"
    _SDM_ATT_MAP = {
        "HeaderVersion": "h264.header.Version-1",
        "HeaderPaddingBit": "h264.header.paddingBit-2",
        "HeaderExtensionBit": "h264.header.extensionBit-3",
        "HeaderCsrcCount": "h264.header.csrcCount-4",
        "HeaderMarker": "h264.header.Marker-5",
        "HeaderPayloadType": "h264.header.payloadType-6",
        "HeaderSequenceNumber": "h264.header.sequenceNumber-7",
        "HeaderTimestamp": "h264.header.timestamp-8",
        "HeaderSynchronizationSourceIdentifier": "h264.header.synchronizationSourceIdentifier-9",
    }

    def __init__(self, parent, list_op=False):
        super(H264, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderPaddingBit(self):
        """
        Display Name: Padding Bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPaddingBit"])
        )

    @property
    def HeaderExtensionBit(self):
        """
        Display Name: Extension Bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderExtensionBit"])
        )

    @property
    def HeaderCsrcCount(self):
        """
        Display Name: CSRC Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCsrcCount"])
        )

    @property
    def HeaderMarker(self):
        """
        Display Name: Marker
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderMarker"]))

    @property
    def HeaderPayloadType(self):
        """
        Display Name: Payload Type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPayloadType"])
        )

    @property
    def HeaderSequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSequenceNumber"])
        )

    @property
    def HeaderTimestamp(self):
        """
        Display Name: Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTimestamp"])
        )

    @property
    def HeaderSynchronizationSourceIdentifier(self):
        """
        Display Name: SSRC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HeaderSynchronizationSourceIdentifier"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
