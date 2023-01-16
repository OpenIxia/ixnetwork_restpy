from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MacsecHw(Base):
    __slots__ = ()
    _SDM_NAME = "MacsecHw"
    _SDM_ATT_MAP = {
        "MetadataScIndex": "MacsecHw.header.secTag.metadata.scIndex-1",
        "MetadataConfEnabled": "MacsecHw.header.secTag.metadata.confEnabled-2",
        "MetadataBadIcv": "MacsecHw.header.secTag.metadata.badIcv-3",
        "TciVer": "MacsecHw.header.secTag.tci.ver-4",
        "TciEs": "MacsecHw.header.secTag.tci.es-5",
        "TciSc": "MacsecHw.header.secTag.tci.sc-6",
        "TciScb": "MacsecHw.header.secTag.tci.scb-7",
        "TciE": "MacsecHw.header.secTag.tci.e-8",
        "TciC": "MacsecHw.header.secTag.tci.c-9",
        "SecTagAn": "MacsecHw.header.secTag.an-10",
        "SecTagSl": "MacsecHw.header.secTag.sl-11",
        "SecTagPn": "MacsecHw.header.secTag.pn-12",
        "SciSysid": "MacsecHw.header.secTag.sci.sysid-13",
        "SciPortid": "MacsecHw.header.secTag.sci.portid-14",
        "LagMemberPortMetadataLagMemberPortId": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.lagMemberPortId-15",
        "LagMemberPortMetadataScIndex": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.scIndex-16",
        "LagMemberPortMetadataConfEnabled": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.confEnabled-17",
        "LagmemberportmetadataTciVer": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.tci.ver-18",
        "LagmemberportmetadataTciEs": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.tci.es-19",
        "LagmemberportmetadataTciSc": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.tci.sc-20",
        "LagmemberportmetadataTciScb": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.tci.scb-21",
        "LagmemberportmetadataTciE": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.tci.e-22",
        "LagmemberportmetadataTciC": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.tci.c-23",
        "LagmemberportmetadataSciSysid": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.sci.sysid-24",
        "LagmemberportmetadataSciPortid": "MacsecHw.header.lagMemberPortsMetadata.lagMemberPortMetadata.sci.portid-25",
    }

    def __init__(self, parent, list_op=False):
        super(MacsecHw, self).__init__(parent, list_op)

    @property
    def MetadataScIndex(self):
        """
        Display Name: Secure Channel Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MetadataScIndex"])
        )

    @property
    def MetadataConfEnabled(self):
        """
        Display Name: Confidentiality Enabled
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MetadataConfEnabled"])
        )

    @property
    def MetadataBadIcv(self):
        """
        Display Name: Bad ICV
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MetadataBadIcv"])
        )

    @property
    def TciVer(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciVer"]))

    @property
    def TciEs(self):
        """
        Display Name: End Station (ES) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciEs"]))

    @property
    def TciSc(self):
        """
        Display Name: Secure Channel (SC) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciSc"]))

    @property
    def TciScb(self):
        """
        Display Name: Single Copy Broadcast (SCB) bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciScb"]))

    @property
    def TciE(self):
        """
        Display Name: Encryption (E) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciE"]))

    @property
    def TciC(self):
        """
        Display Name: Changed Text (C) bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TciC"]))

    @property
    def SecTagAn(self):
        """
        Display Name: Association Number (AN)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SecTagAn"]))

    @property
    def SecTagSl(self):
        """
        Display Name: Short Length (SL)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SecTagSl"]))

    @property
    def SecTagPn(self):
        """
        Display Name: Packet Number (PN)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SecTagPn"]))

    @property
    def SciSysid(self):
        """
        Display Name: System Identifier
        Default Value: 00:11:01:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SciSysid"]))

    @property
    def SciPortid(self):
        """
        Display Name: Port Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SciPortid"]))

    @property
    def LagMemberPortMetadataLagMemberPortId(self):
        """
        Display Name: LAG Member Port Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LagMemberPortMetadataLagMemberPortId"]
            ),
        )

    @property
    def LagMemberPortMetadataScIndex(self):
        """
        Display Name: Secure Channel Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LagMemberPortMetadataScIndex"])
        )

    @property
    def LagMemberPortMetadataConfEnabled(self):
        """
        Display Name: Confidentiality Enabled
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LagMemberPortMetadataConfEnabled"]),
        )

    @property
    def LagmemberportmetadataTciVer(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataTciVer"])
        )

    @property
    def LagmemberportmetadataTciEs(self):
        """
        Display Name: End Station (ES) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataTciEs"])
        )

    @property
    def LagmemberportmetadataTciSc(self):
        """
        Display Name: Secure Channel (SC) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataTciSc"])
        )

    @property
    def LagmemberportmetadataTciScb(self):
        """
        Display Name: Single Copy Broadcast (SCB) bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataTciScb"])
        )

    @property
    def LagmemberportmetadataTciE(self):
        """
        Display Name: Encryption (E) bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataTciE"])
        )

    @property
    def LagmemberportmetadataTciC(self):
        """
        Display Name: Changed Text (C) bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataTciC"])
        )

    @property
    def LagmemberportmetadataSciSysid(self):
        """
        Display Name: System Identifier
        Default Value: 00:11:01:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataSciSysid"]),
        )

    @property
    def LagmemberportmetadataSciPortid(self):
        """
        Display Name: Port Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LagmemberportmetadataSciPortid"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
