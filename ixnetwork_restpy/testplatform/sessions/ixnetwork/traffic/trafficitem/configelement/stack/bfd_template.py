from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Bfd(Base):
    __slots__ = ()
    _SDM_NAME = "bfd"
    _SDM_ATT_MAP = {
        "HeaderVersion": "bfd.header.version-1",
        "HeaderDiagnostic": "bfd.header.diagnostic-2",
        "HeaderState": "bfd.header.state-3",
        "HeaderPollP": "bfd.header.pollP-4",
        "HeaderFinalF": "bfd.header.finalF-5",
        "HeaderControlPlaneIndependentC": "bfd.header.controlPlaneIndependentC-6",
        "HeaderAuthenticationA": "bfd.header.authenticationA-7",
        "HeaderDemandD": "bfd.header.demandD-8",
        "HeaderReserved": "bfd.header.reserved-9",
        "HeaderDetectTimeMultiplier": "bfd.header.detectTimeMultiplier-10",
        "HeaderLength": "bfd.header.length-11",
        "HeaderMyDiscriminator": "bfd.header.myDiscriminator-12",
        "HeaderYourDiscriminator": "bfd.header.yourDiscriminator-13",
        "HeaderDesiredMinTXInterval": "bfd.header.desiredMinTXInterval-14",
        "HeaderRequiredMinRXInterval": "bfd.header.requiredMinRXInterval-15",
        "HeaderRequiredMinEchoRXInterval": "bfd.header.requiredMinEchoRXInterval-16",
        "SimplePasswordType": "bfd.header.authenticationOption.withAuthentication.authentication.simplePassword.type-17",
        "SimplePasswordLength": "bfd.header.authenticationOption.withAuthentication.authentication.simplePassword.length-18",
        "SimplePasswordKeyID": "bfd.header.authenticationOption.withAuthentication.authentication.simplePassword.keyID-19",
        "SimplePasswordPasswordLengthoctets": "bfd.header.authenticationOption.withAuthentication.authentication.simplePassword.passwordLengthoctets-20",
        "SimplePasswordPassword": "bfd.header.authenticationOption.withAuthentication.authentication.simplePassword.password-21",
        "KeyedMD5Type": "bfd.header.authenticationOption.withAuthentication.authentication.keyedMD5.type-22",
        "KeyedMD5Length": "bfd.header.authenticationOption.withAuthentication.authentication.keyedMD5.length-23",
        "KeyedMD5KeyID": "bfd.header.authenticationOption.withAuthentication.authentication.keyedMD5.keyID-24",
        "KeyedMD5Reserved": "bfd.header.authenticationOption.withAuthentication.authentication.keyedMD5.reserved-25",
        "KeyedMD5SequenceNumber": "bfd.header.authenticationOption.withAuthentication.authentication.keyedMD5.sequenceNumber-26",
        "KeyedMD5Checksum": "bfd.header.authenticationOption.withAuthentication.authentication.keyedMD5.checksum-27",
        "MeticulousKeyedMD5Type": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedMD5.type-28",
        "MeticulousKeyedMD5Length": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedMD5.length-29",
        "MeticulousKeyedMD5KeyID": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedMD5.keyID-30",
        "MeticulousKeyedMD5Reserved": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedMD5.reserved-31",
        "MeticulousKeyedMD5SequenceNumber": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedMD5.sequenceNumber-32",
        "MeticulousKeyedMD5Checksum": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedMD5.checksum-33",
        "KeyedSHA1Type": "bfd.header.authenticationOption.withAuthentication.authentication.keyedSHA1.type-34",
        "KeyedSHA1Length": "bfd.header.authenticationOption.withAuthentication.authentication.keyedSHA1.length-35",
        "KeyedSHA1KeyID": "bfd.header.authenticationOption.withAuthentication.authentication.keyedSHA1.keyID-36",
        "KeyedSHA1Reserved": "bfd.header.authenticationOption.withAuthentication.authentication.keyedSHA1.reserved-37",
        "KeyedSHA1SequenceNumber": "bfd.header.authenticationOption.withAuthentication.authentication.keyedSHA1.sequenceNumber-38",
        "KeyedSHA1Checksum": "bfd.header.authenticationOption.withAuthentication.authentication.keyedSHA1.checksum-39",
        "MeticulousKeyedSHA1Type": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedSHA1.type-40",
        "MeticulousKeyedSHA1Length": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedSHA1.length-41",
        "MeticulousKeyedSHA1KeyID": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedSHA1.keyID-42",
        "MeticulousKeyedSHA1Reserved": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedSHA1.reserved-43",
        "MeticulousKeyedSHA1SequenceNumber": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedSHA1.sequenceNumber-44",
        "MeticulousKeyedSHA1Checksum": "bfd.header.authenticationOption.withAuthentication.authentication.meticulousKeyedSHA1.checksum-45",
        "AuthenticationOptionNoAuthentication": "bfd.header.authenticationOption.noAuthentication-46",
    }

    def __init__(self, parent, list_op=False):
        super(Bfd, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderDiagnostic(self):
        """
        Display Name: Diagnostic
        Default Value: 0
        Value Format: decimal
        Available enum values: No diagnostic, 0, Control detection time expired, 1, Echo function disabled, 2, Neighbor signaled session down, 3, Forwarding plane reset, 4, Path down, 5, Concatenated path down, 6, Administratively down, 7, Reverse Concatenated Path Down, 8
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDiagnostic"])
        )

    @property
    def HeaderState(self):
        """
        Display Name: State
        Default Value: 0
        Value Format: decimal
        Available enum values: AdmitDown, 0, Down, 1, Init, 2, Up, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderState"]))

    @property
    def HeaderPollP(self):
        """
        Display Name: Poll (P)
        Default Value: 0
        Value Format: decimal
        Available enum values: Request Connectivity Verification, 1, Not Requesting Verification, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderPollP"]))

    @property
    def HeaderFinalF(self):
        """
        Display Name: Final (F)
        Default Value: 0
        Value Format: decimal
        Available enum values: Responding to Poll, 1, Not Responding to Poll, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFinalF"]))

    @property
    def HeaderControlPlaneIndependentC(self):
        """
        Display Name: Control plane independent (C)
        Default Value: 1
        Value Format: decimal
        Available enum values: Does Not Share to Control Panel, 1, Sharing to Control Panel, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderControlPlaneIndependentC"]),
        )

    @property
    def HeaderAuthenticationA(self):
        """
        Display Name: Authentication (A)
        Default Value: 0
        Value Format: decimal
        Available enum values: Not to be Authenticated, 0, To be Authenticated, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderAuthenticationA"])
        )

    @property
    def HeaderDemandD(self):
        """
        Display Name: Demand (D)
        Default Value: 0
        Value Format: decimal
        Available enum values: Not in Demand Mode, 0, Demand Mode, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderDemandD"]))

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

    @property
    def HeaderDetectTimeMultiplier(self):
        """
        Display Name: Detect time multiplier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDetectTimeMultiplier"])
        )

    @property
    def HeaderLength(self):
        """
        Display Name: Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderLength"]))

    @property
    def HeaderMyDiscriminator(self):
        """
        Display Name: My discriminator
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMyDiscriminator"])
        )

    @property
    def HeaderYourDiscriminator(self):
        """
        Display Name: Your discriminator
        Default Value: 0x2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderYourDiscriminator"])
        )

    @property
    def HeaderDesiredMinTXInterval(self):
        """
        Display Name: Desired min TX interval
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDesiredMinTXInterval"])
        )

    @property
    def HeaderRequiredMinRXInterval(self):
        """
        Display Name: Required min RX interval
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRequiredMinRXInterval"])
        )

    @property
    def HeaderRequiredMinEchoRXInterval(self):
        """
        Display Name: Required min echo RX interval
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderRequiredMinEchoRXInterval"]),
        )

    @property
    def SimplePasswordType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SimplePasswordType"])
        )

    @property
    def SimplePasswordLength(self):
        """
        Display Name: Length
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SimplePasswordLength"])
        )

    @property
    def SimplePasswordKeyID(self):
        """
        Display Name: Key ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SimplePasswordKeyID"])
        )

    @property
    def SimplePasswordPasswordLengthoctets(self):
        """
        Display Name: Password length (octets)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SimplePasswordPasswordLengthoctets"]
            ),
        )

    @property
    def SimplePasswordPassword(self):
        """
        Display Name: Password
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SimplePasswordPassword"])
        )

    @property
    def KeyedMD5Type(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyedMD5Type"]))

    @property
    def KeyedMD5Length(self):
        """
        Display Name: Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedMD5Length"])
        )

    @property
    def KeyedMD5KeyID(self):
        """
        Display Name: Key ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyedMD5KeyID"]))

    @property
    def KeyedMD5Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedMD5Reserved"])
        )

    @property
    def KeyedMD5SequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedMD5SequenceNumber"])
        )

    @property
    def KeyedMD5Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedMD5Checksum"])
        )

    @property
    def MeticulousKeyedMD5Type(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedMD5Type"])
        )

    @property
    def MeticulousKeyedMD5Length(self):
        """
        Display Name: Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedMD5Length"])
        )

    @property
    def MeticulousKeyedMD5KeyID(self):
        """
        Display Name: Key ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedMD5KeyID"])
        )

    @property
    def MeticulousKeyedMD5Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedMD5Reserved"])
        )

    @property
    def MeticulousKeyedMD5SequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedMD5SequenceNumber"]),
        )

    @property
    def MeticulousKeyedMD5Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedMD5Checksum"])
        )

    @property
    def KeyedSHA1Type(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyedSHA1Type"]))

    @property
    def KeyedSHA1Length(self):
        """
        Display Name: Length
        Default Value: 28
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedSHA1Length"])
        )

    @property
    def KeyedSHA1KeyID(self):
        """
        Display Name: Key ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedSHA1KeyID"])
        )

    @property
    def KeyedSHA1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedSHA1Reserved"])
        )

    @property
    def KeyedSHA1SequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedSHA1SequenceNumber"])
        )

    @property
    def KeyedSHA1Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeyedSHA1Checksum"])
        )

    @property
    def MeticulousKeyedSHA1Type(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedSHA1Type"])
        )

    @property
    def MeticulousKeyedSHA1Length(self):
        """
        Display Name: Length
        Default Value: 28
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedSHA1Length"])
        )

    @property
    def MeticulousKeyedSHA1KeyID(self):
        """
        Display Name: Key ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedSHA1KeyID"])
        )

    @property
    def MeticulousKeyedSHA1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedSHA1Reserved"])
        )

    @property
    def MeticulousKeyedSHA1SequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedSHA1SequenceNumber"]),
        )

    @property
    def MeticulousKeyedSHA1Checksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeticulousKeyedSHA1Checksum"])
        )

    @property
    def AuthenticationOptionNoAuthentication(self):
        """
        Display Name: No Authentication
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AuthenticationOptionNoAuthentication"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
