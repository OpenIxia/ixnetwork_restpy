from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class GTPuOptionalFields(Base):
    __slots__ = ()
    _SDM_NAME = "gTPuOptionalFields"
    _SDM_ATT_MAP = {
        "HeaderSequenceNumber": "gTPuOptionalFields.header.sequenceNumber-1",
        "HeaderNpduNumber": "gTPuOptionalFields.header.npduNumber-2",
        "HeaderNextExtHdrField": "gTPuOptionalFields.header.nextExtHdrField-3",
        "NextExtHdrTotalLength": "gTPuOptionalFields.header.nextExtHdrs.nextExtHdr.totalLength-4",
        "NextExtHdrContents": "gTPuOptionalFields.header.nextExtHdrs.nextExtHdr.contents-5",
        "NextExtHdrNextExt": "gTPuOptionalFields.header.nextExtHdrs.nextExtHdr.nextExt-6",
    }

    def __init__(self, parent, list_op=False):
        super(GTPuOptionalFields, self).__init__(parent, list_op)

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
    def HeaderNpduNumber(self):
        """
        Display Name: N-PDU Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNpduNumber"])
        )

    @property
    def HeaderNextExtHdrField(self):
        """
        Display Name: Next Extension Header Field
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNextExtHdrField"])
        )

    @property
    def NextExtHdrTotalLength(self):
        """
        Display Name: Total Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextExtHdrTotalLength"])
        )

    @property
    def NextExtHdrContents(self):
        """
        Display Name: Contents
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextExtHdrContents"])
        )

    @property
    def NextExtHdrNextExt(self):
        """
        Display Name: Next Extension
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextExtHdrNextExt"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
