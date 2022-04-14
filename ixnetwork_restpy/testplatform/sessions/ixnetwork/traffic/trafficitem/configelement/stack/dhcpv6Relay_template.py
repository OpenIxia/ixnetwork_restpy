from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Dhcpv6Relay(Base):
    __slots__ = ()
    _SDM_NAME = "dhcpv6Relay"
    _SDM_ATT_MAP = {
        "HeaderMessageType": "dhcpv6Relay.header.messageType-1",
        "HeaderHopCount": "dhcpv6Relay.header.hopCount-2",
        "HeaderLinkAddress": "dhcpv6Relay.header.linkAddress-3",
        "HeaderPeerAddress": "dhcpv6Relay.header.peerAddress-4",
        "ClientIdCode": "dhcpv6Relay.header.nextOption.option.clientId.code-5",
        "ClientIdLength": "dhcpv6Relay.header.nextOption.option.clientId.length-6",
        "DuidLLTCode": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLLT.code-7",
        "DuidLLTHwType": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLLT.hwType-8",
        "DuidLLTTime": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLLT.time-9",
        "LinkLayerAddressLength": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLLT.linkLayerAddress.length-10",
        "LinkLayerAddressData": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLLT.linkLayerAddress.data-11",
        "DuidENCode": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidEN.code-12",
        "DuidENNumber": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidEN.number-13",
        "UniqueIdLength": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidEN.uniqueId.length-14",
        "UniqueIdData": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidEN.uniqueId.data-15",
        "DuidLLCode": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLL.code-16",
        "DuidLLHwType": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLL.hwType-17",
        "DuidllLinkLayerAddressLength": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLL.linkLayerAddress.length-18",
        "DuidllLinkLayerAddressData": "dhcpv6Relay.header.nextOption.option.clientId.data.duid.duidLL.linkLayerAddress.data-19",
        "ServerIdCode": "dhcpv6Relay.header.nextOption.option.serverId.code-20",
        "ServerIdLength": "dhcpv6Relay.header.nextOption.option.serverId.length-21",
        "DuidDuidLLTCode": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLLT.code-22",
        "DuidDuidLLTHwType": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLLT.hwType-23",
        "DuidDuidLLTTime": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLLT.time-24",
        "DuidlltLinkLayerAddressLength": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLLT.linkLayerAddress.length-25",
        "DuidlltLinkLayerAddressData": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLLT.linkLayerAddress.data-26",
        "DuidDuidENCode": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidEN.code-27",
        "DuidDuidENNumber": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidEN.number-28",
        "DuidenUniqueIdLength": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidEN.uniqueId.length-29",
        "DuidenUniqueIdData": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidEN.uniqueId.data-30",
        "DuidDuidLLCode": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLL.code-31",
        "DuidDuidLLHwType": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLL.hwType-32",
        "LinkLayerAddress1Length": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLL.linkLayerAddress1.length-33",
        "LinkLayerAddress1Data": "dhcpv6Relay.header.nextOption.option.serverId.data.duid.duidLL.linkLayerAddress1.data-34",
        "IdAssociationCode": "dhcpv6Relay.header.nextOption.option.idAssociation.code-35",
        "IdAssociationLength": "dhcpv6Relay.header.nextOption.option.idAssociation.length-36",
        "IdAssociationIaid": "dhcpv6Relay.header.nextOption.option.idAssociation.iaid-37",
        "IdAssociationT1": "dhcpv6Relay.header.nextOption.option.idAssociation.t1-38",
        "IdAssociationT2": "dhcpv6Relay.header.nextOption.option.idAssociation.t2-39",
        "OptionsLength": "dhcpv6Relay.header.nextOption.option.idAssociation.options.length-40",
        "OptionsData": "dhcpv6Relay.header.nextOption.option.idAssociation.options.data-41",
        "IaForTmpAddressCode": "dhcpv6Relay.header.nextOption.option.iaForTmpAddress.code-42",
        "IaForTmpAddressLength": "dhcpv6Relay.header.nextOption.option.iaForTmpAddress.length-43",
        "IaForTmpAddressId": "dhcpv6Relay.header.nextOption.option.iaForTmpAddress.id-44",
        "IafortmpaddressOptionsLength": "dhcpv6Relay.header.nextOption.option.iaForTmpAddress.options.length-45",
        "IafortmpaddressOptionsData": "dhcpv6Relay.header.nextOption.option.iaForTmpAddress.options.data-46",
        "IaAddressCode": "dhcpv6Relay.header.nextOption.option.iaAddress.code-47",
        "IaAddressLength": "dhcpv6Relay.header.nextOption.option.iaAddress.length-48",
        "IaAddressIpv6address": "dhcpv6Relay.header.nextOption.option.iaAddress.ipv6address-49",
        "IaAddressPreferredLifetime": "dhcpv6Relay.header.nextOption.option.iaAddress.preferredLifetime-50",
        "IaAddressValidLifetime": "dhcpv6Relay.header.nextOption.option.iaAddress.validLifetime-51",
        "IaaddressOptionsLength": "dhcpv6Relay.header.nextOption.option.iaAddress.options.length-52",
        "IaaddressOptionsData": "dhcpv6Relay.header.nextOption.option.iaAddress.options.data-53",
        "OptionRequestCode": "dhcpv6Relay.header.nextOption.option.optionRequest.code-54",
        "OptionRequestLength": "dhcpv6Relay.header.nextOption.option.optionRequest.length-55",
        "ReqOptionCode": "dhcpv6Relay.header.nextOption.option.optionRequest.reqOption.code-56",
        "PreferenceCode": "dhcpv6Relay.header.nextOption.option.preference.code-57",
        "PreferenceLength": "dhcpv6Relay.header.nextOption.option.preference.length-58",
        "PreferenceValue": "dhcpv6Relay.header.nextOption.option.preference.value-59",
        "ElapsedTimeCode": "dhcpv6Relay.header.nextOption.option.elapsedTime.code-60",
        "ElapsedTimeLength": "dhcpv6Relay.header.nextOption.option.elapsedTime.length-61",
        "ElapsedTimeValue": "dhcpv6Relay.header.nextOption.option.elapsedTime.value-62",
        "RelayMessageCode": "dhcpv6Relay.header.nextOption.option.relayMessage.code-63",
        "RelayMessageLength": "dhcpv6Relay.header.nextOption.option.relayMessage.length-64",
        "MessageLength": "dhcpv6Relay.header.nextOption.option.relayMessage.message.length-65",
        "MessageData": "dhcpv6Relay.header.nextOption.option.relayMessage.message.data-66",
        "AuthenticationCode": "dhcpv6Relay.header.nextOption.option.authentication.code-67",
        "AuthenticationLength": "dhcpv6Relay.header.nextOption.option.authentication.length-68",
        "AuthenticationProtocol": "dhcpv6Relay.header.nextOption.option.authentication.protocol-69",
        "AuthenticationAlgorithm": "dhcpv6Relay.header.nextOption.option.authentication.algorithm-70",
        "AuthenticationRdm": "dhcpv6Relay.header.nextOption.option.authentication.rdm-71",
        "AuthenticationReplayDetection": "dhcpv6Relay.header.nextOption.option.authentication.replayDetection-72",
        "AuthenticationInformationLength": "dhcpv6Relay.header.nextOption.option.authentication.authenticationInformation.length-73",
        "AuthenticationInformationData": "dhcpv6Relay.header.nextOption.option.authentication.authenticationInformation.data-74",
        "ServerUnicastCode": "dhcpv6Relay.header.nextOption.option.serverUnicast.code-75",
        "ServerUnicastLength": "dhcpv6Relay.header.nextOption.option.serverUnicast.length-76",
        "ServerUnicastAddress": "dhcpv6Relay.header.nextOption.option.serverUnicast.address-77",
        "StatusCodeCode": "dhcpv6Relay.header.nextOption.option.statusCode.code-78",
        "StatusCodeLength": "dhcpv6Relay.header.nextOption.option.statusCode.length-79",
        "StatusCodeValue": "dhcpv6Relay.header.nextOption.option.statusCode.value-80",
        "StatusMessageLength": "dhcpv6Relay.header.nextOption.option.statusCode.statusMessage.length-81",
        "StatusMessageData": "dhcpv6Relay.header.nextOption.option.statusCode.statusMessage.data-82",
        "RapidCommitCode": "dhcpv6Relay.header.nextOption.option.rapidCommit.code-83",
        "RapidCommitLength": "dhcpv6Relay.header.nextOption.option.rapidCommit.length-84",
        "UserClassCode": "dhcpv6Relay.header.nextOption.option.userClass.code-85",
        "UserClassLength": "dhcpv6Relay.header.nextOption.option.userClass.length-86",
        "DataLength": "dhcpv6Relay.header.nextOption.option.userClass.data.length-87",
        "DataData": "dhcpv6Relay.header.nextOption.option.userClass.data.data-88",
        "VendorClassCode": "dhcpv6Relay.header.nextOption.option.vendorClass.code-89",
        "VendorClassLength": "dhcpv6Relay.header.nextOption.option.vendorClass.length-90",
        "VendorClassEnterpriseNumber": "dhcpv6Relay.header.nextOption.option.vendorClass.enterpriseNumber-91",
        "VendorclassDataLength": "dhcpv6Relay.header.nextOption.option.vendorClass.data.length-92",
        "VendorclassDataData": "dhcpv6Relay.header.nextOption.option.vendorClass.data.data-93",
        "VendorInformationCode": "dhcpv6Relay.header.nextOption.option.vendorInformation.code-94",
        "VendorInformationLength": "dhcpv6Relay.header.nextOption.option.vendorInformation.length-95",
        "VendorInformationEnterpriseNumber": "dhcpv6Relay.header.nextOption.option.vendorInformation.enterpriseNumber-96",
        "VendorinformationDataLength": "dhcpv6Relay.header.nextOption.option.vendorInformation.data.length-97",
        "VendorinformationDataData": "dhcpv6Relay.header.nextOption.option.vendorInformation.data.data-98",
        "InterfaceIdCode": "dhcpv6Relay.header.nextOption.option.interfaceId.code-99",
        "InterfaceIdLength": "dhcpv6Relay.header.nextOption.option.interfaceId.length-100",
        "IdLength": "dhcpv6Relay.header.nextOption.option.interfaceId.id.length-101",
        "IdData": "dhcpv6Relay.header.nextOption.option.interfaceId.id.data-102",
        "ReconfigureMessageCode": "dhcpv6Relay.header.nextOption.option.reconfigureMessage.code-103",
        "ReconfigureMessageLength": "dhcpv6Relay.header.nextOption.option.reconfigureMessage.length-104",
        "ReconfigureMessageMsgType": "dhcpv6Relay.header.nextOption.option.reconfigureMessage.msgType-105",
        "ReconfigureAcceptCode": "dhcpv6Relay.header.nextOption.option.reconfigureAccept.code-106",
        "ReconfigureAcceptLength": "dhcpv6Relay.header.nextOption.option.reconfigureAccept.length-107",
        "DnsRecursiveNameServerCode": "dhcpv6Relay.header.nextOption.option.dnsRecursiveNameServer.code-108",
        "DnsRecursiveNameServerLength": "dhcpv6Relay.header.nextOption.option.dnsRecursiveNameServer.length-109",
        "DnsRecursiveNameServerAddress": "dhcpv6Relay.header.nextOption.option.dnsRecursiveNameServer.address-110",
        "DomainSearchListCode": "dhcpv6Relay.header.nextOption.option.domainSearchList.code-111",
        "DomainSearchListLength": "dhcpv6Relay.header.nextOption.option.domainSearchList.length-112",
        "NextDomainDomain": "dhcpv6Relay.header.nextOption.option.domainSearchList.nextDomain.domain-113",
        "DomainSearchListNull": "dhcpv6Relay.header.nextOption.option.domainSearchList.null-114",
    }

    def __init__(self, parent, list_op=False):
        super(Dhcpv6Relay, self).__init__(parent, list_op)

    @property
    def HeaderMessageType(self):
        """
        Display Name: Message Type
        Default Value: 12
        Value Format: decimal
        Available enum values: Relay-forw, 12, Relay-repl, 13
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageType"])
        )

    @property
    def HeaderHopCount(self):
        """
        Display Name: Hop Count
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHopCount"])
        )

    @property
    def HeaderLinkAddress(self):
        """
        Display Name: Link Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderLinkAddress"])
        )

    @property
    def HeaderPeerAddress(self):
        """
        Display Name: Peer Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPeerAddress"])
        )

    @property
    def ClientIdCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientIdCode"]))

    @property
    def ClientIdLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientIdLength"])
        )

    @property
    def DuidLLTCode(self):
        """
        Display Name: LLT Code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DuidLLTCode"]))

    @property
    def DuidLLTHwType(self):
        """
        Display Name: Hardware type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DuidLLTHwType"]))

    @property
    def DuidLLTTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DuidLLTTime"]))

    @property
    def LinkLayerAddressLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkLayerAddressLength"])
        )

    @property
    def LinkLayerAddressData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkLayerAddressData"])
        )

    @property
    def DuidENCode(self):
        """
        Display Name: EN Code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DuidENCode"]))

    @property
    def DuidENNumber(self):
        """
        Display Name: Enterprise Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DuidENNumber"]))

    @property
    def UniqueIdLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniqueIdLength"])
        )

    @property
    def UniqueIdData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UniqueIdData"]))

    @property
    def DuidLLCode(self):
        """
        Display Name: LL Code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DuidLLCode"]))

    @property
    def DuidLLHwType(self):
        """
        Display Name: Hardware type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DuidLLHwType"]))

    @property
    def DuidllLinkLayerAddressLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidllLinkLayerAddressLength"])
        )

    @property
    def DuidllLinkLayerAddressData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidllLinkLayerAddressData"])
        )

    @property
    def ServerIdCode(self):
        """
        Display Name: Code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerIdCode"]))

    @property
    def ServerIdLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerIdLength"])
        )

    @property
    def DuidDuidLLTCode(self):
        """
        Display Name: LLT Code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidLLTCode"])
        )

    @property
    def DuidDuidLLTHwType(self):
        """
        Display Name: Hardware type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidLLTHwType"])
        )

    @property
    def DuidDuidLLTTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidLLTTime"])
        )

    @property
    def DuidlltLinkLayerAddressLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DuidlltLinkLayerAddressLength"]),
        )

    @property
    def DuidlltLinkLayerAddressData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidlltLinkLayerAddressData"])
        )

    @property
    def DuidDuidENCode(self):
        """
        Display Name: EN Code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidENCode"])
        )

    @property
    def DuidDuidENNumber(self):
        """
        Display Name: Enterprise Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidENNumber"])
        )

    @property
    def DuidenUniqueIdLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidenUniqueIdLength"])
        )

    @property
    def DuidenUniqueIdData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidenUniqueIdData"])
        )

    @property
    def DuidDuidLLCode(self):
        """
        Display Name: LL Code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidLLCode"])
        )

    @property
    def DuidDuidLLHwType(self):
        """
        Display Name: Hardware type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidLLHwType"])
        )

    @property
    def LinkLayerAddress1Length(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkLayerAddress1Length"])
        )

    @property
    def LinkLayerAddress1Data(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkLayerAddress1Data"])
        )

    @property
    def IdAssociationCode(self):
        """
        Display Name: Code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IdAssociationCode"])
        )

    @property
    def IdAssociationLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IdAssociationLength"])
        )

    @property
    def IdAssociationIaid(self):
        """
        Display Name: IAID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IdAssociationIaid"])
        )

    @property
    def IdAssociationT1(self):
        """
        Display Name: T1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IdAssociationT1"])
        )

    @property
    def IdAssociationT2(self):
        """
        Display Name: T2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IdAssociationT2"])
        )

    @property
    def OptionsLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionsLength"]))

    @property
    def OptionsData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionsData"]))

    @property
    def IaForTmpAddressCode(self):
        """
        Display Name: Code
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaForTmpAddressCode"])
        )

    @property
    def IaForTmpAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaForTmpAddressLength"])
        )

    @property
    def IaForTmpAddressId(self):
        """
        Display Name: IAID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaForTmpAddressId"])
        )

    @property
    def IafortmpaddressOptionsLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IafortmpaddressOptionsLength"])
        )

    @property
    def IafortmpaddressOptionsData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IafortmpaddressOptionsData"])
        )

    @property
    def IaAddressCode(self):
        """
        Display Name: Code
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IaAddressCode"]))

    @property
    def IaAddressLength(self):
        """
        Display Name: Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaAddressLength"])
        )

    @property
    def IaAddressIpv6address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaAddressIpv6address"])
        )

    @property
    def IaAddressPreferredLifetime(self):
        """
        Display Name: Preferred Lifetime
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaAddressPreferredLifetime"])
        )

    @property
    def IaAddressValidLifetime(self):
        """
        Display Name: Valid Lifetime
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaAddressValidLifetime"])
        )

    @property
    def IaaddressOptionsLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaaddressOptionsLength"])
        )

    @property
    def IaaddressOptionsData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaaddressOptionsData"])
        )

    @property
    def OptionRequestCode(self):
        """
        Display Name: Code
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionRequestCode"])
        )

    @property
    def OptionRequestLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionRequestLength"])
        )

    @property
    def ReqOptionCode(self):
        """
        Display Name: Requested option code
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ReqOptionCode"]))

    @property
    def PreferenceCode(self):
        """
        Display Name: Code
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PreferenceCode"])
        )

    @property
    def PreferenceLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PreferenceLength"])
        )

    @property
    def PreferenceValue(self):
        """
        Display Name: Preference value
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PreferenceValue"])
        )

    @property
    def ElapsedTimeCode(self):
        """
        Display Name: Code
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElapsedTimeCode"])
        )

    @property
    def ElapsedTimeLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElapsedTimeLength"])
        )

    @property
    def ElapsedTimeValue(self):
        """
        Display Name: Elapsed Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ElapsedTimeValue"])
        )

    @property
    def RelayMessageCode(self):
        """
        Display Name: Code
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayMessageCode"])
        )

    @property
    def RelayMessageLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayMessageLength"])
        )

    @property
    def MessageLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MessageLength"]))

    @property
    def MessageData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MessageData"]))

    @property
    def AuthenticationCode(self):
        """
        Display Name: Code
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticationCode"])
        )

    @property
    def AuthenticationLength(self):
        """
        Display Name: Length
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticationLength"])
        )

    @property
    def AuthenticationProtocol(self):
        """
        Display Name: Authentication Protocol
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticationProtocol"])
        )

    @property
    def AuthenticationAlgorithm(self):
        """
        Display Name: Authentication Algorithm
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticationAlgorithm"])
        )

    @property
    def AuthenticationRdm(self):
        """
        Display Name: Replay Detection Mechanism
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticationRdm"])
        )

    @property
    def AuthenticationReplayDetection(self):
        """
        Display Name: Replay Detection
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticationReplayDetection"]),
        )

    @property
    def AuthenticationInformationLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticationInformationLength"]),
        )

    @property
    def AuthenticationInformationData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticationInformationData"]),
        )

    @property
    def ServerUnicastCode(self):
        """
        Display Name: Code
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerUnicastCode"])
        )

    @property
    def ServerUnicastLength(self):
        """
        Display Name: Length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerUnicastLength"])
        )

    @property
    def ServerUnicastAddress(self):
        """
        Display Name: Server Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerUnicastAddress"])
        )

    @property
    def StatusCodeCode(self):
        """
        Display Name: Code
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusCodeCode"])
        )

    @property
    def StatusCodeLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusCodeLength"])
        )

    @property
    def StatusCodeValue(self):
        """
        Display Name: Status Code
        Default Value: 0
        Value Format: decimal
        Available enum values: Success, 0, UnspecFail, 1, NoAddrsAvail, 2, NoBinding, 3, NotOnLink, 4, UseMulticast, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusCodeValue"])
        )

    @property
    def StatusMessageLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusMessageLength"])
        )

    @property
    def StatusMessageData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StatusMessageData"])
        )

    @property
    def RapidCommitCode(self):
        """
        Display Name: Code
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RapidCommitCode"])
        )

    @property
    def RapidCommitLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RapidCommitLength"])
        )

    @property
    def UserClassCode(self):
        """
        Display Name: Code
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UserClassCode"]))

    @property
    def UserClassLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserClassLength"])
        )

    @property
    def DataLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataLength"]))

    @property
    def DataData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataData"]))

    @property
    def VendorClassCode(self):
        """
        Display Name: Code
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorClassCode"])
        )

    @property
    def VendorClassLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorClassLength"])
        )

    @property
    def VendorClassEnterpriseNumber(self):
        """
        Display Name: Enterprise Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorClassEnterpriseNumber"])
        )

    @property
    def VendorclassDataLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorclassDataLength"])
        )

    @property
    def VendorclassDataData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorclassDataData"])
        )

    @property
    def VendorInformationCode(self):
        """
        Display Name: Code
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorInformationCode"])
        )

    @property
    def VendorInformationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorInformationLength"])
        )

    @property
    def VendorInformationEnterpriseNumber(self):
        """
        Display Name: Enterprise Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VendorInformationEnterpriseNumber"]),
        )

    @property
    def VendorinformationDataLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorinformationDataLength"])
        )

    @property
    def VendorinformationDataData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorinformationDataData"])
        )

    @property
    def InterfaceIdCode(self):
        """
        Display Name: Code
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceIdCode"])
        )

    @property
    def InterfaceIdLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceIdLength"])
        )

    @property
    def IdLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IdLength"]))

    @property
    def IdData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IdData"]))

    @property
    def ReconfigureMessageCode(self):
        """
        Display Name: Code
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReconfigureMessageCode"])
        )

    @property
    def ReconfigureMessageLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReconfigureMessageLength"])
        )

    @property
    def ReconfigureMessageMsgType(self):
        """
        Display Name: Message Type
        Default Value: 5
        Value Format: decimal
        Available enum values: Renew Message, 5, Information Request Message, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReconfigureMessageMsgType"])
        )

    @property
    def ReconfigureAcceptCode(self):
        """
        Display Name: Code
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReconfigureAcceptCode"])
        )

    @property
    def ReconfigureAcceptLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReconfigureAcceptLength"])
        )

    @property
    def DnsRecursiveNameServerCode(self):
        """
        Display Name: Code
        Default Value: 23
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DnsRecursiveNameServerCode"])
        )

    @property
    def DnsRecursiveNameServerLength(self):
        """
        Display Name: Length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DnsRecursiveNameServerLength"])
        )

    @property
    def DnsRecursiveNameServerAddress(self):
        """
        Display Name: DNS Server Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DnsRecursiveNameServerAddress"]),
        )

    @property
    def DomainSearchListCode(self):
        """
        Display Name: Code
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainSearchListCode"])
        )

    @property
    def DomainSearchListLength(self):
        """
        Display Name: Length
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainSearchListLength"])
        )

    @property
    def NextDomainDomain(self):
        """
        Display Name: Domain
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NextDomainDomain"])
        )

    @property
    def DomainSearchListNull(self):
        """
        Display Name: Null
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainSearchListNull"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
