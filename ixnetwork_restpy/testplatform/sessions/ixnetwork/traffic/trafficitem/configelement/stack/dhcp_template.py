from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Dhcp(Base):
    __slots__ = ()
    _SDM_NAME = "dhcp"
    _SDM_ATT_MAP = {
        "OpCode": "dhcp.header.opCode-1",
        "HwType": "dhcp.header.hwType-2",
        "HwAddressLen": "dhcp.header.hwAddressLen-3",
        "Hops": "dhcp.header.hops-4",
        "TransactionId": "dhcp.header.transactionId-5",
        "SecondsElapsed": "dhcp.header.secondsElapsed-6",
        "BroadcastFlag": "dhcp.header.broadcastFlag-7",
        "ClientIP": "dhcp.header.clientIP-8",
        "YourIP": "dhcp.header.yourIP-9",
        "ServerIP": "dhcp.header.serverIP-10",
        "RelayAgentIP": "dhcp.header.relayAgentIP-11",
        "ClientHwAddress": "dhcp.header.clientHwAddress-12",
        "OptionalServerName": "dhcp.header.optionalServerName-13",
        "BootFile": "dhcp.header.bootFile-14",
        "OptionsMagicCookie": "dhcp.header.options.magicCookie-15",
        "SubnetMaskCode": "dhcp.header.options.fields.nextOption.field.subnetMask.code-16",
        "SubnetMaskLength": "dhcp.header.options.fields.nextOption.field.subnetMask.length-17",
        "SubnetMaskSubnetMask": "dhcp.header.options.fields.nextOption.field.subnetMask.subnetMask-18",
        "TimeOffsetCode": "dhcp.header.options.fields.nextOption.field.timeOffset.code-19",
        "TimeOffsetLength": "dhcp.header.options.fields.nextOption.field.timeOffset.length-20",
        "TimeOffsetTimeOffset": "dhcp.header.options.fields.nextOption.field.timeOffset.timeOffset-21",
        "GatewaysCode": "dhcp.header.options.fields.nextOption.field.gateways.code-22",
        "GatewaysLength": "dhcp.header.options.fields.nextOption.field.gateways.length-23",
        "AddressesAddress": "dhcp.header.options.fields.nextOption.field.gateways.addresses.address-24",
        "TimeServerCode": "dhcp.header.options.fields.nextOption.field.timeServer.code-25",
        "TimeServerLength": "dhcp.header.options.fields.nextOption.field.timeServer.length-26",
        "TimeserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.timeServer.addresses.address-27",
        "NameServerCode": "dhcp.header.options.fields.nextOption.field.nameServer.code-28",
        "NameServerLength": "dhcp.header.options.fields.nextOption.field.nameServer.length-29",
        "NameserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.nameServer.addresses.address-30",
        "DomainNameServerCode": "dhcp.header.options.fields.nextOption.field.domainNameServer.code-31",
        "DomainNameServerLength": "dhcp.header.options.fields.nextOption.field.domainNameServer.length-32",
        "DomainnameserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.domainNameServer.addresses.address-33",
        "LogServerCode": "dhcp.header.options.fields.nextOption.field.logServer.code-34",
        "LogServerLength": "dhcp.header.options.fields.nextOption.field.logServer.length-35",
        "LogserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.logServer.addresses.address-36",
        "CookieServerCode": "dhcp.header.options.fields.nextOption.field.cookieServer.code-37",
        "CookieServerLength": "dhcp.header.options.fields.nextOption.field.cookieServer.length-38",
        "CookieserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.cookieServer.addresses.address-39",
        "LprServerCode": "dhcp.header.options.fields.nextOption.field.lprServer.code-40",
        "LprServerLength": "dhcp.header.options.fields.nextOption.field.lprServer.length-41",
        "LprserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.lprServer.addresses.address-42",
        "ImpressServerCode": "dhcp.header.options.fields.nextOption.field.impressServer.code-43",
        "ImpressServerLength": "dhcp.header.options.fields.nextOption.field.impressServer.length-44",
        "ImpressserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.impressServer.addresses.address-45",
        "ResourceLocationServerCode": "dhcp.header.options.fields.nextOption.field.resourceLocationServer.code-46",
        "ResourceLocationServerLength": "dhcp.header.options.fields.nextOption.field.resourceLocationServer.length-47",
        "ResourcelocationserverAddressesAddress": "dhcp.header.options.fields.nextOption.field.resourceLocationServer.addresses.address-48",
        "HostNameCode": "dhcp.header.options.fields.nextOption.field.hostName.code-49",
        "HostNameLength": "dhcp.header.options.fields.nextOption.field.hostName.length-50",
        "NameLength": "dhcp.header.options.fields.nextOption.field.hostName.name.length-51",
        "NameData": "dhcp.header.options.fields.nextOption.field.hostName.name.data-52",
        "BootFileSizeCode": "dhcp.header.options.fields.nextOption.field.bootFileSize.code-53",
        "BootFileSizeLength": "dhcp.header.options.fields.nextOption.field.bootFileSize.length-54",
        "BootFileSizeSize": "dhcp.header.options.fields.nextOption.field.bootFileSize.size-55",
        "MeritDumpFileCode": "dhcp.header.options.fields.nextOption.field.meritDumpFile.code-56",
        "MeritDumpFileLength": "dhcp.header.options.fields.nextOption.field.meritDumpFile.length-57",
        "MeritdumpfileNameLength": "dhcp.header.options.fields.nextOption.field.meritDumpFile.name.length-58",
        "MeritdumpfileNameData": "dhcp.header.options.fields.nextOption.field.meritDumpFile.name.data-59",
        "DomainNameCode": "dhcp.header.options.fields.nextOption.field.domainName.code-60",
        "DomainNameLength": "dhcp.header.options.fields.nextOption.field.domainName.length-61",
        "DomainnameNameLength": "dhcp.header.options.fields.nextOption.field.domainName.name.length-62",
        "DomainnameNameData": "dhcp.header.options.fields.nextOption.field.domainName.name.data-63",
        "SwapServerCode": "dhcp.header.options.fields.nextOption.field.swapServer.code-64",
        "SwapServerLength": "dhcp.header.options.fields.nextOption.field.swapServer.length-65",
        "SwapServerAddress": "dhcp.header.options.fields.nextOption.field.swapServer.address-66",
        "RootPathCode": "dhcp.header.options.fields.nextOption.field.rootPath.code-67",
        "RootPathLength": "dhcp.header.options.fields.nextOption.field.rootPath.length-68",
        "PathLength": "dhcp.header.options.fields.nextOption.field.rootPath.path.length-69",
        "PathData": "dhcp.header.options.fields.nextOption.field.rootPath.path.data-70",
        "ExtensionsPathCode": "dhcp.header.options.fields.nextOption.field.extensionsPath.code-71",
        "ExtensionsPathLength": "dhcp.header.options.fields.nextOption.field.extensionsPath.length-72",
        "ExtensionspathPathLength": "dhcp.header.options.fields.nextOption.field.extensionsPath.path.length-73",
        "ExtensionspathPathData": "dhcp.header.options.fields.nextOption.field.extensionsPath.path.data-74",
        "IpForwardingCode": "dhcp.header.options.fields.nextOption.field.ipForwarding.code-75",
        "IpForwardingLength": "dhcp.header.options.fields.nextOption.field.ipForwarding.length-76",
        "IpForwardingFlag": "dhcp.header.options.fields.nextOption.field.ipForwarding.flag-77",
        "NonLocalSourceRoutingCode": "dhcp.header.options.fields.nextOption.field.nonLocalSourceRouting.code-78",
        "NonLocalSourceRoutingLength": "dhcp.header.options.fields.nextOption.field.nonLocalSourceRouting.length-79",
        "NonLocalSourceRoutingFlag": "dhcp.header.options.fields.nextOption.field.nonLocalSourceRouting.flag-80",
        "PolicyFilterCode": "dhcp.header.options.fields.nextOption.field.policyFilter.code-81",
        "PolicyFilterLength": "dhcp.header.options.fields.nextOption.field.policyFilter.length-82",
        "AddressPairAddress1": "dhcp.header.options.fields.nextOption.field.policyFilter.addressPairs.addressPair.address1-83",
        "AddressPairAddress2": "dhcp.header.options.fields.nextOption.field.policyFilter.addressPairs.addressPair.address2-84",
        "MaxReassemblySizeCode": "dhcp.header.options.fields.nextOption.field.maxReassemblySize.code-85",
        "MaxReassemblySizeLength": "dhcp.header.options.fields.nextOption.field.maxReassemblySize.length-86",
        "MaxReassemblySizeSize": "dhcp.header.options.fields.nextOption.field.maxReassemblySize.size-87",
        "DefaultTTLCode": "dhcp.header.options.fields.nextOption.field.defaultTTL.code-88",
        "DefaultTTLLength": "dhcp.header.options.fields.nextOption.field.defaultTTL.length-89",
        "DefaultTTLTtl": "dhcp.header.options.fields.nextOption.field.defaultTTL.ttl-90",
        "PathMTUAgingTimeCode": "dhcp.header.options.fields.nextOption.field.pathMTUAgingTime.code-91",
        "PathMTUAgingTimeLength": "dhcp.header.options.fields.nextOption.field.pathMTUAgingTime.length-92",
        "PathMTUAgingTimeTime": "dhcp.header.options.fields.nextOption.field.pathMTUAgingTime.time-93",
        "PathMTUPlateauTableCode": "dhcp.header.options.fields.nextOption.field.pathMTUPlateauTable.code-94",
        "PathMTUPlateauTableLength": "dhcp.header.options.fields.nextOption.field.pathMTUPlateauTable.length-95",
        "PlateauSizeTableSize": "dhcp.header.options.fields.nextOption.field.pathMTUPlateauTable.plateauSizeTable.size-96",
        "InterfaceMTUCode": "dhcp.header.options.fields.nextOption.field.interfaceMTU.code-97",
        "InterfaceMTULength": "dhcp.header.options.fields.nextOption.field.interfaceMTU.length-98",
        "InterfaceMTUMtu": "dhcp.header.options.fields.nextOption.field.interfaceMTU.mtu-99",
        "SubnetsLocalCode": "dhcp.header.options.fields.nextOption.field.subnetsLocal.code-100",
        "SubnetsLocalLength": "dhcp.header.options.fields.nextOption.field.subnetsLocal.length-101",
        "SubnetsLocalFlag": "dhcp.header.options.fields.nextOption.field.subnetsLocal.flag-102",
        "BroadcastAddressCode": "dhcp.header.options.fields.nextOption.field.broadcastAddress.code-103",
        "BroadcastAddressLength": "dhcp.header.options.fields.nextOption.field.broadcastAddress.length-104",
        "BroadcastAddressAddress": "dhcp.header.options.fields.nextOption.field.broadcastAddress.address-105",
        "PerformMaskDiscoveryCode": "dhcp.header.options.fields.nextOption.field.performMaskDiscovery.code-106",
        "PerformMaskDiscoveryLength": "dhcp.header.options.fields.nextOption.field.performMaskDiscovery.length-107",
        "PerformMaskDiscoveryFlag": "dhcp.header.options.fields.nextOption.field.performMaskDiscovery.flag-108",
        "MaskSupplierOoptionCode": "dhcp.header.options.fields.nextOption.field.maskSupplierOoption.code-109",
        "MaskSupplierOoptionLength": "dhcp.header.options.fields.nextOption.field.maskSupplierOoption.length-110",
        "MaskSupplierOoptionFlag": "dhcp.header.options.fields.nextOption.field.maskSupplierOoption.flag-111",
        "PerformRouterDiscoveryCode": "dhcp.header.options.fields.nextOption.field.performRouterDiscovery.code-112",
        "PerformRouterDiscoveryLength": "dhcp.header.options.fields.nextOption.field.performRouterDiscovery.length-113",
        "PerformRouterDiscoveryFlag": "dhcp.header.options.fields.nextOption.field.performRouterDiscovery.flag-114",
        "RouterSolicitationAddressCode": "dhcp.header.options.fields.nextOption.field.routerSolicitationAddress.code-115",
        "RouterSolicitationAddressLength": "dhcp.header.options.fields.nextOption.field.routerSolicitationAddress.length-116",
        "RouterSolicitationAddressAddress": "dhcp.header.options.fields.nextOption.field.routerSolicitationAddress.address-117",
        "StaticRouteCode": "dhcp.header.options.fields.nextOption.field.staticRoute.code-118",
        "StaticRouteLength": "dhcp.header.options.fields.nextOption.field.staticRoute.length-119",
        "AddresspairsAddressPairAddress1": "dhcp.header.options.fields.nextOption.field.staticRoute.addressPairs.addressPair.address1-120",
        "AddresspairsAddressPairAddress2": "dhcp.header.options.fields.nextOption.field.staticRoute.addressPairs.addressPair.address2-121",
        "TrailerEncapsulationOptionCode": "dhcp.header.options.fields.nextOption.field.trailerEncapsulationOption.code-122",
        "TrailerEncapsulationOptionLength": "dhcp.header.options.fields.nextOption.field.trailerEncapsulationOption.length-123",
        "TrailerEncapsulationOptionFlag": "dhcp.header.options.fields.nextOption.field.trailerEncapsulationOption.flag-124",
        "ArpCacheTimeCode": "dhcp.header.options.fields.nextOption.field.arpCacheTime.code-125",
        "ArpCacheTimeLength": "dhcp.header.options.fields.nextOption.field.arpCacheTime.length-126",
        "ArpCacheTimeTime": "dhcp.header.options.fields.nextOption.field.arpCacheTime.time-127",
        "EthernetEncapsulationCode": "dhcp.header.options.fields.nextOption.field.ethernetEncapsulation.code-128",
        "EthernetEncapsulationLength": "dhcp.header.options.fields.nextOption.field.ethernetEncapsulation.length-129",
        "EthernetEncapsulationFlag": "dhcp.header.options.fields.nextOption.field.ethernetEncapsulation.flag-130",
        "TcpDefaultTTLCode": "dhcp.header.options.fields.nextOption.field.tcpDefaultTTL.code-131",
        "TcpDefaultTTLLength": "dhcp.header.options.fields.nextOption.field.tcpDefaultTTL.length-132",
        "TcpDefaultTTLTtl": "dhcp.header.options.fields.nextOption.field.tcpDefaultTTL.ttl-133",
        "TcpKeepaliveIntervalCode": "dhcp.header.options.fields.nextOption.field.tcpKeepaliveInterval.code-134",
        "TcpKeepaliveIntervalLength": "dhcp.header.options.fields.nextOption.field.tcpKeepaliveInterval.length-135",
        "TcpKeepaliveIntervalTime": "dhcp.header.options.fields.nextOption.field.tcpKeepaliveInterval.time-136",
        "TcpKeepaliveGarbageCode": "dhcp.header.options.fields.nextOption.field.tcpKeepaliveGarbage.code-137",
        "TcpKeepaliveGarbageLength": "dhcp.header.options.fields.nextOption.field.tcpKeepaliveGarbage.length-138",
        "TcpKeepaliveGarbageFlag": "dhcp.header.options.fields.nextOption.field.tcpKeepaliveGarbage.flag-139",
        "NisDomainCode": "dhcp.header.options.fields.nextOption.field.nisDomain.code-140",
        "NisDomainLength": "dhcp.header.options.fields.nextOption.field.nisDomain.length-141",
        "NisdomainNameLength": "dhcp.header.options.fields.nextOption.field.nisDomain.name.length-142",
        "NisdomainNameData": "dhcp.header.options.fields.nextOption.field.nisDomain.name.data-143",
        "NisServersCode": "dhcp.header.options.fields.nextOption.field.nisServers.code-144",
        "NisServersLength": "dhcp.header.options.fields.nextOption.field.nisServers.length-145",
        "NisserversAddressesAddress": "dhcp.header.options.fields.nextOption.field.nisServers.addresses.address-146",
        "NtpServersCode": "dhcp.header.options.fields.nextOption.field.ntpServers.code-147",
        "NtpServersLength": "dhcp.header.options.fields.nextOption.field.ntpServers.length-148",
        "NtpserversAddressesAddress": "dhcp.header.options.fields.nextOption.field.ntpServers.addresses.address-149",
        "VendorSpecificCode": "dhcp.header.options.fields.nextOption.field.vendorSpecific.code-150",
        "VendorSpecificLength": "dhcp.header.options.fields.nextOption.field.vendorSpecific.length-151",
        "ValueLength": "dhcp.header.options.fields.nextOption.field.vendorSpecific.value.length-152",
        "ValueData": "dhcp.header.options.fields.nextOption.field.vendorSpecific.value.data-153",
        "NbnsCode": "dhcp.header.options.fields.nextOption.field.nbns.code-154",
        "NbnsLength": "dhcp.header.options.fields.nextOption.field.nbns.length-155",
        "NbnsAddressesAddress": "dhcp.header.options.fields.nextOption.field.nbns.addresses.address-156",
        "NbddCode": "dhcp.header.options.fields.nextOption.field.nbdd.code-157",
        "NbddLength": "dhcp.header.options.fields.nextOption.field.nbdd.length-158",
        "NbddAddressesAddress": "dhcp.header.options.fields.nextOption.field.nbdd.addresses.address-159",
        "NbntCode": "dhcp.header.options.fields.nextOption.field.nbnt.code-160",
        "NbntLength": "dhcp.header.options.fields.nextOption.field.nbnt.length-161",
        "NbntNodeType": "dhcp.header.options.fields.nextOption.field.nbnt.nodeType-162",
        "NbScopeCode": "dhcp.header.options.fields.nextOption.field.nbScope.code-163",
        "NbScopeLength": "dhcp.header.options.fields.nextOption.field.nbScope.length-164",
        "NbscopeValueLength": "dhcp.header.options.fields.nextOption.field.nbScope.value.length-165",
        "NbscopeValueData": "dhcp.header.options.fields.nextOption.field.nbScope.value.data-166",
        "XFontServersCode": "dhcp.header.options.fields.nextOption.field.xFontServers.code-167",
        "XFontServersLength": "dhcp.header.options.fields.nextOption.field.xFontServers.length-168",
        "XfontserversAddressesAddress": "dhcp.header.options.fields.nextOption.field.xFontServers.addresses.address-169",
        "XFontManagersCode": "dhcp.header.options.fields.nextOption.field.xFontManagers.code-170",
        "XFontManagersLength": "dhcp.header.options.fields.nextOption.field.xFontManagers.length-171",
        "XfontmanagersAddressesAddress": "dhcp.header.options.fields.nextOption.field.xFontManagers.addresses.address-172",
        "RequestedIPAddressCode": "dhcp.header.options.fields.nextOption.field.requestedIPAddress.code-173",
        "RequestedIPAddressLength": "dhcp.header.options.fields.nextOption.field.requestedIPAddress.length-174",
        "RequestedIPAddressAddress": "dhcp.header.options.fields.nextOption.field.requestedIPAddress.address-175",
        "IpAddressLeaseTimeCode": "dhcp.header.options.fields.nextOption.field.ipAddressLeaseTime.code-176",
        "IpAddressLeaseTimeLength": "dhcp.header.options.fields.nextOption.field.ipAddressLeaseTime.length-177",
        "IpAddressLeaseTimeTime": "dhcp.header.options.fields.nextOption.field.ipAddressLeaseTime.time-178",
        "OptionOverloadCode": "dhcp.header.options.fields.nextOption.field.optionOverload.code-179",
        "OptionOverloadLength": "dhcp.header.options.fields.nextOption.field.optionOverload.length-180",
        "OptionOverloadOverloadFlag": "dhcp.header.options.fields.nextOption.field.optionOverload.overloadFlag-181",
        "DhcpMessageTypeCode": "dhcp.header.options.fields.nextOption.field.dhcpMessageType.code-182",
        "DhcpMessageTypeLength": "dhcp.header.options.fields.nextOption.field.dhcpMessageType.length-183",
        "DhcpMessageTypeMessageType": "dhcp.header.options.fields.nextOption.field.dhcpMessageType.messageType-184",
        "ServerIdentifierCode": "dhcp.header.options.fields.nextOption.field.serverIdentifier.code-185",
        "ServerIdentifierLength": "dhcp.header.options.fields.nextOption.field.serverIdentifier.length-186",
        "ServerIdentifierAddress": "dhcp.header.options.fields.nextOption.field.serverIdentifier.address-187",
        "ParameterRequestListCode": "dhcp.header.options.fields.nextOption.field.parameterRequestList.code-188",
        "ParameterRequestListLength": "dhcp.header.options.fields.nextOption.field.parameterRequestList.length-189",
        "DhcpOptionCodesLength": "dhcp.header.options.fields.nextOption.field.parameterRequestList.dhcpOptionCodes.length-190",
        "DhcpOptionCodesData": "dhcp.header.options.fields.nextOption.field.parameterRequestList.dhcpOptionCodes.data-191",
        "MessageCode": "dhcp.header.options.fields.nextOption.field.message.code-192",
        "MessageLength": "dhcp.header.options.fields.nextOption.field.message.length-193",
        "MessageNameLength": "dhcp.header.options.fields.nextOption.field.message.name.length-194",
        "MessageNameData": "dhcp.header.options.fields.nextOption.field.message.name.data-195",
        "MaxDHCPMessageSizeCode": "dhcp.header.options.fields.nextOption.field.maxDHCPMessageSize.code-196",
        "MaxDHCPMessageSizeLength": "dhcp.header.options.fields.nextOption.field.maxDHCPMessageSize.length-197",
        "MaxDHCPMessageSizeSize": "dhcp.header.options.fields.nextOption.field.maxDHCPMessageSize.size-198",
        "RenewalTimeCode": "dhcp.header.options.fields.nextOption.field.renewalTime.code-199",
        "RenewalTimeLength": "dhcp.header.options.fields.nextOption.field.renewalTime.length-200",
        "RenewalTimeTime": "dhcp.header.options.fields.nextOption.field.renewalTime.time-201",
        "RebindingTimeCode": "dhcp.header.options.fields.nextOption.field.rebindingTime.code-202",
        "RebindingTimeLength": "dhcp.header.options.fields.nextOption.field.rebindingTime.length-203",
        "RebindingTimeTime": "dhcp.header.options.fields.nextOption.field.rebindingTime.time-204",
        "ClassIdentifierCode": "dhcp.header.options.fields.nextOption.field.classIdentifier.code-205",
        "ClassIdentifierLength": "dhcp.header.options.fields.nextOption.field.classIdentifier.length-206",
        "IdentifierLength": "dhcp.header.options.fields.nextOption.field.classIdentifier.identifier.length-207",
        "IdentifierData": "dhcp.header.options.fields.nextOption.field.classIdentifier.identifier.data-208",
        "ClientIdentifierCode": "dhcp.header.options.fields.nextOption.field.clientIdentifier.code-209",
        "ClientIdentifierLength": "dhcp.header.options.fields.nextOption.field.clientIdentifier.length-210",
        "ClientIdentifierHwType": "dhcp.header.options.fields.nextOption.field.clientIdentifier.hwType-211",
        "ClientIdLength": "dhcp.header.options.fields.nextOption.field.clientIdentifier.clientId.length-212",
        "ClientIdData": "dhcp.header.options.fields.nextOption.field.clientIdentifier.clientId.data-213",
        "UserClassInformationCode": "dhcp.header.options.fields.nextOption.field.userClassInformation.code-214",
        "UserClassInformationLength": "dhcp.header.options.fields.nextOption.field.userClassInformation.length-215",
        "User_class_informationLength": "dhcp.header.options.fields.nextOption.field.userClassInformation.user_class_information.Length-216",
        "User_class_informationData": "dhcp.header.options.fields.nextOption.field.userClassInformation.user_class_information.data-217",
        "RelayAgent OptionCode": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Code-218",
        "RelayAgent OptionLength": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Length-219",
        "Circuit ID Sub-optionCode": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Circuit ID Sub-option.Code-220",
        "Circuit ID Sub-optionLength": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Circuit ID Sub-option.Length-221",
        "Circuit ID Sub-optionData": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Circuit ID Sub-option.data-222",
        "Remote ID Sub-optionCode": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Remote ID Sub-option.Code-223",
        "Remote ID Sub-optionLength": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Remote ID Sub-option.Length-224",
        "Remote ID Sub-optionData": "dhcp.header.options.fields.nextOption.field.RelayAgent Option.Remote ID Sub-option.data-225",
        "PadEnd": "dhcp.header.options.fields.nextOption.field.pad.end-226",
        "CustomOptionCode": "dhcp.header.options.fields.nextOption.field.customOption.code-227",
        "CustomOptionLength": "dhcp.header.options.fields.nextOption.field.customOption.length-228",
        "CustomOptionData": "dhcp.header.options.fields.nextOption.field.customOption.data-229",
        "FieldsCustomOptionCode": "dhcp.header.options.fields.customOption.code-230",
        "FieldsCustomOptionLength": "dhcp.header.options.fields.customOption.length-231",
        "FieldsCustomOptionData": "dhcp.header.options.fields.customOption.data-232",
        "End255End": "dhcp.header.options.fields.end255.end-233",
        "FieldsPad": "dhcp.header.options.fields.pad-234",
    }

    def __init__(self, parent, list_op=False):
        super(Dhcp, self).__init__(parent, list_op)

    @property
    def OpCode(self):
        """
        Display Name: Message op code
        Default Value: 1
        Value Format: decimal
        Available enum values: BOOTREQUEST, 1, BOOTREPLY, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OpCode"]))

    @property
    def HwType(self):
        """
        Display Name: Hardware type
        Default Value: 1
        Value Format: decimal
        Available enum values: Ethernet(10MB), 1, Ethernet(3MB), 2, Amateur, 3, Proteon, 4, chaos, 5, IEEE 802 Net, 6, ARCNET, 7, Hyperchannel, 8, Lanstar, 9, Autonet, 10, LocalTalk, 11, Localnet, 12, UltraLink, 13, SMDS, 14, Frame Relay, 15, ATM, 16, HDLC, 17, Fibre Channel, 18, Serial Line, 20
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HwType"]))

    @property
    def HwAddressLen(self):
        """
        Display Name: Hardware address length (bytes)
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HwAddressLen"]))

    @property
    def Hops(self):
        """
        Display Name: Hops
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Hops"]))

    @property
    def TransactionId(self):
        """
        Display Name: Transaction ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TransactionId"]))

    @property
    def SecondsElapsed(self):
        """
        Display Name: Seconds elapsed
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SecondsElapsed"])
        )

    @property
    def BroadcastFlag(self):
        """
        Display Name: Broadcast flag
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x0000-No Broadcast, 0, 0x8000-Broadcast, 32768
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BroadcastFlag"]))

    @property
    def ClientIP(self):
        """
        Display Name: Client IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientIP"]))

    @property
    def YourIP(self):
        """
        Display Name: Your IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["YourIP"]))

    @property
    def ServerIP(self):
        """
        Display Name: Server IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerIP"]))

    @property
    def RelayAgentIP(self):
        """
        Display Name: Relay agent IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RelayAgentIP"]))

    @property
    def ClientHwAddress(self):
        """
        Display Name: Client hardware address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientHwAddress"])
        )

    @property
    def OptionalServerName(self):
        """
        Display Name: Optional server hostname
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionalServerName"])
        )

    @property
    def BootFile(self):
        """
        Display Name: Boot file name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BootFile"]))

    @property
    def OptionsMagicCookie(self):
        """
        Display Name: Magic cookie
        Default Value: 0x63825363
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionsMagicCookie"])
        )

    @property
    def SubnetMaskCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubnetMaskCode"])
        )

    @property
    def SubnetMaskLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubnetMaskLength"])
        )

    @property
    def SubnetMaskSubnetMask(self):
        """
        Display Name: Subnet mask
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubnetMaskSubnetMask"])
        )

    @property
    def TimeOffsetCode(self):
        """
        Display Name: Code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeOffsetCode"])
        )

    @property
    def TimeOffsetLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeOffsetLength"])
        )

    @property
    def TimeOffsetTimeOffset(self):
        """
        Display Name: Time offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeOffsetTimeOffset"])
        )

    @property
    def GatewaysCode(self):
        """
        Display Name: Code
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GatewaysCode"]))

    @property
    def GatewaysLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GatewaysLength"])
        )

    @property
    def AddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressesAddress"])
        )

    @property
    def TimeServerCode(self):
        """
        Display Name: Code
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeServerCode"])
        )

    @property
    def TimeServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeServerLength"])
        )

    @property
    def TimeserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TimeserverAddressesAddress"])
        )

    @property
    def NameServerCode(self):
        """
        Display Name: Code
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NameServerCode"])
        )

    @property
    def NameServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NameServerLength"])
        )

    @property
    def NameserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NameserverAddressesAddress"])
        )

    @property
    def DomainNameServerCode(self):
        """
        Display Name: Code
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainNameServerCode"])
        )

    @property
    def DomainNameServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainNameServerLength"])
        )

    @property
    def DomainnameserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DomainnameserverAddressesAddress"]),
        )

    @property
    def LogServerCode(self):
        """
        Display Name: Code
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LogServerCode"]))

    @property
    def LogServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LogServerLength"])
        )

    @property
    def LogserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LogserverAddressesAddress"])
        )

    @property
    def CookieServerCode(self):
        """
        Display Name: Code
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CookieServerCode"])
        )

    @property
    def CookieServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CookieServerLength"])
        )

    @property
    def CookieserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CookieserverAddressesAddress"])
        )

    @property
    def LprServerCode(self):
        """
        Display Name: Code
        Default Value: 9
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LprServerCode"]))

    @property
    def LprServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LprServerLength"])
        )

    @property
    def LprserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LprserverAddressesAddress"])
        )

    @property
    def ImpressServerCode(self):
        """
        Display Name: Code
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ImpressServerCode"])
        )

    @property
    def ImpressServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ImpressServerLength"])
        )

    @property
    def ImpressserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ImpressserverAddressesAddress"]),
        )

    @property
    def ResourceLocationServerCode(self):
        """
        Display Name: Code
        Default Value: 11
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ResourceLocationServerCode"])
        )

    @property
    def ResourceLocationServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ResourceLocationServerLength"])
        )

    @property
    def ResourcelocationserverAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ResourcelocationserverAddressesAddress"]
            ),
        )

    @property
    def HostNameCode(self):
        """
        Display Name: Code
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostNameCode"]))

    @property
    def HostNameLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HostNameLength"])
        )

    @property
    def NameLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NameLength"]))

    @property
    def NameData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NameData"]))

    @property
    def BootFileSizeCode(self):
        """
        Display Name: Code
        Default Value: 13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BootFileSizeCode"])
        )

    @property
    def BootFileSizeLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BootFileSizeLength"])
        )

    @property
    def BootFileSizeSize(self):
        """
        Display Name: Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BootFileSizeSize"])
        )

    @property
    def MeritDumpFileCode(self):
        """
        Display Name: Code
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeritDumpFileCode"])
        )

    @property
    def MeritDumpFileLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeritDumpFileLength"])
        )

    @property
    def MeritdumpfileNameLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeritdumpfileNameLength"])
        )

    @property
    def MeritdumpfileNameData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MeritdumpfileNameData"])
        )

    @property
    def DomainNameCode(self):
        """
        Display Name: Code
        Default Value: 15
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainNameCode"])
        )

    @property
    def DomainNameLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainNameLength"])
        )

    @property
    def DomainnameNameLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainnameNameLength"])
        )

    @property
    def DomainnameNameData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainnameNameData"])
        )

    @property
    def SwapServerCode(self):
        """
        Display Name: Code
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SwapServerCode"])
        )

    @property
    def SwapServerLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SwapServerLength"])
        )

    @property
    def SwapServerAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SwapServerAddress"])
        )

    @property
    def RootPathCode(self):
        """
        Display Name: Code
        Default Value: 17
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RootPathCode"]))

    @property
    def RootPathLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RootPathLength"])
        )

    @property
    def PathLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PathLength"]))

    @property
    def PathData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PathData"]))

    @property
    def ExtensionsPathCode(self):
        """
        Display Name: Code
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionsPathCode"])
        )

    @property
    def ExtensionsPathLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionsPathLength"])
        )

    @property
    def ExtensionspathPathLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionspathPathLength"])
        )

    @property
    def ExtensionspathPathData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionspathPathData"])
        )

    @property
    def IpForwardingCode(self):
        """
        Display Name: Code
        Default Value: 19
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpForwardingCode"])
        )

    @property
    def IpForwardingLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpForwardingLength"])
        )

    @property
    def IpForwardingFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpForwardingFlag"])
        )

    @property
    def NonLocalSourceRoutingCode(self):
        """
        Display Name: Code
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NonLocalSourceRoutingCode"])
        )

    @property
    def NonLocalSourceRoutingLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NonLocalSourceRoutingLength"])
        )

    @property
    def NonLocalSourceRoutingFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NonLocalSourceRoutingFlag"])
        )

    @property
    def PolicyFilterCode(self):
        """
        Display Name: Code
        Default Value: 21
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PolicyFilterCode"])
        )

    @property
    def PolicyFilterLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PolicyFilterLength"])
        )

    @property
    def AddressPairAddress1(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressPairAddress1"])
        )

    @property
    def AddressPairAddress2(self):
        """
        Display Name: Address / mask
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressPairAddress2"])
        )

    @property
    def MaxReassemblySizeCode(self):
        """
        Display Name: Code
        Default Value: 22
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReassemblySizeCode"])
        )

    @property
    def MaxReassemblySizeLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReassemblySizeLength"])
        )

    @property
    def MaxReassemblySizeSize(self):
        """
        Display Name: Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReassemblySizeSize"])
        )

    @property
    def DefaultTTLCode(self):
        """
        Display Name: Code
        Default Value: 23
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultTTLCode"])
        )

    @property
    def DefaultTTLLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DefaultTTLLength"])
        )

    @property
    def DefaultTTLTtl(self):
        """
        Display Name: TTL (Time to live)
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DefaultTTLTtl"]))

    @property
    def PathMTUAgingTimeCode(self):
        """
        Display Name: Code
        Default Value: 24
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathMTUAgingTimeCode"])
        )

    @property
    def PathMTUAgingTimeLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathMTUAgingTimeLength"])
        )

    @property
    def PathMTUAgingTimeTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathMTUAgingTimeTime"])
        )

    @property
    def PathMTUPlateauTableCode(self):
        """
        Display Name: Code
        Default Value: 25
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathMTUPlateauTableCode"])
        )

    @property
    def PathMTUPlateauTableLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathMTUPlateauTableLength"])
        )

    @property
    def PlateauSizeTableSize(self):
        """
        Display Name: Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PlateauSizeTableSize"])
        )

    @property
    def InterfaceMTUCode(self):
        """
        Display Name: Code
        Default Value: 26
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceMTUCode"])
        )

    @property
    def InterfaceMTULength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceMTULength"])
        )

    @property
    def InterfaceMTUMtu(self):
        """
        Display Name: MTU
        Default Value: 594
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterfaceMTUMtu"])
        )

    @property
    def SubnetsLocalCode(self):
        """
        Display Name: Code
        Default Value: 27
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubnetsLocalCode"])
        )

    @property
    def SubnetsLocalLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubnetsLocalLength"])
        )

    @property
    def SubnetsLocalFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubnetsLocalFlag"])
        )

    @property
    def BroadcastAddressCode(self):
        """
        Display Name: Code
        Default Value: 28
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BroadcastAddressCode"])
        )

    @property
    def BroadcastAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BroadcastAddressLength"])
        )

    @property
    def BroadcastAddressAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BroadcastAddressAddress"])
        )

    @property
    def PerformMaskDiscoveryCode(self):
        """
        Display Name: Code
        Default Value: 29
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PerformMaskDiscoveryCode"])
        )

    @property
    def PerformMaskDiscoveryLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PerformMaskDiscoveryLength"])
        )

    @property
    def PerformMaskDiscoveryFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PerformMaskDiscoveryFlag"])
        )

    @property
    def MaskSupplierOoptionCode(self):
        """
        Display Name: Code
        Default Value: 30
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaskSupplierOoptionCode"])
        )

    @property
    def MaskSupplierOoptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaskSupplierOoptionLength"])
        )

    @property
    def MaskSupplierOoptionFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaskSupplierOoptionFlag"])
        )

    @property
    def PerformRouterDiscoveryCode(self):
        """
        Display Name: Code
        Default Value: 31
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PerformRouterDiscoveryCode"])
        )

    @property
    def PerformRouterDiscoveryLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PerformRouterDiscoveryLength"])
        )

    @property
    def PerformRouterDiscoveryFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PerformRouterDiscoveryFlag"])
        )

    @property
    def RouterSolicitationAddressCode(self):
        """
        Display Name: Code
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RouterSolicitationAddressCode"]),
        )

    @property
    def RouterSolicitationAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RouterSolicitationAddressLength"]),
        )

    @property
    def RouterSolicitationAddressAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RouterSolicitationAddressAddress"]),
        )

    @property
    def StaticRouteCode(self):
        """
        Display Name: Code
        Default Value: 33
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StaticRouteCode"])
        )

    @property
    def StaticRouteLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StaticRouteLength"])
        )

    @property
    def AddresspairsAddressPairAddress1(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AddresspairsAddressPairAddress1"]),
        )

    @property
    def AddresspairsAddressPairAddress2(self):
        """
        Display Name: Address / mask
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AddresspairsAddressPairAddress2"]),
        )

    @property
    def TrailerEncapsulationOptionCode(self):
        """
        Display Name: Code
        Default Value: 34
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TrailerEncapsulationOptionCode"]),
        )

    @property
    def TrailerEncapsulationOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TrailerEncapsulationOptionLength"]),
        )

    @property
    def TrailerEncapsulationOptionFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["TrailerEncapsulationOptionFlag"]),
        )

    @property
    def ArpCacheTimeCode(self):
        """
        Display Name: Code
        Default Value: 35
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ArpCacheTimeCode"])
        )

    @property
    def ArpCacheTimeLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ArpCacheTimeLength"])
        )

    @property
    def ArpCacheTimeTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ArpCacheTimeTime"])
        )

    @property
    def EthernetEncapsulationCode(self):
        """
        Display Name: Code
        Default Value: 36
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EthernetEncapsulationCode"])
        )

    @property
    def EthernetEncapsulationLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EthernetEncapsulationLength"])
        )

    @property
    def EthernetEncapsulationFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EthernetEncapsulationFlag"])
        )

    @property
    def TcpDefaultTTLCode(self):
        """
        Display Name: Code
        Default Value: 37
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpDefaultTTLCode"])
        )

    @property
    def TcpDefaultTTLLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpDefaultTTLLength"])
        )

    @property
    def TcpDefaultTTLTtl(self):
        """
        Display Name: TTL (Time to live)
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpDefaultTTLTtl"])
        )

    @property
    def TcpKeepaliveIntervalCode(self):
        """
        Display Name: Code
        Default Value: 38
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpKeepaliveIntervalCode"])
        )

    @property
    def TcpKeepaliveIntervalLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpKeepaliveIntervalLength"])
        )

    @property
    def TcpKeepaliveIntervalTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpKeepaliveIntervalTime"])
        )

    @property
    def TcpKeepaliveGarbageCode(self):
        """
        Display Name: Code
        Default Value: 39
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpKeepaliveGarbageCode"])
        )

    @property
    def TcpKeepaliveGarbageLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpKeepaliveGarbageLength"])
        )

    @property
    def TcpKeepaliveGarbageFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Disable / No, 0, Enable / Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TcpKeepaliveGarbageFlag"])
        )

    @property
    def NisDomainCode(self):
        """
        Display Name: Code
        Default Value: 40
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NisDomainCode"]))

    @property
    def NisDomainLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NisDomainLength"])
        )

    @property
    def NisdomainNameLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NisdomainNameLength"])
        )

    @property
    def NisdomainNameData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NisdomainNameData"])
        )

    @property
    def NisServersCode(self):
        """
        Display Name: Code
        Default Value: 41
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NisServersCode"])
        )

    @property
    def NisServersLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NisServersLength"])
        )

    @property
    def NisserversAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NisserversAddressesAddress"])
        )

    @property
    def NtpServersCode(self):
        """
        Display Name: Code
        Default Value: 42
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NtpServersCode"])
        )

    @property
    def NtpServersLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NtpServersLength"])
        )

    @property
    def NtpserversAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NtpserversAddressesAddress"])
        )

    @property
    def VendorSpecificCode(self):
        """
        Display Name: Code
        Default Value: 43
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorSpecificCode"])
        )

    @property
    def VendorSpecificLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VendorSpecificLength"])
        )

    @property
    def ValueLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueLength"]))

    @property
    def ValueData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ValueData"]))

    @property
    def NbnsCode(self):
        """
        Display Name: Code
        Default Value: 44
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbnsCode"]))

    @property
    def NbnsLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbnsLength"]))

    @property
    def NbnsAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NbnsAddressesAddress"])
        )

    @property
    def NbddCode(self):
        """
        Display Name: Code
        Default Value: 45
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbddCode"]))

    @property
    def NbddLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbddLength"]))

    @property
    def NbddAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NbddAddressesAddress"])
        )

    @property
    def NbntCode(self):
        """
        Display Name: Code
        Default Value: 46
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbntCode"]))

    @property
    def NbntLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbntLength"]))

    @property
    def NbntNodeType(self):
        """
        Display Name: NetBOIS node type
        Default Value: 1
        Value Format: decimal
        Available enum values: B-node, 1, P-node, 2, M-node, 4, H-node, 8
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbntNodeType"]))

    @property
    def NbScopeCode(self):
        """
        Display Name: Code
        Default Value: 47
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbScopeCode"]))

    @property
    def NbScopeLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NbScopeLength"]))

    @property
    def NbscopeValueLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NbscopeValueLength"])
        )

    @property
    def NbscopeValueData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NbscopeValueData"])
        )

    @property
    def XFontServersCode(self):
        """
        Display Name: Code
        Default Value: 48
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["XFontServersCode"])
        )

    @property
    def XFontServersLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["XFontServersLength"])
        )

    @property
    def XfontserversAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["XfontserversAddressesAddress"])
        )

    @property
    def XFontManagersCode(self):
        """
        Display Name: Code
        Default Value: 49
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["XFontManagersCode"])
        )

    @property
    def XFontManagersLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["XFontManagersLength"])
        )

    @property
    def XfontmanagersAddressesAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["XfontmanagersAddressesAddress"]),
        )

    @property
    def RequestedIPAddressCode(self):
        """
        Display Name: Code
        Default Value: 50
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestedIPAddressCode"])
        )

    @property
    def RequestedIPAddressLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestedIPAddressLength"])
        )

    @property
    def RequestedIPAddressAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RequestedIPAddressAddress"])
        )

    @property
    def IpAddressLeaseTimeCode(self):
        """
        Display Name: Code
        Default Value: 51
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpAddressLeaseTimeCode"])
        )

    @property
    def IpAddressLeaseTimeLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpAddressLeaseTimeLength"])
        )

    @property
    def IpAddressLeaseTimeTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpAddressLeaseTimeTime"])
        )

    @property
    def OptionOverloadCode(self):
        """
        Display Name: Code
        Default Value: 52
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionOverloadCode"])
        )

    @property
    def OptionOverloadLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionOverloadLength"])
        )

    @property
    def OptionOverloadOverloadFlag(self):
        """
        Display Name: Overload flag
        Default Value: 1
        Value Format: decimal
        Available enum values: The 'file' field is used to hold options, 1, The 'sname' field is used to hold options, 2, Both fields are used to hold options, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionOverloadOverloadFlag"])
        )

    @property
    def DhcpMessageTypeCode(self):
        """
        Display Name: Code
        Default Value: 53
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DhcpMessageTypeCode"])
        )

    @property
    def DhcpMessageTypeLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DhcpMessageTypeLength"])
        )

    @property
    def DhcpMessageTypeMessageType(self):
        """
        Display Name: DHCP message type
        Default Value: 3
        Value Format: decimal
        Available enum values: DHCPDISCOVER, 1, DHCPOFFER, 2, DHCPREQUEST, 3, DHCPDECLINE, 4, DHCPACK, 5, DHCPNAK, 6, DHCPRELEASE, 7, DHCPINFORM, 8
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DhcpMessageTypeMessageType"])
        )

    @property
    def ServerIdentifierCode(self):
        """
        Display Name: Code
        Default Value: 54
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerIdentifierCode"])
        )

    @property
    def ServerIdentifierLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerIdentifierLength"])
        )

    @property
    def ServerIdentifierAddress(self):
        """
        Display Name: Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerIdentifierAddress"])
        )

    @property
    def ParameterRequestListCode(self):
        """
        Display Name: Code
        Default Value: 55
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ParameterRequestListCode"])
        )

    @property
    def ParameterRequestListLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ParameterRequestListLength"])
        )

    @property
    def DhcpOptionCodesLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DhcpOptionCodesLength"])
        )

    @property
    def DhcpOptionCodesData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DhcpOptionCodesData"])
        )

    @property
    def MessageCode(self):
        """
        Display Name: Code
        Default Value: 56
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MessageCode"]))

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
    def MessageNameLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageNameLength"])
        )

    @property
    def MessageNameData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageNameData"])
        )

    @property
    def MaxDHCPMessageSizeCode(self):
        """
        Display Name: Code
        Default Value: 57
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxDHCPMessageSizeCode"])
        )

    @property
    def MaxDHCPMessageSizeLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxDHCPMessageSizeLength"])
        )

    @property
    def MaxDHCPMessageSizeSize(self):
        """
        Display Name: Size
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxDHCPMessageSizeSize"])
        )

    @property
    def RenewalTimeCode(self):
        """
        Display Name: Code
        Default Value: 58
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RenewalTimeCode"])
        )

    @property
    def RenewalTimeLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RenewalTimeLength"])
        )

    @property
    def RenewalTimeTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RenewalTimeTime"])
        )

    @property
    def RebindingTimeCode(self):
        """
        Display Name: Code
        Default Value: 58
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RebindingTimeCode"])
        )

    @property
    def RebindingTimeLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RebindingTimeLength"])
        )

    @property
    def RebindingTimeTime(self):
        """
        Display Name: Time
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RebindingTimeTime"])
        )

    @property
    def ClassIdentifierCode(self):
        """
        Display Name: Code
        Default Value: 60
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClassIdentifierCode"])
        )

    @property
    def ClassIdentifierLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClassIdentifierLength"])
        )

    @property
    def IdentifierLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IdentifierLength"])
        )

    @property
    def IdentifierData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IdentifierData"])
        )

    @property
    def ClientIdentifierCode(self):
        """
        Display Name: Code
        Default Value: 61
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientIdentifierCode"])
        )

    @property
    def ClientIdentifierLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientIdentifierLength"])
        )

    @property
    def ClientIdentifierHwType(self):
        """
        Display Name: Hardware address type
        Default Value: 6
        Value Format: decimal
        Available enum values: Ethernet(10MB), 1, Ethernet(3MB), 2, Amateur, 3, Proteon, 4, chaos, 5, IEEE 802 Net, 6, ARCNET, 7, Hyperchannel, 8, Lanstar, 9, Autonet, 10, LocalTalk, 11, Localnet, 12, UltraLink, 13, SMDS, 14, Frame Relay, 15, ATM, 16, HDLC, 17, Fibre Channel, 18, Serial Line, 20
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientIdentifierHwType"])
        )

    @property
    def ClientIdLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientIdLength"])
        )

    @property
    def ClientIdData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientIdData"]))

    @property
    def UserClassInformationCode(self):
        """
        Display Name: Code
        Default Value: 77
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserClassInformationCode"])
        )

    @property
    def UserClassInformationLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserClassInformationLength"])
        )

    @property
    def User_class_informationLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["User_class_informationLength"])
        )

    @property
    def User_class_informationData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["User_class_informationData"])
        )

    @property
    def RelayAgentOptionCode(self):
        """
        Display Name: Code
        Default Value: 82
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayAgent OptionCode"])
        )

    @property
    def RelayAgentOptionLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RelayAgent OptionLength"])
        )

    @property
    def CircuitIDSuboptionCode(self):
        """
        Display Name: Code
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Circuit ID Sub-optionCode"])
        )

    @property
    def CircuitIDSuboptionLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Circuit ID Sub-optionLength"])
        )

    @property
    def CircuitIDSuboptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Circuit ID Sub-optionData"])
        )

    @property
    def RemoteIDSuboptionCode(self):
        """
        Display Name: Code
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Remote ID Sub-optionCode"])
        )

    @property
    def RemoteIDSuboptionLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Remote ID Sub-optionLength"])
        )

    @property
    def RemoteIDSuboptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Remote ID Sub-optionData"])
        )

    @property
    def PadEnd(self):
        """
        Display Name: Pad option
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadEnd"]))

    @property
    def CustomOptionCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomOptionCode"])
        )

    @property
    def CustomOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomOptionLength"])
        )

    @property
    def CustomOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomOptionData"])
        )

    @property
    def FieldsCustomOptionCode(self):
        """
        Display Name: Code
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldsCustomOptionCode"])
        )

    @property
    def FieldsCustomOptionLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldsCustomOptionLength"])
        )

    @property
    def FieldsCustomOptionData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FieldsCustomOptionData"])
        )

    @property
    def End255End(self):
        """
        Display Name: End option
        Default Value: 255
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["End255End"]))

    @property
    def FieldsPad(self):
        """
        Display Name: Pad Option
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FieldsPad"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
