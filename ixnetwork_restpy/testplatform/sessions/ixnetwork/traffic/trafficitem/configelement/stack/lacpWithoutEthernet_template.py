from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LacpWithoutEthernet(Base):
    __slots__ = ()
    _SDM_NAME = "lacpWithoutEthernet"
    _SDM_ATT_MAP = {
        "HeaderSubtype": "lacpWithoutEthernet.header.header.subtype-1",
        "HeaderVersion": "lacpWithoutEthernet.header.header.version-2",
        "ActorTlvType": "lacpWithoutEthernet.header.actor.tlvType-3",
        "ActorTlvLength": "lacpWithoutEthernet.header.actor.tlvLength-4",
        "ActorSystemPriority": "lacpWithoutEthernet.header.actor.systemPriority-5",
        "ActorSystem": "lacpWithoutEthernet.header.actor.system-6",
        "ActorKey": "lacpWithoutEthernet.header.actor.key-7",
        "ActorPortPriority": "lacpWithoutEthernet.header.actor.portPriority-8",
        "ActorPort": "lacpWithoutEthernet.header.actor.port-9",
        "ActorState": "lacpWithoutEthernet.header.actor.state-10",
        "ActorReserved": "lacpWithoutEthernet.header.actor.reserved-11",
        "PartnerTlvType": "lacpWithoutEthernet.header.partner.tlvType-12",
        "PartnerTlvLength": "lacpWithoutEthernet.header.partner.tlvLength-13",
        "PartnerSystemPriority": "lacpWithoutEthernet.header.partner.systemPriority-14",
        "PartnerSystem": "lacpWithoutEthernet.header.partner.system-15",
        "PartnerKey": "lacpWithoutEthernet.header.partner.key-16",
        "PartnerPortPriority": "lacpWithoutEthernet.header.partner.portPriority-17",
        "PartnerPort": "lacpWithoutEthernet.header.partner.port-18",
        "PartnerState": "lacpWithoutEthernet.header.partner.state-19",
        "PartnerReserved": "lacpWithoutEthernet.header.partner.reserved-20",
        "CollectorTlvType": "lacpWithoutEthernet.header.collector.tlvType-21",
        "CollectorTlvLength": "lacpWithoutEthernet.header.collector.tlvLength-22",
        "CollectorMaxDelay": "lacpWithoutEthernet.header.collector.maxDelay-23",
        "CollectorReserved": "lacpWithoutEthernet.header.collector.reserved-24",
        "TerminatorTlvType": "lacpWithoutEthernet.header.terminator.tlvType-25",
        "TerminatorTlvLength": "lacpWithoutEthernet.header.terminator.tlvLength-26",
        "HeaderReserved": "lacpWithoutEthernet.header.reserved-27",
        "HeaderFcs": "lacpWithoutEthernet.header.fcs-28",
    }

    def __init__(self, parent, list_op=False):
        super(LacpWithoutEthernet, self).__init__(parent, list_op)

    @property
    def HeaderSubtype(self):
        """
        Display Name: Sub Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSubtype"]))

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def ActorTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorTlvType"]))

    @property
    def ActorTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0x14
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActorTlvLength"])
        )

    @property
    def ActorSystemPriority(self):
        """
        Display Name: Actor System Priority
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActorSystemPriority"])
        )

    @property
    def ActorSystem(self):
        """
        Display Name: Actor System
        Default Value: 0x000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorSystem"]))

    @property
    def ActorKey(self):
        """
        Display Name: Actor Key
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorKey"]))

    @property
    def ActorPortPriority(self):
        """
        Display Name: Actor Port Priority
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActorPortPriority"])
        )

    @property
    def ActorPort(self):
        """
        Display Name: Actor Port
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorPort"]))

    @property
    def ActorState(self):
        """
        Display Name: Actor State
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorState"]))

    @property
    def ActorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ActorReserved"]))

    @property
    def PartnerTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PartnerTlvType"])
        )

    @property
    def PartnerTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0x14
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PartnerTlvLength"])
        )

    @property
    def PartnerSystemPriority(self):
        """
        Display Name: Partner System Priority
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PartnerSystemPriority"])
        )

    @property
    def PartnerSystem(self):
        """
        Display Name: Partner System
        Default Value: 0x000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PartnerSystem"]))

    @property
    def PartnerKey(self):
        """
        Display Name: Partner Key
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PartnerKey"]))

    @property
    def PartnerPortPriority(self):
        """
        Display Name: Partner Port Priority
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PartnerPortPriority"])
        )

    @property
    def PartnerPort(self):
        """
        Display Name: Partner Port
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PartnerPort"]))

    @property
    def PartnerState(self):
        """
        Display Name: Partner State
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PartnerState"]))

    @property
    def PartnerReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PartnerReserved"])
        )

    @property
    def CollectorTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CollectorTlvType"])
        )

    @property
    def CollectorTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0x10
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CollectorTlvLength"])
        )

    @property
    def CollectorMaxDelay(self):
        """
        Display Name: Collector Max Delay
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CollectorMaxDelay"])
        )

    @property
    def CollectorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CollectorReserved"])
        )

    @property
    def TerminatorTlvType(self):
        """
        Display Name: TLV Type
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TerminatorTlvType"])
        )

    @property
    def TerminatorTlvLength(self):
        """
        Display Name: TLV Length
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TerminatorTlvLength"])
        )

    @property
    def HeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderReserved"])
        )

    @property
    def HeaderFcs(self):
        """
        Display Name: Frame Check Sequence CRC-32
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderFcs"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
