from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Icmpv2(Base):
    __slots__ = ()
    _SDM_NAME = "icmpv2"
    _SDM_ATT_MAP = {
        "MessageMessageType": "icmpv2.message.messageType-1",
        "MessageCodeValue": "icmpv2.message.codeValue-2",
        "MessageIcmpChecksum": "icmpv2.message.icmpChecksum-3",
        "MessageIdentifier": "icmpv2.message.identifier-4",
        "MessageSequenceNumber": "icmpv2.message.sequenceNumber-5",
        "NextFieldsNone": "icmpv2.message.nextFields.none-6",
        "NextFieldsNone": "icmpv2.message.nextFields.none-7",
        "FieldsForTimeStampMsgOrigTmpStmp1": "icmpv2.message.nextFields.fieldsForTimeStampMsg.origTmpStmp1-8",
        "FieldsForTimeStampMsgRcvTmpStmp1": "icmpv2.message.nextFields.fieldsForTimeStampMsg.rcvTmpStmp1-9",
        "FieldsForTimeStampMsgTransTmpStmp1": "icmpv2.message.nextFields.fieldsForTimeStampMsg.transTmpStmp1-10",
        "FieldsForTimeStampReplyOrigTmpStmp2": "icmpv2.message.nextFields.fieldsForTimeStampReply.origTmpStmp2-11",
        "FieldsForTimeStampReplyRcvTmpStmp2": "icmpv2.message.nextFields.fieldsForTimeStampReply.rcvTmpStmp2-12",
        "FieldsForTimeStampReplyTransTmpStmp2": "icmpv2.message.nextFields.fieldsForTimeStampReply.transTmpStmp2-13",
        "NextFieldsNone": "icmpv2.message.nextFields.none-14",
        "NextFieldsNone": "icmpv2.message.nextFields.none-15",
    }

    def __init__(self, parent, list_op=False):
        super(Icmpv2, self).__init__(parent, list_op)

    @property
    def MessageMessageType(self):
        """
        Display Name: Message type
        Default Value: 8
        Value Format: decimal
        Available enum values: Echo reply, 0, Echo message, 8, TimeStamp message, 13, TimeStamp reply, 14, Information Request, 15, Information Reply, 16
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageMessageType"])
        )

    @property
    def MessageCodeValue(self):
        """
        Display Name: Code value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageCodeValue"])
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
    def MessageIdentifier(self):
        """
        Display Name: Identifier
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageIdentifier"])
        )

    @property
    def MessageSequenceNumber(self):
        """
        Display Name: Sequence number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageSequenceNumber"])
        )

    @property
    def NextFieldsNone(self):
        """
        Display Name: None
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextFieldsNone"])
        )

    @property
    def NextFieldsNone(self):
        """
        Display Name: None
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextFieldsNone"])
        )

    @property
    def FieldsForTimeStampMsgOrigTmpStmp1(self):
        """
        Display Name: Originate Timestamp in Msg:15
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FieldsForTimeStampMsgOrigTmpStmp1"]),
        )

    @property
    def FieldsForTimeStampMsgRcvTmpStmp1(self):
        """
        Display Name: Receive Timestamp in Msg:15
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FieldsForTimeStampMsgRcvTmpStmp1"]),
        )

    @property
    def FieldsForTimeStampMsgTransTmpStmp1(self):
        """
        Display Name: Transmit Timestamp in Msg:15
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FieldsForTimeStampMsgTransTmpStmp1"]
            ),
        )

    @property
    def FieldsForTimeStampReplyOrigTmpStmp2(self):
        """
        Display Name: Originate Timestamp in Msg:16
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FieldsForTimeStampReplyOrigTmpStmp2"]
            ),
        )

    @property
    def FieldsForTimeStampReplyRcvTmpStmp2(self):
        """
        Display Name: Receive Timestamp in Msg:16
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FieldsForTimeStampReplyRcvTmpStmp2"]
            ),
        )

    @property
    def FieldsForTimeStampReplyTransTmpStmp2(self):
        """
        Display Name: Transmit Timestamp in Msg:16
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FieldsForTimeStampReplyTransTmpStmp2"]
            ),
        )

    @property
    def NextFieldsNone(self):
        """
        Display Name: None
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextFieldsNone"])
        )

    @property
    def NextFieldsNone(self):
        """
        Display Name: None
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextFieldsNone"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
