from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2TPv2Control(Base):
    __slots__ = ()
    _SDM_NAME = "l2TPv2Control"
    _SDM_ATT_MAP = {
        "ControlHeaderControlTBit": "l2TPv2Control.header.controlHeader.controlTBit-1",
        "ControlHeaderControlLBit": "l2TPv2Control.header.controlHeader.controlLBit-2",
        "ControlHeaderXBit": "l2TPv2Control.header.controlHeader.xBit-3",
        "ControlHeaderX1Bit": "l2TPv2Control.header.controlHeader.x1Bit-4",
        "ControlHeaderControlSBit": "l2TPv2Control.header.controlHeader.controlSBit-5",
        "ControlHeaderControlFlags": "l2TPv2Control.header.controlHeader.controlFlags-6",
        "ControlHeaderVer": "l2TPv2Control.header.controlHeader.ver-7",
        "ControlHeaderControlLength": "l2TPv2Control.header.controlHeader.controlLength-8",
        "ControlHeaderTunnelId": "l2TPv2Control.header.controlHeader.tunnelId-9",
        "ControlHeaderSessionId": "l2TPv2Control.header.controlHeader.sessionId-10",
        "ControlHeaderNs": "l2TPv2Control.header.controlHeader.ns-11",
        "ControlHeaderNr": "l2TPv2Control.header.controlHeader.nr-12",
        "MessageTypeAvpMBit": "l2TPv2Control.header.messageTypeAvp.mBit-13",
        "MessageTypeAvpHBit": "l2TPv2Control.header.messageTypeAvp.hBit-14",
        "MessageTypeAvpRsvd4": "l2TPv2Control.header.messageTypeAvp.rsvd4-15",
        "MessageTypeAvpMtLength": "l2TPv2Control.header.messageTypeAvp.mtLength-16",
        "MessageTypeAvpMtVendorId": "l2TPv2Control.header.messageTypeAvp.mtVendorId-17",
        "MessageTypeAvpMtAttribute": "l2TPv2Control.header.messageTypeAvp.mtAttribute-18",
        "MessageTypeAvpMessageType": "l2TPv2Control.header.messageTypeAvp.messageType-19",
        "AvpMBit": "l2TPv2Control.header.nextAvp.avp.mBit-20",
        "AvpAvpHBit": "l2TPv2Control.header.nextAvp.avp.avpHBit-21",
        "AvpRsvd4": "l2TPv2Control.header.nextAvp.avp.rsvd4-22",
        "AvpAvpLength": "l2TPv2Control.header.nextAvp.avp.avpLength-23",
        "AvpVendorId": "l2TPv2Control.header.nextAvp.avp.vendorId-24",
        "AvpAttributeType": "l2TPv2Control.header.nextAvp.avp.attributeType-25",
        "HBitIsOffLength1": "l2TPv2Control.header.nextAvp.avp.attributeValue.hBitIsOff.length1-26",
        "HBitIsOffData1": "l2TPv2Control.header.nextAvp.avp.attributeValue.hBitIsOff.data1-27",
        "HBitIsOnLength2": "l2TPv2Control.header.nextAvp.avp.attributeValue.hBitIsOn.length2-28",
        "HBitIsOnData2": "l2TPv2Control.header.nextAvp.avp.attributeValue.hBitIsOn.data2-29",
        "PaddingPadLength": "l2TPv2Control.header.nextAvp.avp.attributeValue.hBitIsOn.padding.padLength-30",
        "PaddingData3": "l2TPv2Control.header.nextAvp.avp.attributeValue.hBitIsOn.padding.data3-31",
    }

    def __init__(self, parent, list_op=False):
        super(L2TPv2Control, self).__init__(parent, list_op)

    @property
    def ControlHeaderControlTBit(self):
        """
        Display Name: Type bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Control message, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderControlTBit"])
        )

    @property
    def ControlHeaderControlLBit(self):
        """
        Display Name: Length bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Length field present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderControlLBit"])
        )

    @property
    def ControlHeaderXBit(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderXBit"])
        )

    @property
    def ControlHeaderX1Bit(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderX1Bit"])
        )

    @property
    def ControlHeaderControlSBit(self):
        """
        Display Name: Sequence bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Ns and Nr fields present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderControlSBit"])
        )

    @property
    def ControlHeaderControlFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderControlFlags"])
        )

    @property
    def ControlHeaderVer(self):
        """
        Display Name: Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderVer"])
        )

    @property
    def ControlHeaderControlLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderControlLength"])
        )

    @property
    def ControlHeaderTunnelId(self):
        """
        Display Name: Tunnel ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderTunnelId"])
        )

    @property
    def ControlHeaderSessionId(self):
        """
        Display Name: Session ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ControlHeaderSessionId"])
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
    def MessageTypeAvpMBit(self):
        """
        Display Name: Mandatory bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Discard on unrecognised message type, 0, Terminate on unrecognised message type, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpMBit"])
        )

    @property
    def MessageTypeAvpHBit(self):
        """
        Display Name: Hidden bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not hide AVP attribute values, 0
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpHBit"])
        )

    @property
    def MessageTypeAvpRsvd4(self):
        """
        Display Name: Reserved bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpRsvd4"])
        )

    @property
    def MessageTypeAvpMtLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpMtLength"])
        )

    @property
    def MessageTypeAvpMtVendorId(self):
        """
        Display Name: Vendor ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpMtVendorId"])
        )

    @property
    def MessageTypeAvpMtAttribute(self):
        """
        Display Name: Attribute type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpMtAttribute"])
        )

    @property
    def MessageTypeAvpMessageType(self):
        """
        Display Name: Message type
        Default Value: 4
        Value Format: decimal
        Available enum values: Start-Control-Connection-Request, 1, Start-Control-Connection-Reply, 2, Start-Control-Connection-Connected, 3, Stop-Control-Connection-Notification, 4, Hello, 6, Outgoing-Call-Request, 7, Outgoing-Call-Reply, 8, Outgoing-Call-Connected, 9, Incoming-Call-Request, 10, Incoming-Call-Reply, 11, Incoming-Call-Connected, 12, Call-Disconnect-Notify, 14, WAN-Error-Notify, 15, Set-Link-Info, 16
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageTypeAvpMessageType"])
        )

    @property
    def AvpMBit(self):
        """
        Display Name: Mandatory bit
        Default Value: 1
        Value Format: decimal
        Available enum values: Discard on unrecognised message type, 0, Terminate on unrecognised message type, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpMBit"]))

    @property
    def AvpAvpHBit(self):
        """
        Display Name: Hidden bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Do not hide AVP attribute values, 0, Hide AVP attribute values, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpAvpHBit"]))

    @property
    def AvpRsvd4(self):
        """
        Display Name: Reserved bits
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AvpRsvd4"]))

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
    def AvpAttributeType(self):
        """
        Display Name: Attribute type
        Default Value: 1
        Value Format: decimal
        Available enum values: Message Type, 0, Result Code, 1, Protocol Version, 2, Framing Capabilities, 3, Bearer Capabilities, 4, Tie Breaker, 5, Firmware Revision, 6, Host Name, 7, Vendor Name, 8, Assigned Tunnel ID, 9, Receive Window Size, 10, Challenge, 11, Q.931 Cause Code, 12, Challenge Response, 13, Assigned Session ID, 14, Call Serial Number, 15, Minimum BPS, 16, Maximum BPS, 17, Bearer Type, 18, Framing Type, 19, Called Number, 21, Calling Number, 22, Sub-Address, 23, Tx Connect Speed BPS, 24, Physical Channel ID, 25, Initial Received LCP CONFREQ, 26, Last Sent LCP CONFREQ, 27, Last Received LCP CONFREQ, 28, Proxy Authen Type, 29, Proxy Authen Name, 30, Proxy Authen Challenge, 31, Proxy Authen ID, 32, Proxy Authen Response, 33, Call Errors, 34, ACCM, 35, Random Vector, 36, Private Group ID, 37, Rx Connect Speed, 38, Sequencing Required, 39
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AvpAttributeType"])
        )

    @property
    def HBitIsOffLength1(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HBitIsOffLength1"])
        )

    @property
    def HBitIsOffData1(self):
        """
        Display Name: Data
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HBitIsOffData1"])
        )

    @property
    def HBitIsOnLength2(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HBitIsOnLength2"])
        )

    @property
    def HBitIsOnData2(self):
        """
        Display Name: Data
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HBitIsOnData2"]))

    @property
    def PaddingPadLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PaddingPadLength"])
        )

    @property
    def PaddingData3(self):
        """
        Display Name: Data
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PaddingData3"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
