from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MacInMACNoFcs(Base):
    __slots__ = ()
    _SDM_NAME = "macInMACNoFcs"
    _SDM_ATT_MAP = {
        "HeaderBdestinationAddressEthernet": "macInMACNoFcs.header.bdestinationAddressEthernet-1",
        "HeaderBsourceAddressEthernet": "macInMACNoFcs.header.bsourceAddressEthernet-2",
        "BethernetTypeEtherTypeBtag": "macInMACNoFcs.header.bethernetType.etherTypeBtag-3",
        "BvlanTagBvlanPriority": "macInMACNoFcs.header.bethernetType.bvlanTag.bvlanPriority-4",
        "BvlanTagBvlanCanonicalFormatIndicator": "macInMACNoFcs.header.bethernetType.bvlanTag.bvlanCanonicalFormatIndicator-5",
        "BvlanTagBvlanID": "macInMACNoFcs.header.bethernetType.bvlanTag.bvlanID-6",
        "ItagEtherTypeEtherTypeItag": "macInMACNoFcs.header.itagEtherType.etherTypeItag-7",
        "ItagPcp": "macInMACNoFcs.header.itag.pcp-8",
        "ItagDei": "macInMACNoFcs.header.itag.dei-9",
        "ItagFmt": "macInMACNoFcs.header.itag.fmt-10",
        "ItagReserved": "macInMACNoFcs.header.itag.reserved-11",
        "ItagIsid": "macInMACNoFcs.header.itag.isid-12",
        "HeaderCdestinationAddressEthernet": "macInMACNoFcs.header.cdestinationAddressEthernet-13",
        "HeaderCsourceAddressEthernet": "macInMACNoFcs.header.csourceAddressEthernet-14",
        "StagEtherTypeStag": "macInMACNoFcs.header.stag.etherTypeStag-15",
        "SvlanTagSvlanPriority": "macInMACNoFcs.header.stag.svlanTag.svlanPriority-16",
        "SvlanTagSvlanCanonicalFormatIndicator": "macInMACNoFcs.header.stag.svlanTag.svlanCanonicalFormatIndicator-17",
        "SvlanTagSvlanID": "macInMACNoFcs.header.stag.svlanTag.svlanID-18",
        "CtagEtherTypeCtag": "macInMACNoFcs.header.ctag.etherTypeCtag-19",
        "CvlanTagCvlanPriority": "macInMACNoFcs.header.ctag.cvlanTag.cvlanPriority-20",
        "CvlanTagCvlanCanonicalFormatIndicator": "macInMACNoFcs.header.ctag.cvlanTag.cvlanCanonicalFormatIndicator-21",
        "CvlanTagCvlanID": "macInMACNoFcs.header.ctag.cvlanTag.cvlanID-22",
        "HeaderType": "macInMACNoFcs.header.type-23",
    }

    def __init__(self, parent, list_op=False):
        super(MacInMACNoFcs, self).__init__(parent, list_op)

    @property
    def HeaderBdestinationAddressEthernet(self):
        """
        Display Name: B-Destination Address (Ethernet)
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderBdestinationAddressEthernet"]),
        )

    @property
    def HeaderBsourceAddressEthernet(self):
        """
        Display Name: B-Source Address (Ethernet)
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBsourceAddressEthernet"])
        )

    @property
    def BethernetTypeEtherTypeBtag(self):
        """
        Display Name: EtherType B-tag
        Default Value: 0x8100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BethernetTypeEtherTypeBtag"])
        )

    @property
    def BvlanTagBvlanPriority(self):
        """
        Display Name: B-VLAN Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BvlanTagBvlanPriority"])
        )

    @property
    def BvlanTagBvlanCanonicalFormatIndicator(self):
        """
        Display Name: B-VLAN Canonical Format Indicator
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["BvlanTagBvlanCanonicalFormatIndicator"]
            ),
        )

    @property
    def BvlanTagBvlanID(self):
        """
        Display Name: B-VLAN ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BvlanTagBvlanID"])
        )

    @property
    def ItagEtherTypeEtherTypeItag(self):
        """
        Display Name: EtherType I-tag
        Default Value: 0x8100
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ItagEtherTypeEtherTypeItag"])
        )

    @property
    def ItagPcp(self):
        """
        Display Name: PCP
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ItagPcp"]))

    @property
    def ItagDei(self):
        """
        Display Name: DEI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ItagDei"]))

    @property
    def ItagFmt(self):
        """
        Display Name: FMT
        Default Value: 0
        Value Format: decimal
        Available enum values: Payload Encapsulated Wi Fcs, 0, Payload Encapsulated Wo Fcs, 1, No Encapsulation, 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ItagFmt"]))

    @property
    def ItagReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ItagReserved"]))

    @property
    def ItagIsid(self):
        """
        Display Name: I-SID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ItagIsid"]))

    @property
    def HeaderCdestinationAddressEthernet(self):
        """
        Display Name: C-Destination Address (Ethernet)
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderCdestinationAddressEthernet"]),
        )

    @property
    def HeaderCsourceAddressEthernet(self):
        """
        Display Name: C-Source Address (Ethernet)
        Default Value: 0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCsourceAddressEthernet"])
        )

    @property
    def StagEtherTypeStag(self):
        """
        Display Name: EtherType S-tag
        Default Value: 0x88A8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StagEtherTypeStag"])
        )

    @property
    def SvlanTagSvlanPriority(self):
        """
        Display Name: S-VLAN Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SvlanTagSvlanPriority"])
        )

    @property
    def SvlanTagSvlanCanonicalFormatIndicator(self):
        """
        Display Name: S-VLAN Canonical Format Indicator
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SvlanTagSvlanCanonicalFormatIndicator"]
            ),
        )

    @property
    def SvlanTagSvlanID(self):
        """
        Display Name: S-VLAN ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SvlanTagSvlanID"])
        )

    @property
    def CtagEtherTypeCtag(self):
        """
        Display Name: EtherType C-tag
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CtagEtherTypeCtag"])
        )

    @property
    def CvlanTagCvlanPriority(self):
        """
        Display Name: C-VLAN Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CvlanTagCvlanPriority"])
        )

    @property
    def CvlanTagCvlanCanonicalFormatIndicator(self):
        """
        Display Name: C-VLAN Canonical Format Indicator
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CvlanTagCvlanCanonicalFormatIndicator"]
            ),
        )

    @property
    def CvlanTagCvlanID(self):
        """
        Display Name: C-VLAN ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CvlanTagCvlanID"])
        )

    @property
    def HeaderType(self):
        """
        Display Name: Type
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
