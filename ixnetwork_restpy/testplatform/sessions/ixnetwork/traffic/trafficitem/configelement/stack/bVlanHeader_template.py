from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BVlanHeader(Base):
    __slots__ = ()
    _SDM_NAME = "bVlanHeader"
    _SDM_ATT_MAP = {
        "BTAGEthertypeEthertypeValue": "bVlanHeader.bTAGEthertype.ethertypeValue-1",
        "BTagPcp": "bVlanHeader.bTAGEthertype.bTag.pcp-2",
        "BTagDei": "bVlanHeader.bTAGEthertype.bTag.dei-3",
        "BTagVlanID": "bVlanHeader.bTAGEthertype.bTag.vlanID-4",
    }

    def __init__(self, parent, list_op=False):
        super(BVlanHeader, self).__init__(parent, list_op)

    @property
    def BTAGEthertypeEthertypeValue(self):
        """
        Display Name: Ethertype value
        Default Value: 0x88A8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BTAGEthertypeEthertypeValue"])
        )

    @property
    def BTagPcp(self):
        """
        Display Name: B-TAG PCP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BTagPcp"]))

    @property
    def BTagDei(self):
        """
        Display Name: B-TAG DEI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BTagDei"]))

    @property
    def BTagVlanID(self):
        """
        Display Name: B-TAG VLAN ID
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BTagVlanID"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
