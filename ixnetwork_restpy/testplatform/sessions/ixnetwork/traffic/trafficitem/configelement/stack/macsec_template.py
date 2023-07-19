from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Macsec(Base):
    __slots__ = ()
    _SDM_NAME = "macsec"
    _SDM_ATT_MAP = {
        "MetadataCipherSuiteOptions": "macsec.secTag.metadata.cipherSuiteOptions-1",
        "Aes128Sak128": "macsec.secTag.metadata.cipherSuite.aes128.sak128-2",
        "Aes256Sak256": "macsec.secTag.metadata.cipherSuite.aes256.sak256-3",
        "AesXpn128SakXpn128": "macsec.secTag.metadata.cipherSuite.aesXpn128.sakXpn128-4",
        "AesXpn128SsciXpn128": "macsec.secTag.metadata.cipherSuite.aesXpn128.ssciXpn128-5",
        "AesXpn128HighPn32Xpn128": "macsec.secTag.metadata.cipherSuite.aesXpn128.highPn32Xpn128-6",
        "AesXpn128SaltXpn128": "macsec.secTag.metadata.cipherSuite.aesXpn128.saltXpn128-7",
        "AesXpn256SakXpn256": "macsec.secTag.metadata.cipherSuite.aesXpn256.sakXpn256-8",
        "AesXpn256SsciXpn256": "macsec.secTag.metadata.cipherSuite.aesXpn256.ssciXpn256-9",
        "AesXpn256HighPn32Xpn256": "macsec.secTag.metadata.cipherSuite.aesXpn256.highPn32Xpn256-10",
        "AesXpn256SaltXpn256": "macsec.secTag.metadata.cipherSuite.aesXpn256.saltXpn256-11",
        "MetadataConfEnabled": "macsec.secTag.metadata.confEnabled-12",
        "MetadataConfOffset": "macsec.secTag.metadata.confOffset-13",
        "MetadataSysidMeta": "macsec.secTag.metadata.sysidMeta-14",
        "MetadataPortidMeta": "macsec.secTag.metadata.portidMeta-15",
        "TciVer": "macsec.secTag.tci.ver-16",
        "TciEs": "macsec.secTag.tci.es-17",
        "TciSc": "macsec.secTag.tci.sc-18",
        "TciScb": "macsec.secTag.tci.scb-19",
        "TciE": "macsec.secTag.tci.e-20",
        "TciC": "macsec.secTag.tci.c-21",
        "SecTagAn": "macsec.secTag.an-22",
        "SecTagSl": "macsec.secTag.sl-23",
        "SecTagPn": "macsec.secTag.pn-24",
        "SciSysid": "macsec.secTag.sci.sysid-25",
        "SciPortid": "macsec.secTag.sci.portid-26",
    }

    def __init__(self, parent, list_op=False):
        super(Macsec, self).__init__(parent, list_op)

    @property
    def MetadataCipherSuiteOptions(self):
        """
        Display Name: Cipher Suite Option
        Default Value: 0
        Value Format: decimal
        Available enum values: 0:GCM-AES-128, 0, 1:GCM-AES-256, 1, 2:GCM-AES-XPN-128, 2, 3:GCM-AES-XPN-256, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MetadataCipherSuiteOptions"])
        )

    @property
    def Aes128Sak128(self):
        """
        Display Name: SAK
        Default Value: 0xA123456789ABCDEF0123456789ABCDEF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Aes128Sak128"]))

    @property
    def Aes256Sak256(self):
        """
        Display Name: SAK
        Default Value: 0xA123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Aes256Sak256"]))

    @property
    def AesXpn128SakXpn128(self):
        """
        Display Name: SAK
        Default Value: 0xA123456789ABCDEF0123456789ABCDEF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn128SakXpn128"])
        )

    @property
    def AesXpn128SsciXpn128(self):
        """
        Display Name: Short Secure Channel Identifier (SSCI)
        Default Value: 0x01234567
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn128SsciXpn128"])
        )

    @property
    def AesXpn128HighPn32Xpn128(self):
        """
        Display Name: High 32 bits of PN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn128HighPn32Xpn128"])
        )

    @property
    def AesXpn128SaltXpn128(self):
        """
        Display Name: Salt
        Default Value: 0x23456789ABCDEF0123456789
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn128SaltXpn128"])
        )

    @property
    def AesXpn256SakXpn256(self):
        """
        Display Name: SAK
        Default Value: 0xA123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn256SakXpn256"])
        )

    @property
    def AesXpn256SsciXpn256(self):
        """
        Display Name: Short Secure Channel Identifier (SSCI)
        Default Value: 0x01234567
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn256SsciXpn256"])
        )

    @property
    def AesXpn256HighPn32Xpn256(self):
        """
        Display Name: High 32 bits of PN
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn256HighPn32Xpn256"])
        )

    @property
    def AesXpn256SaltXpn256(self):
        """
        Display Name: Salt
        Default Value: 0x23456789ABCDEF0123456789
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AesXpn256SaltXpn256"])
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
    def MetadataConfOffset(self):
        """
        Display Name: Confidentiality Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MetadataConfOffset"])
        )

    @property
    def MetadataSysidMeta(self):
        """
        Display Name: System Identifier
        Default Value: 00:11:01:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MetadataSysidMeta"])
        )

    @property
    def MetadataPortidMeta(self):
        """
        Display Name: Port Identifier
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MetadataPortidMeta"])
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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
