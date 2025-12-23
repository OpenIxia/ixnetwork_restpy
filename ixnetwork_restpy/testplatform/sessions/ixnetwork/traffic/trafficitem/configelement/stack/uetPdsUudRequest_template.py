from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetPdsUudRequest(Base):
    __slots__ = ()
    _SDM_NAME = "uetPdsUudRequest"
    _SDM_ATT_MAP = {
        "HeaderType": "uetPdsUudRequest.header.type-1",
        "HeaderNextHdr": "uetPdsUudRequest.header.nextHdr-2",
        "HeaderFlags": "uetPdsUudRequest.header.flags-3",
        "HeaderReserved": "uetPdsUudRequest.header.reserved-4",
    }

    def __init__(self, parent, list_op=False):
        super(UetPdsUudRequest, self).__init__(parent, list_op)

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        Available enum values: UUD_REQ, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderNextHdr"]))

    @property
    def HeaderFlags(self):
        """
        Display Name: Flags (7-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFlags"]))

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
