from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DhcpWithPadding(Base):
    __slots__ = ()
    _SDM_NAME = "dhcpWithPadding"
    _SDM_ATT_MAP = {
        "HeaderOpCode": "dhcpWithPadding.header.opCode-1",
        "HeaderHwType": "dhcpWithPadding.header.hwType-2",
        "HeaderHwAddressLen": "dhcpWithPadding.header.hwAddressLen-3",
        "HeaderHops": "dhcpWithPadding.header.hops-4",
        "HeaderTransactionId": "dhcpWithPadding.header.transactionId-5",
        "HeaderSecondsElapsed": "dhcpWithPadding.header.secondsElapsed-6",
        "HeaderBroadcastFlag": "dhcpWithPadding.header.broadcastFlag-7",
        "HeaderClientIP": "dhcpWithPadding.header.clientIP-8",
        "HeaderYourIP": "dhcpWithPadding.header.yourIP-9",
        "HeaderServerIP": "dhcpWithPadding.header.serverIP-10",
        "HeaderRelayAgentIP": "dhcpWithPadding.header.relayAgentIP-11",
        "HeaderClientHwAddress": "dhcpWithPadding.header.clientHwAddress-12",
        "HeaderClientHwAddressPad": "dhcpWithPadding.header.clientHwAddressPad-13",
        "HeaderOptionalServerName": "dhcpWithPadding.header.optionalServerName-14",
        "HeaderBootFile": "dhcpWithPadding.header.bootFile-15",
        "OptionsMagicCookie": "dhcpWithPadding.header.options.magicCookie-16",
        "SubnetMaskCode": "dhcpWithPadding.header.options.fields.nextOption.field.subnetMask.code-17",
        "SubnetMaskLength": "dhcpWithPadding.header.options.fields.nextOption.field.subnetMask.length-18",
        "SubnetMaskSubnetMask": "dhcpWithPadding.header.options.fields.nextOption.field.subnetMask.subnetMask-19",
        "TimeOffsetCode": "dhcpWithPadding.header.options.fields.nextOption.field.timeOffset.code-20",
        "TimeOffsetLength": "dhcpWithPadding.header.options.fields.nextOption.field.timeOffset.length-21",
        "TimeOffsetTimeOffset": "dhcpWithPadding.header.options.fields.nextOption.field.timeOffset.timeOffset-22",
        "GatewaysCode": "dhcpWithPadding.header.options.fields.nextOption.field.gateways.code-23",
        "GatewaysLength": "dhcpWithPadding.header.options.fields.nextOption.field.gateways.length-24",
        "AddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.gateways.addresses.address-25",
        "TimeServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.timeServer.code-26",
        "TimeServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.timeServer.length-27",
        "TimeserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.timeServer.addresses.address-28",
        "NameServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.nameServer.code-29",
        "NameServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.nameServer.length-30",
        "NameserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.nameServer.addresses.address-31",
        "DomainNameServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.domainNameServer.code-32",
        "DomainNameServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.domainNameServer.length-33",
        "DomainnameserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.domainNameServer.addresses.address-34",
        "LogServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.logServer.code-35",
        "LogServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.logServer.length-36",
        "LogserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.logServer.addresses.address-37",
        "CookieServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.cookieServer.code-38",
        "CookieServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.cookieServer.length-39",
        "CookieserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.cookieServer.addresses.address-40",
        "LprServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.lprServer.code-41",
        "LprServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.lprServer.length-42",
        "LprserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.lprServer.addresses.address-43",
        "ImpressServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.impressServer.code-44",
        "ImpressServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.impressServer.length-45",
        "ImpressserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.impressServer.addresses.address-46",
        "ResourceLocationServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.resourceLocationServer.code-47",
        "ResourceLocationServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.resourceLocationServer.length-48",
        "ResourcelocationserverAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.resourceLocationServer.addresses.address-49",
        "HostNameCode": "dhcpWithPadding.header.options.fields.nextOption.field.hostName.code-50",
        "HostNameLength": "dhcpWithPadding.header.options.fields.nextOption.field.hostName.length-51",
        "NameLength": "dhcpWithPadding.header.options.fields.nextOption.field.hostName.name.length-52",
        "NameData": "dhcpWithPadding.header.options.fields.nextOption.field.hostName.name.data-53",
        "BootFileSizeCode": "dhcpWithPadding.header.options.fields.nextOption.field.bootFileSize.code-54",
        "BootFileSizeLength": "dhcpWithPadding.header.options.fields.nextOption.field.bootFileSize.length-55",
        "BootFileSizeSize": "dhcpWithPadding.header.options.fields.nextOption.field.bootFileSize.size-56",
        "MeritDumpFileCode": "dhcpWithPadding.header.options.fields.nextOption.field.meritDumpFile.code-57",
        "MeritDumpFileLength": "dhcpWithPadding.header.options.fields.nextOption.field.meritDumpFile.length-58",
        "MeritdumpfileNameLength": "dhcpWithPadding.header.options.fields.nextOption.field.meritDumpFile.name.length-59",
        "MeritdumpfileNameData": "dhcpWithPadding.header.options.fields.nextOption.field.meritDumpFile.name.data-60",
        "DomainNameCode": "dhcpWithPadding.header.options.fields.nextOption.field.domainName.code-61",
        "DomainNameLength": "dhcpWithPadding.header.options.fields.nextOption.field.domainName.length-62",
        "DomainnameNameLength": "dhcpWithPadding.header.options.fields.nextOption.field.domainName.name.length-63",
        "DomainnameNameData": "dhcpWithPadding.header.options.fields.nextOption.field.domainName.name.data-64",
        "SwapServerCode": "dhcpWithPadding.header.options.fields.nextOption.field.swapServer.code-65",
        "SwapServerLength": "dhcpWithPadding.header.options.fields.nextOption.field.swapServer.length-66",
        "SwapServerAddress": "dhcpWithPadding.header.options.fields.nextOption.field.swapServer.address-67",
        "RootPathCode": "dhcpWithPadding.header.options.fields.nextOption.field.rootPath.code-68",
        "RootPathLength": "dhcpWithPadding.header.options.fields.nextOption.field.rootPath.length-69",
        "PathLength": "dhcpWithPadding.header.options.fields.nextOption.field.rootPath.path.length-70",
        "PathData": "dhcpWithPadding.header.options.fields.nextOption.field.rootPath.path.data-71",
        "ExtensionsPathCode": "dhcpWithPadding.header.options.fields.nextOption.field.extensionsPath.code-72",
        "ExtensionsPathLength": "dhcpWithPadding.header.options.fields.nextOption.field.extensionsPath.length-73",
        "ExtensionspathPathLength": "dhcpWithPadding.header.options.fields.nextOption.field.extensionsPath.path.length-74",
        "ExtensionspathPathData": "dhcpWithPadding.header.options.fields.nextOption.field.extensionsPath.path.data-75",
        "IpForwardingCode": "dhcpWithPadding.header.options.fields.nextOption.field.ipForwarding.code-76",
        "IpForwardingLength": "dhcpWithPadding.header.options.fields.nextOption.field.ipForwarding.length-77",
        "IpForwardingFlag": "dhcpWithPadding.header.options.fields.nextOption.field.ipForwarding.flag-78",
        "NonLocalSourceRoutingCode": "dhcpWithPadding.header.options.fields.nextOption.field.nonLocalSourceRouting.code-79",
        "NonLocalSourceRoutingLength": "dhcpWithPadding.header.options.fields.nextOption.field.nonLocalSourceRouting.length-80",
        "NonLocalSourceRoutingFlag": "dhcpWithPadding.header.options.fields.nextOption.field.nonLocalSourceRouting.flag-81",
        "PolicyFilterCode": "dhcpWithPadding.header.options.fields.nextOption.field.policyFilter.code-82",
        "PolicyFilterLength": "dhcpWithPadding.header.options.fields.nextOption.field.policyFilter.length-83",
        "AddressPairAddress1": "dhcpWithPadding.header.options.fields.nextOption.field.policyFilter.addressPairs.addressPair.address1-84",
        "AddressPairAddress2": "dhcpWithPadding.header.options.fields.nextOption.field.policyFilter.addressPairs.addressPair.address2-85",
        "MaxReassemblySizeCode": "dhcpWithPadding.header.options.fields.nextOption.field.maxReassemblySize.code-86",
        "MaxReassemblySizeLength": "dhcpWithPadding.header.options.fields.nextOption.field.maxReassemblySize.length-87",
        "MaxReassemblySizeSize": "dhcpWithPadding.header.options.fields.nextOption.field.maxReassemblySize.size-88",
        "DefaultTTLCode": "dhcpWithPadding.header.options.fields.nextOption.field.defaultTTL.code-89",
        "DefaultTTLLength": "dhcpWithPadding.header.options.fields.nextOption.field.defaultTTL.length-90",
        "DefaultTTLTtl": "dhcpWithPadding.header.options.fields.nextOption.field.defaultTTL.ttl-91",
        "PathMTUAgingTimeCode": "dhcpWithPadding.header.options.fields.nextOption.field.pathMTUAgingTime.code-92",
        "PathMTUAgingTimeLength": "dhcpWithPadding.header.options.fields.nextOption.field.pathMTUAgingTime.length-93",
        "PathMTUAgingTimeTime": "dhcpWithPadding.header.options.fields.nextOption.field.pathMTUAgingTime.time-94",
        "PathMTUPlateauTableCode": "dhcpWithPadding.header.options.fields.nextOption.field.pathMTUPlateauTable.code-95",
        "PathMTUPlateauTableLength": "dhcpWithPadding.header.options.fields.nextOption.field.pathMTUPlateauTable.length-96",
        "PlateauSizeTableSize": "dhcpWithPadding.header.options.fields.nextOption.field.pathMTUPlateauTable.plateauSizeTable.size-97",
        "InterfaceMTUCode": "dhcpWithPadding.header.options.fields.nextOption.field.interfaceMTU.code-98",
        "InterfaceMTULength": "dhcpWithPadding.header.options.fields.nextOption.field.interfaceMTU.length-99",
        "InterfaceMTUMtu": "dhcpWithPadding.header.options.fields.nextOption.field.interfaceMTU.mtu-100",
        "SubnetsLocalCode": "dhcpWithPadding.header.options.fields.nextOption.field.subnetsLocal.code-101",
        "SubnetsLocalLength": "dhcpWithPadding.header.options.fields.nextOption.field.subnetsLocal.length-102",
        "SubnetsLocalFlag": "dhcpWithPadding.header.options.fields.nextOption.field.subnetsLocal.flag-103",
        "BroadcastAddressCode": "dhcpWithPadding.header.options.fields.nextOption.field.broadcastAddress.code-104",
        "BroadcastAddressLength": "dhcpWithPadding.header.options.fields.nextOption.field.broadcastAddress.length-105",
        "BroadcastAddressAddress": "dhcpWithPadding.header.options.fields.nextOption.field.broadcastAddress.address-106",
        "PerformMaskDiscoveryCode": "dhcpWithPadding.header.options.fields.nextOption.field.performMaskDiscovery.code-107",
        "PerformMaskDiscoveryLength": "dhcpWithPadding.header.options.fields.nextOption.field.performMaskDiscovery.length-108",
        "PerformMaskDiscoveryFlag": "dhcpWithPadding.header.options.fields.nextOption.field.performMaskDiscovery.flag-109",
        "MaskSupplierOoptionCode": "dhcpWithPadding.header.options.fields.nextOption.field.maskSupplierOoption.code-110",
        "MaskSupplierOoptionLength": "dhcpWithPadding.header.options.fields.nextOption.field.maskSupplierOoption.length-111",
        "MaskSupplierOoptionFlag": "dhcpWithPadding.header.options.fields.nextOption.field.maskSupplierOoption.flag-112",
        "PerformRouterDiscoveryCode": "dhcpWithPadding.header.options.fields.nextOption.field.performRouterDiscovery.code-113",
        "PerformRouterDiscoveryLength": "dhcpWithPadding.header.options.fields.nextOption.field.performRouterDiscovery.length-114",
        "PerformRouterDiscoveryFlag": "dhcpWithPadding.header.options.fields.nextOption.field.performRouterDiscovery.flag-115",
        "RouterSolicitationAddressCode": "dhcpWithPadding.header.options.fields.nextOption.field.routerSolicitationAddress.code-116",
        "RouterSolicitationAddressLength": "dhcpWithPadding.header.options.fields.nextOption.field.routerSolicitationAddress.length-117",
        "RouterSolicitationAddressAddress": "dhcpWithPadding.header.options.fields.nextOption.field.routerSolicitationAddress.address-118",
        "StaticRouteCode": "dhcpWithPadding.header.options.fields.nextOption.field.staticRoute.code-119",
        "StaticRouteLength": "dhcpWithPadding.header.options.fields.nextOption.field.staticRoute.length-120",
        "AddresspairsAddressPairAddress1": "dhcpWithPadding.header.options.fields.nextOption.field.staticRoute.addressPairs.addressPair.address1-121",
        "AddresspairsAddressPairAddress2": "dhcpWithPadding.header.options.fields.nextOption.field.staticRoute.addressPairs.addressPair.address2-122",
        "TrailerEncapsulationOptionCode": "dhcpWithPadding.header.options.fields.nextOption.field.trailerEncapsulationOption.code-123",
        "TrailerEncapsulationOptionLength": "dhcpWithPadding.header.options.fields.nextOption.field.trailerEncapsulationOption.length-124",
        "TrailerEncapsulationOptionFlag": "dhcpWithPadding.header.options.fields.nextOption.field.trailerEncapsulationOption.flag-125",
        "ArpCacheTimeCode": "dhcpWithPadding.header.options.fields.nextOption.field.arpCacheTime.code-126",
        "ArpCacheTimeLength": "dhcpWithPadding.header.options.fields.nextOption.field.arpCacheTime.length-127",
        "ArpCacheTimeTime": "dhcpWithPadding.header.options.fields.nextOption.field.arpCacheTime.time-128",
        "EthernetEncapsulationCode": "dhcpWithPadding.header.options.fields.nextOption.field.ethernetEncapsulation.code-129",
        "EthernetEncapsulationLength": "dhcpWithPadding.header.options.fields.nextOption.field.ethernetEncapsulation.length-130",
        "EthernetEncapsulationFlag": "dhcpWithPadding.header.options.fields.nextOption.field.ethernetEncapsulation.flag-131",
        "TcpDefaultTTLCode": "dhcpWithPadding.header.options.fields.nextOption.field.tcpDefaultTTL.code-132",
        "TcpDefaultTTLLength": "dhcpWithPadding.header.options.fields.nextOption.field.tcpDefaultTTL.length-133",
        "TcpDefaultTTLTtl": "dhcpWithPadding.header.options.fields.nextOption.field.tcpDefaultTTL.ttl-134",
        "TcpKeepaliveIntervalCode": "dhcpWithPadding.header.options.fields.nextOption.field.tcpKeepaliveInterval.code-135",
        "TcpKeepaliveIntervalLength": "dhcpWithPadding.header.options.fields.nextOption.field.tcpKeepaliveInterval.length-136",
        "TcpKeepaliveIntervalTime": "dhcpWithPadding.header.options.fields.nextOption.field.tcpKeepaliveInterval.time-137",
        "TcpKeepaliveGarbageCode": "dhcpWithPadding.header.options.fields.nextOption.field.tcpKeepaliveGarbage.code-138",
        "TcpKeepaliveGarbageLength": "dhcpWithPadding.header.options.fields.nextOption.field.tcpKeepaliveGarbage.length-139",
        "TcpKeepaliveGarbageFlag": "dhcpWithPadding.header.options.fields.nextOption.field.tcpKeepaliveGarbage.flag-140",
        "NisDomainCode": "dhcpWithPadding.header.options.fields.nextOption.field.nisDomain.code-141",
        "NisDomainLength": "dhcpWithPadding.header.options.fields.nextOption.field.nisDomain.length-142",
        "NisdomainNameLength": "dhcpWithPadding.header.options.fields.nextOption.field.nisDomain.name.length-143",
        "NisdomainNameData": "dhcpWithPadding.header.options.fields.nextOption.field.nisDomain.name.data-144",
        "NisServersCode": "dhcpWithPadding.header.options.fields.nextOption.field.nisServers.code-145",
        "NisServersLength": "dhcpWithPadding.header.options.fields.nextOption.field.nisServers.length-146",
        "NisserversAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.nisServers.addresses.address-147",
        "NtpServersCode": "dhcpWithPadding.header.options.fields.nextOption.field.ntpServers.code-148",
        "NtpServersLength": "dhcpWithPadding.header.options.fields.nextOption.field.ntpServers.length-149",
        "NtpserversAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.ntpServers.addresses.address-150",
        "VendorSpecificCode": "dhcpWithPadding.header.options.fields.nextOption.field.vendorSpecific.code-151",
        "VendorSpecificLength": "dhcpWithPadding.header.options.fields.nextOption.field.vendorSpecific.length-152",
        "ValueLength": "dhcpWithPadding.header.options.fields.nextOption.field.vendorSpecific.value.length-153",
        "ValueData": "dhcpWithPadding.header.options.fields.nextOption.field.vendorSpecific.value.data-154",
        "NbnsCode": "dhcpWithPadding.header.options.fields.nextOption.field.nbns.code-155",
        "NbnsLength": "dhcpWithPadding.header.options.fields.nextOption.field.nbns.length-156",
        "NbnsAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.nbns.addresses.address-157",
        "NbddCode": "dhcpWithPadding.header.options.fields.nextOption.field.nbdd.code-158",
        "NbddLength": "dhcpWithPadding.header.options.fields.nextOption.field.nbdd.length-159",
        "NbddAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.nbdd.addresses.address-160",
        "NbntCode": "dhcpWithPadding.header.options.fields.nextOption.field.nbnt.code-161",
        "NbntLength": "dhcpWithPadding.header.options.fields.nextOption.field.nbnt.length-162",
        "NbntNodeType": "dhcpWithPadding.header.options.fields.nextOption.field.nbnt.nodeType-163",
        "NbScopeCode": "dhcpWithPadding.header.options.fields.nextOption.field.nbScope.code-164",
        "NbScopeLength": "dhcpWithPadding.header.options.fields.nextOption.field.nbScope.length-165",
        "NbscopeValueLength": "dhcpWithPadding.header.options.fields.nextOption.field.nbScope.value.length-166",
        "NbscopeValueData": "dhcpWithPadding.header.options.fields.nextOption.field.nbScope.value.data-167",
        "XFontServersCode": "dhcpWithPadding.header.options.fields.nextOption.field.xFontServers.code-168",
        "XFontServersLength": "dhcpWithPadding.header.options.fields.nextOption.field.xFontServers.length-169",
        "XfontserversAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.xFontServers.addresses.address-170",
        "XFontManagersCode": "dhcpWithPadding.header.options.fields.nextOption.field.xFontManagers.code-171",
        "XFontManagersLength": "dhcpWithPadding.header.options.fields.nextOption.field.xFontManagers.length-172",
        "XfontmanagersAddressesAddress": "dhcpWithPadding.header.options.fields.nextOption.field.xFontManagers.addresses.address-173",
        "RequestedIPAddressCode": "dhcpWithPadding.header.options.fields.nextOption.field.requestedIPAddress.code-174",
        "RequestedIPAddressLength": "dhcpWithPadding.header.options.fields.nextOption.field.requestedIPAddress.length-175",
        "RequestedIPAddressAddress": "dhcpWithPadding.header.options.fields.nextOption.field.requestedIPAddress.address-176",
        "IpAddressLeaseTimeCode": "dhcpWithPadding.header.options.fields.nextOption.field.ipAddressLeaseTime.code-177",
        "IpAddressLeaseTimeLength": "dhcpWithPadding.header.options.fields.nextOption.field.ipAddressLeaseTime.length-178",
        "IpAddressLeaseTimeTime": "dhcpWithPadding.header.options.fields.nextOption.field.ipAddressLeaseTime.time-179",
        "OptionOverloadCode": "dhcpWithPadding.header.options.fields.nextOption.field.optionOverload.code-180",
        "OptionOverloadLength": "dhcpWithPadding.header.options.fields.nextOption.field.optionOverload.length-181",
        "OptionOverloadOverloadFlag": "dhcpWithPadding.header.options.fields.nextOption.field.optionOverload.overloadFlag-182",
        "DhcpMessageTypeCode": "dhcpWithPadding.header.options.fields.nextOption.field.dhcpMessageType.code-183",
        "DhcpMessageTypeLength": "dhcpWithPadding.header.options.fields.nextOption.field.dhcpMessageType.length-184",
        "DhcpMessageTypeMessageType": "dhcpWithPadding.header.options.fields.nextOption.field.dhcpMessageType.messageType-185",
        "ServerIdentifierCode": "dhcpWithPadding.header.options.fields.nextOption.field.serverIdentifier.code-186",
        "ServerIdentifierLength": "dhcpWithPadding.header.options.fields.nextOption.field.serverIdentifier.length-187",
        "ServerIdentifierAddress": "dhcpWithPadding.header.options.fields.nextOption.field.serverIdentifier.address-188",
        "ParameterRequestListCode": "dhcpWithPadding.header.options.fields.nextOption.field.parameterRequestList.code-189",
        "ParameterRequestListLength": "dhcpWithPadding.header.options.fields.nextOption.field.parameterRequestList.length-190",
        "DhcpOptionCodesLength": "dhcpWithPadding.header.options.fields.nextOption.field.parameterRequestList.dhcpOptionCodes.length-191",
        "DhcpOptionCodesData": "dhcpWithPadding.header.options.fields.nextOption.field.parameterRequestList.dhcpOptionCodes.data-192",
        "MessageCode": "dhcpWithPadding.header.options.fields.nextOption.field.message.code-193",
        "MessageLength": "dhcpWithPadding.header.options.fields.nextOption.field.message.length-194",
        "MessageNameLength": "dhcpWithPadding.header.options.fields.nextOption.field.message.name.length-195",
        "MessageNameData": "dhcpWithPadding.header.options.fields.nextOption.field.message.name.data-196",
        "MaxDHCPMessageSizeCode": "dhcpWithPadding.header.options.fields.nextOption.field.maxDHCPMessageSize.code-197",
        "MaxDHCPMessageSizeLength": "dhcpWithPadding.header.options.fields.nextOption.field.maxDHCPMessageSize.length-198",
        "MaxDHCPMessageSizeSize": "dhcpWithPadding.header.options.fields.nextOption.field.maxDHCPMessageSize.size-199",
        "RenewalTimeCode": "dhcpWithPadding.header.options.fields.nextOption.field.renewalTime.code-200",
        "RenewalTimeLength": "dhcpWithPadding.header.options.fields.nextOption.field.renewalTime.length-201",
        "RenewalTimeTime": "dhcpWithPadding.header.options.fields.nextOption.field.renewalTime.time-202",
        "RebindingTimeCode": "dhcpWithPadding.header.options.fields.nextOption.field.rebindingTime.code-203",
        "RebindingTimeLength": "dhcpWithPadding.header.options.fields.nextOption.field.rebindingTime.length-204",
        "RebindingTimeTime": "dhcpWithPadding.header.options.fields.nextOption.field.rebindingTime.time-205",
        "ClassIdentifierCode": "dhcpWithPadding.header.options.fields.nextOption.field.classIdentifier.code-206",
        "ClassIdentifierLength": "dhcpWithPadding.header.options.fields.nextOption.field.classIdentifier.length-207",
        "IdentifierLength": "dhcpWithPadding.header.options.fields.nextOption.field.classIdentifier.identifier.length-208",
        "IdentifierData": "dhcpWithPadding.header.options.fields.nextOption.field.classIdentifier.identifier.data-209",
        "ClientIdentifierCode": "dhcpWithPadding.header.options.fields.nextOption.field.clientIdentifier.code-210",
        "ClientIdentifierLength": "dhcpWithPadding.header.options.fields.nextOption.field.clientIdentifier.length-211",
        "ClientIdentifierHwType": "dhcpWithPadding.header.options.fields.nextOption.field.clientIdentifier.hwType-212",
        "ClientIdLength": "dhcpWithPadding.header.options.fields.nextOption.field.clientIdentifier.clientId.length-213",
        "ClientIdData": "dhcpWithPadding.header.options.fields.nextOption.field.clientIdentifier.clientId.data-214",
        "UserClassInformationCode": "dhcpWithPadding.header.options.fields.nextOption.field.userClassInformation.code-215",
        "UserClassInformationLength": "dhcpWithPadding.header.options.fields.nextOption.field.userClassInformation.length-216",
        "User_class_informationLength": "dhcpWithPadding.header.options.fields.nextOption.field.userClassInformation.user_class_information.Length-217",
        "User_class_informationData": "dhcpWithPadding.header.options.fields.nextOption.field.userClassInformation.user_class_information.data-218",
        "RelayAgent OptionCode": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Code-219",
        "RelayAgent OptionLength": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Length-220",
        "Circuit ID Sub-optionCode": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Circuit ID Sub-option.Code-221",
        "Circuit ID Sub-optionLength": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Circuit ID Sub-option.Length-222",
        "Circuit ID Sub-optionData": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Circuit ID Sub-option.data-223",
        "Remote ID Sub-optionCode": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Remote ID Sub-option.Code-224",
        "Remote ID Sub-optionLength": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Remote ID Sub-option.Length-225",
        "Remote ID Sub-optionData": "dhcpWithPadding.header.options.fields.nextOption.field.RelayAgent Option.Remote ID Sub-option.data-226",
        "PadEnd": "dhcpWithPadding.header.options.fields.nextOption.field.pad.end-227",
        "CustomOptionCode": "dhcpWithPadding.header.options.fields.nextOption.field.customOption.code-228",
        "CustomOptionLength": "dhcpWithPadding.header.options.fields.nextOption.field.customOption.length-229",
        "CustomOptionData": "dhcpWithPadding.header.options.fields.nextOption.field.customOption.data-230",
        "End255End": "dhcpWithPadding.header.options.fields.end255.end-231",
        "FieldsPad": "dhcpWithPadding.header.options.fields.pad-232",
    }

    def __init__(self, parent, list_op=False):
        super(DhcpWithPadding, self).__init__(parent, list_op)

    @property
    def HeaderOpCode(self):
        """
        Display Name: Message op code
        Default Value: 1
        Value Format: decimal
        Available enum values: BOOTREQUEST, 1, BOOTREPLY, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderOpCode"]))

    @property
    def HeaderHwType(self):
        """
        Display Name: Hardware type
        Default Value: 1
        Value Format: decimal
        Available enum values: Ethernet(10MB), 1, Ethernet(3MB), 2, Amateur, 3, Proteon, 4, chaos, 5, IEEE 802 Net, 6, ARCNET, 7, Hyperchannel, 8, Lanstar, 9, Autonet, 10, LocalTalk, 11, Localnet, 12, UltraLink, 13, SMDS, 14, Frame Relay, 15, ATM, 16, HDLC, 17, Fibre Channel, 18, Serial Line, 20
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderHwType"]))

    @property
    def HeaderHwAddressLen(self):
        """
        Display Name: Hardware address length (bytes)
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHwAddressLen"])
        )

    @property
    def HeaderHops(self):
        """
        Display Name: Hops
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderHops"]))

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
    def HeaderSecondsElapsed(self):
        """
        Display Name: Seconds elapsed
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderSecondsElapsed"])
        )

    @property
    def HeaderBroadcastFlag(self):
        """
        Display Name: Broadcast flag
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x0000-No Broadcast, 0, 0x8000-Broadcast, 32768
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBroadcastFlag"])
        )

    @property
    def HeaderClientIP(self):
        """
        Display Name: Client IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderClientIP"])
        )

    @property
    def HeaderYourIP(self):
        """
        Display Name: Your IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderYourIP"]))

    @property
    def HeaderServerIP(self):
        """
        Display Name: Server IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderServerIP"])
        )

    @property
    def HeaderRelayAgentIP(self):
        """
        Display Name: Relay agent IP address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderRelayAgentIP"])
        )

    @property
    def HeaderClientHwAddress(self):
        """
        Display Name: Client hardware address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderClientHwAddress"])
        )

    @property
    def HeaderClientHwAddressPad(self):
        """
        Display Name: Client hardware address padding
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderClientHwAddressPad"])
        )

    @property
    def HeaderOptionalServerName(self):
        """
        Display Name: Optional server hostname
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderOptionalServerName"])
        )

    @property
    def HeaderBootFile(self):
        """
        Display Name: Boot file name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderBootFile"])
        )

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
