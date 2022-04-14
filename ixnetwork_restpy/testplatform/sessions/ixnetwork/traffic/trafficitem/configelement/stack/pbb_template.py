from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Pbb(Base):
    __slots__ = ()
    _SDM_NAME = "pbb"
    _SDM_ATT_MAP = {
        "ITAGPcp": "pbb.header.iTAG.pcp-1",
        "ITAGDrop": "pbb.header.iTAG.drop-2",
        "ITAGFmt": "pbb.header.iTAG.fmt-3",
        "ITAGReserved": "pbb.header.iTAG.reserved-4",
        "ITAGISID": "pbb.header.iTAG.iSID-5",
        "CEthernetHeaderCDestinationAddress": "pbb.header.cEthernetHeader.cDestinationAddress-6",
        "CEthernetHeaderCSourceAddress": "pbb.header.cEthernetHeader.cSourceAddress-7",
        "CEthernetHeaderCEtherType": "pbb.header.cEthernetHeader.cEtherType-8",
        "CEthernetHeaderPfcQueue": "pbb.header.cEthernetHeader.pfcQueue-9",
    }

    def __init__(self, parent, list_op=False):
        super(Pbb, self).__init__(parent, list_op)

    @property
    def ITAGPcp(self):
        """
        Display Name: I-TAG PCP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ITAGPcp"]))

    @property
    def ITAGDrop(self):
        """
        Display Name: I-TAG DEI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ITAGDrop"]))

    @property
    def ITAGFmt(self):
        """
        Display Name: FMT
        Default Value: 0
        Value Format: decimal
        Available enum values: Payload Encapsulated Wi Fcs, 0, Payload Encapsulated Wo Fcs, 1, No Encapsulation, 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ITAGFmt"]))

    @property
    def ITAGReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ITAGReserved"]))

    @property
    def ITAGISID(self):
        """
        Display Name: I-SID
        Default Value: 256
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ITAGISID"]))

    @property
    def CEthernetHeaderCDestinationAddress(self):
        """
        Display Name: C-Destination MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CEthernetHeaderCDestinationAddress"]
            ),
        )

    @property
    def CEthernetHeaderCSourceAddress(self):
        """
        Display Name: C-Source MAC Address
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CEthernetHeaderCSourceAddress"]),
        )

    @property
    def CEthernetHeaderCEtherType(self):
        """
        Display Name: C-Ethernet-Type
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CEthernetHeaderCEtherType"])
        )

    @property
    def CEthernetHeaderPfcQueue(self):
        """
        Display Name: PFC Queue
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CEthernetHeaderPfcQueue"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
