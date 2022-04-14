from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv3LSAAcknowledgement(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv3LSAAcknowledgement"
    _SDM_ATT_MAP = {
        "Ospfv3PacketHeaderOspfVersion": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.ospfVersion-1",
        "Ospfv3PacketHeaderPacketType": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.packetType-2",
        "Ospfv3PacketHeaderPacketLength": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.packetLength-3",
        "Ospfv3PacketHeaderRouterID": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.routerID-4",
        "Ospfv3PacketHeaderAreaID": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.areaID-5",
        "Ospfv3PacketHeaderOspfPacketChecksum": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.ospfPacketChecksum-6",
        "Ospfv3PacketHeaderInstanceID": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.instanceID-7",
        "Ospfv3PacketHeaderReserved": "ospfv3LSAAcknowledgement.header.ospfv3PacketHeader.reserved-8",
        "LinkStateAdvertisementHeaderLinkStateAge": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateAge-9",
        "LinkStateTypeUnrecognizedLSTypeAction": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateType.unrecognizedLSTypeAction-10",
        "LinkStateTypeLsaFloodingScope": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateType.lsaFloodingScope-11",
        "LinkStateTypeLsaFunctionCode": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateType.lsaFunctionCode-12",
        "LinkStateAdvertisementHeaderLinkStateID": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateID-13",
        "LinkStateAdvertisementHeaderLinkStateAdvertisingRouter": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateAdvertisingRouter-14",
        "LinkStateAdvertisementHeaderLinkStateSequenceNumber": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateSequenceNumber-15",
        "LinkStateAdvertisementHeaderLinkStateChecksum": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateChecksum-16",
        "LinkStateAdvertisementHeaderLinkStateLength": "ospfv3LSAAcknowledgement.header.linkStateAcknowledgmentBody.lsaHeadersList.linkStateAdvertisementHeader.linkStateLength-17",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv3LSAAcknowledgement, self).__init__(parent, list_op)

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
        Default Value: 5
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
        Default Value: 36
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
    def Ospfv3PacketHeaderOspfPacketChecksum(self):
        """
        Display Name: OSPF packet checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ospfv3PacketHeaderOspfPacketChecksum"]
            ),
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
    def LinkStateAdvertisementHeaderLinkStateChecksum(self):
        """
        Display Name: Link-State checksum
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateAdvertisementHeaderLinkStateChecksum"]
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
