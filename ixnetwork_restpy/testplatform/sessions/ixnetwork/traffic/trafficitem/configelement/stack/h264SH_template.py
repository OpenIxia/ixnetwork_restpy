from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class H264SH(Base):
    __slots__ = ()
    _SDM_NAME = "h264SH"
    _SDM_ATT_MAP = {
        "H264SpecificHeaderF": "h264SH.h264SpecificHeader.F-1",
        "H264SpecificHeaderNRI": "h264SH.h264SpecificHeader.NRI-2",
        "H264SpecificHeaderNalUnitType": "h264SH.h264SpecificHeader.nalUnitType-3",
        "H264SpecificHeaderLength": "h264SH.h264SpecificHeader.length-4",
        "H264SpecificHeaderRawPayload": "h264SH.h264SpecificHeader.rawPayload-5",
        "H264SpecificHeaderPadding": "h264SH.h264SpecificHeader.Padding-6",
    }

    def __init__(self, parent, list_op=False):
        super(H264SH, self).__init__(parent, list_op)

    @property
    def H264SpecificHeaderF(self):
        """
        Display Name: F
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["H264SpecificHeaderF"])
        )

    @property
    def H264SpecificHeaderNRI(self):
        """
        Display Name: NRI
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["H264SpecificHeaderNRI"])
        )

    @property
    def H264SpecificHeaderNalUnitType(self):
        """
        Display Name: NAL Unit Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["H264SpecificHeaderNalUnitType"]),
        )

    @property
    def H264SpecificHeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["H264SpecificHeaderLength"])
        )

    @property
    def H264SpecificHeaderRawPayload(self):
        """
        Display Name: RAW Byte Sequence Payload
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["H264SpecificHeaderRawPayload"])
        )

    @property
    def H264SpecificHeaderPadding(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["H264SpecificHeaderPadding"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
