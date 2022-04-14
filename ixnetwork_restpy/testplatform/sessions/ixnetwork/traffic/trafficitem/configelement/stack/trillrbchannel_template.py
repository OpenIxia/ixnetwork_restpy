from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Trillrbchannel(Base):
    __slots__ = ()
    _SDM_NAME = "trill_rb_channel"
    _SDM_ATT_MAP = {
        "HeaderVersion": "trill_rb_channel.header.version-1",
        "HeaderRbridge_channel_protocol": "trill_rb_channel.header.rbridge_channel_protocol-2",
        "FlagsSilent_bit": "trill_rb_channel.header.flags.silent_bit-3",
        "FlagsMultihop": "trill_rb_channel.header.flags.multihop-4",
        "FlagsNative_bit": "trill_rb_channel.header.flags.native_bit-5",
        "FlagsAvailable_flags": "trill_rb_channel.header.flags.available_flags-6",
        "HeaderErr": "trill_rb_channel.header.err-7",
    }

    def __init__(self, parent, list_op=False):
        super(Trillrbchannel, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderRbridge_channel_protocol(self):
        """
        Display Name: Channel Protocol
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HeaderRbridge_channel_protocol"]),
        )

    @property
    def FlagsSilent_bit(self):
        """
        Display Name: Silent Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Off, 0, On, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsSilent_bit"])
        )

    @property
    def FlagsMultihop(self):
        """
        Display Name: Multi-Hop Bit
        Default Value: 1
        Value Format: decimal
        Available enum values: One-Hop, 0, Multi-Hop, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsMultihop"]))

    @property
    def FlagsNative_bit(self):
        """
        Display Name: Native Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Off, 0, On, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsNative_bit"])
        )

    @property
    def FlagsAvailable_flags(self):
        """
        Display Name: Available Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsAvailable_flags"])
        )

    @property
    def HeaderErr(self):
        """
        Display Name: ERR
        Default Value: 0
        Value Format: decimal
        Available enum values: Not an RBridge Channel error frame, 0, Frame too short (truncated Ethertype or RBridge Channel Header), 1, Unrecognized Ethertype, 2, Unimplemented value of CHV, 3, Wrong value of NA flag, 4, Channel Protocol is reserved or unimplemented, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderErr"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
