from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv2DatabaseDescription(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv2DatabaseDescription"
    _SDM_ATT_MAP = {
        "Ospfv2PacketHeaderOspfVersion": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.ospfVersion-1",
        "Ospfv2PacketHeaderPacketType": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.packetType-2",
        "Ospfv2PacketHeaderPacketLength": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.packetLength-3",
        "Ospfv2PacketHeaderRouterID": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.routerID-4",
        "Ospfv2PacketHeaderAreaID": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.areaID-5",
        "Ospfv2PacketHeaderChecksum": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.checksum-6",
        "Ospfv2PacketHeaderAuthenticationType": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationType-7",
        "AuthenticationDataNullAuthentication": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationData.nullAuthentication-8",
        "AuthenticationDataSimplePassword": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationData.simplePassword-9",
        "CryptographicAuthenticationDataReserved": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.reserved-10",
        "CryptographicAuthenticationDataKeyID": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.keyID-11",
        "CryptographicAuthenticationDataAuthenticationDataLength": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.authenticationDataLength-12",
        "CryptographicAuthenticationDataCryptographicSequenceNumber": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.cryptographicSequenceNumber-13",
        "UserDefinedAuthenticationDataUserDefinedAuthData": "ospfv2DatabaseDescription.header.ospfv2PacketHeader.authenticationData.userDefinedAuthenticationData.userDefinedAuthData-14",
        "DatabaseDescriptionBodyInterfaceMTU": "ospfv2DatabaseDescription.header.databaseDescriptionBody.interfaceMTU-15",
        "DatabaseDescriptionBodyOptions": "ospfv2DatabaseDescription.header.databaseDescriptionBody.options-16",
        "DatabaseDescriptionBodyReserved": "ospfv2DatabaseDescription.header.databaseDescriptionBody.reserved-17",
        "DatabaseDescriptionBodyDatabaseDescriptionFlags": "ospfv2DatabaseDescription.header.databaseDescriptionBody.databaseDescriptionFlags-18",
        "DatabaseDescriptionBodyDdSequenceNumber": "ospfv2DatabaseDescription.header.databaseDescriptionBody.ddSequenceNumber-19",
        "VariableHeaderLinkStateAge": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.linkStateAge-20",
        "VariableHeaderOptions": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.options-21",
        "VariableHeaderLinkStateType": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.linkStateType-22",
        "VariableHeaderLinkStateID": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.linkStateID-23",
        "VariableHeaderLinkStateAdvertisingRouter": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.linkStateAdvertisingRouter-24",
        "VariableHeaderLinkStateSequenceNumber": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.linkStateSequenceNumber-25",
        "VariableHeaderLinkStateChecksum": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.linkStateChecksum-26",
        "VariableHeaderLinkStateLength": "ospfv2DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.variableHeader.linkStateLength-27",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv2DatabaseDescription, self).__init__(parent, list_op)

    @property
    def Ospfv2PacketHeaderOspfVersion(self):
        """
        Display Name: OSPF Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderOspfVersion"]),
        )

    @property
    def Ospfv2PacketHeaderPacketType(self):
        """
        Display Name: Packet Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderPacketType"])
        )

    @property
    def Ospfv2PacketHeaderPacketLength(self):
        """
        Display Name: Packet length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderPacketLength"]),
        )

    @property
    def Ospfv2PacketHeaderRouterID(self):
        """
        Display Name: Router ID
        Default Value: 1.1.1.1
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderRouterID"])
        )

    @property
    def Ospfv2PacketHeaderAreaID(self):
        """
        Display Name: Area ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderAreaID"])
        )

    @property
    def Ospfv2PacketHeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderChecksum"])
        )

    @property
    def Ospfv2PacketHeaderAuthenticationType(self):
        """
        Display Name: Authentication type
        Default Value: 0
        Value Format: decimal
        Available enum values: Null authentication, 0, Simple password, 1, Cryptographic Authentication, 2, User defined Authentication, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ospfv2PacketHeaderAuthenticationType"]
            ),
        )

    @property
    def AuthenticationDataNullAuthentication(self):
        """
        Display Name: Null authentication
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AuthenticationDataNullAuthentication"]
            ),
        )

    @property
    def AuthenticationDataSimplePassword(self):
        """
        Display Name: Simple password
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticationDataSimplePassword"]),
        )

    @property
    def CryptographicAuthenticationDataReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CryptographicAuthenticationDataReserved"]
            ),
        )

    @property
    def CryptographicAuthenticationDataKeyID(self):
        """
        Display Name: Key ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CryptographicAuthenticationDataKeyID"]
            ),
        )

    @property
    def CryptographicAuthenticationDataAuthenticationDataLength(self):
        """
        Display Name: Authentication data length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CryptographicAuthenticationDataAuthenticationDataLength"
                ]
            ),
        )

    @property
    def CryptographicAuthenticationDataCryptographicSequenceNumber(self):
        """
        Display Name: Cryptographic sequence number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CryptographicAuthenticationDataCryptographicSequenceNumber"
                ]
            ),
        )

    @property
    def UserDefinedAuthenticationDataUserDefinedAuthData(self):
        """
        Display Name: User defined Auth Data
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UserDefinedAuthenticationDataUserDefinedAuthData"]
            ),
        )

    @property
    def DatabaseDescriptionBodyInterfaceMTU(self):
        """
        Display Name: Interface MTU
        Default Value: 1492
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DatabaseDescriptionBodyInterfaceMTU"]
            ),
        )

    @property
    def DatabaseDescriptionBodyOptions(self):
        """
        Display Name: Options
        Default Value: 0x42
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DatabaseDescriptionBodyOptions"]),
        )

    @property
    def DatabaseDescriptionBodyReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DatabaseDescriptionBodyReserved"]),
        )

    @property
    def DatabaseDescriptionBodyDatabaseDescriptionFlags(self):
        """
        Display Name: Database Description flags
        Default Value: 0x7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DatabaseDescriptionBodyDatabaseDescriptionFlags"]
            ),
        )

    @property
    def DatabaseDescriptionBodyDdSequenceNumber(self):
        """
        Display Name: DD sequence number
        Default Value: 1108552800
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DatabaseDescriptionBodyDdSequenceNumber"]
            ),
        )

    @property
    def VariableHeaderLinkStateAge(self):
        """
        Display Name: Link-State age
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateAge"])
        )

    @property
    def VariableHeaderOptions(self):
        """
        Display Name: Options
        Default Value: 0x42
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderOptions"])
        )

    @property
    def VariableHeaderLinkStateType(self):
        """
        Display Name: Link-State type
        Default Value: 1
        Value Format: decimal
        Available enum values: Router LSA, 1, Network LSA, 2, Summary LSA, Routers to Networks, 3, Summary LSA, Routers to AS Boundary, 4, AS-External-LSA, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateType"])
        )

    @property
    def VariableHeaderLinkStateID(self):
        """
        Display Name: Link-State ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateID"])
        )

    @property
    def VariableHeaderLinkStateAdvertisingRouter(self):
        """
        Display Name: Link-State advertising router
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VariableHeaderLinkStateAdvertisingRouter"]
            ),
        )

    @property
    def VariableHeaderLinkStateSequenceNumber(self):
        """
        Display Name: Link-State Sequence Number
        Default Value: 0x80000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VariableHeaderLinkStateSequenceNumber"]
            ),
        )

    @property
    def VariableHeaderLinkStateChecksum(self):
        """
        Display Name: Link-State checksum
        Default Value: 0x1234
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateChecksum"]),
        )

    @property
    def VariableHeaderLinkStateLength(self):
        """
        Display Name: Link-State length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateLength"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
