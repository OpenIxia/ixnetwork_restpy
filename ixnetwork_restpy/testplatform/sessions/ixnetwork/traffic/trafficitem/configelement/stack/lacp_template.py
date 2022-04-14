from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Lacp(Base):
    __slots__ = ()
    _SDM_NAME = "lacp"
    _SDM_ATT_MAP = {
        "DstAddress": "lacp.header.header.dstAddress-1",
        "SrcAddress": "lacp.header.header.srcAddress-2",
        "LengthType": "lacp.header.header.lengthType-3",
        "Subtype": "lacp.header.header.subtype-4",
        "Version": "lacp.header.header.version-5",
        "ActorTlvType": "lacp.header.actor.tlvType-6",
        "ActorTlvLength": "lacp.header.actor.tlvLength-7",
        "ActorSystemPriority": "lacp.header.actor.systemPriority-8",
        "ActorSystem": "lacp.header.actor.system-9",
        "ActorKey": "lacp.header.actor.key-10",
        "ActorPortPriority": "lacp.header.actor.portPriority-11",
        "ActorPort": "lacp.header.actor.port-12",
        "ActorState": "lacp.header.actor.state-13",
        "ActorReserved": "lacp.header.actor.reserved-14",
        "PartnerTlvType": "lacp.header.partner.tlvType-15",
        "PartnerTlvLength": "lacp.header.partner.tlvLength-16",
        "PartnerSystemPriority": "lacp.header.partner.systemPriority-17",
        "PartnerSystem": "lacp.header.partner.system-18",
        "PartnerKey": "lacp.header.partner.key-19",
        "PartnerPortPriority": "lacp.header.partner.portPriority-20",
        "PartnerPort": "lacp.header.partner.port-21",
        "PartnerState": "lacp.header.partner.state-22",
        "PartnerReserved": "lacp.header.partner.reserved-23",
        "CollectorTlvType": "lacp.header.collector.tlvType-24",
        "CollectorTlvLength": "lacp.header.collector.tlvLength-25",
        "CollectorMaxDelay": "lacp.header.collector.maxDelay-26",
        "CollectorReserved": "lacp.header.collector.reserved-27",
        "TerminatorTlvType": "lacp.header.terminator.tlvType-28",
        "TerminatorTlvLength": "lacp.header.terminator.tlvLength-29",
        "HeaderReserved": "lacp.header.reserved-30",
        "HeaderFcs": "lacp.header.fcs-31",
    }

    def __init__(self, parent, list_op=False):
        super(Lacp, self).__init__(parent, list_op)

    @property
    def DstAddress(self):
        """
        Display Name: Destination address
        Default Value: 01:80:C2:00:00:02
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DstAddress"]))

    @property
    def SrcAddress(self):
        """
        Display Name: Source address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcAddress"]))

    @property
    def LengthType(self):
        """
        Display Name: Length Type
        Default Value: 0x8809
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LengthType"]))

    @property
    def Subtype(self):
        """
        Display Name: Sub Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Subtype"]))

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

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
