from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class HTTP200OK(Base):
    __slots__ = ()
    _SDM_NAME = "HTTP_200_OK"
    _SDM_ATT_MAP = {
        "FieldHolder0REQUEST VERSION": "HTTP_200_OK.header.fieldHolder0.REQUEST VERSION-1",
        "FieldHolder0Space3": "HTTP_200_OK.header.fieldHolder0.Space3-2",
        "FieldHolder0STATUS CODE": "HTTP_200_OK.header.fieldHolder0.STATUS CODE-3",
        "FieldHolder0Space4": "HTTP_200_OK.header.fieldHolder0.Space4-4",
        "FieldHolder0Response Phrase": "HTTP_200_OK.header.fieldHolder0.Response Phrase-5",
        "FieldHolder0CRLF2RF": "HTTP_200_OK.header.fieldHolder0.CRLF2RF-6",
        "HeaderDate": "HTTP_200_OK.header.Date-7",
        "HeaderServer": "HTTP_200_OK.header.Server-8",
        "HeaderLast-Modified": "HTTP_200_OK.header.Last-Modified-9",
        "HeaderETag": "HTTP_200_OK.header.ETag-10",
        "HeaderAccept-Ranges": "HTTP_200_OK.header.Accept-Ranges-11",
        "HeaderContent-Length": "HTTP_200_OK.header.Content-Length-12",
        "HeaderKeep-Alive": "HTTP_200_OK.header.Keep-Alive-13",
        "HeaderConnection": "HTTP_200_OK.header.Connection-14",
        "HeaderContent-Type": "HTTP_200_OK.header.Content-Type-15",
        "HeaderCRLF": "HTTP_200_OK.header.CRLF-16",
    }

    def __init__(self, parent, list_op=False):
        super(HTTP200OK, self).__init__(parent, list_op)

    @property
    def FieldHolder0REQUESTVERSION(self):
        """
        Display Name: REQUEST VERSION
        Default Value: 0x485454502F312E31
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldHolder0REQUEST VERSION"])
        )

    @property
    def FieldHolder0Space3(self):
        """
        Display Name: Space3
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldHolder0Space3"])
        )

    @property
    def FieldHolder0STATUSCODE(self):
        """
        Display Name: STATUS CODE
        Default Value: 0x323030
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldHolder0STATUS CODE"])
        )

    @property
    def FieldHolder0Space4(self):
        """
        Display Name: Space4
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldHolder0Space4"])
        )

    @property
    def FieldHolder0ResponsePhrase(self):
        """
        Display Name: Response Phrase
        Default Value: 0x4F4B
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldHolder0Response Phrase"])
        )

    @property
    def FieldHolder0CRLF2RF(self):
        """
        Display Name: CRLF2
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldHolder0CRLF2RF"])
        )

    @property
    def HeaderDate(self):
        """
        Display Name: Date
        Default Value: 0x446174653A205468752C203133204D617920323030342031303A31373A313220474D540D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDate"]))

    @property
    def HeaderServer(self):
        """
        Display Name: Server
        Default Value: 0x5365727665723A204170616368650D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderServer"]))

    @property
    def HeaderLastModified(self):
        """
        Display Name: Last-Modified
        Default Value: 0x4C6173742D4D6F6469666965643A205475652C2032302041707220323030342031333A31373A303020474D540D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLast-Modified"])
        )

    @property
    def HeaderETag(self):
        """
        Display Name: ETag
        Default Value: 0x455461673A202239613031612D343639362D3765333534623030220D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderETag"]))

    @property
    def HeaderAcceptRanges(self):
        """
        Display Name: Accept-Ranges
        Default Value: 0x4163636570742D52616E6765733A2062797465730D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept-Ranges"])
        )

    @property
    def HeaderContentLength(self):
        """
        Display Name: Content-Length
        Default Value: 0x436F6E74656E742D4C656E6774683A2031383037300D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderContent-Length"])
        )

    @property
    def HeaderKeepAlive(self):
        """
        Display Name: Keep-Alive
        Default Value: 0x4B6565702D416C6976653A2074696D656F75743D31352C206D61783D3130300D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderKeep-Alive"])
        )

    @property
    def HeaderConnection(self):
        """
        Display Name: Connection
        Default Value: 0x436F6E6E656374696F6E3A204B6565702D416C6976650D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderConnection"])
        )

    @property
    def HeaderContentType(self):
        """
        Display Name: Content-Type
        Default Value: 0x436F6E74656E742D547970653A20746578742F68746D6C3B20636861727365743D49534F2D383835392D310D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderContent-Type"])
        )

    @property
    def HeaderCRLF(self):
        """
        Display Name: CRLF
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCRLF"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
