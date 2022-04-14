from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Tmpls(Base):
    __slots__ = ()
    _SDM_NAME = "tmpls"
    _SDM_ATT_MAP = {
        "TmpLabelValue": "tmpls.header.tmpLabel.value-1",
        "TmpLabelExperimental": "tmpls.header.tmpLabel.experimental-2",
        "TmpLabelBottomOfStackBit": "tmpls.header.tmpLabel.bottomOfStackBit-3",
        "TmpLabelTtl": "tmpls.header.tmpLabel.ttl-4",
        "TmcLabelValue": "tmpls.header.tmcLabel.value-5",
        "TmcLabelExperimental": "tmpls.header.tmcLabel.experimental-6",
        "TmcLabelBottomOfStackBit": "tmpls.header.tmcLabel.bottomOfStackBit-7",
        "TmcLabelTtl": "tmpls.header.tmcLabel.ttl-8",
        "HeaderCDstMAC": "tmpls.header.cDstMAC-9",
        "HeaderCSrcMAC": "tmpls.header.cSrcMAC-10",
    }

    def __init__(self, parent, list_op=False):
        super(Tmpls, self).__init__(parent, list_op)

    @property
    def TmpLabelValue(self):
        """
        Display Name: Label Value
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TmpLabelValue"]))

    @property
    def TmpLabelExperimental(self):
        """
        Display Name: Experimental
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TmpLabelExperimental"])
        )

    @property
    def TmpLabelBottomOfStackBit(self):
        """
        Display Name: Bottom of Stack Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TmpLabelBottomOfStackBit"])
        )

    @property
    def TmpLabelTtl(self):
        """
        Display Name: Time to Live
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TmpLabelTtl"]))

    @property
    def TmcLabelValue(self):
        """
        Display Name: Label Value
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TmcLabelValue"]))

    @property
    def TmcLabelExperimental(self):
        """
        Display Name: Experimental
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TmcLabelExperimental"])
        )

    @property
    def TmcLabelBottomOfStackBit(self):
        """
        Display Name: Bottom of Stack Bit
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TmcLabelBottomOfStackBit"])
        )

    @property
    def TmcLabelTtl(self):
        """
        Display Name: Time to Live
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TmcLabelTtl"]))

    @property
    def HeaderCDstMAC(self):
        """
        Display Name: C-Destination MAC Address
        Default Value: 00:00:00:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCDstMAC"]))

    @property
    def HeaderCSrcMAC(self):
        """
        Display Name: C-Source MAC Address
        Default Value: 00:00:01:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderCSrcMAC"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
