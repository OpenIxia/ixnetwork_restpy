from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PppPAPCHAP(Base):
    __slots__ = ()
    _SDM_NAME = "pppPAPCHAP"
    _SDM_ATT_MAP = {
        "PapFieldsCode": "pppPAPCHAP.header.authenticationProtocol.papFields.code-1",
        "PapFieldsIdentifier": "pppPAPCHAP.header.authenticationProtocol.papFields.identifier-2",
        "PapFieldsLength": "pppPAPCHAP.header.authenticationProtocol.papFields.length-3",
        "AuthenticateRequestPeerIDLength": "pppPAPCHAP.header.authenticationProtocol.papFields.dataFields.authenticateRequest.peerIDLength-4",
        "AuthenticateRequestPeerID": "pppPAPCHAP.header.authenticationProtocol.papFields.dataFields.authenticateRequest.peerID-5",
        "AuthenticateRequestPasswordLength": "pppPAPCHAP.header.authenticationProtocol.papFields.dataFields.authenticateRequest.passwordLength-6",
        "AuthenticateRequestPassword": "pppPAPCHAP.header.authenticationProtocol.papFields.dataFields.authenticateRequest.password-7",
        "AuthenticateAckNackMessageLength": "pppPAPCHAP.header.authenticationProtocol.papFields.dataFields.authenticateAckNack.messageLength-8",
        "AuthenticateAckNackValue": "pppPAPCHAP.header.authenticationProtocol.papFields.dataFields.authenticateAckNack.value-9",
        "ChapFieldsCode": "pppPAPCHAP.header.authenticationProtocol.chapFields.code-10",
        "ChapFieldsIdentifier": "pppPAPCHAP.header.authenticationProtocol.chapFields.identifier-11",
        "ChapFieldsLength": "pppPAPCHAP.header.authenticationProtocol.chapFields.length-12",
        "ChallengeResponseValueLength": "pppPAPCHAP.header.authenticationProtocol.chapFields.dataFields.challengeResponse.valueLength-13",
        "ChallengeResponseValue": "pppPAPCHAP.header.authenticationProtocol.chapFields.dataFields.challengeResponse.value-14",
        "MessageMessageLength": "pppPAPCHAP.header.authenticationProtocol.chapFields.dataFields.message.messageLength-15",
        "MessageValue": "pppPAPCHAP.header.authenticationProtocol.chapFields.dataFields.message.value-16",
    }

    def __init__(self, parent, list_op=False):
        super(PppPAPCHAP, self).__init__(parent, list_op)

    @property
    def PapFieldsCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        Available enum values: Authenticate_Request, 1, Authenticate-Ack, 2, Authenticate-Nak, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PapFieldsCode"]))

    @property
    def PapFieldsIdentifier(self):
        """
        Display Name: Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PapFieldsIdentifier"])
        )

    @property
    def PapFieldsLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PapFieldsLength"])
        )

    @property
    def AuthenticateRequestPeerIDLength(self):
        """
        Display Name: Peer-ID Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticateRequestPeerIDLength"]),
        )

    @property
    def AuthenticateRequestPeerID(self):
        """
        Display Name: Peer-Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticateRequestPeerID"])
        )

    @property
    def AuthenticateRequestPasswordLength(self):
        """
        Display Name: Passwd-Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticateRequestPasswordLength"]),
        )

    @property
    def AuthenticateRequestPassword(self):
        """
        Display Name: Password
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticateRequestPassword"])
        )

    @property
    def AuthenticateAckNackMessageLength(self):
        """
        Display Name: Message Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticateAckNackMessageLength"]),
        )

    @property
    def AuthenticateAckNackValue(self):
        """
        Display Name: Message
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticateAckNackValue"])
        )

    @property
    def ChapFieldsCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        Available enum values: Challenge, 1, Response, 2, Success, 3, Failure, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChapFieldsCode"])
        )

    @property
    def ChapFieldsIdentifier(self):
        """
        Display Name: Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChapFieldsIdentifier"])
        )

    @property
    def ChapFieldsLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChapFieldsLength"])
        )

    @property
    def ChallengeResponseValueLength(self):
        """
        Display Name: Value-size
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChallengeResponseValueLength"])
        )

    @property
    def ChallengeResponseValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ChallengeResponseValue"])
        )

    @property
    def MessageMessageLength(self):
        """
        Display Name: Message Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageMessageLength"])
        )

    @property
    def MessageValue(self):
        """
        Display Name: Message
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MessageValue"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
