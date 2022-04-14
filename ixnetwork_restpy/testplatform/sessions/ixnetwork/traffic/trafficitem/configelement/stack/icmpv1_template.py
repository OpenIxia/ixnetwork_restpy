from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Icmpv1(Base):
    __slots__ = ()
    _SDM_NAME = "icmpv1"
    _SDM_ATT_MAP = {
        "MessageMessageType": "icmpv1.message.messageType-1",
        "CodeOptionsDestUnreachableCodeOptions": "icmpv1.message.codeOptions.destUnreachableCodeOptions-2",
        "CodeOptionsSrcQuenchOption": "icmpv1.message.codeOptions.srcQuenchOption-3",
        "CodeOptionsInfoRequestOption": "icmpv1.message.codeOptions.infoRequestOption-4",
        "CodeOptionsInfoResponseOption": "icmpv1.message.codeOptions.infoResponseOption-5",
        "CodeOptionsTimeExceededOptions": "icmpv1.message.codeOptions.timeExceededOptions-6",
        "CodeOptionsRedirectMessageOptions": "icmpv1.message.codeOptions.redirectMessageOptions-7",
        "MessageIcmpChecksum": "icmpv1.message.icmpChecksum-8",
        "Next4BytesUnusedBitsInMsgType3": "icmpv1.message.next4Bytes.unusedBitsInMsgType3-9",
        "Next4BytesUnusedBitsInMsgType4": "icmpv1.message.next4Bytes.unusedBitsInMsgType4-10",
        "Next4BytesUnusedBitsInMsgType11": "icmpv1.message.next4Bytes.unusedBitsInMsgType11-11",
        "NextFieldsForParameterProblemPointer": "icmpv1.message.next4Bytes.nextFieldsForParameterProblem.pointer-12",
        "NextFieldsForParameterProblemUnused": "icmpv1.message.next4Bytes.nextFieldsForParameterProblem.unused-13",
        "Next4BytesGatewayInternetAddress": "icmpv1.message.next4Bytes.gatewayInternetAddress-14",
    }

    def __init__(self, parent, list_op=False):
        super(Icmpv1, self).__init__(parent, list_op)

    @property
    def MessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 3
        Value Format: decimal
        Available enum values: Dest. Unreachable, 3, Src. Quench, 4, Redirect Message, 5, Time Exceeded, 11, Parameter Problem, 12
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageMessageType"])
        )

    @property
    def CodeOptionsDestUnreachableCodeOptions(self):
        """
        Display Name: Dest. Unreachable code options
        Default Value: 0
        Value Format: decimal
        Available enum values: Net unreachable, 0, Host unreachable, 1, Protocol unreachable, 2, Port unreachable, 3, Fragmentation needed and DF set, 4, Source route failed, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CodeOptionsDestUnreachableCodeOptions"]
            ),
        )

    @property
    def CodeOptionsSrcQuenchOption(self):
        """
        Display Name: Src. Quench option
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CodeOptionsSrcQuenchOption"])
        )

    @property
    def CodeOptionsInfoRequestOption(self):
        """
        Display Name: Info Request option
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CodeOptionsInfoRequestOption"])
        )

    @property
    def CodeOptionsInfoResponseOption(self):
        """
        Display Name: Info Response option
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CodeOptionsInfoResponseOption"]),
        )

    @property
    def CodeOptionsTimeExceededOptions(self):
        """
        Display Name: Time Exceeded options
        Default Value: 0
        Value Format: decimal
        Available enum values: TTL exceeded in transit, 0, Fragment reassembly time exceeded, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CodeOptionsTimeExceededOptions"]),
        )

    @property
    def CodeOptionsRedirectMessageOptions(self):
        """
        Display Name: Redirect Message options
        Default Value: 0
        Value Format: decimal
        Available enum values: Redirect datagrams for network, 0, Redirect datagrams for the Host, 1, Redirect datagrams for the TOS and network, 2, Redirect datagrams for the TOS and host, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["CodeOptionsRedirectMessageOptions"]),
        )

    @property
    def MessageIcmpChecksum(self):
        """
        Display Name: ICMP checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageIcmpChecksum"])
        )

    @property
    def Next4BytesUnusedBitsInMsgType3(self):
        """
        Display Name: Unused bits in Msg type 3
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Next4BytesUnusedBitsInMsgType3"]),
        )

    @property
    def Next4BytesUnusedBitsInMsgType4(self):
        """
        Display Name: Unused bits in Msg type 4
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Next4BytesUnusedBitsInMsgType4"]),
        )

    @property
    def Next4BytesUnusedBitsInMsgType11(self):
        """
        Display Name: Unused bits in Msg type 11
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Next4BytesUnusedBitsInMsgType11"]),
        )

    @property
    def NextFieldsForParameterProblemPointer(self):
        """
        Display Name: Pointer
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextFieldsForParameterProblemPointer"]
            ),
        )

    @property
    def NextFieldsForParameterProblemUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["NextFieldsForParameterProblemUnused"]
            ),
        )

    @property
    def Next4BytesGatewayInternetAddress(self):
        """
        Display Name: Gateway Internet Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Next4BytesGatewayInternetAddress"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
