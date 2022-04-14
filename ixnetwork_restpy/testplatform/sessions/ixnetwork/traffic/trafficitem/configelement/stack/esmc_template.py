from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Esmc(Base):
    __slots__ = ()
    _SDM_NAME = "esmc"
    _SDM_ATT_MAP = {
        "PacketSubtype": "esmc.packet.subtype-1",
        "PacketItuoui": "esmc.packet.ituoui-2",
        "PacketItusubtype": "esmc.packet.itusubtype-3",
        "PacketVersion": "esmc.packet.version-4",
        "PacketEvent_flag": "esmc.packet.event_flag-5",
        "PacketReserved": "esmc.packet.reserved-6",
        "QltlvField0": "esmc.packet.qltlv.field0-7",
        "QltlvLength": "esmc.packet.qltlv.length-8",
        "QltlvReserved": "esmc.packet.qltlv.Reserved-9",
        "QltlvSsm_code": "esmc.packet.qltlv.ssm_code-10",
        "ExtqltlvField0": "esmc.packet.extqltlv.field0-11",
        "ExtqltlvLength": "esmc.packet.extqltlv.length-12",
        "ExtqltlvEnhanced_ssm_code": "esmc.packet.extqltlv.enhanced_ssm_code-13",
        "ExtqltlvSyncEClockIdentity": "esmc.packet.extqltlv.syncEClockIdentity-14",
        "ExtqltlvUnusedFlag": "esmc.packet.extqltlv.unusedFlag-15",
        "ExtqltlvPartialChainflag": "esmc.packet.extqltlv.partialChainflag-16",
        "ExtqltlvMixedeEECsflag": "esmc.packet.extqltlv.mixedeEECsflag-17",
        "ExtqltlvNumberOfeEECs": "esmc.packet.extqltlv.numberOfeEECs-18",
        "ExtqltlvNumberOfEECs": "esmc.packet.extqltlv.numberOfEECs-19",
        "ExtqltlvExtendedTlvReserved": "esmc.packet.extqltlv.extendedTlvReserved-20",
    }

    def __init__(self, parent, list_op=False):
        super(Esmc, self).__init__(parent, list_op)

    @property
    def PacketSubtype(self):
        """
        Display Name: Slow protocol subtype
        Default Value: 0x0A
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PacketSubtype"]))

    @property
    def PacketItuoui(self):
        """
        Display Name: ITU-OUI
        Default Value: 0x0019A7
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PacketItuoui"]))

    @property
    def PacketItusubtype(self):
        """
        Display Name: ITU Subtype
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PacketItusubtype"])
        )

    @property
    def PacketVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PacketVersion"]))

    @property
    def PacketEvent_flag(self):
        """
        Display Name: Event flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PacketEvent_flag"])
        )

    @property
    def PacketReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PacketReserved"])
        )

    @property
    def QltlvField0(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QltlvField0"]))

    @property
    def QltlvLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QltlvLength"]))

    @property
    def QltlvReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QltlvReserved"]))

    @property
    def QltlvSsm_code(self):
        """
        Display Name: SSM Code
        Default Value: 1
        Value Format: decimal
        Available enum values: QL-STU/UNK, 0, QL-PRS, 1, QL-PRC, 2, QL-INV3, 3, QL-SSU-A/TNC, 4, QL-INV5, 5, QL-INV6, 6, QL-ST2, 7, QL-SSU-B, 8, QL-INV9, 9, QL-EEC2/ST3, 10, QL-EEC1/SEC, 11, QL-SMC, 12, QL-ST3E, 13, QL-PROV, 14, QL-DNU/DUS, 15
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["QltlvSsm_code"]))

    @property
    def ExtqltlvField0(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvField0"])
        )

    @property
    def ExtqltlvLength(self):
        """
        Display Name: Length
        Default Value: 0x14
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvLength"])
        )

    @property
    def ExtqltlvEnhanced_ssm_code(self):
        """
        Display Name: Enhanced SSM Code
        Default Value: 32
        Value Format: decimal
        Available enum values: QL-Default, 255, QL-PRTC, 32, QL-ePRTC, 33, QL-eEEC, 34, QL-ePRC, 35
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvEnhanced_ssm_code"])
        )

    @property
    def ExtqltlvSyncEClockIdentity(self):
        """
        Display Name: SyncE Clock Identity
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvSyncEClockIdentity"])
        )

    @property
    def ExtqltlvUnusedFlag(self):
        """
        Display Name: Unused Flag
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvUnusedFlag"])
        )

    @property
    def ExtqltlvPartialChainflag(self):
        """
        Display Name: Partial Chain Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvPartialChainflag"])
        )

    @property
    def ExtqltlvMixedeEECsflag(self):
        """
        Display Name: Mixed eEECs Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvMixedeEECsflag"])
        )

    @property
    def ExtqltlvNumberOfeEECs(self):
        """
        Display Name: Number of eEECs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvNumberOfeEECs"])
        )

    @property
    def ExtqltlvNumberOfEECs(self):
        """
        Display Name: Number of EECs
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvNumberOfEECs"])
        )

    @property
    def ExtqltlvExtendedTlvReserved(self):
        """
        Display Name: Extended TLV Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtqltlvExtendedTlvReserved"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
