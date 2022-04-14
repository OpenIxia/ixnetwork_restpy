from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Amt(Base):
    __slots__ = ()
    _SDM_NAME = "amt"
    _SDM_ATT_MAP = {
        "RelayDiscoveryVersion": "amt.header.messageTypes.relayDiscovery.version-1",
        "RelayDiscoveryType": "amt.header.messageTypes.relayDiscovery.type-2",
        "RelayDiscoveryReserved": "amt.header.messageTypes.relayDiscovery.reserved-3",
        "RelayDiscoveryDiscoveryNonce": "amt.header.messageTypes.relayDiscovery.discoveryNonce-4",
        "RelayAdvertisementIPv4Version": "amt.header.messageTypes.relayAdvertisementIPv4.version-5",
        "RelayAdvertisementIPv4Type": "amt.header.messageTypes.relayAdvertisementIPv4.type-6",
        "RelayAdvertisementIPv4Reserved": "amt.header.messageTypes.relayAdvertisementIPv4.reserved-7",
        "RelayAdvertisementIPv4DiscoveryNonce": "amt.header.messageTypes.relayAdvertisementIPv4.discoveryNonce-8",
        "RelayAdvertisementIPv4RelayAddress": "amt.header.messageTypes.relayAdvertisementIPv4.relayAddress-9",
        "RelayAdvertisementIPv6Version": "amt.header.messageTypes.relayAdvertisementIPv6.version-10",
        "RelayAdvertisementIPv6Type": "amt.header.messageTypes.relayAdvertisementIPv6.type-11",
        "RelayAdvertisementIPv6Reserved": "amt.header.messageTypes.relayAdvertisementIPv6.reserved-12",
        "RelayAdvertisementIPv6DiscoveryNonce": "amt.header.messageTypes.relayAdvertisementIPv6.discoveryNonce-13",
        "RelayAdvertisementIPv6RelayAddress": "amt.header.messageTypes.relayAdvertisementIPv6.relayAddress-14",
        "RequestVersion": "amt.header.messageTypes.request.version-15",
        "RequestType": "amt.header.messageTypes.request.type-16",
        "RequestReserved7": "amt.header.messageTypes.request.reserved7-17",
        "RequestPFlag": "amt.header.messageTypes.request.pFlag-18",
        "RequestReserved16": "amt.header.messageTypes.request.reserved16-19",
        "RequestRequestNonce": "amt.header.messageTypes.request.requestNonce-20",
        "MembershipQuery1Version": "amt.header.messageTypes.membershipQuery1.version-21",
        "MembershipQuery1Type": "amt.header.messageTypes.membershipQuery1.type-22",
        "MembershipQuery1Reserved6": "amt.header.messageTypes.membershipQuery1.reserved6-23",
        "MembershipQuery1LimitFlag": "amt.header.messageTypes.membershipQuery1.limitFlag-24",
        "MembershipQuery1GatewayAddrFlag": "amt.header.messageTypes.membershipQuery1.gatewayAddrFlag-25",
        "MembershipQuery1ResponseMAC": "amt.header.messageTypes.membershipQuery1.responseMAC-26",
        "MembershipQuery1RequestNonce": "amt.header.messageTypes.membershipQuery1.requestNonce-27",
        "MembershipUpdateVersion": "amt.header.messageTypes.membershipUpdate.version-28",
        "MembershipUpdateType": "amt.header.messageTypes.membershipUpdate.type-29",
        "MembershipUpdateReserved8": "amt.header.messageTypes.membershipUpdate.reserved8-30",
        "MembershipUpdateResponseMAC": "amt.header.messageTypes.membershipUpdate.responseMAC-31",
        "MembershipUpdateRequestNonce": "amt.header.messageTypes.membershipUpdate.requestNonce-32",
        "MulticastDataVersion": "amt.header.messageTypes.multicastData.version-33",
        "MulticastDataType": "amt.header.messageTypes.multicastData.type-34",
        "MulticastDataReserved8": "amt.header.messageTypes.multicastData.reserved8-35",
        "MulticastDataData": "amt.header.messageTypes.multicastData.data-36",
        "TeardownVersion": "amt.header.messageTypes.teardown.version-37",
        "TeardownType": "amt.header.messageTypes.teardown.type-38",
        "TeardownReserved8": "amt.header.messageTypes.teardown.reserved8-39",
        "TeardownResponseMAC": "amt.header.messageTypes.teardown.responseMAC-40",
        "TeardownRequestNonce": "amt.header.messageTypes.teardown.requestNonce-41",
        "TeardownGatewayPortNumber": "amt.header.messageTypes.teardown.gatewayPortNumber-42",
        "TeardownGatewayIPAddress": "amt.header.messageTypes.teardown.gatewayIPAddress-43",
        "MembershipQuery2GatewayPortNumber": "amt.header.messageTypes.membershipQuery2.gatewayPortNumber-44",
        "MembershipQuery2GatewayIPAddress": "amt.header.messageTypes.membershipQuery2.gatewayIPAddress-45",
    }

    def __init__(self, parent, list_op=False):
        super(Amt, self).__init__(parent, list_op)

    @property
    def RelayDiscoveryVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayDiscoveryVersion"])
        )

    @property
    def RelayDiscoveryType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayDiscoveryType"])
        )

    @property
    def RelayDiscoveryReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayDiscoveryReserved"])
        )

    @property
    def RelayDiscoveryDiscoveryNonce(self):
        """
        Display Name: Discovery Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayDiscoveryDiscoveryNonce"])
        )

    @property
    def RelayAdvertisementIPv4Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RelayAdvertisementIPv4Version"]),
        )

    @property
    def RelayAdvertisementIPv4Type(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayAdvertisementIPv4Type"])
        )

    @property
    def RelayAdvertisementIPv4Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RelayAdvertisementIPv4Reserved"]),
        )

    @property
    def RelayAdvertisementIPv4DiscoveryNonce(self):
        """
        Display Name: Discovery Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RelayAdvertisementIPv4DiscoveryNonce"]
            ),
        )

    @property
    def RelayAdvertisementIPv4RelayAddress(self):
        """
        Display Name: Relay Address
        Default Value: 1.2.3.4
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RelayAdvertisementIPv4RelayAddress"]
            ),
        )

    @property
    def RelayAdvertisementIPv6Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RelayAdvertisementIPv6Version"]),
        )

    @property
    def RelayAdvertisementIPv6Type(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayAdvertisementIPv6Type"])
        )

    @property
    def RelayAdvertisementIPv6Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RelayAdvertisementIPv6Reserved"]),
        )

    @property
    def RelayAdvertisementIPv6DiscoveryNonce(self):
        """
        Display Name: Discovery Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RelayAdvertisementIPv6DiscoveryNonce"]
            ),
        )

    @property
    def RelayAdvertisementIPv6RelayAddress(self):
        """
        Display Name: Relay Address
        Default Value: 1:2:3:4:5:6:7:8
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RelayAdvertisementIPv6RelayAddress"]
            ),
        )

    @property
    def RequestVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestVersion"])
        )

    @property
    def RequestType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RequestType"]))

    @property
    def RequestReserved7(self):
        """
        Display Name: Reserved7
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestReserved7"])
        )

    @property
    def RequestPFlag(self):
        """
        Display Name: P Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RequestPFlag"]))

    @property
    def RequestReserved16(self):
        """
        Display Name: Reserved16
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestReserved16"])
        )

    @property
    def RequestRequestNonce(self):
        """
        Display Name: Request Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestRequestNonce"])
        )

    @property
    def MembershipQuery1Version(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipQuery1Version"])
        )

    @property
    def MembershipQuery1Type(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipQuery1Type"])
        )

    @property
    def MembershipQuery1Reserved6(self):
        """
        Display Name: Reserved6
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipQuery1Reserved6"])
        )

    @property
    def MembershipQuery1LimitFlag(self):
        """
        Display Name: Limit (L) Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipQuery1LimitFlag"])
        )

    @property
    def MembershipQuery1GatewayAddrFlag(self):
        """
        Display Name: Gateway Address (G) Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MembershipQuery1GatewayAddrFlag"]),
        )

    @property
    def MembershipQuery1ResponseMAC(self):
        """
        Display Name: Response MAC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipQuery1ResponseMAC"])
        )

    @property
    def MembershipQuery1RequestNonce(self):
        """
        Display Name: Request Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipQuery1RequestNonce"])
        )

    @property
    def MembershipUpdateVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipUpdateVersion"])
        )

    @property
    def MembershipUpdateType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipUpdateType"])
        )

    @property
    def MembershipUpdateReserved8(self):
        """
        Display Name: Reserved8
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipUpdateReserved8"])
        )

    @property
    def MembershipUpdateResponseMAC(self):
        """
        Display Name: Response MAC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipUpdateResponseMAC"])
        )

    @property
    def MembershipUpdateRequestNonce(self):
        """
        Display Name: Request Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MembershipUpdateRequestNonce"])
        )

    @property
    def MulticastDataVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastDataVersion"])
        )

    @property
    def MulticastDataType(self):
        """
        Display Name: Type
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastDataType"])
        )

    @property
    def MulticastDataReserved8(self):
        """
        Display Name: Reserved8
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastDataReserved8"])
        )

    @property
    def MulticastDataData(self):
        """
        Display Name: Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastDataData"])
        )

    @property
    def TeardownVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TeardownVersion"])
        )

    @property
    def TeardownType(self):
        """
        Display Name: Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TeardownType"]))

    @property
    def TeardownReserved8(self):
        """
        Display Name: Reserved8
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TeardownReserved8"])
        )

    @property
    def TeardownResponseMAC(self):
        """
        Display Name: Response MAC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TeardownResponseMAC"])
        )

    @property
    def TeardownRequestNonce(self):
        """
        Display Name: Request Nonce
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TeardownRequestNonce"])
        )

    @property
    def TeardownGatewayPortNumber(self):
        """
        Display Name: Gateway Port Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TeardownGatewayPortNumber"])
        )

    @property
    def TeardownGatewayIPAddress(self):
        """
        Display Name: Gateway IP Address
        Default Value: 00::00
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TeardownGatewayIPAddress"])
        )

    @property
    def MembershipQuery2GatewayPortNumber(self):
        """
        Display Name: Gateway Port Number
        Default Value: 1234
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MembershipQuery2GatewayPortNumber"]),
        )

    @property
    def MembershipQuery2GatewayIPAddress(self):
        """
        Display Name: Gateway IP Address
        Default Value: 1:2:3:4:5:6:7:8
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MembershipQuery2GatewayIPAddress"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
