from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PppoEDiscovery(Base):
    __slots__ = ()
    _SDM_NAME = "pppoEDiscovery"
    _SDM_ATT_MAP = {
        "HeaderVersion": "pppoEDiscovery.header.header.version-1",
        "HeaderType": "pppoEDiscovery.header.header.type-2",
        "HeaderOpcode": "pppoEDiscovery.header.header.opcode-3",
        "HeaderSessionID": "pppoEDiscovery.header.header.sessionID-4",
        "HeaderPayloadLength": "pppoEDiscovery.header.header.payloadLength-5",
        "ServiceNameType": "pppoEDiscovery.header.tags.type.serviceName.type-6",
        "TlvLength": "pppoEDiscovery.header.tags.type.serviceName.tlv.length-7",
        "TlvValue": "pppoEDiscovery.header.tags.type.serviceName.tlv.value-8",
        "AcNameType": "pppoEDiscovery.header.tags.type.acName.type-9",
        "AcnameTlvLength": "pppoEDiscovery.header.tags.type.acName.tlv.length-10",
        "AcnameTlvValue": "pppoEDiscovery.header.tags.type.acName.tlv.value-11",
        "HostUniqType": "pppoEDiscovery.header.tags.type.hostUniq.type-12",
        "TypeLength": "pppoEDiscovery.header.tags.type.hostUniq.type.length-13",
        "TypeValue": "pppoEDiscovery.header.tags.type.hostUniq.type.value-14",
        "AcCookieType": "pppoEDiscovery.header.tags.type.acCookie.type-15",
        "AccookieTlvLength": "pppoEDiscovery.header.tags.type.acCookie.tlv.length-16",
        "AccookieTlvValue": "pppoEDiscovery.header.tags.type.acCookie.tlv.value-17",
        "VendorSpecificType": "pppoEDiscovery.header.tags.type.vendorSpecific.type-18",
        "VendorspecificTlvLength": "pppoEDiscovery.header.tags.type.vendorSpecific.tlv.length-19",
        "VendorspecificTlvValue": "pppoEDiscovery.header.tags.type.vendorSpecific.tlv.value-20",
        "RelaySessionIDType": "pppoEDiscovery.header.tags.type.relaySessionID.type-21",
        "RelaysessionidTlvLength": "pppoEDiscovery.header.tags.type.relaySessionID.tlv.length-22",
        "RelaysessionidTlvValue": "pppoEDiscovery.header.tags.type.relaySessionID.tlv.value-23",
        "ServiceNameErrorType": "pppoEDiscovery.header.tags.type.serviceNameError.type-24",
        "ServicenameerrorTlvLength": "pppoEDiscovery.header.tags.type.serviceNameError.tlv.length-25",
        "ServicenameerrorTlvValue": "pppoEDiscovery.header.tags.type.serviceNameError.tlv.value-26",
        "AcSystemErrorType": "pppoEDiscovery.header.tags.type.acSystemError.type-27",
        "AcsystemerrorTlvLength": "pppoEDiscovery.header.tags.type.acSystemError.tlv.length-28",
        "AcsystemerrorTlvValue": "pppoEDiscovery.header.tags.type.acSystemError.tlv.value-29",
        "GenericErrorType": "pppoEDiscovery.header.tags.type.genericError.type-30",
        "GenericerrorTlvLength": "pppoEDiscovery.header.tags.type.genericError.tlv.length-31",
        "GenericerrorTlvValue": "pppoEDiscovery.header.tags.type.genericError.tlv.value-32",
        "EndOfListType": "pppoEDiscovery.header.tags.type.endOfList.type-33",
        "EndOfListLength": "pppoEDiscovery.header.tags.type.endOfList.length-34",
    }

    def __init__(self, parent, list_op=False):
        super(PppoEDiscovery, self).__init__(parent, list_op)

    @property
    def HeaderVersion(self):
        """
        Display Name: PPPoE protocol version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderVersion"]))

    @property
    def HeaderType(self):
        """
        Display Name: PPPoE type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderType"]))

    @property
    def HeaderOpcode(self):
        """
        Display Name: PPPoE code options
        Default Value: 07
        Value Format: decimal
        Available enum values: PADO, 7, PADI, 9, PADR, 25, PADS, 101, PADT, 167
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderOpcode"]))

    @property
    def HeaderSessionID(self):
        """
        Display Name: PPPoE session ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSessionID"])
        )

    @property
    def HeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPayloadLength"])
        )

    @property
    def ServiceNameType(self):
        """
        Display Name: Tag type
        Default Value: 0x0101
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceNameType"])
        )

    @property
    def TlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TlvLength"]))

    @property
    def TlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TlvValue"]))

    @property
    def AcNameType(self):
        """
        Display Name: Tag type
        Default Value: 0x0102
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AcNameType"]))

    @property
    def AcnameTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcnameTlvLength"])
        )

    @property
    def AcnameTlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcnameTlvValue"])
        )

    @property
    def HostUniqType(self):
        """
        Display Name: Tag type
        Default Value: 0x0103
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostUniqType"]))

    @property
    def TypeLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TypeLength"]))

    @property
    def TypeValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TypeValue"]))

    @property
    def AcCookieType(self):
        """
        Display Name: Tag type
        Default Value: 0x0104
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AcCookieType"]))

    @property
    def AccookieTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AccookieTlvLength"])
        )

    @property
    def AccookieTlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AccookieTlvValue"])
        )

    @property
    def VendorSpecificType(self):
        """
        Display Name: Tag type
        Default Value: 0x0105
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorSpecificType"])
        )

    @property
    def VendorspecificTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorspecificTlvLength"])
        )

    @property
    def VendorspecificTlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorspecificTlvValue"])
        )

    @property
    def RelaySessionIDType(self):
        """
        Display Name: Tag type
        Default Value: 0x0110
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelaySessionIDType"])
        )

    @property
    def RelaysessionidTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelaysessionidTlvLength"])
        )

    @property
    def RelaysessionidTlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelaysessionidTlvValue"])
        )

    @property
    def ServiceNameErrorType(self):
        """
        Display Name: Tag type
        Default Value: 0x0201
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceNameErrorType"])
        )

    @property
    def ServicenameerrorTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServicenameerrorTlvLength"])
        )

    @property
    def ServicenameerrorTlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServicenameerrorTlvValue"])
        )

    @property
    def AcSystemErrorType(self):
        """
        Display Name: Tag type
        Default Value: 0x0202
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcSystemErrorType"])
        )

    @property
    def AcsystemerrorTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcsystemerrorTlvLength"])
        )

    @property
    def AcsystemerrorTlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcsystemerrorTlvValue"])
        )

    @property
    def GenericErrorType(self):
        """
        Display Name: Tag type
        Default Value: 0x0203
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericErrorType"])
        )

    @property
    def GenericerrorTlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericerrorTlvLength"])
        )

    @property
    def GenericerrorTlvValue(self):
        """
        Display Name: Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GenericerrorTlvValue"])
        )

    @property
    def EndOfListType(self):
        """
        Display Name: Tag type
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EndOfListType"]))

    @property
    def EndOfListLength(self):
        """
        Display Name: Tag length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndOfListLength"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
