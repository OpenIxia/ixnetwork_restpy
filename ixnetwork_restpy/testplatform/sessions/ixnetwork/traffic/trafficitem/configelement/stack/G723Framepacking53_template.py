from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class G723Framepacking53(Base):
    __slots__ = ()
    _SDM_NAME = "G723Framepacking5.3"
    _SDM_ATT_MAP = {
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-1",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-2",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-3",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-4",
        "G723MainHeaderHdr": "G723Framepacking5.3.G723MainHeader.hdr-5",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-6",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-7",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-8",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-9",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-10",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-11",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-12",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-13",
        "G723MainHeaderAcl0": "G723Framepacking5.3.G723MainHeader.acl0-14",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-15",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-16",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-17",
        "G723MainHeaderLpc": "G723Framepacking5.3.G723MainHeader.lpc-18",
        "G723MainHeaderAcl2": "G723Framepacking5.3.G723MainHeader.acl2-19",
        "G723MainHeaderAcl2": "G723Framepacking5.3.G723MainHeader.acl2-20",
        "G723MainHeaderAcl1": "G723Framepacking5.3.G723MainHeader.acl1-21",
        "G723MainHeaderAc": "G723Framepacking5.3.G723MainHeader.ac-22",
        "G723MainHeaderGain0": "G723Framepacking5.3.G723MainHeader.gain0-23",
        "G723MainHeaderGain0": "G723Framepacking5.3.G723MainHeader.gain0-24",
        "G723MainHeaderAcl3": "G723Framepacking5.3.G723MainHeader.acl3-25",
        "G723MainHeaderAcl2": "G723Framepacking5.3.G723MainHeader.acl2-26",
        "G723MainHeaderAcl2": "G723Framepacking5.3.G723MainHeader.acl2-27",
        "G723MainHeaderGain0": "G723Framepacking5.3.G723MainHeader.gain0-28",
        "G723MainHeaderGain0": "G723Framepacking5.3.G723MainHeader.gain0-29",
        "G723MainHeaderGain1": "G723Framepacking5.3.G723MainHeader.gain1-30",
        "G723MainHeaderGain1": "G723Framepacking5.3.G723MainHeader.gain1-31",
        "G723MainHeaderGain2": "G723Framepacking5.3.G723MainHeader.gain2-32",
        "G723MainHeaderGain2": "G723Framepacking5.3.G723MainHeader.gain2-33",
        "G723MainHeaderGain1": "G723Framepacking5.3.G723MainHeader.gain1-34",
        "G723MainHeaderGain1": "G723Framepacking5.3.G723MainHeader.gain1-35",
        "G723MainHeaderGain2": "G723Framepacking5.3.G723MainHeader.gain2-36",
        "G723MainHeaderGain2": "G723Framepacking5.3.G723MainHeader.gain2-37",
        "G723MainHeaderGain3": "G723Framepacking5.3.G723MainHeader.gain3-38",
        "G723MainHeaderGain3": "G723Framepacking5.3.G723MainHeader.gain3-39",
        "G723MainHeaderGrid": "G723Framepacking5.3.G723MainHeader.grid-40",
        "G723MainHeaderGain3": "G723Framepacking5.3.G723MainHeader.gain3-41",
        "G723MainHeaderGain3": "G723Framepacking5.3.G723MainHeader.gain3-42",
        "G723MainHeaderPos0": "G723Framepacking5.3.G723MainHeader.pos0-43",
        "G723MainHeaderPos0": "G723Framepacking5.3.G723MainHeader.pos0-44",
        "G723MainHeaderPos1": "G723Framepacking5.3.G723MainHeader.pos1-45",
        "G723MainHeaderPos1": "G723Framepacking5.3.G723MainHeader.pos1-46",
        "G723MainHeaderPos0": "G723Framepacking5.3.G723MainHeader.pos0-47",
        "G723MainHeaderPos0": "G723Framepacking5.3.G723MainHeader.pos0-48",
        "G723MainHeaderPos1": "G723Framepacking5.3.G723MainHeader.pos1-49",
        "G723MainHeaderPos1": "G723Framepacking5.3.G723MainHeader.pos1-50",
        "G723MainHeaderPos2": "G723Framepacking5.3.G723MainHeader.pos2-51",
        "G723MainHeaderPos2": "G723Framepacking5.3.G723MainHeader.pos2-52",
        "G723MainHeaderPos3": "G723Framepacking5.3.G723MainHeader.pos3-53",
        "G723MainHeaderPos3": "G723Framepacking5.3.G723MainHeader.pos3-54",
        "G723MainHeaderPos2": "G723Framepacking5.3.G723MainHeader.pos2-55",
        "G723MainHeaderPos2": "G723Framepacking5.3.G723MainHeader.pos2-56",
        "G723MainHeaderPos3": "G723Framepacking5.3.G723MainHeader.pos3-57",
        "G723MainHeaderPos3": "G723Framepacking5.3.G723MainHeader.pos3-58",
        "G723MainHeaderPsig1": "G723Framepacking5.3.G723MainHeader.psig1-59",
        "G723MainHeaderPsig0": "G723Framepacking5.3.G723MainHeader.psig0-60",
        "G723MainHeaderPsig3": "G723Framepacking5.3.G723MainHeader.psig3-61",
        "G723MainHeaderPsig2": "G723Framepacking5.3.G723MainHeader.psig2-62",
        "G723MainHeaderPsig3": "G723Framepacking5.3.G723MainHeader.psig3-63",
        "G723MainHeaderPsig2": "G723Framepacking5.3.G723MainHeader.psig2-64",
    }

    def __init__(self, parent, list_op=False):
        super(G723Framepacking53, self).__init__(parent, list_op)

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
