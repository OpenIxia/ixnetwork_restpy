from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv3Hello(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv3Hello"
    _SDM_ATT_MAP = {
        "Ospfv3PacketHeaderOspfVersion": "ospfv3Hello.header.ospfv3PacketHeader.ospfVersion-1",
        "Ospfv3PacketHeaderPacketType": "ospfv3Hello.header.ospfv3PacketHeader.packetType-2",
        "Ospfv3PacketHeaderPacketLength": "ospfv3Hello.header.ospfv3PacketHeader.packetLength-3",
        "Ospfv3PacketHeaderRouterID": "ospfv3Hello.header.ospfv3PacketHeader.routerID-4",
        "Ospfv3PacketHeaderAreaID": "ospfv3Hello.header.ospfv3PacketHeader.areaID-5",
        "Ospfv3PacketHeaderOspfPacketChecksum": "ospfv3Hello.header.ospfv3PacketHeader.ospfPacketChecksum-6",
        "Ospfv3PacketHeaderInstanceID": "ospfv3Hello.header.ospfv3PacketHeader.instanceID-7",
        "Ospfv3PacketHeaderReserved": "ospfv3Hello.header.ospfv3PacketHeader.reserved-8",
        "HelloPacketBodyInterfaceID": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.interfaceID-9",
        "HelloPacketBodyRouterPriority": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.routerPriority-10",
        "HelloPacketBodyOptions": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.options-11",
        "HelloPacketBodyHelloInterval": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.helloInterval-12",
        "HelloPacketBodyRouterDeadInterval": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.routerDeadInterval-13",
        "HelloPacketBodyDesignatedRouterID": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.designatedRouterID-14",
        "HelloPacketBodyBackupDesignatedRouterID": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.backupDesignatedRouterID-15",
        "HelloNeighborListNeighborRouterID": "ospfv3Hello.header.ospfv3PacketBody.helloPacketBody.helloNeighborList.neighborRouterID-16",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv3Hello, self).__init__(parent, list_op)

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
        Default Value: 1
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
        Default Value: 44
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
    def HelloPacketBodyInterfaceID(self):
        """
        Display Name: Interface ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HelloPacketBodyInterfaceID"])
        )

    @property
    def HelloPacketBodyRouterPriority(self):
        """
        Display Name: Router priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HelloPacketBodyRouterPriority"]),
        )

    @property
    def HelloPacketBodyOptions(self):
        """
        Display Name: Options
        Default Value: 0x13
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HelloPacketBodyOptions"])
        )

    @property
    def HelloPacketBodyHelloInterval(self):
        """
        Display Name: Hello interval
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HelloPacketBodyHelloInterval"])
        )

    @property
    def HelloPacketBodyRouterDeadInterval(self):
        """
        Display Name: Router dead interval
        Default Value: 40
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HelloPacketBodyRouterDeadInterval"]),
        )

    @property
    def HelloPacketBodyDesignatedRouterID(self):
        """
        Display Name: Designated Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HelloPacketBodyDesignatedRouterID"]),
        )

    @property
    def HelloPacketBodyBackupDesignatedRouterID(self):
        """
        Display Name: Backup Designated Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HelloPacketBodyBackupDesignatedRouterID"]
            ),
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
