from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ITagHeader(Base):
    __slots__ = ()
    _SDM_NAME = "iTagHeader"
    _SDM_ATT_MAP = {
        "ITAGEthertypeEthertypeValue": "iTagHeader.iTAGEthertype.ethertypeValue-1",
        "ITAGPcp": "iTagHeader.iTAGEthertype.iTAG.pcp-2",
        "ITAGDrop": "iTagHeader.iTAGEthertype.iTAG.drop-3",
        "ITAGFmt": "iTagHeader.iTAGEthertype.iTAG.fmt-4",
        "ITAGReserved": "iTagHeader.iTAGEthertype.iTAG.reserved-5",
        "ITAGISID": "iTagHeader.iTAGEthertype.iTAG.iSID-6",
    }

    def __init__(self, parent, list_op=False):
        super(ITagHeader, self).__init__(parent, list_op)

    @property
    def ITAGEthertypeEthertypeValue(self):
        """
        Display Name: Ethertype value
        Default Value: 0x88E7
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ITAGEthertypeEthertypeValue"])
        )

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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
