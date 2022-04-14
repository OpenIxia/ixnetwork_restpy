from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTSPDESCRIBE(Base):
    __slots__ = ()
    _SDM_NAME = "RTSP_DESCRIBE"
    _SDM_ATT_MAP = {
        "REQUESTREQUEST METHOD": "RTSP_DESCRIBE.header.REQUEST.REQUEST METHOD-1",
        "REQUESTSP": "RTSP_DESCRIBE.header.REQUEST.SP-2",
        "REQUESTREQUEST URI": "RTSP_DESCRIBE.header.REQUEST.REQUEST URI-3",
        "REQUESTSpace1": "RTSP_DESCRIBE.header.REQUEST.Space1-4",
        "REQUESTField1": "RTSP_DESCRIBE.header.REQUEST.field1-5",
        "REQUESTCRLF": "RTSP_DESCRIBE.header.REQUEST.CRLF-6",
        "HeaderUser-Agent": "RTSP_DESCRIBE.header.User-Agent-7",
        "HeaderAccept": "RTSP_DESCRIBE.header.Accept-8",
        "HeaderAccept-Charset": "RTSP_DESCRIBE.header.Accept-Charset-9",
        "HeaderX-Accept-Authentication": "RTSP_DESCRIBE.header.X-Accept-Authentication-10",
        "HeaderAccept-Language": "RTSP_DESCRIBE.header.Accept-Language-11",
        "HeaderCSeq": "RTSP_DESCRIBE.header.CSeq-12",
        "HeaderSupported": "RTSP_DESCRIBE.header.Supported-13",
        "HeaderCRLF": "RTSP_DESCRIBE.header.CRLF-14",
    }

    def __init__(self, parent, list_op=False):
        super(RTSPDESCRIBE, self).__init__(parent, list_op)

    @property
    def REQUESTREQUESTMETHOD(self):
        """
        Display Name: REQUEST METHOD
        Default Value: 0x4445534352494245
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTREQUEST METHOD"])
        )

    @property
    def REQUESTSP(self):
        """
        Display Name: SP
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["REQUESTSP"]))

    @property
    def REQUESTREQUESTURI(self):
        """
        Display Name: REQUEST URI
        Default Value: 0x727473703A2F2F454D4150312E706C616E657477696465726164696F2E636F6D2F74666D
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["REQUESTREQUEST URI"])
        )

    @property
    def REQUESTSpace1(self):
        """
        Display Name: Space1
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["REQUESTSpace1"]))

    @property
    def REQUESTField1(self):
        """
        Display Name: REQUEST VERSION
        Default Value: 0x525453502F312E30
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["REQUESTField1"]))

    @property
    def REQUESTCRLF(self):
        """
        Display Name: CRLF
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["REQUESTCRLF"]))

    @property
    def HeaderUserAgent(self):
        """
        Display Name: User-Agent
        Default Value: 0x557365722D4167656E743A20574D506C617965722F31302E302E302E33383020677569642F37343035453134332D323641432D344233372D393830322D4133354545384336434641370D0A
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
        Default Value: 0x4163636570743A206170706C69636174696F6E2F7364700D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept"]))

    @property
    def HeaderAcceptCharset(self):
        """
        Display Name: Accept-Charset
        Default Value: 0x4163636570742D436861727365743A205554462D382C202A3B713D302E310D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept-Charset"])
        )

    @property
    def HeaderXAcceptAuthentication(self):
        """
        Display Name: X-Accept-Authentication
        Default Value: 0x582D4163636570742D41757468656E7469636174696F6E3A204E65676F74696174652C204E544C4D2C204469676573742C2042617369630D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderX-Accept-Authentication"]),
        )

    @property
    def HeaderAcceptLanguage(self):
        """
        Display Name: Accept-Language
        Default Value: 0x4163636570742D4C616E67756167653A20656E2D47422C202A3B713D302E310D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAccept-Language"])
        )

    @property
    def HeaderCSeq(self):
        """
        Display Name: CSeq
        Default Value: 0x435365713A20310D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCSeq"]))

    @property
    def HeaderSupported(self):
        """
        Display Name: Supported
        Default Value: 0x537570706F727465643A20636F6D2E6D6963726F736F66742E776D2E73727670706169722C20636F6D2E6D6963726F736F66742E776D2E737377697463682C20636F6D2E6D6963726F736F66742E776D2E656F736D73672C20636F6D2E6D6963726F736F66742E776D2E707265647374726D2C20636F6D2E6D6963726F736F66742E776D2E7374617274757070726F66696C650D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSupported"])
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
