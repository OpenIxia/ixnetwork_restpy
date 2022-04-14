from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MobileIP(Base):
    __slots__ = ()
    _SDM_NAME = "mobileIP"
    _SDM_ATT_MAP = {
        "RegistrationRequestType": "mobileIP.header.packetType.registrationRequest.type-1",
        "RegistrationRequestSBit": "mobileIP.header.packetType.registrationRequest.sBit-2",
        "RegistrationRequestBBit": "mobileIP.header.packetType.registrationRequest.bBit-3",
        "RegistrationRequestDBit": "mobileIP.header.packetType.registrationRequest.dBit-4",
        "RegistrationRequestMBit": "mobileIP.header.packetType.registrationRequest.mBit-5",
        "RegistrationRequestGBit": "mobileIP.header.packetType.registrationRequest.gBit-6",
        "RegistrationRequestRBit": "mobileIP.header.packetType.registrationRequest.rBit-7",
        "RegistrationRequestTBit": "mobileIP.header.packetType.registrationRequest.tBit-8",
        "RegistrationRequestXBit": "mobileIP.header.packetType.registrationRequest.xBit-9",
        "RegistrationRequestLifetime": "mobileIP.header.packetType.registrationRequest.lifetime-10",
        "RegistrationRequestHomeAddress": "mobileIP.header.packetType.registrationRequest.homeAddress-11",
        "RegistrationRequestHomeAgent": "mobileIP.header.packetType.registrationRequest.homeAgent-12",
        "RegistrationRequestCareOfAddress": "mobileIP.header.packetType.registrationRequest.careOfAddress-13",
        "RegistrationRequestIdentification": "mobileIP.header.packetType.registrationRequest.identification-14",
        "MobileHomeAuthenticationType": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileHomeAuthentication.type-15",
        "MobileHomeAuthenticationLength": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileHomeAuthentication.length-16",
        "MobileHomeAuthenticationSpi": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileHomeAuthentication.spi-17",
        "MobileHomeAuthenticationAuthenticatorLength": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileHomeAuthentication.authenticatorLength-18",
        "MobileHomeAuthenticationAuthenticator": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileHomeAuthentication.authenticator-19",
        "MobileForeignAuthenticationType": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileForeignAuthentication.type-20",
        "MobileForeignAuthenticationLength": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileForeignAuthentication.length-21",
        "MobileForeignAuthenticationSpi": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileForeignAuthentication.spi-22",
        "MobileForeignAuthenticationAuthenticatorLength": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileForeignAuthentication.authenticatorLength-23",
        "MobileForeignAuthenticationAuthenticator": "mobileIP.header.packetType.registrationRequest.tlv.option.mobileForeignAuthentication.authenticator-24",
        "ForeignHomeAuthenticationType": "mobileIP.header.packetType.registrationRequest.tlv.option.foreignHomeAuthentication.type-25",
        "ForeignHomeAuthenticationLength": "mobileIP.header.packetType.registrationRequest.tlv.option.foreignHomeAuthentication.length-26",
        "ForeignHomeAuthenticationSpi": "mobileIP.header.packetType.registrationRequest.tlv.option.foreignHomeAuthentication.spi-27",
        "ForeignHomeAuthenticationAuthenticatorLength": "mobileIP.header.packetType.registrationRequest.tlv.option.foreignHomeAuthentication.authenticatorLength-28",
        "ForeignHomeAuthenticationAuthenticator": "mobileIP.header.packetType.registrationRequest.tlv.option.foreignHomeAuthentication.authenticator-29",
        "RegistrationReplyType": "mobileIP.header.packetType.registrationReply.type-30",
        "RegistrationReplyCode": "mobileIP.header.packetType.registrationReply.code-31",
        "RegistrationReplyLifetime": "mobileIP.header.packetType.registrationReply.lifetime-32",
        "RegistrationReplyHomeAddress": "mobileIP.header.packetType.registrationReply.homeAddress-33",
        "RegistrationReplyHomeAgent": "mobileIP.header.packetType.registrationReply.homeAgent-34",
        "RegistrationReplyIdentification": "mobileIP.header.packetType.registrationReply.identification-35",
        "OptionMobileHomeAuthenticationType": "mobileIP.header.packetType.registrationReply.tlv.option.mobileHomeAuthentication.type-36",
        "OptionMobileHomeAuthenticationLength": "mobileIP.header.packetType.registrationReply.tlv.option.mobileHomeAuthentication.length-37",
        "OptionMobileHomeAuthenticationSpi": "mobileIP.header.packetType.registrationReply.tlv.option.mobileHomeAuthentication.spi-38",
        "OptionMobileHomeAuthenticationAuthenticatorLength": "mobileIP.header.packetType.registrationReply.tlv.option.mobileHomeAuthentication.authenticatorLength-39",
        "OptionMobileHomeAuthenticationAuthenticator": "mobileIP.header.packetType.registrationReply.tlv.option.mobileHomeAuthentication.authenticator-40",
        "OptionMobileForeignAuthenticationType": "mobileIP.header.packetType.registrationReply.tlv.option.mobileForeignAuthentication.type-41",
        "OptionMobileForeignAuthenticationLength": "mobileIP.header.packetType.registrationReply.tlv.option.mobileForeignAuthentication.length-42",
        "OptionMobileForeignAuthenticationSpi": "mobileIP.header.packetType.registrationReply.tlv.option.mobileForeignAuthentication.spi-43",
        "OptionMobileForeignAuthenticationAuthenticatorLength": "mobileIP.header.packetType.registrationReply.tlv.option.mobileForeignAuthentication.authenticatorLength-44",
        "OptionMobileForeignAuthenticationAuthenticator": "mobileIP.header.packetType.registrationReply.tlv.option.mobileForeignAuthentication.authenticator-45",
        "OptionForeignHomeAuthenticationType": "mobileIP.header.packetType.registrationReply.tlv.option.foreignHomeAuthentication.type-46",
        "OptionForeignHomeAuthenticationLength": "mobileIP.header.packetType.registrationReply.tlv.option.foreignHomeAuthentication.length-47",
        "OptionForeignHomeAuthenticationSpi": "mobileIP.header.packetType.registrationReply.tlv.option.foreignHomeAuthentication.spi-48",
        "OptionForeignHomeAuthenticationAuthenticatorLength": "mobileIP.header.packetType.registrationReply.tlv.option.foreignHomeAuthentication.authenticatorLength-49",
        "OptionForeignHomeAuthenticationAuthenticator": "mobileIP.header.packetType.registrationReply.tlv.option.foreignHomeAuthentication.authenticator-50",
    }

    def __init__(self, parent, list_op=False):
        super(MobileIP, self).__init__(parent, list_op)

    @property
    def RegistrationRequestType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestType"])
        )

    @property
    def RegistrationRequestSBit(self):
        """
        Display Name: S
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestSBit"])
        )

    @property
    def RegistrationRequestBBit(self):
        """
        Display Name: B
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestBBit"])
        )

    @property
    def RegistrationRequestDBit(self):
        """
        Display Name: D
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestDBit"])
        )

    @property
    def RegistrationRequestMBit(self):
        """
        Display Name: M
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestMBit"])
        )

    @property
    def RegistrationRequestGBit(self):
        """
        Display Name: G
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestGBit"])
        )

    @property
    def RegistrationRequestRBit(self):
        """
        Display Name: r
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestRBit"])
        )

    @property
    def RegistrationRequestTBit(self):
        """
        Display Name: T
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestTBit"])
        )

    @property
    def RegistrationRequestXBit(self):
        """
        Display Name: x
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestXBit"])
        )

    @property
    def RegistrationRequestLifetime(self):
        """
        Display Name: LifeTime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestLifetime"])
        )

    @property
    def RegistrationRequestHomeAddress(self):
        """
        Display Name: Home Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestHomeAddress"]),
        )

    @property
    def RegistrationRequestHomeAgent(self):
        """
        Display Name: Home Agent
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestHomeAgent"])
        )

    @property
    def RegistrationRequestCareOfAddress(self):
        """
        Display Name: Care-of Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestCareOfAddress"]),
        )

    @property
    def RegistrationRequestIdentification(self):
        """
        Display Name: Identification
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RegistrationRequestIdentification"]),
        )

    @property
    def MobileHomeAuthenticationType(self):
        """
        Display Name: Type
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileHomeAuthenticationType"])
        )

    @property
    def MobileHomeAuthenticationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileHomeAuthenticationLength"]),
        )

    @property
    def MobileHomeAuthenticationSpi(self):
        """
        Display Name: SPI
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileHomeAuthenticationSpi"])
        )

    @property
    def MobileHomeAuthenticationAuthenticatorLength(self):
        """
        Display Name: Authenticator Length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobileHomeAuthenticationAuthenticatorLength"]
            ),
        )

    @property
    def MobileHomeAuthenticationAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobileHomeAuthenticationAuthenticator"]
            ),
        )

    @property
    def MobileForeignAuthenticationType(self):
        """
        Display Name: Type
        Default Value: 33
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileForeignAuthenticationType"]),
        )

    @property
    def MobileForeignAuthenticationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileForeignAuthenticationLength"]),
        )

    @property
    def MobileForeignAuthenticationSpi(self):
        """
        Display Name: SPI
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MobileForeignAuthenticationSpi"]),
        )

    @property
    def MobileForeignAuthenticationAuthenticatorLength(self):
        """
        Display Name: Authenticator Length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobileForeignAuthenticationAuthenticatorLength"]
            ),
        )

    @property
    def MobileForeignAuthenticationAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MobileForeignAuthenticationAuthenticator"]
            ),
        )

    @property
    def ForeignHomeAuthenticationType(self):
        """
        Display Name: Type
        Default Value: 34
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ForeignHomeAuthenticationType"]),
        )

    @property
    def ForeignHomeAuthenticationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ForeignHomeAuthenticationLength"]),
        )

    @property
    def ForeignHomeAuthenticationSpi(self):
        """
        Display Name: SPI
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ForeignHomeAuthenticationSpi"])
        )

    @property
    def ForeignHomeAuthenticationAuthenticatorLength(self):
        """
        Display Name: Authenticator Length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ForeignHomeAuthenticationAuthenticatorLength"]
            ),
        )

    @property
    def ForeignHomeAuthenticationAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ForeignHomeAuthenticationAuthenticator"]
            ),
        )

    @property
    def RegistrationReplyType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationReplyType"])
        )

    @property
    def RegistrationReplyCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        Available enum values: Registration accepted, 0, Registration accepted, but simultaneous mobility bindings unsupported, 1, Reason unspecified, 64, Administratively prohibited, 65, Insufficient resources, 66, Mobile node failed authentication, 67, Home agent failed authentication, 68, Requested Lifetime too long, 69, Poorly formed Request, 70, Poorly formed Reply, 71, Requested encapsulation unavailable, 72, Reserved and unavailable, 73, Invalid care-of address, 77, Registration timeout, 78, Home network unreachable (ICMP error received), 80, Home agent host unreachable (ICMP error received), 81, Home agent port unreachable (ICMP error received), 82, Home agent unreachable (other ICMP error received), 88, Reason unspecified, 128, Administratively prohibited, 129, Insufficient resources, 130, Mobile node failed authentication, 131, Foreign agent failed authentication, 132, Registration Identification mismatch, 133, Poorly formed Request, 134, Too many simultaneous mobility bindings, 135, Unknown home agent address, 136
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationReplyCode"])
        )

    @property
    def RegistrationReplyLifetime(self):
        """
        Display Name: LifeTime
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationReplyLifetime"])
        )

    @property
    def RegistrationReplyHomeAddress(self):
        """
        Display Name: Home Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationReplyHomeAddress"])
        )

    @property
    def RegistrationReplyHomeAgent(self):
        """
        Display Name: Home Agent
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RegistrationReplyHomeAgent"])
        )

    @property
    def RegistrationReplyIdentification(self):
        """
        Display Name: Identification
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RegistrationReplyIdentification"]),
        )

    @property
    def OptionMobileHomeAuthenticationType(self):
        """
        Display Name: Type
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileHomeAuthenticationType"]
            ),
        )

    @property
    def OptionMobileHomeAuthenticationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileHomeAuthenticationLength"]
            ),
        )

    @property
    def OptionMobileHomeAuthenticationSpi(self):
        """
        Display Name: SPI
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OptionMobileHomeAuthenticationSpi"]),
        )

    @property
    def OptionMobileHomeAuthenticationAuthenticatorLength(self):
        """
        Display Name: Authenticator Length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileHomeAuthenticationAuthenticatorLength"]
            ),
        )

    @property
    def OptionMobileHomeAuthenticationAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileHomeAuthenticationAuthenticator"]
            ),
        )

    @property
    def OptionMobileForeignAuthenticationType(self):
        """
        Display Name: Type
        Default Value: 33
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileForeignAuthenticationType"]
            ),
        )

    @property
    def OptionMobileForeignAuthenticationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileForeignAuthenticationLength"]
            ),
        )

    @property
    def OptionMobileForeignAuthenticationSpi(self):
        """
        Display Name: SPI
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileForeignAuthenticationSpi"]
            ),
        )

    @property
    def OptionMobileForeignAuthenticationAuthenticatorLength(self):
        """
        Display Name: Authenticator Length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "OptionMobileForeignAuthenticationAuthenticatorLength"
                ]
            ),
        )

    @property
    def OptionMobileForeignAuthenticationAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionMobileForeignAuthenticationAuthenticator"]
            ),
        )

    @property
    def OptionForeignHomeAuthenticationType(self):
        """
        Display Name: Type
        Default Value: 34
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionForeignHomeAuthenticationType"]
            ),
        )

    @property
    def OptionForeignHomeAuthenticationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionForeignHomeAuthenticationLength"]
            ),
        )

    @property
    def OptionForeignHomeAuthenticationSpi(self):
        """
        Display Name: SPI
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionForeignHomeAuthenticationSpi"]
            ),
        )

    @property
    def OptionForeignHomeAuthenticationAuthenticatorLength(self):
        """
        Display Name: Authenticator Length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionForeignHomeAuthenticationAuthenticatorLength"]
            ),
        )

    @property
    def OptionForeignHomeAuthenticationAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionForeignHomeAuthenticationAuthenticator"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
