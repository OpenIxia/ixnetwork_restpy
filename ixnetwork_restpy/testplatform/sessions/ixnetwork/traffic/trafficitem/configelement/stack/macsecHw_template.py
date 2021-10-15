from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MacsecHw(Base):
    __slots__ = ()
    _SDM_NAME = 'macsecHw'
    _SDM_ATT_MAP = {
        'MetadataScIndex': 'MacsecHw.secTag.metadata.scIndex-1',
        'MetadataConfEnabled': 'MacsecHw.secTag.metadata.confEnabled-2',
        'MetadataBadIcv': 'MacsecHw.secTag.metadata.badIcv-3',
        'TciVer': 'MacsecHw.secTag.tci.ver-4',
        'TciEs': 'MacsecHw.secTag.tci.es-5',
        'TciSc': 'MacsecHw.secTag.tci.sc-6',
        'TciScb': 'MacsecHw.secTag.tci.scb-7',
        'TciE': 'MacsecHw.secTag.tci.e-8',
        'TciC': 'MacsecHw.secTag.tci.c-9',
        'SecTagAn': 'MacsecHw.secTag.an-10',
        'SecTagSl': 'MacsecHw.secTag.sl-11',
        'SecTagPn': 'MacsecHw.secTag.pn-12',
        'SciSysid': 'MacsecHw.secTag.sci.sysid-13',
        'SciPortid': 'MacsecHw.secTag.sci.portid-14',
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
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetadataScIndex']))

    @property
    def MetadataConfEnabled(self):
        """
        Display Name: Confidentiality Enabled
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetadataConfEnabled']))

    @property
    def MetadataBadIcv(self):
        """
        Display Name: Bad ICV
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MetadataBadIcv']))

    @property
    def TciVer(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciVer']))

    @property
    def TciEs(self):
        """
        Display Name: End Station (ES) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciEs']))

    @property
    def TciSc(self):
        """
        Display Name: Secure Channel (SC) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciSc']))

    @property
    def TciScb(self):
        """
        Display Name: Single Copy Broadcast (SCB) bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciScb']))

    @property
    def TciE(self):
        """
        Display Name: Encryption (E) bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciE']))

    @property
    def TciC(self):
        """
        Display Name: Changed Text (C) bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Set, 0, Set, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TciC']))

    @property
    def SecTagAn(self):
        """
        Display Name: Association Number (AN)
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecTagAn']))

    @property
    def SecTagSl(self):
        """
        Display Name: Short Length (SL)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecTagSl']))

    @property
    def SecTagPn(self):
        """
        Display Name: Packet Number (PN)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecTagPn']))

    @property
    def SciSysid(self):
        """
        Display Name: System Identifier
        Default Value: 00:11:01:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SciSysid']))

    @property
    def SciPortid(self):
        """
        Display Name: Port Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SciPortid']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
