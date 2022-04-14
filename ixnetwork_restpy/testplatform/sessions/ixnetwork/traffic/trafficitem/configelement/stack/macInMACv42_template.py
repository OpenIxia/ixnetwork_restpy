from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MacInMACv42(Base):
    __slots__ = ()
    _SDM_NAME = "macInMACv42"
    _SDM_ATT_MAP = {
        "HeaderBDstAddress": "macInMACv42.header.bDstAddress-1",
        "HeaderBSrcAddress": "macInMACv42.header.bSrcAddress-2",
        "BTAGEthertypeEthertypeValue": "macInMACv42.header.bTAGEthertype.ethertypeValue-3",
        "BTagPcp": "macInMACv42.header.bTAGEthertype.bTag.pcp-4",
        "BTagDei": "macInMACv42.header.bTAGEthertype.bTag.dei-5",
        "BTagVlanID": "macInMACv42.header.bTAGEthertype.bTag.vlanID-6",
        "ITAGEthertypeEthertypeValue": "macInMACv42.header.iTAGEthertype.ethertypeValue-7",
        "ITAGPcp": "macInMACv42.header.iTAGEthertype.iTAG.pcp-8",
        "ITAGDrop": "macInMACv42.header.iTAGEthertype.iTAG.drop-9",
        "ITAGFmt": "macInMACv42.header.iTAGEthertype.iTAG.fmt-10",
        "ITAGReserved": "macInMACv42.header.iTAGEthertype.iTAG.reserved-11",
        "ITAGISID": "macInMACv42.header.iTAGEthertype.iTAG.iSID-12",
        "HeaderCDstAddress": "macInMACv42.header.cDstAddress-13",
        "HeaderCSrcAddress": "macInMACv42.header.cSrcAddress-14",
        "STAGSTAGEthertype": "macInMACv42.header.sTAGCTAG.tag.sTAG.sTAGEthertype-15",
        "STAGPcp": "macInMACv42.header.sTAGCTAG.tag.sTAG.sTAG.pcp-16",
        "STAGDei": "macInMACv42.header.sTAGCTAG.tag.sTAG.sTAG.dei-17",
        "STAGVlanID": "macInMACv42.header.sTAGCTAG.tag.sTAG.sTAG.vlanID-18",
        "CTAGCTAGEthertype": "macInMACv42.header.sTAGCTAG.tag.cTAG.cTAGEthertype-19",
        "CTAGUserPriority": "macInMACv42.header.sTAGCTAG.tag.cTAG.cTAG.userPriority-20",
        "CTAGCfi": "macInMACv42.header.sTAGCTAG.tag.cTAG.cTAG.cfi-21",
        "CTAGVlanId": "macInMACv42.header.sTAGCTAG.tag.cTAG.cTAG.vlanId-22",
        "BothSTAGCTAGSTAGEthertype": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.sTAGEthertype-23",
        "BothstagctagSTAGPcp": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.sTAG.pcp-24",
        "BothstagctagSTAGDei": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.sTAG.dei-25",
        "BothstagctagSTAGVlanID": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.sTAG.vlanID-26",
        "BothSTAGCTAGCTAGEthertype": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.cTAGEthertype-27",
        "BothstagctagCTAGUserPriority": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.cTAG.userPriority-28",
        "BothstagctagCTAGCfi": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.cTAG.cfi-29",
        "BothstagctagCTAGVlanId": "macInMACv42.header.sTAGCTAG.tag.bothSTAGCTAG.cTAG.vlanId-30",
        "TagNoSTAGCTAG": "macInMACv42.header.sTAGCTAG.tag.noSTAGCTAG-31",
    }

    def __init__(self, parent, list_op=False):
        super(MacInMACv42, self).__init__(parent, list_op)

    @property
    def HeaderBDstAddress(self):
        """
        Display Name: B-Destination Address (Ethernet)
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBDstAddress"])
        )

    @property
    def HeaderBSrcAddress(self):
        """
        Display Name: B-Source Address (Ethernet)
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBSrcAddress"])
        )

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

    @property
    def HeaderCDstAddress(self):
        """
        Display Name: C-Destination Address (Ethernet)
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCDstAddress"])
        )

    @property
    def HeaderCSrcAddress(self):
        """
        Display Name: C-Source Address (Ethernet)
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCSrcAddress"])
        )

    @property
    def STAGSTAGEthertype(self):
        """
        Display Name: S-TAG Ethertype
        Default Value: 0x88A8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["STAGSTAGEthertype"])
        )

    @property
    def STAGPcp(self):
        """
        Display Name: S-TAG PCP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["STAGPcp"]))

    @property
    def STAGDei(self):
        """
        Display Name: S-TAG DEI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["STAGDei"]))

    @property
    def STAGVlanID(self):
        """
        Display Name: S-TAG VLAN ID
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["STAGVlanID"]))

    @property
    def CTAGCTAGEthertype(self):
        """
        Display Name: C-TAG Ethertype
        Default Value: 0x8100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CTAGCTAGEthertype"])
        )

    @property
    def CTAGUserPriority(self):
        """
        Display Name: C-TAG User Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CTAGUserPriority"])
        )

    @property
    def CTAGCfi(self):
        """
        Display Name: C-TAG CFI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CTAGCfi"]))

    @property
    def CTAGVlanId(self):
        """
        Display Name: C-TAG VLAN ID
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CTAGVlanId"]))

    @property
    def BothSTAGCTAGSTAGEthertype(self):
        """
        Display Name: S-TAG Ethertype
        Default Value: 0x88A8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothSTAGCTAGSTAGEthertype"])
        )

    @property
    def BothstagctagSTAGPcp(self):
        """
        Display Name: S-TAG PCP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothstagctagSTAGPcp"])
        )

    @property
    def BothstagctagSTAGDei(self):
        """
        Display Name: S-TAG DEI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothstagctagSTAGDei"])
        )

    @property
    def BothstagctagSTAGVlanID(self):
        """
        Display Name: S-TAG VLAN ID
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothstagctagSTAGVlanID"])
        )

    @property
    def BothSTAGCTAGCTAGEthertype(self):
        """
        Display Name: C-TAG Ethertype
        Default Value: 0x8100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothSTAGCTAGCTAGEthertype"])
        )

    @property
    def BothstagctagCTAGUserPriority(self):
        """
        Display Name: C-TAG User Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothstagctagCTAGUserPriority"])
        )

    @property
    def BothstagctagCTAGCfi(self):
        """
        Display Name: C-TAG CFI
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothstagctagCTAGCfi"])
        )

    @property
    def BothstagctagCTAGVlanId(self):
        """
        Display Name: C-TAG VLAN ID
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BothstagctagCTAGVlanId"])
        )

    @property
    def TagNoSTAGCTAG(self):
        """
        Display Name: No S-TAG/C-TAG
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TagNoSTAGCTAG"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
