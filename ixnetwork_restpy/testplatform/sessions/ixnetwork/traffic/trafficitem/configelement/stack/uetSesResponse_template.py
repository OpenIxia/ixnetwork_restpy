from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UetSesResponse(Base):
    __slots__ = ()
    _SDM_NAME = "uetSesResponse"
    _SDM_ATT_MAP = {
        "UetDefaultResponseList": "uetSesResponse.header.sesResponseType.uetDefaultResponse.list-1",
        "UetDefaultResponseOpCode": "uetSesResponse.header.sesResponseType.uetDefaultResponse.opCode-2",
        "UetDefaultResponseVersion": "uetSesResponse.header.sesResponseType.uetDefaultResponse.version-3",
        "UetDefaultResponseReturnCode": "uetSesResponse.header.sesResponseType.uetDefaultResponse.returnCode-4",
        "UetDefaultResponseMessageId": "uetSesResponse.header.sesResponseType.uetDefaultResponse.messageId-5",
        "UetDefaultResponseRiGeneration": "uetSesResponse.header.sesResponseType.uetDefaultResponse.riGeneration-6",
        "UetDefaultResponseJobId": "uetSesResponse.header.sesResponseType.uetDefaultResponse.jobId-7",
        "UetDefaultResponseModifiedLength": "uetSesResponse.header.sesResponseType.uetDefaultResponse.modifiedLength-8",
        "UetNoResponseList": "uetSesResponse.header.sesResponseType.uetNoResponse.list-9",
        "UetNoResponseOpCode": "uetSesResponse.header.sesResponseType.uetNoResponse.opCode-10",
        "UetNoResponseVersion": "uetSesResponse.header.sesResponseType.uetNoResponse.version-11",
        "UetNoResponseReturnCode": "uetSesResponse.header.sesResponseType.uetNoResponse.returnCode-12",
        "UetNoResponseMessageId": "uetSesResponse.header.sesResponseType.uetNoResponse.messageId-13",
        "UetNoResponseRiGeneration": "uetSesResponse.header.sesResponseType.uetNoResponse.riGeneration-14",
        "UetNoResponseJobId": "uetSesResponse.header.sesResponseType.uetNoResponse.jobId-15",
        "UetNoResponseModifiedLength": "uetSesResponse.header.sesResponseType.uetNoResponse.modifiedLength-16",
    }

    def __init__(self, parent, list_op=False):
        super(UetSesResponse, self).__init__(parent, list_op)

    @property
    def UetDefaultResponseList(self):
        """
        Display Name: List
        Default Value: 0
        Value Format: decimal
        Available enum values: UET_EXPECTED, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseList"])
        )

    @property
    def UetDefaultResponseOpCode(self):
        """
        Display Name: Op Code
        Default Value: 0
        Value Format: decimal
        Available enum values: UET_DEFAULT_RESPONSE, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseOpCode"])
        )

    @property
    def UetDefaultResponseVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseVersion"])
        )

    @property
    def UetDefaultResponseReturnCode(self):
        """
        Display Name: Return Code
        Default Value: 0
        Value Format: decimal
        Available enum values: RC_NULL, 0, RC_OK, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseReturnCode"])
        )

    @property
    def UetDefaultResponseMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseMessageId"])
        )

    @property
    def UetDefaultResponseRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseRiGeneration"]),
        )

    @property
    def UetDefaultResponseJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseJobId"])
        )

    @property
    def UetDefaultResponseModifiedLength(self):
        """
        Display Name: Modified Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["UetDefaultResponseModifiedLength"]),
        )

    @property
    def UetNoResponseList(self):
        """
        Display Name: List
        Default Value: 0
        Value Format: decimal
        Available enum values: UET_EXPECTED, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseList"])
        )

    @property
    def UetNoResponseOpCode(self):
        """
        Display Name: Op Code
        Default Value: 3
        Value Format: decimal
        Available enum values: UET_NO_RESPONSE, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseOpCode"])
        )

    @property
    def UetNoResponseVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseVersion"])
        )

    @property
    def UetNoResponseReturnCode(self):
        """
        Display Name: Return Code
        Default Value: 0
        Value Format: decimal
        Available enum values: RC_NULL, 0, RC_OK, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseReturnCode"])
        )

    @property
    def UetNoResponseMessageId(self):
        """
        Display Name: Message Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseMessageId"])
        )

    @property
    def UetNoResponseRiGeneration(self):
        """
        Display Name: Ri Generation
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseRiGeneration"])
        )

    @property
    def UetNoResponseJobId(self):
        """
        Display Name: Job Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseJobId"])
        )

    @property
    def UetNoResponseModifiedLength(self):
        """
        Display Name: Modified Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UetNoResponseModifiedLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
