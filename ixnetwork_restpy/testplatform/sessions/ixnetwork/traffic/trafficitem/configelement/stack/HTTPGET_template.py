from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class HTTPGET(Base):
    __slots__ = ()
    _SDM_NAME = "HTTP_GET"
    _SDM_ATT_MAP = {
        "RequestRequest Method": "HTTP_GET.header.Request.Request Method-1",
        "RequestSpace1": "HTTP_GET.header.Request.Space1-2",
        "RequestRequest URI": "HTTP_GET.header.Request.Request URI-3",
        "RequestSpace2": "HTTP_GET.header.Request.Space2-4",
        "RequestRequest version": "HTTP_GET.header.Request.Request version-5",
        "RequestCRLF1": "HTTP_GET.header.Request.CRLF1-6",
        "HeaderHost": "HTTP_GET.header.Host-7",
        "HeaderUser-Agent": "HTTP_GET.header.User-Agent-8",
        "HeaderAccept": "HTTP_GET.header.Accept-9",
        "HeaderAccept-Language": "HTTP_GET.header.Accept-Language-10",
        "HeaderAccept-Encoding": "HTTP_GET.header.Accept-Encoding-11",
        "HeaderAccept-Charset": "HTTP_GET.header.Accept-Charset-12",
        "HeaderKeep-Alive": "HTTP_GET.header.Keep-Alive-13",
        "HeaderConnection": "HTTP_GET.header.Connection-14",
        "HeaderReferer": "HTTP_GET.header.Referer-15",
        "HeaderCRLF": "HTTP_GET.header.CRLF-16",
    }

    def __init__(self, parent, list_op=False):
        super(HTTPGET, self).__init__(parent, list_op)

    @property
    def RequestRequestMethod(self):
        """
        Display Name: Request Method
        Default Value: 0x474554
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestRequest Method"])
        )

    @property
    def RequestSpace1(self):
        """
        Display Name: Space1
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RequestSpace1"]))

    @property
    def RequestRequestURI(self):
        """
        Display Name: Request URI
        Default Value: 0x2F646F776E6C6F61642E68746D6C
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestRequest URI"])
        )

    @property
    def RequestSpace2(self):
        """
        Display Name: Space2
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RequestSpace2"]))

    @property
    def RequestRequestversion(self):
        """
        Display Name: Request version
        Default Value: 0x485454502F312E31
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestRequest version"])
        )

    @property
    def RequestCRLF1(self):
        """
        Display Name: CRLF1
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RequestCRLF1"]))

    @property
    def HeaderHost(self):
        """
        Display Name: Host
        Default Value: 0x486F73743A207777772E657468657265616C2E636F6D0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderHost"]))

    @property
    def HeaderUserAgent(self):
        """
        Display Name: User-Agent
        Default Value: 0x557365722D4167656E743A204D6F7A696C6C612F352E30202857696E646F77733B20553B2057696E646F7773204E5420352E313B20656E2D55533B2072763A312E3629204765636B6F2F32303034303131330D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderUser-Agent"])
        )

    @property
    def HeaderAccept(self):
        """
        Display Name: Accept
        Default Value: 0x4163636570743A20746578742F786D6C2C6170706C69636174696F6E2F786D6C2C6170706C69636174696F6E2F7868746D6C2B786D6C2C746578742F68746D6C3B713D302E392C746578742F706C61696E3B713D302E382C696D6167652F706E672C696D6167652F6A7065672C696D6167652F6769663B713D302E322C2A2F2A3B713D302E310D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept"]))

    @property
    def HeaderAcceptLanguage(self):
        """
        Display Name: Accept-Language
        Default Value: 0x4163636570742D4C616E67756167653A20656E2D75732C656E3B713D302E350D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept-Language"])
        )

    @property
    def HeaderAcceptEncoding(self):
        """
        Display Name: Accept-Encoding
        Default Value: 0x4163636570742D456E636F64696E673A20677A69702C6465666C6174650D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept-Encoding"])
        )

    @property
    def HeaderAcceptCharset(self):
        """
        Display Name: Accept-Charset
        Default Value: 0x4163636570742D436861727365743A2049534F2D383835392D312C7574662D383B713D302E372C2A3B713D302E370D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept-Charset"])
        )

    @property
    def HeaderKeepAlive(self):
        """
        Display Name: Keep-Alive
        Default Value: 0x4B6565702D416C6976653A203330300D0A
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
        Default Value: 0x436F6E6E656374696F6E3A206B6565702D616C6976650D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderConnection"])
        )

    @property
    def HeaderReferer(self):
        """
        Display Name: Referer
        Default Value: 0x526566657265723A20687474703A2F2F7777772E657468657265616C2E636F6D2F646576656C6F706D656E742E68746D6C0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderReferer"]))

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
