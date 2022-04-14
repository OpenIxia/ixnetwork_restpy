from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv3LSARequest(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv3LSARequest"
    _SDM_ATT_MAP = {
        "Ospfv3PacketHeaderOspfVersion": "ospfv3LSARequest.header.ospfv3PacketHeader.ospfVersion-1",
        "Ospfv3PacketHeaderPacketType": "ospfv3LSARequest.header.ospfv3PacketHeader.packetType-2",
        "Ospfv3PacketHeaderPacketLength": "ospfv3LSARequest.header.ospfv3PacketHeader.packetLength-3",
        "Ospfv3PacketHeaderRouterID": "ospfv3LSARequest.header.ospfv3PacketHeader.routerID-4",
        "Ospfv3PacketHeaderAreaID": "ospfv3LSARequest.header.ospfv3PacketHeader.areaID-5",
        "Ospfv3PacketHeaderOspfPacketChecksum": "ospfv3LSARequest.header.ospfv3PacketHeader.ospfPacketChecksum-6",
        "Ospfv3PacketHeaderInstanceID": "ospfv3LSARequest.header.ospfv3PacketHeader.instanceID-7",
        "Ospfv3PacketHeaderReserved": "ospfv3LSARequest.header.ospfv3PacketHeader.reserved-8",
        "RequestedLSADescriptionReserved": "ospfv3LSARequest.header.linkStateRequestBody.requestedLSAsList.requestedLSADescription.reserved-9",
        "LinkStateTypeUnrecognizedLSTypeAction": "ospfv3LSARequest.header.linkStateRequestBody.requestedLSAsList.requestedLSADescription.linkStateType.unrecognizedLSTypeAction-10",
        "LinkStateTypeLsaFloodingScope": "ospfv3LSARequest.header.linkStateRequestBody.requestedLSAsList.requestedLSADescription.linkStateType.lsaFloodingScope-11",
        "LinkStateTypeLsaFunctionCode": "ospfv3LSARequest.header.linkStateRequestBody.requestedLSAsList.requestedLSADescription.linkStateType.lsaFunctionCode-12",
        "RequestedLSADescriptionLinkStateID": "ospfv3LSARequest.header.linkStateRequestBody.requestedLSAsList.requestedLSADescription.linkStateID-13",
        "RequestedLSADescriptionLinkStateAdvertisingRouter": "ospfv3LSARequest.header.linkStateRequestBody.requestedLSAsList.requestedLSADescription.linkStateAdvertisingRouter-14",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv3LSARequest, self).__init__(parent, list_op)

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
        Default Value: 3
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
        Default Value: 28
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
    def RequestedLSADescriptionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RequestedLSADescriptionReserved"]),
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
        Default Value: 0
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
    def RequestedLSADescriptionLinkStateID(self):
        """
        Display Name: Link-State ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestedLSADescriptionLinkStateID"]
            ),
        )

    @property
    def RequestedLSADescriptionLinkStateAdvertisingRouter(self):
        """
        Display Name: Link-State advertising router
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RequestedLSADescriptionLinkStateAdvertisingRouter"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
