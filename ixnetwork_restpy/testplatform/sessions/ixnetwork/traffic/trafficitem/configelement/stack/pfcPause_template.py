from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PfcPause(Base):
    __slots__ = ()
    _SDM_NAME = "pfcPause"
    _SDM_ATT_MAP = {
        "HeaderDstAddress": "pfcPause.header.header.dstAddress-1",
        "HeaderSrcAddress": "pfcPause.header.header.srcAddress-2",
        "HeaderEthertype": "pfcPause.header.header.ethertype-3",
        "MacControlControlOpcode": "pfcPause.header.macControl.controlOpcode-4",
        "MacControlPriorityEnableVector": "pfcPause.header.macControl.priorityEnableVector-5",
        "PauseQuantaPfcQueue0": "pfcPause.header.macControl.pauseQuanta.pfcQueue0-6",
        "PauseQuantaPfcQueue1": "pfcPause.header.macControl.pauseQuanta.pfcQueue1-7",
        "PauseQuantaPfcQueue2": "pfcPause.header.macControl.pauseQuanta.pfcQueue2-8",
        "PauseQuantaPfcQueue3": "pfcPause.header.macControl.pauseQuanta.pfcQueue3-9",
        "PauseQuantaPfcQueue4": "pfcPause.header.macControl.pauseQuanta.pfcQueue4-10",
        "PauseQuantaPfcQueue5": "pfcPause.header.macControl.pauseQuanta.pfcQueue5-11",
        "PauseQuantaPfcQueue6": "pfcPause.header.macControl.pauseQuanta.pfcQueue6-12",
        "PauseQuantaPfcQueue7": "pfcPause.header.macControl.pauseQuanta.pfcQueue7-13",
    }

    def __init__(self, parent, list_op=False):
        super(PfcPause, self).__init__(parent, list_op)

    @property
    def HeaderDstAddress(self):
        """
        Display Name: Destination address
        Default Value: 01:80:C2:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderDstAddress"])
        )

    @property
    def HeaderSrcAddress(self):
        """
        Display Name: Source address
        Default Value: 00:00:AA:00:00:01
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcAddress"])
        )

    @property
    def HeaderEthertype(self):
        """
        Display Name: Ethertype
        Default Value: 0x8808
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderEthertype"])
        )

    @property
    def MacControlControlOpcode(self):
        """
        Display Name: Control opcode
        Default Value: 0x0101
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MacControlControlOpcode"])
        )

    @property
    def MacControlPriorityEnableVector(self):
        """
        Display Name: priority_enable_vector
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MacControlPriorityEnableVector"]),
        )

    @property
    def PauseQuantaPfcQueue0(self):
        """
        Display Name: PFC Queue 0
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue0"])
        )

    @property
    def PauseQuantaPfcQueue1(self):
        """
        Display Name: PFC Queue 1
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue1"])
        )

    @property
    def PauseQuantaPfcQueue2(self):
        """
        Display Name: PFC Queue 2
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue2"])
        )

    @property
    def PauseQuantaPfcQueue3(self):
        """
        Display Name: PFC Queue 3
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue3"])
        )

    @property
    def PauseQuantaPfcQueue4(self):
        """
        Display Name: PFC Queue 4
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue4"])
        )

    @property
    def PauseQuantaPfcQueue5(self):
        """
        Display Name: PFC Queue 5
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue5"])
        )

    @property
    def PauseQuantaPfcQueue6(self):
        """
        Display Name: PFC Queue 6
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue6"])
        )

    @property
    def PauseQuantaPfcQueue7(self):
        """
        Display Name: PFC Queue 7
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PauseQuantaPfcQueue7"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
