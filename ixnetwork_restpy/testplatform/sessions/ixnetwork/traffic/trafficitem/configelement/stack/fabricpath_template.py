from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Fabricpath(Base):
    __slots__ = ()
    _SDM_NAME = "fabricpath"
    _SDM_ATT_MAP = {
        "OuterdestinationAddressMacformat": "fabricpath.fabricpathHeader.outerdestinationAddress.macformat-1",
        "DestaddEndnodeid1": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.endnodeid1-2",
        "DestaddUbit": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.ubit-3",
        "DestaddIbit": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.ibit-4",
        "DestaddEndnodeid2": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.endnodeid2-5",
        "DestaddResv": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.resv-6",
        "DestaddOoo_dl_bit": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.ooo_dl_bit-7",
        "DestaddSwitchid": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.switchid-8",
        "DestaddSubswitchid": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.subswitchid-9",
        "DestaddPortid": "fabricpath.fabricpathHeader.outerdestinationAddress.destadd.portid-10",
        "OutersrcAddressMacformat": "fabricpath.fabricpathHeader.outersrcAddress.macformat-11",
        "SrcaddEndnodeid1": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.endnodeid1-12",
        "SrcaddUbit": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.ubit-13",
        "SrcaddIbit": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.ibit-14",
        "SrcaddEndnodeid2": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.endnodeid2-15",
        "SrcaddResv": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.resv-16",
        "SrcaddOoo_dl_bit": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.ooo_dl_bit-17",
        "SrcaddSwitchid": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.switchid-18",
        "SrcaddSubswitchid": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.subswitchid-19",
        "SrcaddPortid": "fabricpath.fabricpathHeader.outersrcAddress.srcadd.portid-20",
        "FptagEtherType": "fabricpath.fabricpathHeader.fptag.etherType-21",
        "FptagFtag": "fabricpath.fabricpathHeader.fptag.ftag-22",
        "FptagTtl": "fabricpath.fabricpathHeader.fptag.ttl-23",
    }

    def __init__(self, parent, list_op=False):
        super(Fabricpath, self).__init__(parent, list_op)

    @property
    def OuterdestinationAddressMacformat(self):
        """
        Display Name: DA Mac Format
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OuterdestinationAddressMacformat"]),
        )

    @property
    def DestaddEndnodeid1(self):
        """
        Display Name: EndNodeId-[5:0]
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestaddEndnodeid1"])
        )

    @property
    def DestaddUbit(self):
        """
        Display Name: U/L bit
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DestaddUbit"]))

    @property
    def DestaddIbit(self):
        """
        Display Name: I/G Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Individual Address, 0, Group Address, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DestaddIbit"]))

    @property
    def DestaddEndnodeid2(self):
        """
        Display Name: EndNodeId-[7:6]
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestaddEndnodeid2"])
        )

    @property
    def DestaddResv(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DestaddResv"]))

    @property
    def DestaddOoo_dl_bit(self):
        """
        Display Name: OOO/DL Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestaddOoo_dl_bit"])
        )

    @property
    def DestaddSwitchid(self):
        """
        Display Name: Switch ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestaddSwitchid"])
        )

    @property
    def DestaddSubswitchid(self):
        """
        Display Name: Sub Switch ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DestaddSubswitchid"])
        )

    @property
    def DestaddPortid(self):
        """
        Display Name: Port ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DestaddPortid"]))

    @property
    def OutersrcAddressMacformat(self):
        """
        Display Name: SA Mac Format
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OutersrcAddressMacformat"])
        )

    @property
    def SrcaddEndnodeid1(self):
        """
        Display Name: EndNodeId-[5:0]
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcaddEndnodeid1"])
        )

    @property
    def SrcaddUbit(self):
        """
        Display Name: U/L bit
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcaddUbit"]))

    @property
    def SrcaddIbit(self):
        """
        Display Name: I/G Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: IndividualAddress, 0, GroupAddress, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcaddIbit"]))

    @property
    def SrcaddEndnodeid2(self):
        """
        Display Name: EndNodeId-[7:6]
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcaddEndnodeid2"])
        )

    @property
    def SrcaddResv(self):
        """
        Display Name: RSVD
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcaddResv"]))

    @property
    def SrcaddOoo_dl_bit(self):
        """
        Display Name: OOO/DL Bit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcaddOoo_dl_bit"])
        )

    @property
    def SrcaddSwitchid(self):
        """
        Display Name: Switch ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcaddSwitchid"])
        )

    @property
    def SrcaddSubswitchid(self):
        """
        Display Name: Sub Switch ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcaddSubswitchid"])
        )

    @property
    def SrcaddPortid(self):
        """
        Display Name: Port ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrcaddPortid"]))

    @property
    def FptagEtherType(self):
        """
        Display Name: EtherType
        Default Value: 0x8903
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FptagEtherType"])
        )

    @property
    def FptagFtag(self):
        """
        Display Name: FTag
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FptagFtag"]))

    @property
    def FptagTtl(self):
        """
        Display Name: TTL
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FptagTtl"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
