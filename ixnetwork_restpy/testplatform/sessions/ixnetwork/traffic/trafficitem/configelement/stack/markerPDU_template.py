from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MarkerPDU(Base):
    __slots__ = ()
    _SDM_NAME = "markerPDU"
    _SDM_ATT_MAP = {
        "HeaderDstAddress": "markerPDU.header.header.dstAddress-1",
        "HeaderSrcAddress": "markerPDU.header.header.srcAddress-2",
        "HeaderLengthType": "markerPDU.header.header.lengthType-3",
        "HeaderSubtype": "markerPDU.header.header.subtype-4",
        "HeaderVersion": "markerPDU.header.header.version-5",
        "ActorTlvType": "markerPDU.header.actor.tlvType-6",
        "ActorTlvLength": "markerPDU.header.actor.tlvLength-7",
        "ActorRequesterPort": "markerPDU.header.actor.requesterPort-8",
        "ActorRequesterSystem": "markerPDU.header.actor.requesterSystem-9",
        "ActorRequesterTransactionId": "markerPDU.header.actor.requesterTransactionId-10",
        "ActorPad": "markerPDU.header.actor.pad-11",
        "TerminatorTlvType": "markerPDU.header.terminator.tlvType-12",
        "TerminatorTlvLength": "markerPDU.header.terminator.tlvLength-13",
        "HeaderReserved": "markerPDU.header.reserved-14",
        "HeaderFcs": "markerPDU.header.fcs-15",
    }

    def __init__(self, parent, list_op=False):
        super(MarkerPDU, self).__init__(parent, list_op)

    @property
    def HeaderDstAddress(self):
        """
        Display Name: Destination address
        Default Value: 01:80:C2:00:00:02
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDstAddress"])
        )

    @property
    def HeaderSrcAddress(self):
        """
        Display Name: Source address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcAddress"])
        )

    @property
    def HeaderLengthType(self):
        """
        Display Name: Length Type
        Default Value: 0x8809
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLengthType"])
        )

    @property
    def HeaderSubtype(self):
        """
        Display Name: Sub Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSubtype"]))

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def ActorTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 0x01
        Value Format: hex
        Available enum values: Marker Information, 1, Marker Response Information, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorTlvType"]))

    @property
    def ActorTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0x10
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActorTlvLength"])
        )

    @property
    def ActorRequesterPort(self):
        """
        Display Name: Requester Port
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActorRequesterPort"])
        )

    @property
    def ActorRequesterSystem(self):
        """
        Display Name: Requester System
        Default Value: 0x000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActorRequesterSystem"])
        )

    @property
    def ActorRequesterTransactionId(self):
        """
        Display Name: Requester Transaction Id
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActorRequesterTransactionId"])
        )

    @property
    def ActorPad(self):
        """
        Display Name: Pad
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorPad"]))

    @property
    def TerminatorTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TerminatorTlvType"])
        )

    @property
    def TerminatorTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TerminatorTlvLength"])
        )

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderFcs(self):
        """
        Display Name: Frame Check Sequence CRC-32
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFcs"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
