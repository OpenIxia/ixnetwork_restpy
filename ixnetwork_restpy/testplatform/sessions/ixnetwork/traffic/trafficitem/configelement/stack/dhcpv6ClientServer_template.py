from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Dhcpv6ClientServer(Base):
    __slots__ = ()
    _SDM_NAME = "dhcpv6ClientServer"
    _SDM_ATT_MAP = {
        "HeaderMessageType": "dhcpv6ClientServer.header.messageType-1",
        "HeaderTransactionId": "dhcpv6ClientServer.header.transactionId-2",
        "ClientIdCode": "dhcpv6ClientServer.header.nextOption.option.clientId.code-3",
        "ClientIdLength": "dhcpv6ClientServer.header.nextOption.option.clientId.length-4",
        "DuidLLTCode": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLLT.code-5",
        "DuidLLTHwType": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLLT.hwType-6",
        "DuidLLTTime": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLLT.time-7",
        "LinkLayerAddressLength": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLLT.linkLayerAddress.length-8",
        "LinkLayerAddressData": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLLT.linkLayerAddress.data-9",
        "DuidENCode": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidEN.code-10",
        "DuidENNumber": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidEN.number-11",
        "UniqueIdLength": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidEN.uniqueId.length-12",
        "UniqueIdData": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidEN.uniqueId.data-13",
        "DuidLLCode": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLL.code-14",
        "DuidLLHwType": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLL.hwType-15",
        "DuidllLinkLayerAddressLength": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLL.linkLayerAddress.length-16",
        "DuidllLinkLayerAddressData": "dhcpv6ClientServer.header.nextOption.option.clientId.data.duid.duidLL.linkLayerAddress.data-17",
        "ServerIdCode": "dhcpv6ClientServer.header.nextOption.option.serverId.code-18",
        "ServerIdLength": "dhcpv6ClientServer.header.nextOption.option.serverId.length-19",
        "DuidDuidLLTCode": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLLT.code-20",
        "DuidDuidLLTHwType": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLLT.hwType-21",
        "DuidDuidLLTTime": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLLT.time-22",
        "DuidlltLinkLayerAddressLength": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLLT.linkLayerAddress.length-23",
        "DuidlltLinkLayerAddressData": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLLT.linkLayerAddress.data-24",
        "DuidDuidENCode": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidEN.code-25",
        "DuidDuidENNumber": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidEN.number-26",
        "DuidenUniqueIdLength": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidEN.uniqueId.length-27",
        "DuidenUniqueIdData": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidEN.uniqueId.data-28",
        "DuidDuidLLCode": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLL.code-29",
        "DuidDuidLLHwType": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLL.hwType-30",
        "DuidDuidllLinkLayerAddressLength": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLL.linkLayerAddress.length-31",
        "DuidDuidllLinkLayerAddressData": "dhcpv6ClientServer.header.nextOption.option.serverId.data.duid.duidLL.linkLayerAddress.data-32",
        "IdAssociationCode": "dhcpv6ClientServer.header.nextOption.option.idAssociation.code-33",
        "IdAssociationLength": "dhcpv6ClientServer.header.nextOption.option.idAssociation.length-34",
        "IdAssociationIaid": "dhcpv6ClientServer.header.nextOption.option.idAssociation.iaid-35",
        "IdAssociationT1": "dhcpv6ClientServer.header.nextOption.option.idAssociation.t1-36",
        "IdAssociationT2": "dhcpv6ClientServer.header.nextOption.option.idAssociation.t2-37",
        "IaNAOptionsLength": "dhcpv6ClientServer.header.nextOption.option.idAssociation.iaNAOptions.length-38",
        "IaNAOptionsData": "dhcpv6ClientServer.header.nextOption.option.idAssociation.iaNAOptions.data-39",
        "IaForTmpAddressCode": "dhcpv6ClientServer.header.nextOption.option.iaForTmpAddress.code-40",
        "IaForTmpAddressLength": "dhcpv6ClientServer.header.nextOption.option.iaForTmpAddress.length-41",
        "IaForTmpAddressId": "dhcpv6ClientServer.header.nextOption.option.iaForTmpAddress.id-42",
        "OptionsLength": "dhcpv6ClientServer.header.nextOption.option.iaForTmpAddress.options.length-43",
        "OptionsData": "dhcpv6ClientServer.header.nextOption.option.iaForTmpAddress.options.data-44",
        "IaAddressCode": "dhcpv6ClientServer.header.nextOption.option.iaAddress.code-45",
        "IaAddressLength": "dhcpv6ClientServer.header.nextOption.option.iaAddress.length-46",
        "IaAddressIpv6Address": "dhcpv6ClientServer.header.nextOption.option.iaAddress.ipv6Address-47",
        "IaAddressPreferredLifetime": "dhcpv6ClientServer.header.nextOption.option.iaAddress.preferredLifetime-48",
        "IaAddressValidLifetime": "dhcpv6ClientServer.header.nextOption.option.iaAddress.validLifetime-49",
        "IaaddressOptionsLength": "dhcpv6ClientServer.header.nextOption.option.iaAddress.options.length-50",
        "IaaddressOptionsData": "dhcpv6ClientServer.header.nextOption.option.iaAddress.options.data-51",
        "OptionRequestCode": "dhcpv6ClientServer.header.nextOption.option.optionRequest.code-52",
        "OptionRequestLength": "dhcpv6ClientServer.header.nextOption.option.optionRequest.length-53",
        "ReqOptionCode": "dhcpv6ClientServer.header.nextOption.option.optionRequest.reqOption.code-54",
        "PreferenceCode": "dhcpv6ClientServer.header.nextOption.option.preference.code-55",
        "PreferenceLength": "dhcpv6ClientServer.header.nextOption.option.preference.length-56",
        "PreferenceValue": "dhcpv6ClientServer.header.nextOption.option.preference.value-57",
        "ElapsedTimeCode": "dhcpv6ClientServer.header.nextOption.option.elapsedTime.code-58",
        "ElapsedTimeLength": "dhcpv6ClientServer.header.nextOption.option.elapsedTime.length-59",
        "ElapsedTimeValue": "dhcpv6ClientServer.header.nextOption.option.elapsedTime.value-60",
        "RelayMessageCode": "dhcpv6ClientServer.header.nextOption.option.relayMessage.code-61",
        "RelayMessageLength": "dhcpv6ClientServer.header.nextOption.option.relayMessage.length-62",
        "MessageLength": "dhcpv6ClientServer.header.nextOption.option.relayMessage.message.length-63",
        "MessageData": "dhcpv6ClientServer.header.nextOption.option.relayMessage.message.data-64",
        "AuthenticationCode": "dhcpv6ClientServer.header.nextOption.option.authentication.code-65",
        "AuthenticationLength": "dhcpv6ClientServer.header.nextOption.option.authentication.length-66",
        "AuthenticationProtocol": "dhcpv6ClientServer.header.nextOption.option.authentication.protocol-67",
        "AuthenticationAlgorithm": "dhcpv6ClientServer.header.nextOption.option.authentication.algorithm-68",
        "AuthenticationRdm": "dhcpv6ClientServer.header.nextOption.option.authentication.rdm-69",
        "AuthenticationReplayDetection": "dhcpv6ClientServer.header.nextOption.option.authentication.replayDetection-70",
        "AuthenticationInformationLength": "dhcpv6ClientServer.header.nextOption.option.authentication.authenticationInformation.length-71",
        "AuthenticationInformationData": "dhcpv6ClientServer.header.nextOption.option.authentication.authenticationInformation.data-72",
        "ServerUnicastCode": "dhcpv6ClientServer.header.nextOption.option.serverUnicast.code-73",
        "ServerUnicastLength": "dhcpv6ClientServer.header.nextOption.option.serverUnicast.length-74",
        "ServerUnicastAddress": "dhcpv6ClientServer.header.nextOption.option.serverUnicast.address-75",
        "StatusCodeCode": "dhcpv6ClientServer.header.nextOption.option.statusCode.code-76",
        "StatusCodeLength": "dhcpv6ClientServer.header.nextOption.option.statusCode.length-77",
        "StatusCodeValue": "dhcpv6ClientServer.header.nextOption.option.statusCode.value-78",
        "StatusMessageLength": "dhcpv6ClientServer.header.nextOption.option.statusCode.statusMessage.length-79",
        "StatusMessageData": "dhcpv6ClientServer.header.nextOption.option.statusCode.statusMessage.data-80",
        "RapidCommitCode": "dhcpv6ClientServer.header.nextOption.option.rapidCommit.code-81",
        "RapidCommitLength": "dhcpv6ClientServer.header.nextOption.option.rapidCommit.length-82",
        "UserClassCode": "dhcpv6ClientServer.header.nextOption.option.userClass.code-83",
        "UserClassLength": "dhcpv6ClientServer.header.nextOption.option.userClass.length-84",
        "DataLength": "dhcpv6ClientServer.header.nextOption.option.userClass.data.length-85",
        "DataData": "dhcpv6ClientServer.header.nextOption.option.userClass.data.data-86",
        "VendorClassCode": "dhcpv6ClientServer.header.nextOption.option.vendorClass.code-87",
        "VendorClassLength": "dhcpv6ClientServer.header.nextOption.option.vendorClass.length-88",
        "VendorClassEnterpriseNumber": "dhcpv6ClientServer.header.nextOption.option.vendorClass.enterpriseNumber-89",
        "VendorclassDataLength": "dhcpv6ClientServer.header.nextOption.option.vendorClass.data.length-90",
        "VendorclassDataData": "dhcpv6ClientServer.header.nextOption.option.vendorClass.data.data-91",
        "VendorInformationCode": "dhcpv6ClientServer.header.nextOption.option.vendorInformation.code-92",
        "VendorInformationLength": "dhcpv6ClientServer.header.nextOption.option.vendorInformation.length-93",
        "VendorInformationEnterpriseNumber": "dhcpv6ClientServer.header.nextOption.option.vendorInformation.enterpriseNumber-94",
        "VendorinformationDataLength": "dhcpv6ClientServer.header.nextOption.option.vendorInformation.data.length-95",
        "VendorinformationDataData": "dhcpv6ClientServer.header.nextOption.option.vendorInformation.data.data-96",
        "InterfaceIdCode": "dhcpv6ClientServer.header.nextOption.option.interfaceId.code-97",
        "InterfaceIdLength": "dhcpv6ClientServer.header.nextOption.option.interfaceId.length-98",
        "IdLength": "dhcpv6ClientServer.header.nextOption.option.interfaceId.id.length-99",
        "IdData": "dhcpv6ClientServer.header.nextOption.option.interfaceId.id.data-100",
        "ReconfigureMessageCode": "dhcpv6ClientServer.header.nextOption.option.reconfigureMessage.code-101",
        "ReconfigureMessageLength": "dhcpv6ClientServer.header.nextOption.option.reconfigureMessage.length-102",
        "ReconfigureMessageMsgType": "dhcpv6ClientServer.header.nextOption.option.reconfigureMessage.msgType-103",
        "ReconfigureAcceptCode": "dhcpv6ClientServer.header.nextOption.option.reconfigureAccept.code-104",
        "ReconfigureAcceptLength": "dhcpv6ClientServer.header.nextOption.option.reconfigureAccept.length-105",
        "DnsRecursiveNameServerCode": "dhcpv6ClientServer.header.nextOption.option.dnsRecursiveNameServer.code-106",
        "DnsRecursiveNameServerLength": "dhcpv6ClientServer.header.nextOption.option.dnsRecursiveNameServer.length-107",
        "DnsRecursiveNameServerAddress": "dhcpv6ClientServer.header.nextOption.option.dnsRecursiveNameServer.address-108",
        "DomainSearchListCode": "dhcpv6ClientServer.header.nextOption.option.domainSearchList.code-109",
        "DomainSearchListLength": "dhcpv6ClientServer.header.nextOption.option.domainSearchList.length-110",
        "NextDomainDomain": "dhcpv6ClientServer.header.nextOption.option.domainSearchList.nextDomain.domain-111",
        "DomainSearchListNull": "dhcpv6ClientServer.header.nextOption.option.domainSearchList.null-112",
        "LeaseQueryCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.code-113",
        "LeaseQueryLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.length-114",
        "LeaseQueryQueryType": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.queryType-115",
        "LeaseQueryLinkAddress": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.linkAddress-116",
        "OptionIaAddressCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.iaAddress.code-117",
        "OptionIaAddressLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.iaAddress.length-118",
        "OptionIaAddressIpv6Address": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.iaAddress.ipv6Address-119",
        "OptionIaAddressPreferredLifetime": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.iaAddress.preferredLifetime-120",
        "OptionIaAddressValidLifetime": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.iaAddress.validLifetime-121",
        "OptionIaaddressOptionsLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.iaAddress.options.length-122",
        "OptionIaaddressOptionsData": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.iaAddress.options.data-123",
        "OptionClientIdCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.code-124",
        "OptionClientIdLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.length-125",
        "DataDuidDuidLLTCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLLT.code-126",
        "DataDuidDuidLLTHwType": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLLT.hwType-127",
        "DataDuidDuidLLTTime": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLLT.time-128",
        "DuidDuidlltLinkLayerAddressLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLLT.linkLayerAddress.length-129",
        "DuidDuidlltLinkLayerAddressData": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLLT.linkLayerAddress.data-130",
        "DataDuidDuidENCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidEN.code-131",
        "DataDuidDuidENNumber": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidEN.number-132",
        "DuidDuidenUniqueIdLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidEN.uniqueId.length-133",
        "DuidDuidenUniqueIdData": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidEN.uniqueId.data-134",
        "DataDuidDuidLLCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLL.code-135",
        "DataDuidDuidLLHwType": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLL.hwType-136",
        "DataDuidDuidllLinkLayerAddressLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLL.linkLayerAddress.length-137",
        "DataDuidDuidllLinkLayerAddressData": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.clientId.data.duid.duidLL.linkLayerAddress.data-138",
        "OptionOptionRequestCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.optionRequest.code-139",
        "OptionOptionRequestLength": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.optionRequest.length-140",
        "OptionrequestReqOptionCode": "dhcpv6ClientServer.header.nextOption.option.leaseQuery.nextQueryOption.option.optionRequest.reqOption.code-141",
    }

    def __init__(self, parent, list_op=False):
        super(Dhcpv6ClientServer, self).__init__(parent, list_op)

    @property
    def HeaderMessageType(self):
        """
        Display Name: Message Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Solicit, 1, Advertise, 2, Request, 3, Confirm, 4, Renew, 5, Rebind, 6, Reply, 7, Release, 8, Decline, 9, Reconfigure, 10, Information-request, 11, Leasequery, 14, Leasequery reply, 15
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderMessageType"])
        )

    @property
    def HeaderTransactionId(self):
        """
        Display Name: Transaction ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderTransactionId"])
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
    def DuidDuidllLinkLayerAddressLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DuidDuidllLinkLayerAddressLength"]),
        )

    @property
    def DuidDuidllLinkLayerAddressData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DuidDuidllLinkLayerAddressData"]),
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
    def IaNAOptionsLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaNAOptionsLength"])
        )

    @property
    def IaNAOptionsData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaNAOptionsData"])
        )

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
    def IaAddressIpv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IaAddressIpv6Address"])
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

    @property
    def LeaseQueryCode(self):
        """
        Display Name: Code
        Default Value: 44
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LeaseQueryCode"])
        )

    @property
    def LeaseQueryLength(self):
        """
        Display Name: Length
        Default Value: 48
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LeaseQueryLength"])
        )

    @property
    def LeaseQueryQueryType(self):
        """
        Display Name: Query Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Query By Address, 1, Query By ClientID, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LeaseQueryQueryType"])
        )

    @property
    def LeaseQueryLinkAddress(self):
        """
        Display Name: Link Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LeaseQueryLinkAddress"])
        )

    @property
    def OptionIaAddressCode(self):
        """
        Display Name: Code
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionIaAddressCode"])
        )

    @property
    def OptionIaAddressLength(self):
        """
        Display Name: Length
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionIaAddressLength"])
        )

    @property
    def OptionIaAddressIpv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionIaAddressIpv6Address"])
        )

    @property
    def OptionIaAddressPreferredLifetime(self):
        """
        Display Name: Preferred Lifetime
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OptionIaAddressPreferredLifetime"]),
        )

    @property
    def OptionIaAddressValidLifetime(self):
        """
        Display Name: Valid Lifetime
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionIaAddressValidLifetime"])
        )

    @property
    def OptionIaaddressOptionsLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionIaaddressOptionsLength"])
        )

    @property
    def OptionIaaddressOptionsData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionIaaddressOptionsData"])
        )

    @property
    def OptionClientIdCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionClientIdCode"])
        )

    @property
    def OptionClientIdLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionClientIdLength"])
        )

    @property
    def DataDuidDuidLLTCode(self):
        """
        Display Name: LLT Code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataDuidDuidLLTCode"])
        )

    @property
    def DataDuidDuidLLTHwType(self):
        """
        Display Name: Hardware type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataDuidDuidLLTHwType"])
        )

    @property
    def DataDuidDuidLLTTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataDuidDuidLLTTime"])
        )

    @property
    def DuidDuidlltLinkLayerAddressLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DuidDuidlltLinkLayerAddressLength"]),
        )

    @property
    def DuidDuidlltLinkLayerAddressData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DuidDuidlltLinkLayerAddressData"]),
        )

    @property
    def DataDuidDuidENCode(self):
        """
        Display Name: EN Code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataDuidDuidENCode"])
        )

    @property
    def DataDuidDuidENNumber(self):
        """
        Display Name: Enterprise Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataDuidDuidENNumber"])
        )

    @property
    def DuidDuidenUniqueIdLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidenUniqueIdLength"])
        )

    @property
    def DuidDuidenUniqueIdData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DuidDuidenUniqueIdData"])
        )

    @property
    def DataDuidDuidLLCode(self):
        """
        Display Name: LL Code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataDuidDuidLLCode"])
        )

    @property
    def DataDuidDuidLLHwType(self):
        """
        Display Name: Hardware type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataDuidDuidLLHwType"])
        )

    @property
    def DataDuidDuidllLinkLayerAddressLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataDuidDuidllLinkLayerAddressLength"]
            ),
        )

    @property
    def DataDuidDuidllLinkLayerAddressData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataDuidDuidllLinkLayerAddressData"]
            ),
        )

    @property
    def OptionOptionRequestCode(self):
        """
        Display Name: Code
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionOptionRequestCode"])
        )

    @property
    def OptionOptionRequestLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionOptionRequestLength"])
        )

    @property
    def OptionrequestReqOptionCode(self):
        """
        Display Name: Requested option code
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionrequestReqOptionCode"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
