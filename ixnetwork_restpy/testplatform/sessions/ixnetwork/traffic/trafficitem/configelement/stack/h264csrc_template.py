from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class H264csrc(Base):
    __slots__ = ()
    _SDM_NAME = "h264_csrc"
    _SDM_ATT_MAP = {
        "HeaderCsrcList": "h264_csrc.header.csrcList-1",
    }

    def __init__(self, parent, list_op=False):
        super(H264csrc, self).__init__(parent, list_op)

    @property
    def HeaderCsrcList(self):
        """
        Display Name: CSRC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderCsrcList"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
