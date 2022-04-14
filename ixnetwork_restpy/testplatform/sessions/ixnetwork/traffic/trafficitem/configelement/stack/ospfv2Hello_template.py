from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv2Hello(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv2Hello"
    _SDM_ATT_MAP = {
        "Ospfv2PacketHeaderOspfVersion": "ospfv2Hello.header.ospfv2PacketHeader.ospfVersion-1",
        "Ospfv2PacketHeaderPacketType": "ospfv2Hello.header.ospfv2PacketHeader.packetType-2",
        "Ospfv2PacketHeaderPacketLength": "ospfv2Hello.header.ospfv2PacketHeader.packetLength-3",
        "Ospfv2PacketHeaderRouterID": "ospfv2Hello.header.ospfv2PacketHeader.routerID-4",
        "Ospfv2PacketHeaderAreaID": "ospfv2Hello.header.ospfv2PacketHeader.areaID-5",
        "Ospfv2PacketHeaderChecksum": "ospfv2Hello.header.ospfv2PacketHeader.checksum-6",
        "Ospfv2PacketHeaderAuthenticationType": "ospfv2Hello.header.ospfv2PacketHeader.authenticationType-7",
        "AuthenticationDataNullAuthentication": "ospfv2Hello.header.ospfv2PacketHeader.authenticationData.nullAuthentication-8",
        "AuthenticationDataSimplePassword": "ospfv2Hello.header.ospfv2PacketHeader.authenticationData.simplePassword-9",
        "CryptographicAuthenticationDataReserved": "ospfv2Hello.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.reserved-10",
        "CryptographicAuthenticationDataKeyID": "ospfv2Hello.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.keyID-11",
        "CryptographicAuthenticationDataAuthenticationDataLength": "ospfv2Hello.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.authenticationDataLength-12",
        "CryptographicAuthenticationDataCryptographicSequenceNumber": "ospfv2Hello.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.cryptographicSequenceNumber-13",
        "UserDefinedAuthenticationDataUserDefinedAuthData": "ospfv2Hello.header.ospfv2PacketHeader.authenticationData.userDefinedAuthenticationData.userDefinedAuthData-14",
        "HeaderNetworkMask": "ospfv2Hello.header.networkMask-15",
        "HeaderHelloInterval": "ospfv2Hello.header.helloInterval-16",
        "HeaderOptions": "ospfv2Hello.header.options-17",
        "HeaderRouterPriority": "ospfv2Hello.header.routerPriority-18",
        "HeaderRouterDeadInterval": "ospfv2Hello.header.routerDeadInterval-19",
        "HeaderDesignatedRouterID": "ospfv2Hello.header.designatedRouterID-20",
        "HeaderBackupDesignatedRouterID": "ospfv2Hello.header.backupDesignatedRouterID-21",
        "HelloNeighborListNeighborRouterID": "ospfv2Hello.header.helloNeighborList.neighborRouterID-22",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv2Hello, self).__init__(parent, list_op)

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
        Default Value: 1
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
    def HeaderNetworkMask(self):
        """
        Display Name: Network mask
        Default Value: 255.255.255.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNetworkMask"])
        )

    @property
    def HeaderHelloInterval(self):
        """
        Display Name: Hello interval
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHelloInterval"])
        )

    @property
    def HeaderOptions(self):
        """
        Display Name: Options
        Default Value: 0x02
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderOptions"]))

    @property
    def HeaderRouterPriority(self):
        """
        Display Name: Router priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRouterPriority"])
        )

    @property
    def HeaderRouterDeadInterval(self):
        """
        Display Name: Router dead interval
        Default Value: 40
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRouterDeadInterval"])
        )

    @property
    def HeaderDesignatedRouterID(self):
        """
        Display Name: Designated Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDesignatedRouterID"])
        )

    @property
    def HeaderBackupDesignatedRouterID(self):
        """
        Display Name: Backup Designated Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderBackupDesignatedRouterID"]),
        )

    @property
    def HelloNeighborListNeighborRouterID(self):
        """
        Display Name: Neighbor router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HelloNeighborListNeighborRouterID"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
