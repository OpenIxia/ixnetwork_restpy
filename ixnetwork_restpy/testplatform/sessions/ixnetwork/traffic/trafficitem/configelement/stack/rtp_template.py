from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Rtp(Base):
    __slots__ = ()
    _SDM_NAME = "rtp"
    _SDM_ATT_MAP = {
        "Version": "rtp.header.version-1",
        "Pad": "rtp.header.pad-2",
        "ExtensionBit": "rtp.header.extensionBit-3",
        "ContributingSrcCount": "rtp.header.contributingSrcCount-4",
        "MarkerBit": "rtp.header.markerBit-5",
        "PayloadType": "rtp.header.payloadType-6",
        "SequenceNumber": "rtp.header.sequenceNumber-7",
        "Timestamp": "rtp.header.timestamp-8",
        "SynchronizationSource": "rtp.header.synchronizationSource-9",
        "NextContributingSourceContributingSource": "rtp.header.nextContributingSource.contributingSource-10",
        "HeaderExtensionIdentifier": "rtp.header.headerExtension.identifier-11",
        "HeaderExtensionLength": "rtp.header.headerExtension.length-12",
        "HeaderExtensionData": "rtp.header.headerExtension.data-13",
    }

    def __init__(self, parent, list_op=False):
        super(Rtp, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Pad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Pad"]))

    @property
    def ExtensionBit(self):
        """
        Display Name: Extension Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: No header extension is present, 0, Header Extension is present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExtensionBit"]))

    @property
    def ContributingSrcCount(self):
        """
        Display Name: Contributing source count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ContributingSrcCount"])
        )

    @property
    def MarkerBit(self):
        """
        Display Name: Marker Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MarkerBit"]))

    @property
    def PayloadType(self):
        """
        Display Name: Payload Type
        Default Value: 8
        Value Format: decimal
        Available enum values: PCMU, 0, 1016, 1, G721, 2, GSM, 3, DVI4 @ 8000Hz, 5, DVI4 @ 16000Hz, 6, LPC, 7, PCMA, 8, G722, 9, L16 (2 audio ch), 10, L16 (1 audio ch), 11, MPA, 14, G728, 15, CelB, 25, JPEG, 26, nv, 28, H261, 31, MPV, 32, MP2T, 33
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PayloadType"]))

    @property
    def SequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SequenceNumber"])
        )

    @property
    def Timestamp(self):
        """
        Display Name: Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Timestamp"]))

    @property
    def SynchronizationSource(self):
        """
        Display Name: Synchronization source
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SynchronizationSource"])
        )

    @property
    def NextContributingSourceContributingSource(self):
        """
        Display Name: Contributing source
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextContributingSourceContributingSource"]
            ),
        )

    @property
    def HeaderExtensionIdentifier(self):
        """
        Display Name: Extension header identifier
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderExtensionIdentifier"])
        )

    @property
    def HeaderExtensionLength(self):
        """
        Display Name: Extension header length(in 4 octets)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderExtensionLength"])
        )

    @property
    def HeaderExtensionData(self):
        """
        Display Name: Extension header data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderExtensionData"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
