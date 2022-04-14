from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class G723Framepacking(Base):
    __slots__ = ()
    _SDM_NAME = "G723Framepacking"
    _SDM_ATT_MAP = {
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-1",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-2",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-3",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-4",
        "G723MainHeaderHdr": "G723Framepacking.G723MainHeader.hdr-5",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-6",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-7",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-8",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-9",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-10",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-11",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-12",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-13",
        "G723MainHeaderAcl0": "G723Framepacking.G723MainHeader.acl0-14",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-15",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-16",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-17",
        "G723MainHeaderLpc": "G723Framepacking.G723MainHeader.lpc-18",
        "G723MainHeaderAcl2": "G723Framepacking.G723MainHeader.acl2-19",
        "G723MainHeaderAcl2": "G723Framepacking.G723MainHeader.acl2-20",
        "G723MainHeaderAcl1": "G723Framepacking.G723MainHeader.acl1-21",
        "G723MainHeaderAc": "G723Framepacking.G723MainHeader.ac-22",
        "G723MainHeaderGain0": "G723Framepacking.G723MainHeader.gain0-23",
        "G723MainHeaderGain0": "G723Framepacking.G723MainHeader.gain0-24",
        "G723MainHeaderAcl3": "G723Framepacking.G723MainHeader.acl3-25",
        "G723MainHeaderAcl2": "G723Framepacking.G723MainHeader.acl2-26",
        "G723MainHeaderAcl2": "G723Framepacking.G723MainHeader.acl2-27",
        "G723MainHeaderGain0": "G723Framepacking.G723MainHeader.gain0-28",
        "G723MainHeaderGain0": "G723Framepacking.G723MainHeader.gain0-29",
        "G723MainHeaderGain1": "G723Framepacking.G723MainHeader.gain1-30",
        "G723MainHeaderGain1": "G723Framepacking.G723MainHeader.gain1-31",
        "G723MainHeaderGain2": "G723Framepacking.G723MainHeader.gain2-32",
        "G723MainHeaderGain2": "G723Framepacking.G723MainHeader.gain2-33",
        "G723MainHeaderGain1": "G723Framepacking.G723MainHeader.gain1-34",
        "G723MainHeaderGain1": "G723Framepacking.G723MainHeader.gain1-35",
        "G723MainHeaderGain2": "G723Framepacking.G723MainHeader.gain2-36",
        "G723MainHeaderGain2": "G723Framepacking.G723MainHeader.gain2-37",
        "G723MainHeaderGain3": "G723Framepacking.G723MainHeader.gain3-38",
        "G723MainHeaderGain3": "G723Framepacking.G723MainHeader.gain3-39",
        "G723MainHeaderGrid": "G723Framepacking.G723MainHeader.grid-40",
        "G723MainHeaderGain3": "G723Framepacking.G723MainHeader.gain3-41",
        "G723MainHeaderGain3": "G723Framepacking.G723MainHeader.gain3-42",
        "G723MainHeaderMsbPos": "G723Framepacking.G723MainHeader.msbPos-43",
        "G723MainHeaderMsbPos": "G723Framepacking.G723MainHeader.msbPos-44",
        "G723MainHeaderZ": "G723Framepacking.G723MainHeader.z-45",
        "G723MainHeaderPos": "G723Framepacking.G723MainHeader.pos-46",
        "G723MainHeaderMsbPos": "G723Framepacking.G723MainHeader.msbPos-47",
        "G723MainHeaderMsbPos": "G723Framepacking.G723MainHeader.msbPos-48",
        "G723MainHeaderPos0": "G723Framepacking.G723MainHeader.pos0-49",
        "G723MainHeaderPos0": "G723Framepacking.G723MainHeader.pos0-50",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-51",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-52",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-53",
        "G723MainHeaderPos0": "G723Framepacking.G723MainHeader.pos0-54",
        "G723MainHeaderPos0": "G723Framepacking.G723MainHeader.pos0-55",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-56",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-57",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-58",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-59",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-60",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-61",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-62",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-63",
        "G723MainHeaderPos1": "G723Framepacking.G723MainHeader.pos1-64",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-65",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-66",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-67",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-68",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-69",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-70",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-71",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-72",
        "G723MainHeaderPos2": "G723Framepacking.G723MainHeader.pos2-73",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-74",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-75",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-76",
        "G723MainHeaderPsig0": "G723Framepacking.G723MainHeader.psig0-77",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-78",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-79",
        "G723MainHeaderPos3": "G723Framepacking.G723MainHeader.pos3-80",
        "G723MainHeaderPsig2": "G723Framepacking.G723MainHeader.psig2-81",
        "G723MainHeaderPsig3": "G723Framepacking.G723MainHeader.psig3-82",
        "G723MainHeaderPsig2": "G723Framepacking.G723MainHeader.psig2-83",
        "G723MainHeaderPsig1": "G723Framepacking.G723MainHeader.psig1-84",
        "G723MainHeaderPsig2": "G723Framepacking.G723MainHeader.psig2-85",
        "G723MainHeaderPsig3": "G723Framepacking.G723MainHeader.psig3-86",
        "G723MainHeaderPsig2": "G723Framepacking.G723MainHeader.psig2-87",
        "G723MainHeaderPsig2": "G723Framepacking.G723MainHeader.psig2-88",
        "G723MainHeaderPsig3": "G723Framepacking.G723MainHeader.psig3-89",
        "G723MainHeaderPsig2": "G723Framepacking.G723MainHeader.psig2-90",
    }

    def __init__(self, parent, list_op=False):
        super(G723Framepacking, self).__init__(parent, list_op)

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderHdr(self):
        """
        Display Name: HDR
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderHdr"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderAcl0(self):
        """
        Display Name: ACL0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAcl0"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderLpc(self):
        """
        Display Name: LPC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderLpc"])
        )

    @property
    def G723MainHeaderAcl2(self):
        """
        Display Name: ACL2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAcl2"])
        )

    @property
    def G723MainHeaderAcl2(self):
        """
        Display Name: ACL2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAcl2"])
        )

    @property
    def G723MainHeaderAcl1(self):
        """
        Display Name: ACL1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAcl1"])
        )

    @property
    def G723MainHeaderAc(self):
        """
        Display Name: AC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAc"])
        )

    @property
    def G723MainHeaderGain0(self):
        """
        Display Name: GAIN0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain0"])
        )

    @property
    def G723MainHeaderGain0(self):
        """
        Display Name: GAIN0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain0"])
        )

    @property
    def G723MainHeaderAcl3(self):
        """
        Display Name: ACL3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAcl3"])
        )

    @property
    def G723MainHeaderAcl2(self):
        """
        Display Name: ACL2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAcl2"])
        )

    @property
    def G723MainHeaderAcl2(self):
        """
        Display Name: ACL2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderAcl2"])
        )

    @property
    def G723MainHeaderGain0(self):
        """
        Display Name: GAIN0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain0"])
        )

    @property
    def G723MainHeaderGain0(self):
        """
        Display Name: GAIN0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain0"])
        )

    @property
    def G723MainHeaderGain1(self):
        """
        Display Name: GAIN1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain1"])
        )

    @property
    def G723MainHeaderGain1(self):
        """
        Display Name: GAIN1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain1"])
        )

    @property
    def G723MainHeaderGain2(self):
        """
        Display Name: GAIN2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain2"])
        )

    @property
    def G723MainHeaderGain2(self):
        """
        Display Name: GAIN2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain2"])
        )

    @property
    def G723MainHeaderGain1(self):
        """
        Display Name: GAIN1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain1"])
        )

    @property
    def G723MainHeaderGain1(self):
        """
        Display Name: GAIN1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain1"])
        )

    @property
    def G723MainHeaderGain2(self):
        """
        Display Name: GAIN2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain2"])
        )

    @property
    def G723MainHeaderGain2(self):
        """
        Display Name: GAIN2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain2"])
        )

    @property
    def G723MainHeaderGain3(self):
        """
        Display Name: GAIN3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain3"])
        )

    @property
    def G723MainHeaderGain3(self):
        """
        Display Name: GAIN3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain3"])
        )

    @property
    def G723MainHeaderGrid(self):
        """
        Display Name: GRID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGrid"])
        )

    @property
    def G723MainHeaderGain3(self):
        """
        Display Name: GAIN3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain3"])
        )

    @property
    def G723MainHeaderGain3(self):
        """
        Display Name: GAIN3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderGain3"])
        )

    @property
    def G723MainHeaderMsbPos(self):
        """
        Display Name: MSBPOS
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderMsbPos"])
        )

    @property
    def G723MainHeaderMsbPos(self):
        """
        Display Name:  MSBPOS
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderMsbPos"])
        )

    @property
    def G723MainHeaderZ(self):
        """
        Display Name: Z
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderZ"])
        )

    @property
    def G723MainHeaderPos(self):
        """
        Display Name:  POS
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos"])
        )

    @property
    def G723MainHeaderMsbPos(self):
        """
        Display Name: MSBPOS
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderMsbPos"])
        )

    @property
    def G723MainHeaderMsbPos(self):
        """
        Display Name:  MSBPOS
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderMsbPos"])
        )

    @property
    def G723MainHeaderPos0(self):
        """
        Display Name:  POS0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos0"])
        )

    @property
    def G723MainHeaderPos0(self):
        """
        Display Name:  POS0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos0"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos0(self):
        """
        Display Name:  POS0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos0"])
        )

    @property
    def G723MainHeaderPos0(self):
        """
        Display Name:  POS0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos0"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos1(self):
        """
        Display Name:  POS1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos1"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos2(self):
        """
        Display Name:  POS2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos2"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPsig0(self):
        """
        Display Name:  PSIG0
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig0"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPos3(self):
        """
        Display Name:  POS3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPos3"])
        )

    @property
    def G723MainHeaderPsig2(self):
        """
        Display Name:  PSIG2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig2"])
        )

    @property
    def G723MainHeaderPsig3(self):
        """
        Display Name:  PSIG3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig3"])
        )

    @property
    def G723MainHeaderPsig2(self):
        """
        Display Name:  PSIG2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig2"])
        )

    @property
    def G723MainHeaderPsig1(self):
        """
        Display Name:  PSIG1
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig1"])
        )

    @property
    def G723MainHeaderPsig2(self):
        """
        Display Name:  PSIG2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig2"])
        )

    @property
    def G723MainHeaderPsig3(self):
        """
        Display Name:  PSIG3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig3"])
        )

    @property
    def G723MainHeaderPsig2(self):
        """
        Display Name:  PSIG2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig2"])
        )

    @property
    def G723MainHeaderPsig2(self):
        """
        Display Name:  PSIG2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig2"])
        )

    @property
    def G723MainHeaderPsig3(self):
        """
        Display Name:  PSIG3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig3"])
        )

    @property
    def G723MainHeaderPsig2(self):
        """
        Display Name:  PSIG2
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G723MainHeaderPsig2"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
