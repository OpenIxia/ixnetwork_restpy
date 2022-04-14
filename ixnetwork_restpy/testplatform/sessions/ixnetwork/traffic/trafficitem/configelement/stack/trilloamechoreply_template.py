from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Trilloamechoreply(Base):
    __slots__ = ()
    _SDM_NAME = "trill_oam_echo_reply"
    _SDM_ATT_MAP = {
        "HeaderSpid": "trill_oam_echo_reply.header.spid-1",
        "HeaderSequence": "trill_oam_echo_reply.header.sequence-2",
        "HeaderTlv_total_length": "trill_oam_echo_reply.header.tlv_total_length-3",
        "DefaultTlv_code": "trill_oam_echo_reply.header..tlv_code-4",
        "DefaultTlv_length": "trill_oam_echo_reply.header..tlv_length-5",
        "DefaultTlv_value": "trill_oam_echo_reply.header..tlv_value-6",
    }

    def __init__(self, parent, list_op=False):
        super(Trilloamechoreply, self).__init__(parent, list_op)

    @property
    def HeaderSpid(self):
        """
        Display Name: SPID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSpid"]))

    @property
    def HeaderSequence(self):
        """
        Display Name: Sequence Number
        Default Value: 0x0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSequence"])
        )

    @property
    def HeaderTlv_total_length(self):
        """
        Display Name: TLV Total Length
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTlv_total_length"])
        )

    @property
    def DefaultTlv_code(self):
        """
        Display Name: TLV Type (IS-IS System ID)
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultTlv_code"])
        )

    @property
    def DefaultTlv_length(self):
        """
        Display Name: TLV Length
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultTlv_length"])
        )

    @property
    def DefaultTlv_value(self):
        """
        Display Name: TLV Value (System ID)
        Default Value: 00:00:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultTlv_value"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
