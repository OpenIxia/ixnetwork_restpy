from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SdiVideoFormat(Base):
    __slots__ = ()
    _SDM_NAME = "sdiVideoFormat"
    _SDM_ATT_MAP = {
        "SdiHeaderMap": "sdiVideoFormat.sdiHeader.Map-1",
        "SdiHeaderSample": "sdiVideoFormat.sdiHeader.sample-2",
        "SdiHeaderFrame": "sdiVideoFormat.sdiHeader.frame-3",
        "SdiHeaderFrameRate": "sdiVideoFormat.sdiHeader.frameRate-4",
        "SdiHeaderFrameCount": "sdiVideoFormat.sdiHeader.frameCount-5",
    }

    def __init__(self, parent, list_op=False):
        super(SdiVideoFormat, self).__init__(parent, list_op)

    @property
    def SdiHeaderMap(self):
        """
        Display Name: Map
        Default Value: 0xf
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SdiHeaderMap"]))

    @property
    def SdiHeaderSample(self):
        """
        Display Name: Sample
        Default Value: 0xf
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SdiHeaderSample"])
        )

    @property
    def SdiHeaderFrame(self):
        """
        Display Name: Frame
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SdiHeaderFrame"])
        )

    @property
    def SdiHeaderFrameRate(self):
        """
        Display Name: Frame rate
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SdiHeaderFrameRate"])
        )

    @property
    def SdiHeaderFrameCount(self):
        """
        Display Name: Frame Count
        Default Value: 0xff
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SdiHeaderFrameCount"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
