from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetPdsRudiRequestResponse(Base):
    __slots__ = ()
    _SDM_NAME = "uetPdsRudiRequestResponse"
    _SDM_ATT_MAP = {
        "RudiRequestType": "uetPdsRudiRequestResponse.header.headerType.rudiRequest.type-1",
        "RudiRequestNextHdr": "uetPdsRudiRequestResponse.header.headerType.rudiRequest.nextHdr-2",
        "RudiRequestReserved": "uetPdsRudiRequestResponse.header.headerType.rudiRequest.reserved-3",
        "RudiRequestRetransmit": "uetPdsRudiRequestResponse.header.headerType.rudiRequest.retransmit-4",
        "RudiRequestReserved1": "uetPdsRudiRequestResponse.header.headerType.rudiRequest.reserved1-5",
        "RudiRequestReserved2": "uetPdsRudiRequestResponse.header.headerType.rudiRequest.reserved2-6",
        "RudiRequestPktId": "uetPdsRudiRequestResponse.header.headerType.rudiRequest.pktId-7",
        "RudiResponseType": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.type-8",
        "RudiResponseNextHdr": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.nextHdr-9",
        "RudiResponseReserved": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.reserved-10",
        "RudiResponseMFlag": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.mFlag-11",
        "RudiResponseRetransmit": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.retransmit-12",
        "RudiResponseReserved1": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.reserved1-13",
        "RudiResponseReserved2": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.reserved2-14",
        "RudiResponsePktId": "uetPdsRudiRequestResponse.header.headerType.rudiResponse.pktId-15",
    }

    def __init__(self, parent, list_op=False):
        super(UetPdsRudiRequestResponse, self).__init__(parent, list_op)

    @property
    def RudiRequestType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        Available enum values: RUDI_REQ, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiRequestType"])
        )

    @property
    def RudiRequestNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_HDR_REQUEST_STD, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiRequestNextHdr"])
        )

    @property
    def RudiRequestReserved(self):
        """
        Display Name: Reserved Flag (2-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiRequestReserved"])
        )

    @property
    def RudiRequestRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiRequestRetransmit"])
        )

    @property
    def RudiRequestReserved1(self):
        """
        Display Name: Reserved Flag (4-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiRequestReserved1"])
        )

    @property
    def RudiRequestReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiRequestReserved2"])
        )

    @property
    def RudiRequestPktId(self):
        """
        Display Name: Pkt Identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiRequestPktId"])
        )

    @property
    def RudiResponseType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        Available enum values: RUDI_RES, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponseType"])
        )

    @property
    def RudiResponseNextHdr(self):
        """
        Display Name: Next Hdr
        Default Value: 4
        Value Format: decimal
        Available enum values: UET_HDR_RESPONSE, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponseNextHdr"])
        )

    @property
    def RudiResponseReserved(self):
        """
        Display Name: Reserved Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponseReserved"])
        )

    @property
    def RudiResponseMFlag(self):
        """
        Display Name: m Flag (ECN marked request)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponseMFlag"])
        )

    @property
    def RudiResponseRetransmit(self):
        """
        Display Name: Retransmit Flag (1-bit)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponseRetransmit"])
        )

    @property
    def RudiResponseReserved1(self):
        """
        Display Name: Reserved Flag (4-bits)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponseReserved1"])
        )

    @property
    def RudiResponseReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponseReserved2"])
        )

    @property
    def RudiResponsePktId(self):
        """
        Display Name: Pkt Identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RudiResponsePktId"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
