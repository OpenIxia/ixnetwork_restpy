from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IMAPResponseCapabilityOK(Base):
    __slots__ = ()
    _SDM_NAME = "IMAP_Response_Capability_OK"
    _SDM_ATT_MAP = {
        "RESPONSE1Response Tag1": "IMAP_Response_Capability_OK.header.RESPONSE1.Response Tag1-1",
        "RESPONSE1Space5": "IMAP_Response_Capability_OK.header.RESPONSE1.Space5-2",
        "RESPONSE1Response": "IMAP_Response_Capability_OK.header.RESPONSE1.Response-3",
        "RESPONSE1CRLF": "IMAP_Response_Capability_OK.header.RESPONSE1.CRLF-4",
        "RESPONSE2Response Tag": "IMAP_Response_Capability_OK.header.RESPONSE2.Response Tag-5",
        "RESPONSE2Space6": "IMAP_Response_Capability_OK.header.RESPONSE2.Space6-6",
        "RESPONSE2Response": "IMAP_Response_Capability_OK.header.RESPONSE2.Response-7",
        "RESPONSE2CRLF": "IMAP_Response_Capability_OK.header.RESPONSE2.CRLF-8",
    }

    def __init__(self, parent, list_op=False):
        super(IMAPResponseCapabilityOK, self).__init__(parent, list_op)

    @property
    def RESPONSE1ResponseTag1(self):
        """
        Display Name: Response Tag1
        Default Value: 0x2A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE1Response Tag1"])
        )

    @property
    def RESPONSE1Space5(self):
        """
        Display Name: Space5
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE1Space5"])
        )

    @property
    def RESPONSE1Response(self):
        """
        Display Name: Response
        Default Value: 0x4341504142494C49545920494D41503420494D415034726576312049444C45204C49544552414C2B204C4F47494E2D524546455252414C53204D41494C424F582D524546455252414C53204E414D45535041434520415554483D4E544C4D
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE1Response"])
        )

    @property
    def RESPONSE1CRLF(self):
        """
        Display Name: CRLF
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE1CRLF"]))

    @property
    def RESPONSE2ResponseTag(self):
        """
        Display Name: Response Tag
        Default Value: 0x6130303030
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE2Response Tag"])
        )

    @property
    def RESPONSE2Space6(self):
        """
        Display Name: Space6
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE2Space6"])
        )

    @property
    def RESPONSE2Response(self):
        """
        Display Name: Response
        Default Value: 0x4F4B204341504142494C49545920636F6D706C657465642E
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE2Response"])
        )

    @property
    def RESPONSE2CRLF(self):
        """
        Display Name: CRLF
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RESPONSE2CRLF"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
