from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2TPv3ControlIP(Base):
    __slots__ = ()
    _SDM_NAME = "l2TPv3ControlIP"
    _SDM_ATT_MAP = {
        "ControlHeaderZeroSessionId": "l2TPv3ControlIP.header.controlHeader.zeroSessionId-1",
        "ControlHeaderControlMask": "l2TPv3ControlIP.header.controlHeader.controlMask-2",
        "ControlHeaderVersion": "l2TPv3ControlIP.header.controlHeader.version-3",
        "ControlHeaderLength": "l2TPv3ControlIP.header.controlHeader.length-4",
        "ControlHeaderConnectionId": "l2TPv3ControlIP.header.controlHeader.connectionId-5",
        "ControlHeaderNs": "l2TPv3ControlIP.header.controlHeader.ns-6",
        "ControlHeaderNr": "l2TPv3ControlIP.header.controlHeader.nr-7",
        "MessageTypeAvpMandatory": "l2TPv3ControlIP.header.messageTypeAvp.mandatory-8",
        "MessageTypeAvpHidden": "l2TPv3ControlIP.header.messageTypeAvp.hidden-9",
        "MessageTypeAvpReserved": "l2TPv3ControlIP.header.messageTypeAvp.reserved-10",
        "MessageTypeAvpLength": "l2TPv3ControlIP.header.messageTypeAvp.length-11",
        "MessageTypeAvpVendorId": "l2TPv3ControlIP.header.messageTypeAvp.vendorId-12",
        "MessageTypeAvpAttributeType": "l2TPv3ControlIP.header.messageTypeAvp.attributeType-13",
        "MessageTypeAvpMessageType": "l2TPv3ControlIP.header.messageTypeAvp.messageType-14",
        "AvpMandatory": "l2TPv3ControlIP.header.nextAvp.avp.mandatory-15",
        "AvpHidden": "l2TPv3ControlIP.header.nextAvp.avp.hidden-16",
        "AvpReserved": "l2TPv3ControlIP.header.nextAvp.avp.reserved-17",
        "AvpAvpLength": "l2TPv3ControlIP.header.nextAvp.avp.avpLength-18",
        "AvpVendorId": "l2TPv3ControlIP.header.nextAvp.avp.vendorId-19",
        "IetfAvpIetfAttributeType": "l2TPv3ControlIP.header.nextAvp.avp.attributeType.ietfAvp.ietfAttributeType-20",
        "CiscoAvpCiscoAttrType": "l2TPv3ControlIP.header.nextAvp.avp.attributeType.ciscoAvp.ciscoAttrType-21",
        "HiddenOffLength": "l2TPv3ControlIP.header.nextAvp.avp.value.hiddenOff.length-22",
        "HiddenOffData": "l2TPv3ControlIP.header.nextAvp.avp.value.hiddenOff.data-23",
        "HidderOnLength": "l2TPv3ControlIP.header.nextAvp.avp.value.hidderOn.length-24",
        "HidderOnData": "l2TPv3ControlIP.header.nextAvp.avp.value.hidderOn.data-25",
        "PaddingLength": "l2TPv3ControlIP.header.nextAvp.avp.value.hidderOn.padding.length-26",
        "PaddingData": "l2TPv3ControlIP.header.nextAvp.avp.value.hidderOn.padding.data-27",
    }

    def __init__(self, parent, list_op=False):
        super(L2TPv3ControlIP, self).__init__(parent, list_op)

    @property
    def ControlHeaderZeroSessionId(self):
        """
        Display Name: Session ID (zero)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderZeroSessionId"])
        )

    @property
    def ControlHeaderControlMask(self):
        """
        Display Name: Control message bitmask
        Default Value: 0xC80
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderControlMask"])
        )

    @property
    def ControlHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderVersion"])
        )

    @property
    def ControlHeaderLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderLength"])
        )

    @property
    def ControlHeaderConnectionId(self):
        """
        Display Name: Control Connnection ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderConnectionId"])
        )

    @property
    def ControlHeaderNs(self):
        """
        Display Name: Sequence number for this message
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderNs"])
        )

    @property
    def ControlHeaderNr(self):
        """
        Display Name: Sequence number expected next message
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderNr"])
        )

    @property
    def MessageTypeAvpMandatory(self):
        """
        Display Name: Mandatory bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Discard on unrecognised message type, 0, Terminate on unrecognised message type, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpMandatory"])
        )

    @property
    def MessageTypeAvpHidden(self):
        """
        Display Name: Hidden bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpHidden"])
        )

    @property
    def MessageTypeAvpReserved(self):
        """
        Display Name: Reserved bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpReserved"])
        )

    @property
    def MessageTypeAvpLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpLength"])
        )

    @property
    def MessageTypeAvpVendorId(self):
        """
        Display Name: Vendor ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpVendorId"])
        )

    @property
    def MessageTypeAvpAttributeType(self):
        """
        Display Name: Attribute type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpAttributeType"])
        )

    @property
    def MessageTypeAvpMessageType(self):
        """
        Display Name: Message type
        Default Value: 4
        Value Format: decimal
        Available enum values: Start-Control-Connection-Request, 1, Start-Control-Connection-Reply, 2, Start-Control-Connection-Connected, 3, Stop-Control-Connection-Notification, 4, Hello, 6, Outgoing-Call-Request, 7, Outgoing-Call-Reply, 8, Outgoing-Call-Connected, 9, Incoming-Call-Request, 10, Incoming-Call-Reply, 11, Incoming-Call-Connected, 12, Call-Disconnect-Notify, 14, WAN-Error-Notify, 15, Set-Link-Info, 16, Explicit Acknowledgement, 20
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpMessageType"])
        )

    @property
    def AvpMandatory(self):
        """
        Display Name: Mandatory bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Discard on unrecognised message type, 0, Terminate on unrecognised message type, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpMandatory"]))

    @property
    def AvpHidden(self):
        """
        Display Name: Hidden bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpHidden"]))

    @property
    def AvpReserved(self):
        """
        Display Name: Reserved bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpReserved"]))

    @property
    def AvpAvpLength(self):
        """
        Display Name: Length
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpAvpLength"]))

    @property
    def AvpVendorId(self):
        """
        Display Name: Vendor ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpVendorId"]))

    @property
    def IetfAvpIetfAttributeType(self):
        """
        Display Name: IETF Attribute Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Result Code, 1, Protocol Version, 2, Framing Capabilities, 3, Bearer Capabilities, 4, Tie Breaker, 5, Firmward Revision, 6, Host Name, 7, Vendor Name, 8, Assigned Tunnel ID, 9, Receive Window Size, 10, Challenge, 11, Q.931 Cause Code, 12, Challenge Response, 13, Assigned Session ID, 14, Call Serial Number, 15, Minimum BPS, 16, Maximum BPS, 17, Bearer Type, 18, Framing Type, 19, Called Number, 21, Calling Number, 22, Sub-Address, 23, Tx Connect Speed BPS, 24, Physical Channel ID, 25, Initial Received LCP CONFREQ, 26, Last Sent LCP CONFREQ, 27, Last Received LCP CONFREQ, 28, Proxy Authen Type, 29, Proxy Authen Name, 30, Proxy Authen Challenge, 31, Proxy Authen ID, 32, Proxy Authen Response, 33, Call Errors, 34, ACCM, 35, Random Vector, 36, Private Group ID, 37, Rx Connect Speed, 38, Sequencing Required, 39, Extended Vendor ID AVP, 58, Message Digest, 59, Router ID, 60, Assigned Control Connection ID, 61, Pseudowire Capabilities List, 62, Local Session ID, 63, Remote Session ID, 64, Assigned Cookie, 65, Remote End ID, 66, Pseudowire Type, 68, L2-Specific Sublayer, 69, Data Sequencing, 70, Circuit Status, 71, Preferred Language, 72, Control Message Authentication Nonce, 73, Tx Connect Speed, 74, Rx Connect Speed, 75
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IetfAvpIetfAttributeType"])
        )

    @property
    def CiscoAvpCiscoAttrType(self):
        """
        Display Name: CISCO Attribute Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Assigned Control Connection ID, 1, Pseudowire Capabilities List, 2, Local Session ID, 3, Remote Session ID, 4, Assigned Cookie, 5, Remote End ID, 6, Pseudowire Type, 7, Circuit Status, 8, Session Tie Breaker, 9, ATM Maximum Concatenated Cells, 11, Message Digest, 12, Control Message Authentication Nonce, 13, Layer 2-Specific Sublayer, 69, OAM Emulation Required, 108, ATM Alarm Status, 109
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CiscoAvpCiscoAttrType"])
        )

    @property
    def HiddenOffLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HiddenOffLength"])
        )

    @property
    def HiddenOffData(self):
        """
        Display Name: Data
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HiddenOffData"]))

    @property
    def HidderOnLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HidderOnLength"])
        )

    @property
    def HidderOnData(self):
        """
        Display Name: Data
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HidderOnData"]))

    @property
    def PaddingLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PaddingLength"]))

    @property
    def PaddingData(self):
        """
        Display Name: Data
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PaddingData"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
