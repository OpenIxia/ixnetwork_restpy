from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Iec61883624BitData(Base):
    __slots__ = ()
    _SDM_NAME = "iec61883-6_24-BitData"
    _SDM_ATT_MAP = {
        "GenericAM824Label1": "iec61883-6_24-BitData.genericAM824.label1-1",
        "GenericAM824Audio_sample": "iec61883-6_24-BitData.genericAM824.audio_sample-2",
        "GenericAM824Label_2": "iec61883-6_24-BitData.genericAM824.label_2-3",
        "GenericAM824Audio_sample": "iec61883-6_24-BitData.genericAM824.audio_sample-4",
    }

    def __init__(self, parent, list_op=False):
        super(Iec61883624BitData, self).__init__(parent, list_op)

    @property
    def GenericAM824Label1(self):
        """
        Display Name: Label(Left channel)
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericAM824Label1"])
        )

    @property
    def GenericAM824Audio_sample(self):
        """
        Display Name: 24-Bit Audio Sample(Left channel)
        Default Value: 0x000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericAM824Audio_sample"])
        )

    @property
    def GenericAM824Label_2(self):
        """
        Display Name: Label(Right channel)
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericAM824Label_2"])
        )

    @property
    def GenericAM824Audio_sample(self):
        """
        Display Name: 24-Bit Audio Sample(Right channel)
        Default Value: 0x000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericAM824Audio_sample"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
