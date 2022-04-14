from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv3DatabaseDescription(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv3DatabaseDescription"
    _SDM_ATT_MAP = {
        "Ospfv3PacketHeaderOspfVersion": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.ospfVersion-1",
        "Ospfv3PacketHeaderPacketType": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.packetType-2",
        "Ospfv3PacketHeaderPacketLength": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.packetLength-3",
        "Ospfv3PacketHeaderRouterID": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.routerID-4",
        "Ospfv3PacketHeaderAreaID": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.areaID-5",
        "Ospfv3PacketHeaderChecksum": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.checksum-6",
        "Ospfv3PacketHeaderInstanceID": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.instanceID-7",
        "Ospfv3PacketHeaderReserved": "ospfv3DatabaseDescription.header.ospfv3PacketHeader.reserved-8",
        "DatabaseDescriptionBodyReserved": "ospfv3DatabaseDescription.header.databaseDescriptionBody.reserved-9",
        "DatabaseDescriptionBodyOptions": "ospfv3DatabaseDescription.header.databaseDescriptionBody.options-10",
        "DatabaseDescriptionBodyInterfaceMTU": "ospfv3DatabaseDescription.header.databaseDescriptionBody.interfaceMTU-11",
        "DatabaseDescriptionBodyReserved": "ospfv3DatabaseDescription.header.databaseDescriptionBody.reserved-12",
        "DatabaseDescriptionBodyDatabaseDescriptionFlags": "ospfv3DatabaseDescription.header.databaseDescriptionBody.databaseDescriptionFlags-13",
        "DatabaseDescriptionBodyDdSequenceNumber": "ospfv3DatabaseDescription.header.databaseDescriptionBody.ddSequenceNumber-14",
        "LinkStateAdvertisementHeaderLinkStateAge": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateAge-15",
        "LinkStateTypeUnrecognizedLSTypeAction": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateType.unrecognizedLSTypeAction-16",
        "LinkStateTypeLsaFloodingScope": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateType.lsaFloodingScope-17",
        "LinkStateTypeLsaFunctionCode": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateType.lsaFunctionCode-18",
        "LinkStateAdvertisementHeaderLinkStateID": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateID-19",
        "LinkStateAdvertisementHeaderLinkStateAdvertisingRouter": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateAdvertisingRouter-20",
        "LinkStateAdvertisementHeaderLinkStateSequenceNumber": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateSequenceNumber-21",
        "LinkStateAdvertisementHeaderChecksum": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.checksum-22",
        "LinkStateAdvertisementHeaderLinkStateLength": "ospfv3DatabaseDescription.header.databaseDescriptionBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateLength-23",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv3DatabaseDescription, self).__init__(parent, list_op)

    @property
    def Ospfv3PacketHeaderOspfVersion(self):
        """
        Display Name: OSPF Version
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderOspfVersion"]),
        )

    @property
    def Ospfv3PacketHeaderPacketType(self):
        """
        Display Name: Packet Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderPacketType"])
        )

    @property
    def Ospfv3PacketHeaderPacketLength(self):
        """
        Display Name: Packet length
        Default Value: 48
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderPacketLength"]),
        )

    @property
    def Ospfv3PacketHeaderRouterID(self):
        """
        Display Name: Router ID
        Default Value: 1.1.1.1
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderRouterID"])
        )

    @property
    def Ospfv3PacketHeaderAreaID(self):
        """
        Display Name: Area ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderAreaID"])
        )

    @property
    def Ospfv3PacketHeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderChecksum"])
        )

    @property
    def Ospfv3PacketHeaderInstanceID(self):
        """
        Display Name: Instance ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderInstanceID"])
        )

    @property
    def Ospfv3PacketHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderReserved"])
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
    def DatabaseDescriptionBodyOptions(self):
        """
        Display Name: Options
        Default Value: 0x13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DatabaseDescriptionBodyOptions"]),
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
        Value Format: hex
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
    def LinkStateAdvertisementHeaderLinkStateAge(self):
        """
        Display Name: Link-State age
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateAdvertisementHeaderLinkStateAge"]
            ),
        )

    @property
    def LinkStateTypeUnrecognizedLSTypeAction(self):
        """
        Display Name: Unrecognized LS Type Action
        Default Value: 0
        Value Format: decimal
        Available enum values: Treat the LSA as if it had link-local flooding scope, 0, Store and flood the LSA, as if type understood, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateTypeUnrecognizedLSTypeAction"]
            ),
        )

    @property
    def LinkStateTypeLsaFloodingScope(self):
        """
        Display Name: LSA flooding scope
        Default Value: 1
        Value Format: decimal
        Available enum values: Link-Local Scoping. Flooded only on link it is originating on., 0, Area Scoping. Flooded to all routers in the originating area., 1, AS Scoping. Flooded to all routers in the AS., 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LinkStateTypeLsaFloodingScope"]),
        )

    @property
    def LinkStateTypeLsaFunctionCode(self):
        """
        Display Name: LSA function code
        Default Value: 1
        Value Format: decimal
        Available enum values: Router-LSA, 1, Network-LSA., 2, Inter-Area-Prefix-LSA, 3, Inter-Area-Router-LSA, 4, AS-External-LSA, 5, Group-membership-LSA, 6, Type-7-LSA, 7, Link-LSA, 8, Intra-Area-Prefix-LSA, 9
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkStateTypeLsaFunctionCode"])
        )

    @property
    def LinkStateAdvertisementHeaderLinkStateID(self):
        """
        Display Name: Link-State ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateAdvertisementHeaderLinkStateID"]
            ),
        )

    @property
    def LinkStateAdvertisementHeaderLinkStateAdvertisingRouter(self):
        """
        Display Name: Link-State advertising router
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "LinkStateAdvertisementHeaderLinkStateAdvertisingRouter"
                ]
            ),
        )

    @property
    def LinkStateAdvertisementHeaderLinkStateSequenceNumber(self):
        """
        Display Name: Link-State Sequence Number
        Default Value: 0x80000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateAdvertisementHeaderLinkStateSequenceNumber"]
            ),
        )

    @property
    def LinkStateAdvertisementHeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateAdvertisementHeaderChecksum"]
            ),
        )

    @property
    def LinkStateAdvertisementHeaderLinkStateLength(self):
        """
        Display Name: Link-State length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateAdvertisementHeaderLinkStateLength"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
