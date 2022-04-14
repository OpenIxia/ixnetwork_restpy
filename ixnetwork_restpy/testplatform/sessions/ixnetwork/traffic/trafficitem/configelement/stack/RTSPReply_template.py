from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTSPReply(Base):
    __slots__ = ()
    _SDM_NAME = "RTSP_Reply"
    _SDM_ATT_MAP = {
        "RESPONSEField0": "RTSP_Reply.header.RESPONSE.field0-1",
        "RESPONSESP": "RTSP_Reply.header.RESPONSE.SP-2",
        "RESPONSERTSP STATUS CODE": "RTSP_Reply.header.RESPONSE.RTSP STATUS CODE-3",
        "RESPONSESP1": "RTSP_Reply.header.RESPONSE.SP1-4",
        "RESPONSEREASON-PHRASE": "RTSP_Reply.header.RESPONSE.REASON-PHRASE-5",
        "RESPONSECRLF": "RTSP_Reply.header.RESPONSE.CRLF-6",
        "HeaderDATE": "RTSP_Reply.header.DATE-7",
        "HeaderCSeq": "RTSP_Reply.header.CSeq-8",
        "HeaderServer": "RTSP_Reply.header.Server-9",
        "HeaderSupported": "RTSP_Reply.header.Supported-10",
        "HeaderCRLFX": "RTSP_Reply.header.CRLFX-11",
    }

    def __init__(self, parent, list_op=False):
        super(RTSPReply, self).__init__(parent, list_op)

    @property
    def RESPONSEField0(self):
        """
        Display Name: RTSP VERSION
        Default Value: 0x525453502F312E30
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSEField0"])
        )

    @property
    def RESPONSESP(self):
        """
        Display Name: SP
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RESPONSESP"]))

    @property
    def RESPONSERTSPSTATUSCODE(self):
        """
        Display Name: RTSP STATUS CODE
        Default Value: 0x353030
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSERTSP STATUS CODE"])
        )

    @property
    def RESPONSESP1(self):
        """
        Display Name: SP1
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RESPONSESP1"]))

    @property
    def RESPONSEREASONPHRASE(self):
        """
        Display Name: REASON-PHRASE
        Default Value: 0x496E7465726E616C20536572766572204572726F72
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RESPONSEREASON-PHRASE"])
        )

    @property
    def RESPONSECRLF(self):
        """
        Display Name: CRLF
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RESPONSECRLF"]))

    @property
    def HeaderDATE(self):
        """
        Display Name: DATE
        Default Value: 0x446174653A2053756E2C203033204A756C20323030352031303A35323A353320474D540D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDATE"]))

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
    def HeaderServer(self):
        """
        Display Name: Server
        Default Value: 0x5365727665723A20574D5365727665722F392E302E302E333338300D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderServer"]))

    @property
    def HeaderSupported(self):
        """
        Display Name: Supported
        Default Value: 0x537570706F727465643A20636F6D2E6D6963726F736F66742E776D2E73727670706169722C20636F6D2E6D6963726F736F66742E776D2E737377697463682C20636F6D2E6D6963726F736F66742E776D2E656F736D73672C20636F6D2E6D6963726F736F66742E776D2E6661737463616368652C20636F6D2E6D6963726F736F66742E776D2E7061636B657470616972737372630D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSupported"])
        )

    @property
    def HeaderCRLFX(self):
        """
        Display Name: CRLFX
        Default Value: 0x0D0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCRLFX"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
