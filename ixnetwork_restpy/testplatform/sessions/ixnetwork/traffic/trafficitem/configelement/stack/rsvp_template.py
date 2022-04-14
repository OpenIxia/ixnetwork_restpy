from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Rsvp(Base):
    __slots__ = ()
    _SDM_NAME = "rsvp"
    _SDM_ATT_MAP = {
        "RsvpMessegeVersion": "rsvp.rsvpMessege.version-1",
        "RsvpMessegeFlag": "rsvp.rsvpMessege.flag-2",
        "RsvpMessegeMessegeType": "rsvp.rsvpMessege.messegeType-3",
        "RsvpMessegeRsvpChecksum": "rsvp.rsvpMessege.rsvpChecksum-4",
        "RsvpMessegeTtl": "rsvp.rsvpMessege.ttl-5",
        "RsvpMessegeReserved": "rsvp.rsvpMessege.reserved-6",
        "RsvpMessegeRsvpLength": "rsvp.rsvpMessege.rsvpLength-7",
        "BundleMsgOptionalHeaderVersion": "rsvp.rsvpMessege.objects.object.bundleMsgOptionalHeader.version-8",
        "BundleMsgOptionalHeaderFlag": "rsvp.rsvpMessege.objects.object.bundleMsgOptionalHeader.flag-9",
        "BundleMsgOptionalHeaderMessegeType": "rsvp.rsvpMessege.objects.object.bundleMsgOptionalHeader.messegeType-10",
        "BundleMsgOptionalHeaderRsvpChecksum": "rsvp.rsvpMessege.objects.object.bundleMsgOptionalHeader.rsvpChecksum-11",
        "BundleMsgOptionalHeaderTtl": "rsvp.rsvpMessege.objects.object.bundleMsgOptionalHeader.ttl-12",
        "BundleMsgOptionalHeaderReserved": "rsvp.rsvpMessege.objects.object.bundleMsgOptionalHeader.reserved-13",
        "BundleMsgOptionalHeaderRsvpLength": "rsvp.rsvpMessege.objects.object.bundleMsgOptionalHeader.rsvpLength-14",
        "ObjectObjectLength": "rsvp.rsvpMessege.objects.object.objectLength-15",
        "ObjectClass": "rsvp.rsvpMessege.objects.object.class-16",
        "ObjectType": "rsvp.rsvpMessege.objects.object.type-17",
        "DataMessegeDataLength": "rsvp.rsvpMessege.objects.object.objectBody.dataMessege.dataLength-18",
        "DataMessegeData": "rsvp.rsvpMessege.objects.object.objectBody.dataMessege.data-19",
        "Ipv4UDPSESSIONClass1CType1DestAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4UDPSESSIONClass1CType1.destAddress-20",
        "Ipv4UDPSESSIONClass1CType1ProtocolId": "rsvp.rsvpMessege.objects.object.objectBody.ipv4UDPSESSIONClass1CType1.protocolId-21",
        "Ipv4UDPSESSIONClass1CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.ipv4UDPSESSIONClass1CType1.flags-22",
        "Ipv4UDPSESSIONClass1CType1DestPort": "rsvp.rsvpMessege.objects.object.objectBody.ipv4UDPSESSIONClass1CType1.destPort-23",
        "Ipv6UDPSESSIONClass1CType2DestAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6UDPSESSIONClass1CType2.destAddress-24",
        "Ipv6UDPSESSIONClass1CType2ProtocolId": "rsvp.rsvpMessege.objects.object.objectBody.ipv6UDPSESSIONClass1CType2.protocolId-25",
        "Ipv6UDPSESSIONClass1CType2Flags": "rsvp.rsvpMessege.objects.object.objectBody.ipv6UDPSESSIONClass1CType2.flags-26",
        "Ipv6UDPSESSIONClass1CType2DestPort": "rsvp.rsvpMessege.objects.object.objectBody.ipv6UDPSESSIONClass1CType2.destPort-27",
        "Ipv4GPISESSIONClass1CType3DestAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPISESSIONClass1CType3.destAddress-28",
        "Ipv4GPISESSIONClass1CType3ProtocolId": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPISESSIONClass1CType3.protocolId-29",
        "Ipv4GPISESSIONClass1CType3Flags": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPISESSIONClass1CType3.flags-30",
        "Ipv4GPISESSIONClass1CType3DestPort": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPISESSIONClass1CType3.destPort-31",
        "Ipv6GPISESSIONClass1CType4DestAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPISESSIONClass1CType4.destAddress-32",
        "Ipv6GPISESSIONClass1CType4ProtocolId": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPISESSIONClass1CType4.protocolId-33",
        "Ipv6GPISESSIONClass1CType4Flags": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPISESSIONClass1CType4.flags-34",
        "Ipv6GPISESSIONClass1CType4DestPort": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPISESSIONClass1CType4.destPort-35",
        "Lsptunnelipv4Class1CType7Ipv4TunnelEndPointAddress": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4Class1CType7.ipv4TunnelEndPointAddress-36",
        "Lsptunnelipv4Class1CType7Reserved": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4Class1CType7.reserved-37",
        "Lsptunnelipv4Class1CType7TunnelId": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4Class1CType7.tunnelId-38",
        "Lsptunnelipv4Class1CType7ExtendedTunnelId": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4Class1CType7.extendedTunnelId-39",
        "Lsptunnelipv6Class1CType8Ipv6TunnelEndPointAddress": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6Class1CType8.ipv6TunnelEndPointAddress-40",
        "Lsptunnelipv6Class1CType8Reserved": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6Class1CType8.reserved-41",
        "Lsptunnelipv6Class1CType8TunnelId": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6Class1CType8.tunnelId-42",
        "Lsptunnelipv6Class1CType8ExtendedTunnelId": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6Class1CType8.extendedTunnelId-43",
        "Rsvpaggregateip4class1CType9Ipv4SessionAddress": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip4class1CType9.ipv4SessionAddress-44",
        "Rsvpaggregateip4class1CType9Reserved": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip4class1CType9.reserved-45",
        "Rsvpaggregateip4class1CType9Flag": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip4class1CType9.flag-46",
        "Rsvpaggregateip4class1CType9Unused": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip4class1CType9.unused-47",
        "Rsvpaggregateip4class1CType9Dscp": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip4class1CType9.dscp-48",
        "Rsvpaggregateip6class1CType10Ipv6SessionAddress": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip6class1CType10.ipv6SessionAddress-49",
        "Rsvpaggregateip6class1CType10Reserved": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip6class1CType10.reserved-50",
        "Rsvpaggregateip6class1CType10Flag": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip6class1CType10.flag-51",
        "Rsvpaggregateip6class1CType10Unused": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip6class1CType10.unused-52",
        "Rsvpaggregateip6class1CType10Dscp": "rsvp.rsvpMessege.objects.object.objectBody.rsvpaggregateip6class1CType10.dscp-53",
        "P2mplsptunnelipv4Class1CType13P2mpId": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4Class1CType13.p2mpId-54",
        "P2mplsptunnelipv4Class1CType13Reserved": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4Class1CType13.reserved-55",
        "P2mplsptunnelipv4Class1CType13TunnelId": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4Class1CType13.tunnelId-56",
        "P2mplsptunnelipv4Class1CType13ExtendedTunnelId": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4Class1CType13.extendedTunnelId-57",
        "P2mplsptunnelipv6Class1CType14P2mpId": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6Class1CType14.p2mpId-58",
        "P2mplsptunnelipv6Class1CType14Reserved": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6Class1CType14.reserved-59",
        "P2mplsptunnelipv6Class1CType14TunnelId": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6Class1CType14.tunnelId-60",
        "P2mplsptunnelipv6Class1CType14ExtendedTunnelId": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6Class1CType14.extendedTunnelId-61",
        "RsvphopClassClass3CType1Ipv4NextPreviousHopAddress": "rsvp.rsvpMessege.objects.object.objectBody.rsvphopClassClass3CType1.ipv4NextPreviousHopAddress-62",
        "RsvphopClassClass3CType1LogicalInterfaceHandle": "rsvp.rsvpMessege.objects.object.objectBody.rsvphopClassClass3CType1.logicalInterfaceHandle-63",
        "RsvphopClassClass3CType2Ipv6NextPreviousHopAddress": "rsvp.rsvpMessege.objects.object.objectBody.rsvphopClassClass3CType2.ipv6NextPreviousHopAddress-64",
        "RsvphopClassClass3CType2LogicalInterfaceHandle": "rsvp.rsvpMessege.objects.object.objectBody.rsvphopClassClass3CType2.logicalInterfaceHandle-65",
        "Integrityclass4CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.integrityclass4CType1.flags-66",
        "Integrityclass4CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.integrityclass4CType1.reserved-67",
        "Integrityclass4CType1KeyId": "rsvp.rsvpMessege.objects.object.objectBody.integrityclass4CType1.keyId-68",
        "Integrityclass4CType1SequenceNumber": "rsvp.rsvpMessege.objects.object.objectBody.integrityclass4CType1.sequenceNumber-69",
        "Integrityclass4CType1MsgLength": "rsvp.rsvpMessege.objects.object.objectBody.integrityclass4CType1.msgLength-70",
        "Integrityclass4CType1KeyedMessege": "rsvp.rsvpMessege.objects.object.objectBody.integrityclass4CType1.keyedMessege-71",
        "TimevaluesClassClass5CType1RefreshPeriodR": "rsvp.rsvpMessege.objects.object.objectBody.timevaluesClassClass5CType1.refreshPeriodR-72",
        "Ipv4ERRORSPECClass6CType1Ipv4ErrorNodeAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4ERRORSPECClass6CType1.ipv4ErrorNodeAddress-73",
        "Ipv4ERRORSPECClass6CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.ipv4ERRORSPECClass6CType1.flags-74",
        "Ipv4ERRORSPECClass6CType1ErrorCode": "rsvp.rsvpMessege.objects.object.objectBody.ipv4ERRORSPECClass6CType1.errorCode-75",
        "Ipv4ERRORSPECClass6CType1ErrorValue": "rsvp.rsvpMessege.objects.object.objectBody.ipv4ERRORSPECClass6CType1.errorValue-76",
        "Ipv6ERRORSPECClass6CType2Ipv6ErrorNodeAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6ERRORSPECClass6CType2.ipv6ErrorNodeAddress-77",
        "Ipv6ERRORSPECClass6CType2Flags": "rsvp.rsvpMessege.objects.object.objectBody.ipv6ERRORSPECClass6CType2.flags-78",
        "Ipv6ERRORSPECClass6CType2ErrorCode": "rsvp.rsvpMessege.objects.object.objectBody.ipv6ERRORSPECClass6CType2.errorCode-79",
        "Ipv6ERRORSPECClass6CType2ErrorValue": "rsvp.rsvpMessege.objects.object.objectBody.ipv6ERRORSPECClass6CType2.errorValue-80",
        "Ipv4ScopeClassClass7CType1Ipv4SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4ScopeClassClass7CType1.ipv4SrcAddress-81",
        "Ipv6ScopeClassClass7CType2Ipv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6ScopeClassClass7CType2.ipv6SrcAddress-82",
        "StyleClassClass8CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.styleClassClass8CType1.flags-83",
        "StyleClassClass8CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.styleClassClass8CType1.reserved-84",
        "StyleClassClass8CType1SharingControl": "rsvp.rsvpMessege.objects.object.objectBody.styleClassClass8CType1.sharingControl-85",
        "StyleClassClass8CType1SenderSelectionControl": "rsvp.rsvpMessege.objects.object.objectBody.styleClassClass8CType1.senderSelectionControl-86",
        "SonetsdhClass9CType4SignalType": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass9CType4.signalType-87",
        "SonetsdhClass9CType4Rcc": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass9CType4.rcc-88",
        "SonetsdhClass9CType4Ncc": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass9CType4.ncc-89",
        "SonetsdhClass9CType4Nvc": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass9CType4.nvc-90",
        "SonetsdhClass9CType4Multiplier": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass9CType4.multiplier-91",
        "SonetsdhClass9CType4Transparency": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass9CType4.transparency-92",
        "SonetsdhClass9CType4Profile": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass9CType4.profile-93",
        "G709Class9CType5SignalType": "rsvp.rsvpMessege.objects.object.objectBody.g709Class9CType5.signalType-94",
        "G709Class9CType5Reserved": "rsvp.rsvpMessege.objects.object.objectBody.g709Class9CType5.reserved-95",
        "G709Class9CType5Nmc": "rsvp.rsvpMessege.objects.object.objectBody.g709Class9CType5.nmc-96",
        "G709Class9CType5Nvc": "rsvp.rsvpMessege.objects.object.objectBody.g709Class9CType5.nvc-97",
        "G709Class9CType5Multiplier": "rsvp.rsvpMessege.objects.object.objectBody.g709Class9CType5.multiplier-98",
        "ObjectbodyG709Class9CType5Reserved": "rsvp.rsvpMessege.objects.object.objectBody.g709Class9CType5.reserved-99",
        "Filterspecclass10CType1Ipv4SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType1.ipv4SrcAddress-100",
        "Filterspecclass10CType1Unused": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType1.unused-101",
        "Filterspecclass10CType1SrcPort": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType1.srcPort-102",
        "Filterspecclass10CType2Ipv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType2.ipv6SrcAddress-103",
        "Filterspecclass10CType2Unused": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType2.unused-104",
        "Filterspecclass10CType2SrcPort": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType2.srcPort-105",
        "Filterspecclass10CType3Ipv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType3.ipv6SrcAddress-106",
        "Filterspecclass10CType3Unused": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType3.unused-107",
        "Filterspecclass10CType3FlowLabel": "rsvp.rsvpMessege.objects.object.objectBody.filterspecclass10CType3.flowLabel-108",
        "Ipv4GPIFILTERSPECClass10CType4Ipv4SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPIFILTERSPECClass10CType4.ipv4SrcAddress-109",
        "Ipv4GPIFILTERSPECClass10CType4Gpi": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPIFILTERSPECClass10CType4.gpi-110",
        "Ipv6GPIFILTERSPECClass10CType5Ipv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPIFILTERSPECClass10CType5.ipv6SrcAddress-111",
        "Ipv6GPIFILTERSPECClass10CType5Gpi": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPIFILTERSPECClass10CType5.gpi-112",
        "Lsptunnelipv4FILTERSPECClass10CType7Ipv4TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4FILTERSPECClass10CType7.ipv4TunnelSenderAddress-113",
        "Lsptunnelipv4FILTERSPECClass10CType7Unused": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4FILTERSPECClass10CType7.unused-114",
        "Lsptunnelipv4FILTERSPECClass10CType7LspID": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4FILTERSPECClass10CType7.lspID-115",
        "Lsptunnelipv6FILTERSPECClass10CType8Ipv6TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6FILTERSPECClass10CType8.ipv6TunnelSenderAddress-116",
        "Lsptunnelipv6FILTERSPECClass10CType8Unused": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6FILTERSPECClass10CType8.unused-117",
        "Lsptunnelipv6FILTERSPECClass10CType8LspID": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6FILTERSPECClass10CType8.lspID-118",
        "P2mpLSPIPv4FILTERSPECClass10CType12Ipv4TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv4FILTERSPECClass10CType12.ipv4TunnelSenderAddress-119",
        "P2mpLSPIPv4FILTERSPECClass10CType12Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv4FILTERSPECClass10CType12.unused-120",
        "P2mpLSPIPv4FILTERSPECClass10CType12LspID": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv4FILTERSPECClass10CType12.lspID-121",
        "P2mpLSPIPv4FILTERSPECClass10CType12SubGroupOriginatorID": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv4FILTERSPECClass10CType12.subGroupOriginatorID-122",
        "ObjectbodyP2mpLSPIPv4FILTERSPECClass10CType12Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv4FILTERSPECClass10CType12.unused-123",
        "P2mpLSPIPv4FILTERSPECClass10CType12SubGroupID": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv4FILTERSPECClass10CType12.subGroupID-124",
        "P2mpLSPIPv6FILTERSPECClass10CType13Ipv6TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv6FILTERSPECClass10CType13.ipv6TunnelSenderAddress-125",
        "P2mpLSPIPv6FILTERSPECClass10CType13Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv6FILTERSPECClass10CType13.unused-126",
        "P2mpLSPIPv6FILTERSPECClass10CType13LspID": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv6FILTERSPECClass10CType13.lspID-127",
        "P2mpLSPIPv6FILTERSPECClass10CType13SubGroupOriginatorID": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv6FILTERSPECClass10CType13.subGroupOriginatorID-128",
        "ObjectbodyP2mpLSPIPv6FILTERSPECClass10CType13Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv6FILTERSPECClass10CType13.unused-129",
        "P2mpLSPIPv6FILTERSPECClass10CType13SubGroupID": "rsvp.rsvpMessege.objects.object.objectBody.p2mpLSPIPv6FILTERSPECClass10CType13.subGroupID-130",
        "Ipv4SENDERTEMPLATEClass11CType1Ipv4SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4SENDERTEMPLATEClass11CType1.ipv4SrcAddress-131",
        "Ipv4SENDERTEMPLATEClass11CType1Unused": "rsvp.rsvpMessege.objects.object.objectBody.ipv4SENDERTEMPLATEClass11CType1.unused-132",
        "Ipv4SENDERTEMPLATEClass11CType1SrcPort": "rsvp.rsvpMessege.objects.object.objectBody.ipv4SENDERTEMPLATEClass11CType1.srcPort-133",
        "Ipv6SENDERTEMPLATEClass11CType2Ipv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6SENDERTEMPLATEClass11CType2.ipv6SrcAddress-134",
        "Ipv6SENDERTEMPLATEClass11CType2Unused": "rsvp.rsvpMessege.objects.object.objectBody.ipv6SENDERTEMPLATEClass11CType2.unused-135",
        "Ipv6SENDERTEMPLATEClass11CType2SrcPort": "rsvp.rsvpMessege.objects.object.objectBody.ipv6SENDERTEMPLATEClass11CType2.srcPort-136",
        "Ipv4FlowlabelSENDERTEMPLATEClass11CType3Ipv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4FlowlabelSENDERTEMPLATEClass11CType3.ipv6SrcAddress-137",
        "Ipv4FlowlabelSENDERTEMPLATEClass11CType3Unused": "rsvp.rsvpMessege.objects.object.objectBody.ipv4FlowlabelSENDERTEMPLATEClass11CType3.unused-138",
        "Ipv4FlowlabelSENDERTEMPLATEClass11CType3FlowLabel": "rsvp.rsvpMessege.objects.object.objectBody.ipv4FlowlabelSENDERTEMPLATEClass11CType3.flowLabel-139",
        "Ipv4GPISENDERTEMPLATEClass11CType4Ipv4SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPISENDERTEMPLATEClass11CType4.ipv4SrcAddress-140",
        "Ipv4GPISENDERTEMPLATEClass11CType4Gpi": "rsvp.rsvpMessege.objects.object.objectBody.ipv4GPISENDERTEMPLATEClass11CType4.gpi-141",
        "Ipv6GPISENDERTEMPLATEClass11CType5Ipv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPISENDERTEMPLATEClass11CType5.ipv6SrcAddress-142",
        "Ipv6GPISENDERTEMPLATEClass11CType5Gpi": "rsvp.rsvpMessege.objects.object.objectBody.ipv6GPISENDERTEMPLATEClass11CType5.gpi-143",
        "Lsptunnelipv4SENDERTEMPLATEClass11CType7Ipv4TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4SENDERTEMPLATEClass11CType7.ipv4TunnelSenderAddress-144",
        "Lsptunnelipv4SENDERTEMPLATEClass11CType7Unused": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4SENDERTEMPLATEClass11CType7.unused-145",
        "Lsptunnelipv4SENDERTEMPLATEClass11CType7LspID": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv4SENDERTEMPLATEClass11CType7.lspID-146",
        "Lsptunnelipv6SENDERTEMPLATEClass11CType8Ipv6TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6SENDERTEMPLATEClass11CType8.ipv6TunnelSenderAddress-147",
        "Lsptunnelipv6SENDERTEMPLATEClass11CType8Unused": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6SENDERTEMPLATEClass11CType8.unused-148",
        "Lsptunnelipv6SENDERTEMPLATEClass11CType8LspID": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelipv6SENDERTEMPLATEClass11CType8.lspID-149",
        "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12Ipv4TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4SENDERTEMPLATEClass11CType12.ipv4TunnelSenderAddress-150",
        "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4SENDERTEMPLATEClass11CType12.unused-151",
        "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12LspID": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4SENDERTEMPLATEClass11CType12.lspID-152",
        "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12SubGroupOriginatorID": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4SENDERTEMPLATEClass11CType12.subGroupOriginatorID-153",
        "ObjectbodyP2mplsptunnelipv4SENDERTEMPLATEClass11CType12Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4SENDERTEMPLATEClass11CType12.unused-154",
        "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12SubGroupID": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv4SENDERTEMPLATEClass11CType12.subGroupID-155",
        "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13Ipv6TunnelSenderAddress": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6SENDERTEMPLATEClass11CType13.ipv6TunnelSenderAddress-156",
        "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6SENDERTEMPLATEClass11CType13.unused-157",
        "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13LspID": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6SENDERTEMPLATEClass11CType13.lspID-158",
        "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13SubGroupOriginatorID": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6SENDERTEMPLATEClass11CType13.subGroupOriginatorID-159",
        "ObjectbodyP2mplsptunnelipv6SENDERTEMPLATEClass11CType13Unused": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6SENDERTEMPLATEClass11CType13.unused-160",
        "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13SubGroupID": "rsvp.rsvpMessege.objects.object.objectBody.p2mplsptunnelipv6SENDERTEMPLATEClass11CType13.subGroupID-161",
        "IntservSENDERTSPECTEMPLATEClass12CType2VersionNumber": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.versionNumber-162",
        "IntservSENDERTSPECTEMPLATEClass12CType2Reserved1": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.reserved1-163",
        "IntservSENDERTSPECTEMPLATEClass12CType2OverallLength": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.overallLength-164",
        "IntservSENDERTSPECTEMPLATEClass12CType2ServiceHeader": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.serviceHeader-165",
        "IntservSENDERTSPECTEMPLATEClass12CType2ZeroBit": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.zeroBit-166",
        "IntservSENDERTSPECTEMPLATEClass12CType2Reserved2": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.reserved2-167",
        "IntservSENDERTSPECTEMPLATEClass12CType2LengthOfService1Data": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.lengthOfService1Data-168",
        "IntservSENDERTSPECTEMPLATEClass12CType2ParameterIDTokenBucketTSpec": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.parameterIDTokenBucketTSpec-169",
        "IntservSENDERTSPECTEMPLATEClass12CType2Parameter127Flag": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.parameter127Flag-170",
        "IntservSENDERTSPECTEMPLATEClass12CType2Parameter127Length": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.parameter127Length-171",
        "IntservSENDERTSPECTEMPLATEClass12CType2TokenBucketRate": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.tokenBucketRate-172",
        "IntservSENDERTSPECTEMPLATEClass12CType2TokenBucketSize": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.tokenBucketSize-173",
        "IntservSENDERTSPECTEMPLATEClass12CType2PeakDataRate": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.peakDataRate-174",
        "IntservSENDERTSPECTEMPLATEClass12CType2MinimumPolicedUnit": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.minimumPolicedUnit-175",
        "IntservSENDERTSPECTEMPLATEClass12CType2MaximumPacketSize": "rsvp.rsvpMessege.objects.object.objectBody.intservSENDERTSPECTEMPLATEClass12CType2.maximumPacketSize-176",
        "SonetsdhClass12CType4SignalType": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass12CType4.signalType-177",
        "SonetsdhClass12CType4Rcc": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass12CType4.rcc-178",
        "SonetsdhClass12CType4Ncc": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass12CType4.ncc-179",
        "SonetsdhClass12CType4Nvc": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass12CType4.nvc-180",
        "SonetsdhClass12CType4Multiplier": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass12CType4.multiplier-181",
        "SonetsdhClass12CType4Transparency": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass12CType4.transparency-182",
        "SonetsdhClass12CType4Profile": "rsvp.rsvpMessege.objects.object.objectBody.sonetsdhClass12CType4.profile-183",
        "G709Class12CType5SignalType": "rsvp.rsvpMessege.objects.object.objectBody.g709Class12CType5.signalType-184",
        "G709Class12CType5Reserved": "rsvp.rsvpMessege.objects.object.objectBody.g709Class12CType5.reserved-185",
        "G709Class12CType5Nmc": "rsvp.rsvpMessege.objects.object.objectBody.g709Class12CType5.nmc-186",
        "G709Class12CType5Nvc": "rsvp.rsvpMessege.objects.object.objectBody.g709Class12CType5.nvc-187",
        "G709Class12CType5Multiplier": "rsvp.rsvpMessege.objects.object.objectBody.g709Class12CType5.multiplier-188",
        "ObjectbodyG709Class12CType5Reserved": "rsvp.rsvpMessege.objects.object.objectBody.g709Class12CType5.reserved-189",
        "IntservADSPECTEMPLATEClass13CType2MessageFormatVersionNumber": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.messageFormatVersionNumber-190",
        "IntservADSPECTEMPLATEClass13CType2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.reserved-191",
        "IntservADSPECTEMPLATEClass13CType2MsgLength": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.msgLength-192",
        "GeneralParametersFragmentService1PerServiceHeaderServiceNumber1": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.perServiceHeaderServiceNumber1-193",
        "GeneralParametersFragmentService1X": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.x-194",
        "GeneralParametersFragmentService1Reserved3": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.reserved3-195",
        "GeneralParametersFragmentService1GlobalBreakBit": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.globalBreakBit-196",
        "GeneralParametersFragmentService1ParameterID4": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameterID4-197",
        "GeneralParametersFragmentService1Parameter4FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter4FlagByte-198",
        "GeneralParametersFragmentService1Parameter4Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter4Length-199",
        "GeneralParametersFragmentService1IsHopCnt": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.isHopCnt-200",
        "GeneralParametersFragmentService1ParameterID6": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameterID6-201",
        "GeneralParametersFragmentService1Parameter6FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter6FlagByte-202",
        "GeneralParametersFragmentService1Parameter6Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter6Length-203",
        "GeneralParametersFragmentService1PathBwEstimate": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.pathBwEstimate-204",
        "GeneralParametersFragmentService1ParameterID8": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameterID8-205",
        "GeneralParametersFragmentService1Parameter8FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter8FlagByte-206",
        "GeneralParametersFragmentService1Parameter8Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter8Length-207",
        "GeneralParametersFragmentService1MinimumPathLatency": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.minimumPathLatency-208",
        "GeneralParametersFragmentService1ParameterID10": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameterID10-209",
        "GeneralParametersFragmentService1Parameter10FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter10FlagByte-210",
        "GeneralParametersFragmentService1Parameter10Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.parameter10Length-211",
        "GeneralParametersFragmentService1ComposedMTU": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.generalParametersFragmentService1.composedMTU-212",
        "GuaranteedServiceFragmentService2PerServiceHeaderServiceNumber2": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.perServiceHeaderServiceNumber2-213",
        "GuaranteedServiceFragmentService2XBit": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.xBit-214",
        "GuaranteedServiceFragmentService2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.reserved-215",
        "GuaranteedServiceFragmentService2BreakBitAndLengthOfPerserviceData": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.breakBitAndLengthOfPerserviceData-216",
        "OptionalFieldsParameterIDParameter133ComposedCtot": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameterIDParameter133ComposedCtot-217",
        "OptionalFieldsParameter133FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter133FlagByte-218",
        "OptionalFieldsParameter133Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter133Length-219",
        "OptionalFieldsEndtoendComposedValueForCCtot": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.endtoendComposedValueForCCtot-220",
        "OptionalFieldsParameterIDParameter134ComposedDtot": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameterIDParameter134ComposedDtot-221",
        "OptionalFieldsParameter134FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter134FlagByte-222",
        "OptionalFieldsParameter134Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter134Length-223",
        "OptionalFieldsEndtoendComposedValueForDDtot": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.endtoendComposedValueForDDtot-224",
        "OptionalFieldsParameterIDParameter135ComposedCsum": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameterIDParameter135ComposedCsum-225",
        "OptionalFieldsParameter135FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter135FlagByte-226",
        "OptionalFieldsParameter135Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter135Length-227",
        "OptionalFieldsSincelastreshapingPointComposedCCsum": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.sincelastreshapingPointComposedCCsum-228",
        "OptionalFieldsParameterIDParameter136ComposedDsum": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameterIDParameter136ComposedDsum-229",
        "OptionalFieldsParameter136FlagByte": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter136FlagByte-230",
        "OptionalFieldsParameter136Length": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.parameter136Length-231",
        "OptionalFieldsSincelastreshapingPointComposedDDsum": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.sincelastreshapingPointComposedDDsum-232",
        "ServicespecificGeneralParameterHeadersvaluesServicespecificGeneralParameterHeadervalue": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.guaranteedServiceFragmentService2.optionalFields.servicespecificGeneralParameterHeadersvalues.servicespecificGeneralParameterHeadervalue-233",
        "ControlledLoadServiceDataFragmentPerServiceHeaderServiceNumber5": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.controlledLoadServiceDataFragment.perServiceHeaderServiceNumber5-234",
        "ControlledLoadServiceDataFragmentXBit": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.controlledLoadServiceDataFragment.xBit-235",
        "ControlledLoadServiceDataFragmentBreakBit": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.controlledLoadServiceDataFragment.breakBit-236",
        "ControlledLoadServiceDataFragmentLengthOfPerserviceData": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.controlledLoadServiceDataFragment.lengthOfPerserviceData-237",
        "ServicespecificGeneralParameterHeadersServicespecificGeneralParameterHeader": "rsvp.rsvpMessege.objects.object.objectBody.intservADSPECTEMPLATEClass13CType2.controlledLoadServiceDataFragment.servicespecificGeneralParameterHeaders.servicespecificGeneralParameterHeader-238",
        "PolicydataObjectClass14CType1Length": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.length-239",
        "PolicydataObjectClass14CType1Policydata": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.policydata-240",
        "PolicydataObjectClass14CType1Unused": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.unused-241",
        "PolicydataObjectClass14CType1DataOffset": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.dataOffset-242",
        "ObjectbodyPolicydataObjectClass14CType1Unused": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.unused-243",
        "PolicydataObjectClass14CType1OptionDataLength": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.optionDataLength-244",
        "PolicydataObjectClass14CType1OptionData": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.optionData-245",
        "PolicydataObjectClass14CType1PolicyDataLength": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.policyDataLength-246",
        "PolicydataObjectClass14CType1PolicyData": "rsvp.rsvpMessege.objects.object.objectBody.policydataObjectClass14CType1.policyData-247",
        "Ipv4RESVCONFIRMClass15CType1Ipv4ReceiverAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4RESVCONFIRMClass15CType1.ipv4ReceiverAddress-248",
        "Ipv6RESVCONFIRMClass15CType2Ipv6ReceiverAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6RESVCONFIRMClass15CType2.ipv6ReceiverAddress-249",
        "LabelObjectClass16CType1TopLabel": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectClass16CType1.topLabel-250",
        "LabelRequestWithoutLabelRangeClass19CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.labelRequestWithoutLabelRangeClass19CType1.reserved-251",
        "LabelRequestWithoutLabelRangeClass19CType1L3pid": "rsvp.rsvpMessege.objects.object.objectBody.labelRequestWithoutLabelRangeClass19CType1.l3pid-252",
        "LabelObjectWithATMLabelRangeClass19CType2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.reserved-253",
        "LabelObjectWithATMLabelRangeClass19CType2L3pid": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.l3pid-254",
        "LabelObjectWithATMLabelRangeClass19CType2MBit": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.mBit-255",
        "ObjectbodyLabelObjectWithATMLabelRangeClass19CType2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.reserved-256",
        "LabelObjectWithATMLabelRangeClass19CType2MinimumVPI": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.minimumVPI-257",
        "LabelObjectWithATMLabelRangeClass19CType2MinimumVCI": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.minimumVCI-258",
        "ObjectObjectbodyLabelObjectWithATMLabelRangeClass19CType2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.reserved-259",
        "LabelObjectWithATMLabelRangeClass19CType2MaximumVPI": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.maximumVPI-260",
        "LabelObjectWithATMLabelRangeClass19CType2MaximumVCI": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithATMLabelRangeClass19CType2.maximumVCI-261",
        "LabelObjectWithFrameRelayLabelRangeClass19CType3Reserved": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithFrameRelayLabelRangeClass19CType3.reserved-262",
        "LabelObjectWithFrameRelayLabelRangeClass19CType3L3pid": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithFrameRelayLabelRangeClass19CType3.l3pid-263",
        "LabelObjectWithFrameRelayLabelRangeClass19CType3Res": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithFrameRelayLabelRangeClass19CType3.res-264",
        "LabelObjectWithFrameRelayLabelRangeClass19CType3Dli": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithFrameRelayLabelRangeClass19CType3.dli-265",
        "LabelObjectWithFrameRelayLabelRangeClass19CType3MinimumDLCI": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithFrameRelayLabelRangeClass19CType3.minimumDLCI-266",
        "ObjectbodyLabelObjectWithFrameRelayLabelRangeClass19CType3Res": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithFrameRelayLabelRangeClass19CType3.res-267",
        "LabelObjectWithFrameRelayLabelRangeClass19CType3MaximumDLCI": "rsvp.rsvpMessege.objects.object.objectBody.labelObjectWithFrameRelayLabelRangeClass19CType3.maximumDLCI-268",
        "Ctype1LBit": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype1.lBit-269",
        "Ctype1Type": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype1.type-270",
        "Ctype1Length": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype1.length-271",
        "Ctype1Ipv4Address": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype1.ipv4Address-272",
        "Ctype1PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype1.prefixLength-273",
        "Ctype1Padding": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype1.padding-274",
        "Ctype2LBit": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype2.lBit-275",
        "Ctype2Type": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype2.type-276",
        "Ctype2Length": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype2.length-277",
        "Ctype2Ipv6Address": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype2.ipv6Address-278",
        "Ctype2PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype2.prefixLength-279",
        "Ctype2Padding": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype2.padding-280",
        "Ctype32LBit": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype32.lBit-281",
        "Ctype32Type": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype32.type-282",
        "Ctype32Length": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype32.length-283",
        "Ctype32AsNumber": "rsvp.rsvpMessege.objects.object.objectBody.explicitrouteClass20.subType.ctype32.asNumber-284",
        "SubtypeCtype1Type": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype1.type-285",
        "SubtypeCtype1Length": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype1.length-286",
        "SubtypeCtype1Ipv4Address": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype1.ipv4Address-287",
        "SubtypeCtype1PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype1.prefixLength-288",
        "Ctype1Flags": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype1.flags-289",
        "SubtypeCtype2Type": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype2.type-290",
        "SubtypeCtype2Length": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype2.length-291",
        "SubtypeCtype2Ipv6Address": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype2.ipv6Address-292",
        "SubtypeCtype2PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype2.prefixLength-293",
        "Ctype2Flags": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype2.flags-294",
        "Ctype3Type": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype3.type-295",
        "Ctype3Length": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype3.length-296",
        "Ctype3Flags": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype3.flags-297",
        "Ctype3Ctype": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype3.ctype-298",
        "Ctype3ContentsOfLabelObject": "rsvp.rsvpMessege.objects.object.objectBody.recordrouteClass21.subType.ctype3.contentsOfLabelObject-299",
        "HelloREQUESTAckClass22CType12SrcInstance": "rsvp.rsvpMessege.objects.object.objectBody.helloREQUESTAckClass22CType12.srcInstance-300",
        "HelloREQUESTAckClass22CType12DestInstance": "rsvp.rsvpMessege.objects.object.objectBody.helloREQUESTAckClass22CType12.destInstance-301",
        "Messageidclass23CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.messageidclass23CType1.flags-302",
        "Messageidclass23CType1Epoch": "rsvp.rsvpMessege.objects.object.objectBody.messageidclass23CType1.epoch-303",
        "Messageidclass23CType1MessageIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.messageidclass23CType1.messageIdentifier-304",
        "MessageidAckNackclass24CType12Flags": "rsvp.rsvpMessege.objects.object.objectBody.messageidAckNackclass24CType12.flags-305",
        "MessageidAckNackclass24CType12Epoch": "rsvp.rsvpMessege.objects.object.objectBody.messageidAckNackclass24CType12.epoch-306",
        "MessageidAckNackclass24CType12MessageIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.messageidAckNackclass24CType12.messageIdentifier-307",
        "Messageidlistclass25CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.messageidlistclass25CType1.flags-308",
        "Messageidlistclass25CType1Epoch": "rsvp.rsvpMessege.objects.object.objectBody.messageidlistclass25CType1.epoch-309",
        "MessageidlistMessageIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.messageidlistclass25CType1.messageidlist.messageIdentifier-310",
        "MessageidsourceListIPv4class25CType2Flags": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv4class25CType2.flags-311",
        "MessageidsourceListIPv4class25CType2Epoch": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv4class25CType2.epoch-312",
        "Messageidsourcelistipv4class25ctype2MessageidlistMessageIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv4class25CType2.messageidlist.messageIdentifier-313",
        "MessageidlistSourceIPAddress": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv4class25CType2.messageidlist.sourceIPAddress-314",
        "MessageidsourceListIPv6class25CType3Flags": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv6class25CType3.flags-315",
        "MessageidsourceListIPv6class25CType3Epoch": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv6class25CType3.epoch-316",
        "Messageidsourcelistipv6class25ctype3MessageidlistMessageIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv6class25CType3.messageidlist.messageIdentifier-317",
        "Messageidsourcelistipv6class25ctype3MessageidlistSourceIPAddress": "rsvp.rsvpMessege.objects.object.objectBody.messageidsourceListIPv6class25CType3.messageidlist.sourceIPAddress-318",
        "MessageidmcastlistIPv4class25CType4Flags": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv4class25CType4.flags-319",
        "MessageidmcastlistIPv4class25CType4Epoch": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv4class25CType4.epoch-320",
        "Messageidmcastlistipv4class25ctype4MessageidlistMessageIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv4class25CType4.messageidlist.messageIdentifier-321",
        "Messageidmcastlistipv4class25ctype4MessageidlistSourceIPAddress": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv4class25CType4.messageidlist.sourceIPAddress-322",
        "MessageidlistDestinationIPAddress": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv4class25CType4.messageidlist.destinationIPAddress-323",
        "MessageidmcastlistIPv6class25CType5Flags": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv6class25CType5.flags-324",
        "MessageidmcastlistIPv6class25CType5Epoch": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv6class25CType5.epoch-325",
        "Messageidmcastlistipv6class25ctype5MessageidlistMessageIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv6class25CType5.messageidlist.messageIdentifier-326",
        "Messageidmcastlistipv6class25ctype5MessageidlistSourceIPAddress": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv6class25CType5.messageidlist.sourceIPAddress-327",
        "Messageidmcastlistipv6class25ctype5MessageidlistDestinationIPAddress": "rsvp.rsvpMessege.objects.object.objectBody.messageidmcastlistIPv6class25CType5.messageidlist.destinationIPAddress-328",
        "Ipv4DIAGNOSTICclass30CType1MaxRSVPhops": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.maxRSVPhops-329",
        "Ipv4DIAGNOSTICclass30CType1Rsvphopcount": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.rsvphopcount-330",
        "Ipv4DIAGNOSTICclass30CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.reserved-331",
        "Ipv4DIAGNOSTICclass30CType1MfBit": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.mfBit-332",
        "Ipv4DIAGNOSTICclass30CType1RequestIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.requestIdentifier-333",
        "Ipv4DIAGNOSTICclass30CType1PathMTU": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.pathMTU-334",
        "Ipv4DIAGNOSTICclass30CType1FragmentOffset": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.fragmentOffset-335",
        "Ipv4DIAGNOSTICclass30CType1Lasthopaddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.lasthopaddress-336",
        "SenderTemplateObjectIpv4SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.senderTemplateObject.ipv4SrcAddress-337",
        "SenderTemplateObjectGeneralizedPortIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.senderTemplateObject.generalizedPortIdentifier-338",
        "FilterSpecTemplateObjectIpv4SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.filterSpecTemplateObject.ipv4SrcAddress-339",
        "FilterSpecTemplateObjectGeneralizedPortIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.ipv4DIAGNOSTICclass30CType1.filterSpecTemplateObject.generalizedPortIdentifier-340",
        "Ipv6DIAGNOSTICclass30CType2MaxRSVPhops": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.maxRSVPhops-341",
        "Ipv6DIAGNOSTICclass30CType2Rsvphopcount": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.rsvphopcount-342",
        "Ipv6DIAGNOSTICclass30CType2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.reserved-343",
        "Ipv6DIAGNOSTICclass30CType2MfBit": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.mfBit-344",
        "Ipv6DIAGNOSTICclass30CType2RequestIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.requestIdentifier-345",
        "Ipv6DIAGNOSTICclass30CType2PathMTU": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.pathMTU-346",
        "Ipv6DIAGNOSTICclass30CType2FragmentOffset": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.fragmentOffset-347",
        "Ipv6DIAGNOSTICclass30CType2Lasthopaddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.lasthopaddress-348",
        "SenderTemplateObjectIpv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.senderTemplateObject.ipv6SrcAddress-349",
        "Ipv6diagnosticclass30ctype2SenderTemplateObjectGeneralizedPortIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.senderTemplateObject.generalizedPortIdentifier-350",
        "FilterSpecTemplateObjectIpv6SrcAddress": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.filterSpecTemplateObject.ipv6SrcAddress-351",
        "Ipv6diagnosticclass30ctype2FilterSpecTemplateObjectGeneralizedPortIdentifier": "rsvp.rsvpMessege.objects.object.objectBody.ipv6DIAGNOSTICclass30CType2.filterSpecTemplateObject.generalizedPortIdentifier-352",
        "ClassTypeClass": "rsvp.rsvpMessege.objects.object.objectBody.diagselectclass33CType1.classType.class-353",
        "ClassTypeCtype": "rsvp.rsvpMessege.objects.object.objectBody.diagselectclass33CType1.classType.ctype-354",
        "RouteIPv4Objectclass31CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.routeIPv4Objectclass31CType1.reserved-355",
        "RouteIPv4Objectclass31CType1RPointer": "rsvp.rsvpMessege.objects.object.objectBody.routeIPv4Objectclass31CType1.rPointer-356",
        "NodeAddressListRsvpNodeAddress": "rsvp.rsvpMessege.objects.object.objectBody.routeIPv4Objectclass31CType1.nodeAddressList.rsvpNodeAddress-357",
        "RouteIPv6Objectclass31CType2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.routeIPv6Objectclass31CType2.reserved-358",
        "RouteIPv6Objectclass31CType2RPointer": "rsvp.rsvpMessege.objects.object.objectBody.routeIPv6Objectclass31CType2.rPointer-359",
        "Routeipv6objectclass31ctype2NodeAddressListRsvpNodeAddress": "rsvp.rsvpMessege.objects.object.objectBody.routeIPv6Objectclass31CType2.nodeAddressList.rsvpNodeAddress-360",
        "Diagresponseclass32CType1DreqArrivalTime": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.dreqArrivalTime-361",
        "Diagresponseclass32CType1IncomingInterfaceAddress": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.incomingInterfaceAddress-362",
        "Diagresponseclass32CType1OutgoingInterfaceAddress": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.outgoingInterfaceAddress-363",
        "Diagresponseclass32CType1PreviousRSVPHopRouterAddress": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.previousRSVPHopRouterAddress-364",
        "Diagresponseclass32CType1Dttl": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.dttl-365",
        "Diagresponseclass32CType1MBit": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.mBit-366",
        "Diagresponseclass32CType1Rerr": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.rerr-367",
        "Diagresponseclass32CType1K": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.k-368",
        "Diagresponseclass32CType1TimerValue": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseclass32CType1.timerValue-369",
        "DiagresponseIPv6class32CType2DreqArrivalTime": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.dreqArrivalTime-370",
        "DiagresponseIPv6class32CType2IncomingInterfaceAddress": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.incomingInterfaceAddress-371",
        "DiagresponseIPv6class32CType2OutgoingInterfaceAddress": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.outgoingInterfaceAddress-372",
        "DiagresponseIPv6class32CType2PreviousRSVPHopRouterAddress": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.previousRSVPHopRouterAddress-373",
        "DiagresponseIPv6class32CType2Dttl": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.dttl-374",
        "DiagresponseIPv6class32CType2MBit": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.mBit-375",
        "DiagresponseIPv6class32CType2Rerr": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.rerr-376",
        "DiagresponseIPv6class32CType2K": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.k-377",
        "DiagresponseIPv6class32CType2TimerValue": "rsvp.rsvpMessege.objects.object.objectBody.diagresponseIPv6class32CType2.timerValue-378",
        "S2lsublspipv4Class50CType1Ipv4S2LSubLSPDestinationAddress": "rsvp.rsvpMessege.objects.object.objectBody.s2lsublspipv4Class50CType1.ipv4S2LSubLSPDestinationAddress-379",
        "S2lsublspipv6Class50CType2Ipv6S2LSubLSPDestinationAddress": "rsvp.rsvpMessege.objects.object.objectBody.s2lsublspipv6Class50CType2.ipv6S2LSubLSPDestinationAddress-380",
        "DetourObjectIPv4class63CType7Lengthbytes": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv4class63CType7.lengthbytes-381",
        "DetourObjectIPv4class63CType7ClassNum": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv4class63CType7.classNum-382",
        "DetourObjectIPv4class63CType7Ctype": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv4class63CType7.ctype-383",
        "PlrAddressListPlrID": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv4class63CType7.plrAddressList.plrID-384",
        "PlrAddressListAvoidNodeID": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv4class63CType7.plrAddressList.avoidNodeID-385",
        "DetourObjectIPv6class63CType8Lengthbytes": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv6class63CType8.lengthbytes-386",
        "DetourObjectIPv6class63CType8ClassNum": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv6class63CType8.classNum-387",
        "DetourObjectIPv6class63CType8Ctype": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv6class63CType8.ctype-388",
        "Detourobjectipv6class63ctype8PlrAddressListPlrID": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv6class63CType8.plrAddressList.plrID-389",
        "Detourobjectipv6class63ctype8PlrAddressListAvoidNodeID": "rsvp.rsvpMessege.objects.object.objectBody.detourObjectIPv6class63CType8.plrAddressList.avoidNodeID-390",
        "ChallengeObjectclass64CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.challengeObjectclass64CType1.reserved-391",
        "ChallengeObjectclass64CType1KeyId": "rsvp.rsvpMessege.objects.object.objectBody.challengeObjectclass64CType1.keyId-392",
        "ChallengeObjectclass64CType1ChallengeCookie": "rsvp.rsvpMessege.objects.object.objectBody.challengeObjectclass64CType1.challengeCookie-393",
        "DiffservELSPclass65CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.diffservELSPclass65CType1.reserved-394",
        "DiffservELSPclass65CType1Mapnb": "rsvp.rsvpMessege.objects.object.objectBody.diffservELSPclass65CType1.mapnb-395",
        "MapListReserved": "rsvp.rsvpMessege.objects.object.objectBody.diffservELSPclass65CType1.mapList.reserved-396",
        "MapListExp": "rsvp.rsvpMessege.objects.object.objectBody.diffservELSPclass65CType1.mapList.exp-397",
        "MapListPhbid": "rsvp.rsvpMessege.objects.object.objectBody.diffservELSPclass65CType1.mapList.phbid-398",
        "DiffservLLSPclass65CType2Reserved": "rsvp.rsvpMessege.objects.object.objectBody.diffservLLSPclass65CType2.reserved-399",
        "DiffservLLSPclass65CType2Psc": "rsvp.rsvpMessege.objects.object.objectBody.diffservLLSPclass65CType2.psc-400",
        "Classtypeclass66CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.classtypeclass66CType1.reserved-401",
        "Classtypeclass66CType1Ct": "rsvp.rsvpMessege.objects.object.objectBody.classtypeclass66CType1.ct-402",
        "Lsptunnelinterfaceidclass193CType1LsrId": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelinterfaceidclass193CType1.lsrId-403",
        "Lsptunnelinterfaceidclass193CType1InterfaceID": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelinterfaceidclass193CType1.interfaceID-404",
        "SubtypeCtype1LBit": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype1.lBit-405",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype1Type": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype1.type-406",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype1Length": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype1.length-407",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype1Ipv4Address": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype1.ipv4Address-408",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype1PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype1.prefixLength-409",
        "SubtypeCtype1Padding": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype1.padding-410",
        "SubtypeCtype2LBit": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype2.lBit-411",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype2Type": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype2.type-412",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype2Length": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype2.length-413",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype2Ipv6Address": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype2.ipv6Address-414",
        "Secondaryexplicitrouteclass200ctype2SubtypeCtype2PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype2.prefixLength-415",
        "SubtypeCtype2Padding": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype2.padding-416",
        "SubtypeCtype32LBit": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype32.lBit-417",
        "SubtypeCtype32Type": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype32.type-418",
        "SubtypeCtype32Length": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype32.length-419",
        "SubtypeCtype32AsNumber": "rsvp.rsvpMessege.objects.object.objectBody.secondaryexplicitrouteClass200CType2.subType.ctype32.asNumber-420",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype1Type": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype1.type-421",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype1Length": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype1.length-422",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype1Ipv4Address": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype1.ipv4Address-423",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype1PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype1.prefixLength-424",
        "SubtypeCtype1Flags": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype1.flags-425",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype2Type": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype2.type-426",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype2Length": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype2.length-427",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype2Ipv6Address": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype2.ipv6Address-428",
        "Secondaryrecordrouteclass201ctype2SubtypeCtype2PrefixLength": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype2.prefixLength-429",
        "SubtypeCtype2Flags": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype2.flags-430",
        "SubtypeCtype3Type": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype3.type-431",
        "SubtypeCtype3Length": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype3.length-432",
        "SubtypeCtype3Flags": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype3.flags-433",
        "SubtypeCtype3Ctype": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype3.ctype-434",
        "SubtypeCtype3ContentsOfLabelObject": "rsvp.rsvpMessege.objects.object.objectBody.secondaryrecordrouteClass201CType2.subType.ctype3.contentsOfLabelObject-435",
        "Fastrerouteclass205CType1Lengthbytes": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.lengthbytes-436",
        "Fastrerouteclass205CType1ClassNum": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.classNum-437",
        "Fastrerouteclass205CType1Ctype": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.ctype-438",
        "Fastrerouteclass205CType1SetupPrio": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.setupPrio-439",
        "Fastrerouteclass205CType1HoldingPrio": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.holdingPrio-440",
        "Fastrerouteclass205CType1Hoplimit": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.hoplimit-441",
        "Fastrerouteclass205CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.flags-442",
        "Fastrerouteclass205CType1Bandwidth": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.bandwidth-443",
        "Fastrerouteclass205CType1Includeany": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.includeany-444",
        "Fastrerouteclass205CType1Excludeany": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.excludeany-445",
        "Fastrerouteclass205CType1Includeall": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType1.includeall-446",
        "Fastrerouteclass205CType7Lengthbytes": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.lengthbytes-447",
        "Fastrerouteclass205CType7ClassNum": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.classNum-448",
        "Fastrerouteclass205CType7Ctype": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.ctype-449",
        "Fastrerouteclass205CType7SetupPrio": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.setupPrio-450",
        "Fastrerouteclass205CType7HoldingPrio": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.holdingPrio-451",
        "Fastrerouteclass205CType7Hoplimit": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.hoplimit-452",
        "Fastrerouteclass205CType7Reserved": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.reserved-453",
        "Fastrerouteclass205CType7Bandwidth": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.bandwidth-454",
        "Fastrerouteclass205CType7Includeany": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.includeany-455",
        "Fastrerouteclass205CType7Excludeany": "rsvp.rsvpMessege.objects.object.objectBody.fastrerouteclass205CType7.excludeany-456",
        "Lsptunnelsessionattributeclass207CType7SetupPrio": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelsessionattributeclass207CType7.setupPrio-457",
        "Lsptunnelsessionattributeclass207CType7HoldingPrio": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelsessionattributeclass207CType7.holdingPrio-458",
        "Lsptunnelsessionattributeclass207CType7Flags": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelsessionattributeclass207CType7.flags-459",
        "Lsptunnelsessionattributeclass207CType7NameLength": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelsessionattributeclass207CType7.nameLength-460",
        "Lsptunnelsessionattributeclass207CType7SessionName": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelsessionattributeclass207CType7.sessionName-461",
        "Lsptunnelrasessionattributeclass207CType1Excludeany": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.excludeany-462",
        "Lsptunnelrasessionattributeclass207CType1Includeany": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.includeany-463",
        "Lsptunnelrasessionattributeclass207CType1Includeall": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.includeall-464",
        "Lsptunnelrasessionattributeclass207CType1SetupPrio": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.setupPrio-465",
        "Lsptunnelrasessionattributeclass207CType1HoldingPrio": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.holdingPrio-466",
        "Lsptunnelrasessionattributeclass207CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.flags-467",
        "Lsptunnelrasessionattributeclass207CType1NameLength": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.nameLength-468",
        "Lsptunnelrasessionattributeclass207CType1SessionName": "rsvp.rsvpMessege.objects.object.objectBody.lsptunnelrasessionattributeclass207CType1.sessionName-469",
        "Atmserviceclassclass227CType1Reserved": "rsvp.rsvpMessege.objects.object.objectBody.atmserviceclassclass227CType1.reserved-470",
        "Atmserviceclassclass227CType1Flags": "rsvp.rsvpMessege.objects.object.objectBody.atmserviceclassclass227CType1.flags-471",
        "CallCapabilityObjectclass228CType2Lengthbytes": "rsvp.rsvpMessege.objects.object.objectBody.callCapabilityObjectclass228CType2.lengthbytes-472",
        "CallCapabilityObjectclass228CType2ClassNum": "rsvp.rsvpMessege.objects.object.objectBody.callCapabilityObjectclass228CType2.classNum-473",
        "CallCapabilityObjectclass228CType2Ctype": "rsvp.rsvpMessege.objects.object.objectBody.callCapabilityObjectclass228CType2.ctype-474",
        "CallCapabilityObjectclass228CType2Resv": "rsvp.rsvpMessege.objects.object.objectBody.callCapabilityObjectclass228CType2.resv-475",
        "CallCapabilityObjectclass228CType2CallOpsFlag": "rsvp.rsvpMessege.objects.object.objectBody.callCapabilityObjectclass228CType2.callOpsFlag-476",
        "Ipv4SourceIDUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4SourceID.uBit-477",
        "Ipv4SourceIDFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4SourceID.fBit-478",
        "Ipv4SourceIDSourceIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4SourceID.sourceIDType-479",
        "Ipv4SourceIDLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4SourceID.length-480",
        "Ipv4SourceIDIpv4Address": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4SourceID.ipv4Address-481",
        "Ipv4SourceIDLogicalPortId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4SourceID.logicalPortId-482",
        "Ipv6SourceIDUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6SourceID.uBit-483",
        "Ipv6SourceIDFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6SourceID.fBit-484",
        "Ipv6SourceIDSourceIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6SourceID.sourceIDType-485",
        "Ipv6SourceIDLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6SourceID.length-486",
        "Ipv6SourceIDIpv6Address": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6SourceID.ipv6Address-487",
        "Ipv6SourceIDLogicalPortId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6SourceID.logicalPortId-488",
        "NsapSourceIDUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapSourceID.uBit-489",
        "NsapSourceIDFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapSourceID.fBit-490",
        "NsapSourceIDSourceIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapSourceID.sourceIDType-491",
        "NsapSourceIDLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapSourceID.length-492",
        "NsapSourceIDDataLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapSourceID.dataLength-493",
        "NsapSourceIDNsap": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapSourceID.nsap-494",
        "NsapSourceIDLogicalPortId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapSourceID.logicalPortId-495",
        "Ipv4DestIDUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4DestID.uBit-496",
        "Ipv4DestIDFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4DestID.fBit-497",
        "Ipv4DestIDDestIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4DestID.destIDType-498",
        "Ipv4DestIDLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4DestID.length-499",
        "Ipv4DestIDIpv4Address": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4DestID.ipv4Address-500",
        "Ipv4DestIDLogicalPortId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv4DestID.logicalPortId-501",
        "Ipv6DestIDUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6DestID.uBit-502",
        "Ipv6DestIDFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6DestID.fBit-503",
        "Ipv6DestIDDestIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6DestID.destIDType-504",
        "Ipv6DestIDLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6DestID.length-505",
        "Ipv6DestIDIpv6Address": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6DestID.ipv6Address-506",
        "Ipv6DestIDLogicalPortId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.ipv6DestID.logicalPortId-507",
        "NsapDestIDUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapDestID.uBit-508",
        "NsapDestIDFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapDestID.fBit-509",
        "NsapDestIDDestIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapDestID.destIDType-510",
        "NsapDestIDLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapDestID.length-511",
        "NsapDestIDDataLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapDestID.dataLength-512",
        "NsapDestIDNsap": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapDestID.nsap-513",
        "NsapDestIDLogicalPortId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.nsapDestID.logicalPortId-514",
        "EgressLabelTLVUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.uBit-515",
        "EgressLabelTLVFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.fBit-516",
        "EgressLabelTLVEgressIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.egressIDType-517",
        "EgressLabelTLVLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.length-518",
        "EgressLabelTLVReserved": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.reserved-519",
        "EgressLabelTLVLbit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.lbit-520",
        "EgressLabelTLVLogicalPortId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.logicalPortId-521",
        "EgressLabelTLVLabelLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.labelLength-522",
        "EgressLabelTLVLabel": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.egressLabelTLV.label-523",
        "LocalConnectionIDUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.localConnectionID.uBit-524",
        "LocalConnectionIDFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.localConnectionID.fBit-525",
        "LocalConnectionIDConnectionIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.localConnectionID.connectionIDType-526",
        "LocalConnectionIDLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.localConnectionID.length-527",
        "LocalConnectionIDReserved": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.localConnectionID.reserved-528",
        "LocalConnectionIDCbit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.localConnectionID.cbit-529",
        "LocalConnectionIDLogicalConnectionId": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.localConnectionID.logicalConnectionId-530",
        "DiversityUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.diversity.uBit-531",
        "DiversityFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.diversity.fBit-532",
        "DiversityDiversityIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.diversity.diversityIDType-533",
        "DiversityLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.diversity.length-534",
        "IteratingListLocalConnectionID": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.diversity.iteratingList.localConnectionID-535",
        "IteratingListReserved": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.diversity.iteratingList.reserved-536",
        "IteratingListDivT": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.diversity.iteratingList.divT-537",
        "ContractIdUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.contractId.uBit-538",
        "ContractIdFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.contractId.fBit-539",
        "ContractIdContractIDType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.contractId.contractIDType-540",
        "ContractIdLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.contractId.length-541",
        "ContractIdContractID": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.contractId.contractID-542",
        "UniServiceLevelUBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.uniServiceLevel.uBit-543",
        "UniServiceLevelFBit": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.uniServiceLevel.fBit-544",
        "UniServiceLevelServiceLevelType": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.uniServiceLevel.serviceLevelType-545",
        "UniServiceLevelLength": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.uniServiceLevel.length-546",
        "UniServiceLevelReserved": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.uniServiceLevel.reserved-547",
        "UniServiceLevelServiceLevel": "rsvp.rsvpMessege.objects.object.objectBody.uniSignalingClass229CType1.subType.uniServiceLevel.serviceLevel-548",
        "CallIdentifierObjectclass230CType1Lengthbytes": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.lengthbytes-549",
        "CallIdentifierObjectclass230CType1ClassNum": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.classNum-550",
        "CallIdentifierObjectclass230CType1Ctype": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.ctype-551",
        "SrcLSRAddressLength4BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength4Bytes.type-552",
        "SrcLSRAddressLength4BytesResv": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength4Bytes.resv-553",
        "SrcLSRAddressLength4BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength4Bytes.srcLSRAddress-554",
        "SrcLSRAddressLength4BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength4Bytes.localId-555",
        "SrcLSRAddressLength16BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength16Bytes.type-556",
        "SrcLSRAddressLength16BytesResv": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength16Bytes.resv-557",
        "SrcLSRAddressLength16BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength16Bytes.srcLSRAddress-558",
        "SrcLSRAddressLength16BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength16Bytes.localId-559",
        "SrcLSRAddressLength20BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength20Bytes.type-560",
        "SrcLSRAddressLength20BytesResv": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength20Bytes.resv-561",
        "SrcLSRAddressLength20BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength20Bytes.srcLSRAddress-562",
        "SrcLSRAddressLength20BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength20Bytes.localId-563",
        "SrcLSRAddressLength6BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength6Bytes.type-564",
        "SrcLSRAddressLength6BytesResv": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength6Bytes.resv-565",
        "SrcLSRAddressLength6BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength6Bytes.srcLSRAddress-566",
        "SrcLSRAddressLength6BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLength6Bytes.localId-567",
        "SrcLSRAddressLengthVendorDefinedType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLengthVendorDefined.type-568",
        "SrcLSRAddressLengthVendorDefinedResv": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLengthVendorDefined.resv-569",
        "SrcLSRAddressAddressLength": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLengthVendorDefined.srcLSRAddress.addressLength-570",
        "SrcLSRAddressAddressValue": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLengthVendorDefined.srcLSRAddress.addressValue-571",
        "SrcLSRAddressLengthVendorDefinedLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType1.callIdentifiers.srcLSRAddressLengthVendorDefined.localId-572",
        "CallIdentifierObjectclass230CType2Lengthbytes": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.lengthbytes-573",
        "CallIdentifierObjectclass230CType2ClassNum": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.classNum-574",
        "CallIdentifierObjectclass230CType2Ctype": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.ctype-575",
        "CallidentifiersSrcLSRAddressLength4BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength4Bytes.type-576",
        "SrcLSRAddressLength4BytesIs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength4Bytes.is-577",
        "SrcLSRAddressLength4BytesNs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength4Bytes.ns-578",
        "CallidentifiersSrcLSRAddressLength4BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength4Bytes.srcLSRAddress-579",
        "CallidentifiersSrcLSRAddressLength4BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength4Bytes.localId-580",
        "CallidentifiersSrcLSRAddressLength16BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength16Bytes.type-581",
        "SrcLSRAddressLength16BytesIs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength16Bytes.is-582",
        "SrcLSRAddressLength16BytesNs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength16Bytes.ns-583",
        "CallidentifiersSrcLSRAddressLength16BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength16Bytes.srcLSRAddress-584",
        "CallidentifiersSrcLSRAddressLength16BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength16Bytes.localId-585",
        "CallidentifiersSrcLSRAddressLength20BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength20Bytes.type-586",
        "SrcLSRAddressLength20BytesIs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength20Bytes.is-587",
        "SrcLSRAddressLength20BytesNs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength20Bytes.ns-588",
        "CallidentifiersSrcLSRAddressLength20BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength20Bytes.srcLSRAddress-589",
        "CallidentifiersSrcLSRAddressLength20BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength20Bytes.localId-590",
        "CallidentifiersSrcLSRAddressLength6BytesType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength6Bytes.type-591",
        "SrcLSRAddressLength6BytesIs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength6Bytes.is-592",
        "SrcLSRAddressLength6BytesNs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength6Bytes.ns-593",
        "CallidentifiersSrcLSRAddressLength6BytesSrcLSRAddress": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength6Bytes.srcLSRAddress-594",
        "CallidentifiersSrcLSRAddressLength6BytesLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLength6Bytes.localId-595",
        "CallidentifiersSrcLSRAddressLengthVendorDefinedType": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLengthVendorDefined.type-596",
        "SrcLSRAddressLengthVendorDefinedIs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLengthVendorDefined.is-597",
        "SrcLSRAddressLengthVendorDefinedNs": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLengthVendorDefined.ns-598",
        "SrclsraddresslengthvendordefinedSrcLSRAddressAddressLength": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLengthVendorDefined.srcLSRAddress.addressLength-599",
        "SrclsraddresslengthvendordefinedSrcLSRAddressAddressValue": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLengthVendorDefined.srcLSRAddress.addressValue-600",
        "CallidentifiersSrcLSRAddressLengthVendorDefinedLocalId": "rsvp.rsvpMessege.objects.object.objectBody.callIdentifierObjectclass230CType2.callIdentifiers.srcLSRAddressLengthVendorDefined.localId-601",
    }

    def __init__(self, parent, list_op=False):
        super(Rsvp, self).__init__(parent, list_op)

    @property
    def RsvpMessegeVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpMessegeVersion"])
        )

    @property
    def RsvpMessegeFlag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: decimal
        Available enum values: Not refresh reduction capable, 0, Refresh reduction capable, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpMessegeFlag"])
        )

    @property
    def RsvpMessegeMessegeType(self):
        """
        Display Name: Messege Type
        Default Value: 1
        Value Format: decimal
        Available enum values: Path, 1, Resv, 2, PathErr, 3, ResvErr, 4, PathTear, 5, ResvTear, 6, ResvConf, 7, DREQ, Diagnostic Request, 8, DREP, Diagnostic Reply, 9, ResvTearConfirm, 10, Bundle, 12, ACK, 13, Srefresh, 15, Hello, 20, Notify Message, 21, Integrity Challenge, 25, Integrity Response, 26, DSBM_willing, 66, I_AM_DSBM, 67
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpMessegeMessegeType"])
        )

    @property
    def RsvpMessegeRsvpChecksum(self):
        """
        Display Name: RSVP checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpMessegeRsvpChecksum"])
        )

    @property
    def RsvpMessegeTtl(self):
        """
        Display Name: TTL
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpMessegeTtl"])
        )

    @property
    def RsvpMessegeReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpMessegeReserved"])
        )

    @property
    def RsvpMessegeRsvpLength(self):
        """
        Display Name: RSVP Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpMessegeRsvpLength"])
        )

    @property
    def BundleMsgOptionalHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BundleMsgOptionalHeaderVersion"]),
        )

    @property
    def BundleMsgOptionalHeaderFlag(self):
        """
        Display Name: Flag
        Default Value: 1
        Value Format: decimal
        Available enum values: Refresh (overhead) reduction capable, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BundleMsgOptionalHeaderFlag"])
        )

    @property
    def BundleMsgOptionalHeaderMessegeType(self):
        """
        Display Name: Messege Type
        Default Value: 12
        Value Format: decimal
        Available enum values: Bundle Message, 12
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["BundleMsgOptionalHeaderMessegeType"]
            ),
        )

    @property
    def BundleMsgOptionalHeaderRsvpChecksum(self):
        """
        Display Name: RSVP checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["BundleMsgOptionalHeaderRsvpChecksum"]
            ),
        )

    @property
    def BundleMsgOptionalHeaderTtl(self):
        """
        Display Name: TTL
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BundleMsgOptionalHeaderTtl"])
        )

    @property
    def BundleMsgOptionalHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BundleMsgOptionalHeaderReserved"]),
        )

    @property
    def BundleMsgOptionalHeaderRsvpLength(self):
        """
        Display Name: RSVP Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BundleMsgOptionalHeaderRsvpLength"]),
        )

    @property
    def ObjectObjectLength(self):
        """
        Display Name: Object Length
        Default Value: 0x0004
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ObjectObjectLength"])
        )

    @property
    def ObjectClass(self):
        """
        Display Name: Class
        Default Value: 0
        Value Format: decimal
        Available enum values: NULL, 0, SESSION, 1, RSVP_HOP, 3, INTEGRITY, 4, TIME_VALUES, 5, ERROR_SPEC, 6, SCOPE, 7, STYLE, 8, FLOWSPEC, 9, FILTER_SPEC, 10, SENDER_TEMPLATE, 11, SENDER_TSPEC, 12, ADSPEC, 13, POLICY_DATA, 14, RESV_CONFIRM, 15, RSVP_LABEL, 16, HOP_COUNT, 17, STRICT_SOURCE_ROUTE, 18, LABEL_REQUEST, 19, EXPLICIT_ROUTE, 20, ROUTE_RECORD, 21, HELLO, 22, MESSAGE_ID, 23, MESSAGE_ID_ACK, 24, MESSAGE_ID_LIST, 25, DIAGNOSTIC, 30, ROUTE, 31, DIAG_RESPONSE, 32, DIAG_SELECT, 33, RECOVERY_LABEL, 34, UPSTREAM_LABEL, 35, LABEL_SET, 36, PROTECTION, 37, DSBM IP ADDRESS, 42, SBM_PRIORITY, 43, DSBM TIMER INTERVALS, 44, SBM_INFO, 45, S2L SUB LSP, 50, DETOUR, 63, CHALLENGE, 64, DIFF-SERV, 65, CLASSTYPE, 66, NODE_CHAR, 128, SUGGESTED_LABEL, 129, ACCEPTABLE_LABEL_SET, 130, RESTART_CAP, 131, RSVP_HOP_L2, 161, LAN_NHOP_L2, 162, LAN_NHOP_L3, 163, LAN_LOOPBACK, 164, TCLASS, 165, TUNNEL, 192, LSP_TUNNEL_INTERFACE_ID, 193, NOTIFY_REQUEST, 195, ADMIN-STATUS, 196, SECONDARY EXPLICIT ROUTE OBJECT, 200, SECONDARY RECORD ROUTE OBJECT, 201, FAST_REROUTE, 205, SESSION_ATTRIBUTE, 207, DCLASS, 225, PACKETCABLE EXTENSIONS, 226, ATM_SERVICECLASS, 227, CALL_OPS (ASON), 228, GENERALIZED_UNI, 229, CALL-ID, 230
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ObjectClass"]))

    @property
    def ObjectType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ObjectType"]))

    @property
    def DataMessegeDataLength(self):
        """
        Display Name: Data Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataMessegeDataLength"])
        )

    @property
    def DataMessegeData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataMessegeData"])
        )

    @property
    def Ipv4UDPSESSIONClass1CType1DestAddress(self):
        """
        Display Name: Dest. Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4UDPSESSIONClass1CType1DestAddress"]
            ),
        )

    @property
    def Ipv4UDPSESSIONClass1CType1ProtocolId(self):
        """
        Display Name: Protocol Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4UDPSESSIONClass1CType1ProtocolId"]
            ),
        )

    @property
    def Ipv4UDPSESSIONClass1CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4UDPSESSIONClass1CType1Flags"]),
        )

    @property
    def Ipv4UDPSESSIONClass1CType1DestPort(self):
        """
        Display Name: Dest. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4UDPSESSIONClass1CType1DestPort"]
            ),
        )

    @property
    def Ipv6UDPSESSIONClass1CType2DestAddress(self):
        """
        Display Name: Dest. Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6UDPSESSIONClass1CType2DestAddress"]
            ),
        )

    @property
    def Ipv6UDPSESSIONClass1CType2ProtocolId(self):
        """
        Display Name: Protocol Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6UDPSESSIONClass1CType2ProtocolId"]
            ),
        )

    @property
    def Ipv6UDPSESSIONClass1CType2Flags(self):
        """
        Display Name: Flags
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6UDPSESSIONClass1CType2Flags"]),
        )

    @property
    def Ipv6UDPSESSIONClass1CType2DestPort(self):
        """
        Display Name: Dest. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6UDPSESSIONClass1CType2DestPort"]
            ),
        )

    @property
    def Ipv4GPISESSIONClass1CType3DestAddress(self):
        """
        Display Name: Dest. Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4GPISESSIONClass1CType3DestAddress"]
            ),
        )

    @property
    def Ipv4GPISESSIONClass1CType3ProtocolId(self):
        """
        Display Name: Protocol Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4GPISESSIONClass1CType3ProtocolId"]
            ),
        )

    @property
    def Ipv4GPISESSIONClass1CType3Flags(self):
        """
        Display Name: Flags
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4GPISESSIONClass1CType3Flags"]),
        )

    @property
    def Ipv4GPISESSIONClass1CType3DestPort(self):
        """
        Display Name: Dest. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4GPISESSIONClass1CType3DestPort"]
            ),
        )

    @property
    def Ipv6GPISESSIONClass1CType4DestAddress(self):
        """
        Display Name: Dest. Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6GPISESSIONClass1CType4DestAddress"]
            ),
        )

    @property
    def Ipv6GPISESSIONClass1CType4ProtocolId(self):
        """
        Display Name: Protocol Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6GPISESSIONClass1CType4ProtocolId"]
            ),
        )

    @property
    def Ipv6GPISESSIONClass1CType4Flags(self):
        """
        Display Name: Flags
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6GPISESSIONClass1CType4Flags"]),
        )

    @property
    def Ipv6GPISESSIONClass1CType4DestPort(self):
        """
        Display Name: Dest. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6GPISESSIONClass1CType4DestPort"]
            ),
        )

    @property
    def Lsptunnelipv4Class1CType7Ipv4TunnelEndPointAddress(self):
        """
        Display Name: IPv4 tunnel end point address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv4Class1CType7Ipv4TunnelEndPointAddress"]
            ),
        )

    @property
    def Lsptunnelipv4Class1CType7Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Lsptunnelipv4Class1CType7Reserved"]),
        )

    @property
    def Lsptunnelipv4Class1CType7TunnelId(self):
        """
        Display Name: Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Lsptunnelipv4Class1CType7TunnelId"]),
        )

    @property
    def Lsptunnelipv4Class1CType7ExtendedTunnelId(self):
        """
        Display Name: Extended Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv4Class1CType7ExtendedTunnelId"]
            ),
        )

    @property
    def Lsptunnelipv6Class1CType8Ipv6TunnelEndPointAddress(self):
        """
        Display Name: IPv6 tunnel end point address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv6Class1CType8Ipv6TunnelEndPointAddress"]
            ),
        )

    @property
    def Lsptunnelipv6Class1CType8Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Lsptunnelipv6Class1CType8Reserved"]),
        )

    @property
    def Lsptunnelipv6Class1CType8TunnelId(self):
        """
        Display Name: Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Lsptunnelipv6Class1CType8TunnelId"]),
        )

    @property
    def Lsptunnelipv6Class1CType8ExtendedTunnelId(self):
        """
        Display Name: Extended Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv6Class1CType8ExtendedTunnelId"]
            ),
        )

    @property
    def Rsvpaggregateip4class1CType9Ipv4SessionAddress(self):
        """
        Display Name: IPv4 session address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Rsvpaggregateip4class1CType9Ipv4SessionAddress"]
            ),
        )

    @property
    def Rsvpaggregateip4class1CType9Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Rsvpaggregateip4class1CType9Reserved"]
            ),
        )

    @property
    def Rsvpaggregateip4class1CType9Flag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Rsvpaggregateip4class1CType9Flag"]),
        )

    @property
    def Rsvpaggregateip4class1CType9Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Rsvpaggregateip4class1CType9Unused"]
            ),
        )

    @property
    def Rsvpaggregateip4class1CType9Dscp(self):
        """
        Display Name: DSCP
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Rsvpaggregateip4class1CType9Dscp"]),
        )

    @property
    def Rsvpaggregateip6class1CType10Ipv6SessionAddress(self):
        """
        Display Name: IPv6 session address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Rsvpaggregateip6class1CType10Ipv6SessionAddress"]
            ),
        )

    @property
    def Rsvpaggregateip6class1CType10Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Rsvpaggregateip6class1CType10Reserved"]
            ),
        )

    @property
    def Rsvpaggregateip6class1CType10Flag(self):
        """
        Display Name: Flag
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Rsvpaggregateip6class1CType10Flag"]),
        )

    @property
    def Rsvpaggregateip6class1CType10Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Rsvpaggregateip6class1CType10Unused"]
            ),
        )

    @property
    def Rsvpaggregateip6class1CType10Dscp(self):
        """
        Display Name: DSCP
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Rsvpaggregateip6class1CType10Dscp"]),
        )

    @property
    def P2mplsptunnelipv4Class1CType13P2mpId(self):
        """
        Display Name: P2MP Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv4Class1CType13P2mpId"]
            ),
        )

    @property
    def P2mplsptunnelipv4Class1CType13Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv4Class1CType13Reserved"]
            ),
        )

    @property
    def P2mplsptunnelipv4Class1CType13TunnelId(self):
        """
        Display Name: Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv4Class1CType13TunnelId"]
            ),
        )

    @property
    def P2mplsptunnelipv4Class1CType13ExtendedTunnelId(self):
        """
        Display Name: Extended Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv4Class1CType13ExtendedTunnelId"]
            ),
        )

    @property
    def P2mplsptunnelipv6Class1CType14P2mpId(self):
        """
        Display Name: P2MP Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv6Class1CType14P2mpId"]
            ),
        )

    @property
    def P2mplsptunnelipv6Class1CType14Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv6Class1CType14Reserved"]
            ),
        )

    @property
    def P2mplsptunnelipv6Class1CType14TunnelId(self):
        """
        Display Name: Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv6Class1CType14TunnelId"]
            ),
        )

    @property
    def P2mplsptunnelipv6Class1CType14ExtendedTunnelId(self):
        """
        Display Name: Extended Tunnel Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv6Class1CType14ExtendedTunnelId"]
            ),
        )

    @property
    def RsvphopClassClass3CType1Ipv4NextPreviousHopAddress(self):
        """
        Display Name: IPv4 Next/Previous Hop Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RsvphopClassClass3CType1Ipv4NextPreviousHopAddress"]
            ),
        )

    @property
    def RsvphopClassClass3CType1LogicalInterfaceHandle(self):
        """
        Display Name: Logical Interface Handle
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RsvphopClassClass3CType1LogicalInterfaceHandle"]
            ),
        )

    @property
    def RsvphopClassClass3CType2Ipv6NextPreviousHopAddress(self):
        """
        Display Name: IPv6 Next/Previous Hop Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RsvphopClassClass3CType2Ipv6NextPreviousHopAddress"]
            ),
        )

    @property
    def RsvphopClassClass3CType2LogicalInterfaceHandle(self):
        """
        Display Name: Logical Interface Handle
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RsvphopClassClass3CType2LogicalInterfaceHandle"]
            ),
        )

    @property
    def Integrityclass4CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Integrityclass4CType1Flags"])
        )

    @property
    def Integrityclass4CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Integrityclass4CType1Reserved"]),
        )

    @property
    def Integrityclass4CType1KeyId(self):
        """
        Display Name: Key Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Integrityclass4CType1KeyId"])
        )

    @property
    def Integrityclass4CType1SequenceNumber(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Integrityclass4CType1SequenceNumber"]
            ),
        )

    @property
    def Integrityclass4CType1MsgLength(self):
        """
        Display Name: Msg Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Integrityclass4CType1MsgLength"]),
        )

    @property
    def Integrityclass4CType1KeyedMessege(self):
        """
        Display Name: Keyed Messege
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Integrityclass4CType1KeyedMessege"]),
        )

    @property
    def TimevaluesClassClass5CType1RefreshPeriodR(self):
        """
        Display Name: Refresh Period R
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TimevaluesClassClass5CType1RefreshPeriodR"]
            ),
        )

    @property
    def Ipv4ERRORSPECClass6CType1Ipv4ErrorNodeAddress(self):
        """
        Display Name: IPv4 Error Node Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4ERRORSPECClass6CType1Ipv4ErrorNodeAddress"]
            ),
        )

    @property
    def Ipv4ERRORSPECClass6CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: InPlace, 1, NotGuilty, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4ERRORSPECClass6CType1Flags"]),
        )

    @property
    def Ipv4ERRORSPECClass6CType1ErrorCode(self):
        """
        Display Name: Error Code
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4ERRORSPECClass6CType1ErrorCode"]
            ),
        )

    @property
    def Ipv4ERRORSPECClass6CType1ErrorValue(self):
        """
        Display Name: Error Value
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4ERRORSPECClass6CType1ErrorValue"]
            ),
        )

    @property
    def Ipv6ERRORSPECClass6CType2Ipv6ErrorNodeAddress(self):
        """
        Display Name: IPv6 Error Node Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6ERRORSPECClass6CType2Ipv6ErrorNodeAddress"]
            ),
        )

    @property
    def Ipv6ERRORSPECClass6CType2Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: InPlace, 1, NotGuilty, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6ERRORSPECClass6CType2Flags"]),
        )

    @property
    def Ipv6ERRORSPECClass6CType2ErrorCode(self):
        """
        Display Name: Error Code
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6ERRORSPECClass6CType2ErrorCode"]
            ),
        )

    @property
    def Ipv6ERRORSPECClass6CType2ErrorValue(self):
        """
        Display Name: Error Value
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6ERRORSPECClass6CType2ErrorValue"]
            ),
        )

    @property
    def Ipv4ScopeClassClass7CType1Ipv4SrcAddress(self):
        """
        Display Name: IPv4 Src Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4ScopeClassClass7CType1Ipv4SrcAddress"]
            ),
        )

    @property
    def Ipv6ScopeClassClass7CType2Ipv6SrcAddress(self):
        """
        Display Name: IPv6 Src Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6ScopeClassClass7CType2Ipv6SrcAddress"]
            ),
        )

    @property
    def StyleClassClass8CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StyleClassClass8CType1Flags"])
        )

    @property
    def StyleClassClass8CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["StyleClassClass8CType1Reserved"]),
        )

    @property
    def StyleClassClass8CType1SharingControl(self):
        """
        Display Name: Sharing Control
        Default Value: 0
        Value Format: decimal
        Available enum values: Reserved, 0, Distinct reservations, 1, Shared reservations, 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StyleClassClass8CType1SharingControl"]
            ),
        )

    @property
    def StyleClassClass8CType1SenderSelectionControl(self):
        """
        Display Name: Sender selection control
        Default Value: 0
        Value Format: decimal
        Available enum values: Reserved, 0, Wildcard, 1, Explicit, 2, Reserved, 3, Reserved, 4, Reserved, 5, Reserved, 6, Reserved, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["StyleClassClass8CType1SenderSelectionControl"]
            ),
        )

    @property
    def SonetsdhClass9CType4SignalType(self):
        """
        Display Name: Signal Type
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass9CType4SignalType"]),
        )

    @property
    def SonetsdhClass9CType4Rcc(self):
        """
        Display Name: RCC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass9CType4Rcc"])
        )

    @property
    def SonetsdhClass9CType4Ncc(self):
        """
        Display Name: NCC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass9CType4Ncc"])
        )

    @property
    def SonetsdhClass9CType4Nvc(self):
        """
        Display Name: NVC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass9CType4Nvc"])
        )

    @property
    def SonetsdhClass9CType4Multiplier(self):
        """
        Display Name: Multiplier
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass9CType4Multiplier"]),
        )

    @property
    def SonetsdhClass9CType4Transparency(self):
        """
        Display Name: Transparency
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass9CType4Transparency"]),
        )

    @property
    def SonetsdhClass9CType4Profile(self):
        """
        Display Name: Profile
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass9CType4Profile"])
        )

    @property
    def G709Class9CType5SignalType(self):
        """
        Display Name: Signal Type
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class9CType5SignalType"])
        )

    @property
    def G709Class9CType5Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class9CType5Reserved"])
        )

    @property
    def G709Class9CType5Nmc(self):
        """
        Display Name: NMC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class9CType5Nmc"])
        )

    @property
    def G709Class9CType5Nvc(self):
        """
        Display Name: NVC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class9CType5Nvc"])
        )

    @property
    def G709Class9CType5Multiplier(self):
        """
        Display Name: Multiplier
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class9CType5Multiplier"])
        )

    @property
    def ObjectbodyG709Class9CType5Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ObjectbodyG709Class9CType5Reserved"]
            ),
        )

    @property
    def Filterspecclass10CType1Ipv4SrcAddress(self):
        """
        Display Name: IPv4 SrcAddress
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Filterspecclass10CType1Ipv4SrcAddress"]
            ),
        )

    @property
    def Filterspecclass10CType1Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Filterspecclass10CType1Unused"]),
        )

    @property
    def Filterspecclass10CType1SrcPort(self):
        """
        Display Name: Src. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Filterspecclass10CType1SrcPort"]),
        )

    @property
    def Filterspecclass10CType2Ipv6SrcAddress(self):
        """
        Display Name: IPv6 SrcAddress
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Filterspecclass10CType2Ipv6SrcAddress"]
            ),
        )

    @property
    def Filterspecclass10CType2Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Filterspecclass10CType2Unused"]),
        )

    @property
    def Filterspecclass10CType2SrcPort(self):
        """
        Display Name: Src. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Filterspecclass10CType2SrcPort"]),
        )

    @property
    def Filterspecclass10CType3Ipv6SrcAddress(self):
        """
        Display Name: IPv6 SrcAddress
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Filterspecclass10CType3Ipv6SrcAddress"]
            ),
        )

    @property
    def Filterspecclass10CType3Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Filterspecclass10CType3Unused"]),
        )

    @property
    def Filterspecclass10CType3FlowLabel(self):
        """
        Display Name: Flow Label
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Filterspecclass10CType3FlowLabel"]),
        )

    @property
    def Ipv4GPIFILTERSPECClass10CType4Ipv4SrcAddress(self):
        """
        Display Name: IPv4 SrcAddress
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4GPIFILTERSPECClass10CType4Ipv4SrcAddress"]
            ),
        )

    @property
    def Ipv4GPIFILTERSPECClass10CType4Gpi(self):
        """
        Display Name: GPI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4GPIFILTERSPECClass10CType4Gpi"]),
        )

    @property
    def Ipv6GPIFILTERSPECClass10CType5Ipv6SrcAddress(self):
        """
        Display Name: IPv6 SrcAddress
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6GPIFILTERSPECClass10CType5Ipv6SrcAddress"]
            ),
        )

    @property
    def Ipv6GPIFILTERSPECClass10CType5Gpi(self):
        """
        Display Name: GPI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6GPIFILTERSPECClass10CType5Gpi"]),
        )

    @property
    def Lsptunnelipv4FILTERSPECClass10CType7Ipv4TunnelSenderAddress(self):
        """
        Display Name: IPv4 Tunnel Sender Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Lsptunnelipv4FILTERSPECClass10CType7Ipv4TunnelSenderAddress"
                ]
            ),
        )

    @property
    def Lsptunnelipv4FILTERSPECClass10CType7Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv4FILTERSPECClass10CType7Unused"]
            ),
        )

    @property
    def Lsptunnelipv4FILTERSPECClass10CType7LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv4FILTERSPECClass10CType7LspID"]
            ),
        )

    @property
    def Lsptunnelipv6FILTERSPECClass10CType8Ipv6TunnelSenderAddress(self):
        """
        Display Name: IPv6 Tunnel Sender Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Lsptunnelipv6FILTERSPECClass10CType8Ipv6TunnelSenderAddress"
                ]
            ),
        )

    @property
    def Lsptunnelipv6FILTERSPECClass10CType8Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv6FILTERSPECClass10CType8Unused"]
            ),
        )

    @property
    def Lsptunnelipv6FILTERSPECClass10CType8LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv6FILTERSPECClass10CType8LspID"]
            ),
        )

    @property
    def P2mpLSPIPv4FILTERSPECClass10CType12Ipv4TunnelSenderAddress(self):
        """
        Display Name: IPv4 Tunnel Sender Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mpLSPIPv4FILTERSPECClass10CType12Ipv4TunnelSenderAddress"
                ]
            ),
        )

    @property
    def P2mpLSPIPv4FILTERSPECClass10CType12Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mpLSPIPv4FILTERSPECClass10CType12Unused"]
            ),
        )

    @property
    def P2mpLSPIPv4FILTERSPECClass10CType12LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mpLSPIPv4FILTERSPECClass10CType12LspID"]
            ),
        )

    @property
    def P2mpLSPIPv4FILTERSPECClass10CType12SubGroupOriginatorID(self):
        """
        Display Name: Sub-Group Originator ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mpLSPIPv4FILTERSPECClass10CType12SubGroupOriginatorID"
                ]
            ),
        )

    @property
    def ObjectbodyP2mpLSPIPv4FILTERSPECClass10CType12Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ObjectbodyP2mpLSPIPv4FILTERSPECClass10CType12Unused"]
            ),
        )

    @property
    def P2mpLSPIPv4FILTERSPECClass10CType12SubGroupID(self):
        """
        Display Name: Sub-Group ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mpLSPIPv4FILTERSPECClass10CType12SubGroupID"]
            ),
        )

    @property
    def P2mpLSPIPv6FILTERSPECClass10CType13Ipv6TunnelSenderAddress(self):
        """
        Display Name: IPv6 Tunnel Sender Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mpLSPIPv6FILTERSPECClass10CType13Ipv6TunnelSenderAddress"
                ]
            ),
        )

    @property
    def P2mpLSPIPv6FILTERSPECClass10CType13Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mpLSPIPv6FILTERSPECClass10CType13Unused"]
            ),
        )

    @property
    def P2mpLSPIPv6FILTERSPECClass10CType13LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mpLSPIPv6FILTERSPECClass10CType13LspID"]
            ),
        )

    @property
    def P2mpLSPIPv6FILTERSPECClass10CType13SubGroupOriginatorID(self):
        """
        Display Name: Sub-Group Originator ID
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mpLSPIPv6FILTERSPECClass10CType13SubGroupOriginatorID"
                ]
            ),
        )

    @property
    def ObjectbodyP2mpLSPIPv6FILTERSPECClass10CType13Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ObjectbodyP2mpLSPIPv6FILTERSPECClass10CType13Unused"]
            ),
        )

    @property
    def P2mpLSPIPv6FILTERSPECClass10CType13SubGroupID(self):
        """
        Display Name: Sub-Group ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mpLSPIPv6FILTERSPECClass10CType13SubGroupID"]
            ),
        )

    @property
    def Ipv4SENDERTEMPLATEClass11CType1Ipv4SrcAddress(self):
        """
        Display Name: IPv4 SrcAddress
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4SENDERTEMPLATEClass11CType1Ipv4SrcAddress"]
            ),
        )

    @property
    def Ipv4SENDERTEMPLATEClass11CType1Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4SENDERTEMPLATEClass11CType1Unused"]
            ),
        )

    @property
    def Ipv4SENDERTEMPLATEClass11CType1SrcPort(self):
        """
        Display Name: Src. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4SENDERTEMPLATEClass11CType1SrcPort"]
            ),
        )

    @property
    def Ipv6SENDERTEMPLATEClass11CType2Ipv6SrcAddress(self):
        """
        Display Name: IPv6 SrcAddress
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6SENDERTEMPLATEClass11CType2Ipv6SrcAddress"]
            ),
        )

    @property
    def Ipv6SENDERTEMPLATEClass11CType2Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6SENDERTEMPLATEClass11CType2Unused"]
            ),
        )

    @property
    def Ipv6SENDERTEMPLATEClass11CType2SrcPort(self):
        """
        Display Name: Src. Port
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6SENDERTEMPLATEClass11CType2SrcPort"]
            ),
        )

    @property
    def Ipv4FlowlabelSENDERTEMPLATEClass11CType3Ipv6SrcAddress(self):
        """
        Display Name: IPv6 SrcAddress
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Ipv4FlowlabelSENDERTEMPLATEClass11CType3Ipv6SrcAddress"
                ]
            ),
        )

    @property
    def Ipv4FlowlabelSENDERTEMPLATEClass11CType3Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4FlowlabelSENDERTEMPLATEClass11CType3Unused"]
            ),
        )

    @property
    def Ipv4FlowlabelSENDERTEMPLATEClass11CType3FlowLabel(self):
        """
        Display Name: Flow Label
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4FlowlabelSENDERTEMPLATEClass11CType3FlowLabel"]
            ),
        )

    @property
    def Ipv4GPISENDERTEMPLATEClass11CType4Ipv4SrcAddress(self):
        """
        Display Name: IPv4 SrcAddress
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4GPISENDERTEMPLATEClass11CType4Ipv4SrcAddress"]
            ),
        )

    @property
    def Ipv4GPISENDERTEMPLATEClass11CType4Gpi(self):
        """
        Display Name: GPI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4GPISENDERTEMPLATEClass11CType4Gpi"]
            ),
        )

    @property
    def Ipv6GPISENDERTEMPLATEClass11CType5Ipv6SrcAddress(self):
        """
        Display Name: IPv6 SrcAddress
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6GPISENDERTEMPLATEClass11CType5Ipv6SrcAddress"]
            ),
        )

    @property
    def Ipv6GPISENDERTEMPLATEClass11CType5Gpi(self):
        """
        Display Name: GPI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6GPISENDERTEMPLATEClass11CType5Gpi"]
            ),
        )

    @property
    def Lsptunnelipv4SENDERTEMPLATEClass11CType7Ipv4TunnelSenderAddress(self):
        """
        Display Name: IPv4 Tunnel Sender Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Lsptunnelipv4SENDERTEMPLATEClass11CType7Ipv4TunnelSenderAddress"
                ]
            ),
        )

    @property
    def Lsptunnelipv4SENDERTEMPLATEClass11CType7Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv4SENDERTEMPLATEClass11CType7Unused"]
            ),
        )

    @property
    def Lsptunnelipv4SENDERTEMPLATEClass11CType7LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv4SENDERTEMPLATEClass11CType7LspID"]
            ),
        )

    @property
    def Lsptunnelipv6SENDERTEMPLATEClass11CType8Ipv6TunnelSenderAddress(self):
        """
        Display Name: IPv6 Tunnel Sender Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Lsptunnelipv6SENDERTEMPLATEClass11CType8Ipv6TunnelSenderAddress"
                ]
            ),
        )

    @property
    def Lsptunnelipv6SENDERTEMPLATEClass11CType8Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv6SENDERTEMPLATEClass11CType8Unused"]
            ),
        )

    @property
    def Lsptunnelipv6SENDERTEMPLATEClass11CType8LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelipv6SENDERTEMPLATEClass11CType8LspID"]
            ),
        )

    @property
    def P2mplsptunnelipv4SENDERTEMPLATEClass11CType12Ipv4TunnelSenderAddress(self):
        """
        Display Name: IPv4 Tunnel Sender Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12Ipv4TunnelSenderAddress"
                ]
            ),
        )

    @property
    def P2mplsptunnelipv4SENDERTEMPLATEClass11CType12Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv4SENDERTEMPLATEClass11CType12Unused"]
            ),
        )

    @property
    def P2mplsptunnelipv4SENDERTEMPLATEClass11CType12LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv4SENDERTEMPLATEClass11CType12LspID"]
            ),
        )

    @property
    def P2mplsptunnelipv4SENDERTEMPLATEClass11CType12SubGroupOriginatorID(self):
        """
        Display Name: Sub-Group Originator ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12SubGroupOriginatorID"
                ]
            ),
        )

    @property
    def ObjectbodyP2mplsptunnelipv4SENDERTEMPLATEClass11CType12Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ObjectbodyP2mplsptunnelipv4SENDERTEMPLATEClass11CType12Unused"
                ]
            ),
        )

    @property
    def P2mplsptunnelipv4SENDERTEMPLATEClass11CType12SubGroupID(self):
        """
        Display Name: Sub-Group ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mplsptunnelipv4SENDERTEMPLATEClass11CType12SubGroupID"
                ]
            ),
        )

    @property
    def P2mplsptunnelipv6SENDERTEMPLATEClass11CType13Ipv6TunnelSenderAddress(self):
        """
        Display Name: IPv6 Tunnel Sender Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13Ipv6TunnelSenderAddress"
                ]
            ),
        )

    @property
    def P2mplsptunnelipv6SENDERTEMPLATEClass11CType13Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv6SENDERTEMPLATEClass11CType13Unused"]
            ),
        )

    @property
    def P2mplsptunnelipv6SENDERTEMPLATEClass11CType13LspID(self):
        """
        Display Name: LSP ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["P2mplsptunnelipv6SENDERTEMPLATEClass11CType13LspID"]
            ),
        )

    @property
    def P2mplsptunnelipv6SENDERTEMPLATEClass11CType13SubGroupOriginatorID(self):
        """
        Display Name: Sub-Group Originator ID
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13SubGroupOriginatorID"
                ]
            ),
        )

    @property
    def ObjectbodyP2mplsptunnelipv6SENDERTEMPLATEClass11CType13Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ObjectbodyP2mplsptunnelipv6SENDERTEMPLATEClass11CType13Unused"
                ]
            ),
        )

    @property
    def P2mplsptunnelipv6SENDERTEMPLATEClass11CType13SubGroupID(self):
        """
        Display Name: Sub-Group ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "P2mplsptunnelipv6SENDERTEMPLATEClass11CType13SubGroupID"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2VersionNumber(self):
        """
        Display Name: Version Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2VersionNumber"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2Reserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntservSENDERTSPECTEMPLATEClass12CType2Reserved1"]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2OverallLength(self):
        """
        Display Name: Overall Length
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2OverallLength"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2ServiceHeader(self):
        """
        Display Name: Service Header
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2ServiceHeader"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2ZeroBit(self):
        """
        Display Name: Zero Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntservSENDERTSPECTEMPLATEClass12CType2ZeroBit"]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2Reserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntservSENDERTSPECTEMPLATEClass12CType2Reserved2"]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2LengthOfService1Data(self):
        """
        Display Name: Length of service 1 data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2LengthOfService1Data"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2ParameterIDTokenBucketTSpec(self):
        """
        Display Name: Parameter ID (Token_Bucket_TSpec)
        Default Value: 0x7F
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2ParameterIDTokenBucketTSpec"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2Parameter127Flag(self):
        """
        Display Name: Parameter 127 Flag
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2Parameter127Flag"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2Parameter127Length(self):
        """
        Display Name: Parameter 127 length
        Default Value: 0x05
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2Parameter127Length"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2TokenBucketRate(self):
        """
        Display Name: Token Bucket Rate
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2TokenBucketRate"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2TokenBucketSize(self):
        """
        Display Name: Token Bucket Size
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2TokenBucketSize"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2PeakDataRate(self):
        """
        Display Name: Peak Data Rate
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntservSENDERTSPECTEMPLATEClass12CType2PeakDataRate"]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2MinimumPolicedUnit(self):
        """
        Display Name: Minimum Policed Unit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2MinimumPolicedUnit"
                ]
            ),
        )

    @property
    def IntservSENDERTSPECTEMPLATEClass12CType2MaximumPacketSize(self):
        """
        Display Name: Maximum Packet Size
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservSENDERTSPECTEMPLATEClass12CType2MaximumPacketSize"
                ]
            ),
        )

    @property
    def SonetsdhClass12CType4SignalType(self):
        """
        Display Name: Signal Type
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass12CType4SignalType"]),
        )

    @property
    def SonetsdhClass12CType4Rcc(self):
        """
        Display Name: RCC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass12CType4Rcc"])
        )

    @property
    def SonetsdhClass12CType4Ncc(self):
        """
        Display Name: NCC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass12CType4Ncc"])
        )

    @property
    def SonetsdhClass12CType4Nvc(self):
        """
        Display Name: NVC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass12CType4Nvc"])
        )

    @property
    def SonetsdhClass12CType4Multiplier(self):
        """
        Display Name: Multiplier
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass12CType4Multiplier"]),
        )

    @property
    def SonetsdhClass12CType4Transparency(self):
        """
        Display Name: Transparency
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass12CType4Transparency"]),
        )

    @property
    def SonetsdhClass12CType4Profile(self):
        """
        Display Name: Profile
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SonetsdhClass12CType4Profile"])
        )

    @property
    def G709Class12CType5SignalType(self):
        """
        Display Name: Signal Type
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class12CType5SignalType"])
        )

    @property
    def G709Class12CType5Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class12CType5Reserved"])
        )

    @property
    def G709Class12CType5Nmc(self):
        """
        Display Name: NMC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class12CType5Nmc"])
        )

    @property
    def G709Class12CType5Nvc(self):
        """
        Display Name: NVC
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class12CType5Nvc"])
        )

    @property
    def G709Class12CType5Multiplier(self):
        """
        Display Name: Multiplier
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["G709Class12CType5Multiplier"])
        )

    @property
    def ObjectbodyG709Class12CType5Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ObjectbodyG709Class12CType5Reserved"]
            ),
        )

    @property
    def IntservADSPECTEMPLATEClass13CType2MessageFormatVersionNumber(self):
        """
        Display Name: Message format version number
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntservADSPECTEMPLATEClass13CType2MessageFormatVersionNumber"
                ]
            ),
        )

    @property
    def IntservADSPECTEMPLATEClass13CType2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntservADSPECTEMPLATEClass13CType2Reserved"]
            ),
        )

    @property
    def IntservADSPECTEMPLATEClass13CType2MsgLength(self):
        """
        Display Name: Msg length
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntservADSPECTEMPLATEClass13CType2MsgLength"]
            ),
        )

    @property
    def GeneralParametersFragmentService1PerServiceHeaderServiceNumber1(self):
        """
        Display Name: Per-Service header, service number1
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "GeneralParametersFragmentService1PerServiceHeaderServiceNumber1"
                ]
            ),
        )

    @property
    def GeneralParametersFragmentService1X(self):
        """
        Display Name: x
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1X"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Reserved3(self):
        """
        Display Name: Reserved3
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Reserved3"]
            ),
        )

    @property
    def GeneralParametersFragmentService1GlobalBreakBit(self):
        """
        Display Name: Global Break bit
        Default Value: 0x08
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1GlobalBreakBit"]
            ),
        )

    @property
    def GeneralParametersFragmentService1ParameterID4(self):
        """
        Display Name: Parameter ID(4)
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1ParameterID4"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter4FlagByte(self):
        """
        Display Name: Parameter 4 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Parameter4FlagByte"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter4Length(self):
        """
        Display Name: Parameter 4 length
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Parameter4Length"]
            ),
        )

    @property
    def GeneralParametersFragmentService1IsHopCnt(self):
        """
        Display Name: IS hop cnt
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1IsHopCnt"]
            ),
        )

    @property
    def GeneralParametersFragmentService1ParameterID6(self):
        """
        Display Name: Parameter ID(6)
        Default Value: 0x06
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1ParameterID6"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter6FlagByte(self):
        """
        Display Name: Parameter 6 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Parameter6FlagByte"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter6Length(self):
        """
        Display Name: Parameter 6 length
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Parameter6Length"]
            ),
        )

    @property
    def GeneralParametersFragmentService1PathBwEstimate(self):
        """
        Display Name: Path b/w estimate
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1PathBwEstimate"]
            ),
        )

    @property
    def GeneralParametersFragmentService1ParameterID8(self):
        """
        Display Name: Parameter ID (8)
        Default Value: 0x08
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1ParameterID8"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter8FlagByte(self):
        """
        Display Name: Parameter 8 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Parameter8FlagByte"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter8Length(self):
        """
        Display Name: Parameter 8 length
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Parameter8Length"]
            ),
        )

    @property
    def GeneralParametersFragmentService1MinimumPathLatency(self):
        """
        Display Name: Minimum path latency
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1MinimumPathLatency"]
            ),
        )

    @property
    def GeneralParametersFragmentService1ParameterID10(self):
        """
        Display Name: Parameter ID (10)
        Default Value: 0x10
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1ParameterID10"]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter10FlagByte(self):
        """
        Display Name: Parameter 10 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "GeneralParametersFragmentService1Parameter10FlagByte"
                ]
            ),
        )

    @property
    def GeneralParametersFragmentService1Parameter10Length(self):
        """
        Display Name: Parameter 10 length
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1Parameter10Length"]
            ),
        )

    @property
    def GeneralParametersFragmentService1ComposedMTU(self):
        """
        Display Name: Composed MTU
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GeneralParametersFragmentService1ComposedMTU"]
            ),
        )

    @property
    def GuaranteedServiceFragmentService2PerServiceHeaderServiceNumber2(self):
        """
        Display Name: Per-Service header, service number 2
        Default Value: 0x08
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "GuaranteedServiceFragmentService2PerServiceHeaderServiceNumber2"
                ]
            ),
        )

    @property
    def GuaranteedServiceFragmentService2XBit(self):
        """
        Display Name: x Bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GuaranteedServiceFragmentService2XBit"]
            ),
        )

    @property
    def GuaranteedServiceFragmentService2Reserved(self):
        """
        Display Name: reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["GuaranteedServiceFragmentService2Reserved"]
            ),
        )

    @property
    def GuaranteedServiceFragmentService2BreakBitAndLengthOfPerserviceData(self):
        """
        Display Name: Break bit and Length of per-service data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "GuaranteedServiceFragmentService2BreakBitAndLengthOfPerserviceData"
                ]
            ),
        )

    @property
    def OptionalFieldsParameterIDParameter133ComposedCtot(self):
        """
        Display Name: Parameter ID, parameter 133 (Composed Ctot)
        Default Value: 0x85
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameterIDParameter133ComposedCtot"]
            ),
        )

    @property
    def OptionalFieldsParameter133FlagByte(self):
        """
        Display Name: Parameter 133 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameter133FlagByte"]
            ),
        )

    @property
    def OptionalFieldsParameter133Length(self):
        """
        Display Name: Parameter 133 length
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OptionalFieldsParameter133Length"]),
        )

    @property
    def OptionalFieldsEndtoendComposedValueForCCtot(self):
        """
        Display Name: End-to-end composed value for C [Ctot]
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsEndtoendComposedValueForCCtot"]
            ),
        )

    @property
    def OptionalFieldsParameterIDParameter134ComposedDtot(self):
        """
        Display Name: Parameter ID, parameter 134 (Composed Dtot)
        Default Value: 0x86
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameterIDParameter134ComposedDtot"]
            ),
        )

    @property
    def OptionalFieldsParameter134FlagByte(self):
        """
        Display Name: Parameter 134 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameter134FlagByte"]
            ),
        )

    @property
    def OptionalFieldsParameter134Length(self):
        """
        Display Name: Parameter 134 length
        Default Value: 1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OptionalFieldsParameter134Length"]),
        )

    @property
    def OptionalFieldsEndtoendComposedValueForDDtot(self):
        """
        Display Name: End-to-end composed value for D [Dtot]
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsEndtoendComposedValueForDDtot"]
            ),
        )

    @property
    def OptionalFieldsParameterIDParameter135ComposedCsum(self):
        """
        Display Name: Parameter ID, parameter 135 (Composed Csum)
        Default Value: 0x87
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameterIDParameter135ComposedCsum"]
            ),
        )

    @property
    def OptionalFieldsParameter135FlagByte(self):
        """
        Display Name: Parameter 135 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameter135FlagByte"]
            ),
        )

    @property
    def OptionalFieldsParameter135Length(self):
        """
        Display Name: Parameter 135 length
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OptionalFieldsParameter135Length"]),
        )

    @property
    def OptionalFieldsSincelastreshapingPointComposedCCsum(self):
        """
        Display Name: Since-last-reshaping point composed C [Csum]
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsSincelastreshapingPointComposedCCsum"]
            ),
        )

    @property
    def OptionalFieldsParameterIDParameter136ComposedDsum(self):
        """
        Display Name: Parameter ID, parameter 136 (Composed Dsum)
        Default Value: 0x88
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameterIDParameter136ComposedDsum"]
            ),
        )

    @property
    def OptionalFieldsParameter136FlagByte(self):
        """
        Display Name: Parameter 136 flag byte
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsParameter136FlagByte"]
            ),
        )

    @property
    def OptionalFieldsParameter136Length(self):
        """
        Display Name: Parameter 136 length
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["OptionalFieldsParameter136Length"]),
        )

    @property
    def OptionalFieldsSincelastreshapingPointComposedDDsum(self):
        """
        Display Name: Since-last-reshaping point composed D [Dsum]
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["OptionalFieldsSincelastreshapingPointComposedDDsum"]
            ),
        )

    @property
    def ServicespecificGeneralParameterHeadersvaluesServicespecificGeneralParameterHeadervalue(
        self,
    ):
        """
        Display Name: Service-specific general parameter header/value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ServicespecificGeneralParameterHeadersvaluesServicespecificGeneralParameterHeadervalue"
                ]
            ),
        )

    @property
    def ControlledLoadServiceDataFragmentPerServiceHeaderServiceNumber5(self):
        """
        Display Name: Per-Service header, service number 5
        Default Value: 5
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControlledLoadServiceDataFragmentPerServiceHeaderServiceNumber5"
                ]
            ),
        )

    @property
    def ControlledLoadServiceDataFragmentXBit(self):
        """
        Display Name: x Bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControlledLoadServiceDataFragmentXBit"]
            ),
        )

    @property
    def ControlledLoadServiceDataFragmentBreakBit(self):
        """
        Display Name: Break bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ControlledLoadServiceDataFragmentBreakBit"]
            ),
        )

    @property
    def ControlledLoadServiceDataFragmentLengthOfPerserviceData(self):
        """
        Display Name: Length of per-service data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ControlledLoadServiceDataFragmentLengthOfPerserviceData"
                ]
            ),
        )

    @property
    def ServicespecificGeneralParameterHeadersServicespecificGeneralParameterHeader(
        self,
    ):
        """
        Display Name: Service-specific general parameter header
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ServicespecificGeneralParameterHeadersServicespecificGeneralParameterHeader"
                ]
            ),
        )

    @property
    def PolicydataObjectClass14CType1Length(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1Length"]
            ),
        )

    @property
    def PolicydataObjectClass14CType1Policydata(self):
        """
        Display Name: POLICY_DATA
        Default Value: 8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1Policydata"]
            ),
        )

    @property
    def PolicydataObjectClass14CType1Unused(self):
        """
        Display Name: Unused
        Default Value: 0x1
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1Unused"]
            ),
        )

    @property
    def PolicydataObjectClass14CType1DataOffset(self):
        """
        Display Name: Data Offset
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1DataOffset"]
            ),
        )

    @property
    def ObjectbodyPolicydataObjectClass14CType1Unused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ObjectbodyPolicydataObjectClass14CType1Unused"]
            ),
        )

    @property
    def PolicydataObjectClass14CType1OptionDataLength(self):
        """
        Display Name: Option Data Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1OptionDataLength"]
            ),
        )

    @property
    def PolicydataObjectClass14CType1OptionData(self):
        """
        Display Name: Option Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1OptionData"]
            ),
        )

    @property
    def PolicydataObjectClass14CType1PolicyDataLength(self):
        """
        Display Name: Policy Data Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1PolicyDataLength"]
            ),
        )

    @property
    def PolicydataObjectClass14CType1PolicyData(self):
        """
        Display Name: Policy Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["PolicydataObjectClass14CType1PolicyData"]
            ),
        )

    @property
    def Ipv4RESVCONFIRMClass15CType1Ipv4ReceiverAddress(self):
        """
        Display Name: IPv4 Receiver Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4RESVCONFIRMClass15CType1Ipv4ReceiverAddress"]
            ),
        )

    @property
    def Ipv6RESVCONFIRMClass15CType2Ipv6ReceiverAddress(self):
        """
        Display Name: IPv6 Receiver Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6RESVCONFIRMClass15CType2Ipv6ReceiverAddress"]
            ),
        )

    @property
    def LabelObjectClass16CType1TopLabel(self):
        """
        Display Name: Top Label
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LabelObjectClass16CType1TopLabel"]),
        )

    @property
    def LabelRequestWithoutLabelRangeClass19CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelRequestWithoutLabelRangeClass19CType1Reserved"]
            ),
        )

    @property
    def LabelRequestWithoutLabelRangeClass19CType1L3pid(self):
        """
        Display Name: L3PID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelRequestWithoutLabelRangeClass19CType1L3pid"]
            ),
        )

    @property
    def LabelObjectWithATMLabelRangeClass19CType2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithATMLabelRangeClass19CType2Reserved"]
            ),
        )

    @property
    def LabelObjectWithATMLabelRangeClass19CType2L3pid(self):
        """
        Display Name: L3PID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithATMLabelRangeClass19CType2L3pid"]
            ),
        )

    @property
    def LabelObjectWithATMLabelRangeClass19CType2MBit(self):
        """
        Display Name: M bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithATMLabelRangeClass19CType2MBit"]
            ),
        )

    @property
    def ObjectbodyLabelObjectWithATMLabelRangeClass19CType2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ObjectbodyLabelObjectWithATMLabelRangeClass19CType2Reserved"
                ]
            ),
        )

    @property
    def LabelObjectWithATMLabelRangeClass19CType2MinimumVPI(self):
        """
        Display Name: Minimum VPI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithATMLabelRangeClass19CType2MinimumVPI"]
            ),
        )

    @property
    def LabelObjectWithATMLabelRangeClass19CType2MinimumVCI(self):
        """
        Display Name: Minimum VCI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithATMLabelRangeClass19CType2MinimumVCI"]
            ),
        )

    @property
    def ObjectObjectbodyLabelObjectWithATMLabelRangeClass19CType2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ObjectObjectbodyLabelObjectWithATMLabelRangeClass19CType2Reserved"
                ]
            ),
        )

    @property
    def LabelObjectWithATMLabelRangeClass19CType2MaximumVPI(self):
        """
        Display Name: Maximum VPI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithATMLabelRangeClass19CType2MaximumVPI"]
            ),
        )

    @property
    def LabelObjectWithATMLabelRangeClass19CType2MaximumVCI(self):
        """
        Display Name: Maximum VCI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithATMLabelRangeClass19CType2MaximumVCI"]
            ),
        )

    @property
    def LabelObjectWithFrameRelayLabelRangeClass19CType3Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "LabelObjectWithFrameRelayLabelRangeClass19CType3Reserved"
                ]
            ),
        )

    @property
    def LabelObjectWithFrameRelayLabelRangeClass19CType3L3pid(self):
        """
        Display Name: L3PID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "LabelObjectWithFrameRelayLabelRangeClass19CType3L3pid"
                ]
            ),
        )

    @property
    def LabelObjectWithFrameRelayLabelRangeClass19CType3Res(self):
        """
        Display Name: Res
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithFrameRelayLabelRangeClass19CType3Res"]
            ),
        )

    @property
    def LabelObjectWithFrameRelayLabelRangeClass19CType3Dli(self):
        """
        Display Name: DLI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LabelObjectWithFrameRelayLabelRangeClass19CType3Dli"]
            ),
        )

    @property
    def LabelObjectWithFrameRelayLabelRangeClass19CType3MinimumDLCI(self):
        """
        Display Name: Minimum DLCI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "LabelObjectWithFrameRelayLabelRangeClass19CType3MinimumDLCI"
                ]
            ),
        )

    @property
    def ObjectbodyLabelObjectWithFrameRelayLabelRangeClass19CType3Res(self):
        """
        Display Name: Res
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ObjectbodyLabelObjectWithFrameRelayLabelRangeClass19CType3Res"
                ]
            ),
        )

    @property
    def LabelObjectWithFrameRelayLabelRangeClass19CType3MaximumDLCI(self):
        """
        Display Name: Maximum DLCI
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "LabelObjectWithFrameRelayLabelRangeClass19CType3MaximumDLCI"
                ]
            ),
        )

    @property
    def Ctype1LBit(self):
        """
        Display Name: L bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype1LBit"]))

    @property
    def Ctype1Type(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype1Type"]))

    @property
    def Ctype1Length(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype1Length"]))

    @property
    def Ctype1Ipv4Address(self):
        """
        Display Name: IPv4 Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ctype1Ipv4Address"])
        )

    @property
    def Ctype1PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ctype1PrefixLength"])
        )

    @property
    def Ctype1Padding(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype1Padding"]))

    @property
    def Ctype2LBit(self):
        """
        Display Name: L bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype2LBit"]))

    @property
    def Ctype2Type(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype2Type"]))

    @property
    def Ctype2Length(self):
        """
        Display Name: Length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype2Length"]))

    @property
    def Ctype2Ipv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ctype2Ipv6Address"])
        )

    @property
    def Ctype2PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ctype2PrefixLength"])
        )

    @property
    def Ctype2Padding(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype2Padding"]))

    @property
    def Ctype32LBit(self):
        """
        Display Name: L bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype32LBit"]))

    @property
    def Ctype32Type(self):
        """
        Display Name: Type
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype32Type"]))

    @property
    def Ctype32Length(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype32Length"]))

    @property
    def Ctype32AsNumber(self):
        """
        Display Name: AS Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ctype32AsNumber"])
        )

    @property
    def SubtypeCtype1Type(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype1Type"])
        )

    @property
    def SubtypeCtype1Length(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype1Length"])
        )

    @property
    def SubtypeCtype1Ipv4Address(self):
        """
        Display Name: IPv4 Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype1Ipv4Address"])
        )

    @property
    def SubtypeCtype1PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype1PrefixLength"])
        )

    @property
    def Ctype1Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: Local protection available, 1, Local protection in use, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype1Flags"]))

    @property
    def SubtypeCtype2Type(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype2Type"])
        )

    @property
    def SubtypeCtype2Length(self):
        """
        Display Name: Length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype2Length"])
        )

    @property
    def SubtypeCtype2Ipv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype2Ipv6Address"])
        )

    @property
    def SubtypeCtype2PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype2PrefixLength"])
        )

    @property
    def Ctype2Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: Local protection available, 1, Local protection in use, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype2Flags"]))

    @property
    def Ctype3Type(self):
        """
        Display Name: Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype3Type"]))

    @property
    def Ctype3Length(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype3Length"]))

    @property
    def Ctype3Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype3Flags"]))

    @property
    def Ctype3Ctype(self):
        """
        Display Name: C-Type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ctype3Ctype"]))

    @property
    def Ctype3ContentsOfLabelObject(self):
        """
        Display Name: Contents of Label Object
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ctype3ContentsOfLabelObject"])
        )

    @property
    def HelloREQUESTAckClass22CType12SrcInstance(self):
        """
        Display Name: Src Instance
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HelloREQUESTAckClass22CType12SrcInstance"]
            ),
        )

    @property
    def HelloREQUESTAckClass22CType12DestInstance(self):
        """
        Display Name: Dest Instance
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HelloREQUESTAckClass22CType12DestInstance"]
            ),
        )

    @property
    def Messageidclass23CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Messageidclass23CType1Flags"])
        )

    @property
    def Messageidclass23CType1Epoch(self):
        """
        Display Name: Epoch
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Messageidclass23CType1Epoch"])
        )

    @property
    def Messageidclass23CType1MessageIdentifier(self):
        """
        Display Name: Message_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Messageidclass23CType1MessageIdentifier"]
            ),
        )

    @property
    def MessageidAckNackclass24CType12Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidAckNackclass24CType12Flags"]
            ),
        )

    @property
    def MessageidAckNackclass24CType12Epoch(self):
        """
        Display Name: Epoch
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidAckNackclass24CType12Epoch"]
            ),
        )

    @property
    def MessageidAckNackclass24CType12MessageIdentifier(self):
        """
        Display Name: Message_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidAckNackclass24CType12MessageIdentifier"]
            ),
        )

    @property
    def Messageidlistclass25CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Messageidlistclass25CType1Flags"]),
        )

    @property
    def Messageidlistclass25CType1Epoch(self):
        """
        Display Name: Epoch
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Messageidlistclass25CType1Epoch"]),
        )

    @property
    def MessageidlistMessageIdentifier(self):
        """
        Display Name: Message_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MessageidlistMessageIdentifier"]),
        )

    @property
    def MessageidsourceListIPv4class25CType2Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidsourceListIPv4class25CType2Flags"]
            ),
        )

    @property
    def MessageidsourceListIPv4class25CType2Epoch(self):
        """
        Display Name: Epoch
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidsourceListIPv4class25CType2Epoch"]
            ),
        )

    @property
    def Messageidsourcelistipv4class25ctype2MessageidlistMessageIdentifier(self):
        """
        Display Name: Message_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidsourcelistipv4class25ctype2MessageidlistMessageIdentifier"
                ]
            ),
        )

    @property
    def MessageidlistSourceIPAddress(self):
        """
        Display Name: Source_IP_Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MessageidlistSourceIPAddress"])
        )

    @property
    def MessageidsourceListIPv6class25CType3Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidsourceListIPv6class25CType3Flags"]
            ),
        )

    @property
    def MessageidsourceListIPv6class25CType3Epoch(self):
        """
        Display Name: Epoch
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidsourceListIPv6class25CType3Epoch"]
            ),
        )

    @property
    def Messageidsourcelistipv6class25ctype3MessageidlistMessageIdentifier(self):
        """
        Display Name: Message_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidsourcelistipv6class25ctype3MessageidlistMessageIdentifier"
                ]
            ),
        )

    @property
    def Messageidsourcelistipv6class25ctype3MessageidlistSourceIPAddress(self):
        """
        Display Name: Source_IP_Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidsourcelistipv6class25ctype3MessageidlistSourceIPAddress"
                ]
            ),
        )

    @property
    def MessageidmcastlistIPv4class25CType4Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidmcastlistIPv4class25CType4Flags"]
            ),
        )

    @property
    def MessageidmcastlistIPv4class25CType4Epoch(self):
        """
        Display Name: Epoch
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidmcastlistIPv4class25CType4Epoch"]
            ),
        )

    @property
    def Messageidmcastlistipv4class25ctype4MessageidlistMessageIdentifier(self):
        """
        Display Name: Message_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidmcastlistipv4class25ctype4MessageidlistMessageIdentifier"
                ]
            ),
        )

    @property
    def Messageidmcastlistipv4class25ctype4MessageidlistSourceIPAddress(self):
        """
        Display Name: Source_IP_Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidmcastlistipv4class25ctype4MessageidlistSourceIPAddress"
                ]
            ),
        )

    @property
    def MessageidlistDestinationIPAddress(self):
        """
        Display Name: Destination_IP_Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MessageidlistDestinationIPAddress"]),
        )

    @property
    def MessageidmcastlistIPv6class25CType5Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidmcastlistIPv6class25CType5Flags"]
            ),
        )

    @property
    def MessageidmcastlistIPv6class25CType5Epoch(self):
        """
        Display Name: Epoch
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MessageidmcastlistIPv6class25CType5Epoch"]
            ),
        )

    @property
    def Messageidmcastlistipv6class25ctype5MessageidlistMessageIdentifier(self):
        """
        Display Name: Message_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidmcastlistipv6class25ctype5MessageidlistMessageIdentifier"
                ]
            ),
        )

    @property
    def Messageidmcastlistipv6class25ctype5MessageidlistSourceIPAddress(self):
        """
        Display Name: Source_IP_Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidmcastlistipv6class25ctype5MessageidlistSourceIPAddress"
                ]
            ),
        )

    @property
    def Messageidmcastlistipv6class25ctype5MessageidlistDestinationIPAddress(self):
        """
        Display Name: Destination_IP_Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Messageidmcastlistipv6class25ctype5MessageidlistDestinationIPAddress"
                ]
            ),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1MaxRSVPhops(self):
        """
        Display Name: Max-RSVP-hops
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1MaxRSVPhops"]
            ),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1Rsvphopcount(self):
        """
        Display Name: RSVP-hop-count
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1Rsvphopcount"]
            ),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1Reserved"]
            ),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1MfBit(self):
        """
        Display Name: MF bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1MfBit"]),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1RequestIdentifier(self):
        """
        Display Name: Request_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1RequestIdentifier"]
            ),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1PathMTU(self):
        """
        Display Name: Path MTU
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1PathMTU"]
            ),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1FragmentOffset(self):
        """
        Display Name: Fragment Offset
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1FragmentOffset"]
            ),
        )

    @property
    def Ipv4DIAGNOSTICclass30CType1Lasthopaddress(self):
        """
        Display Name: LAST_HOP_Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv4DIAGNOSTICclass30CType1Lasthopaddress"]
            ),
        )

    @property
    def SenderTemplateObjectIpv4SrcAddress(self):
        """
        Display Name: IPv4 Src address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SenderTemplateObjectIpv4SrcAddress"]
            ),
        )

    @property
    def SenderTemplateObjectGeneralizedPortIdentifier(self):
        """
        Display Name: Generalized Port Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SenderTemplateObjectGeneralizedPortIdentifier"]
            ),
        )

    @property
    def FilterSpecTemplateObjectIpv4SrcAddress(self):
        """
        Display Name: IPv4 Src Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FilterSpecTemplateObjectIpv4SrcAddress"]
            ),
        )

    @property
    def FilterSpecTemplateObjectGeneralizedPortIdentifier(self):
        """
        Display Name: Generalized Port Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FilterSpecTemplateObjectGeneralizedPortIdentifier"]
            ),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2MaxRSVPhops(self):
        """
        Display Name: Max-RSVP-hops
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2MaxRSVPhops"]
            ),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2Rsvphopcount(self):
        """
        Display Name: RSVP-hop-count
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2Rsvphopcount"]
            ),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2Reserved"]
            ),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2MfBit(self):
        """
        Display Name: MF bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2MfBit"]),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2RequestIdentifier(self):
        """
        Display Name: Request_Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2RequestIdentifier"]
            ),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2PathMTU(self):
        """
        Display Name: Path MTU
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2PathMTU"]
            ),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2FragmentOffset(self):
        """
        Display Name: Fragment Offset
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2FragmentOffset"]
            ),
        )

    @property
    def Ipv6DIAGNOSTICclass30CType2Lasthopaddress(self):
        """
        Display Name: LAST_HOP_Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ipv6DIAGNOSTICclass30CType2Lasthopaddress"]
            ),
        )

    @property
    def SenderTemplateObjectIpv6SrcAddress(self):
        """
        Display Name: IPv6 Src address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SenderTemplateObjectIpv6SrcAddress"]
            ),
        )

    @property
    def Ipv6diagnosticclass30ctype2SenderTemplateObjectGeneralizedPortIdentifier(self):
        """
        Display Name: Generalized Port Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Ipv6diagnosticclass30ctype2SenderTemplateObjectGeneralizedPortIdentifier"
                ]
            ),
        )

    @property
    def FilterSpecTemplateObjectIpv6SrcAddress(self):
        """
        Display Name: IPv6 Src Address
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FilterSpecTemplateObjectIpv6SrcAddress"]
            ),
        )

    @property
    def Ipv6diagnosticclass30ctype2FilterSpecTemplateObjectGeneralizedPortIdentifier(
        self,
    ):
        """
        Display Name: Generalized Port Identifier
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Ipv6diagnosticclass30ctype2FilterSpecTemplateObjectGeneralizedPortIdentifier"
                ]
            ),
        )

    @property
    def ClassTypeClass(self):
        """
        Display Name: Class
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClassTypeClass"])
        )

    @property
    def ClassTypeCtype(self):
        """
        Display Name: C-type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClassTypeCtype"])
        )

    @property
    def RouteIPv4Objectclass31CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouteIPv4Objectclass31CType1Reserved"]
            ),
        )

    @property
    def RouteIPv4Objectclass31CType1RPointer(self):
        """
        Display Name: R Pointer
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouteIPv4Objectclass31CType1RPointer"]
            ),
        )

    @property
    def NodeAddressListRsvpNodeAddress(self):
        """
        Display Name: RSVP Node Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["NodeAddressListRsvpNodeAddress"]),
        )

    @property
    def RouteIPv6Objectclass31CType2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouteIPv6Objectclass31CType2Reserved"]
            ),
        )

    @property
    def RouteIPv6Objectclass31CType2RPointer(self):
        """
        Display Name: R Pointer
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouteIPv6Objectclass31CType2RPointer"]
            ),
        )

    @property
    def Routeipv6objectclass31ctype2NodeAddressListRsvpNodeAddress(self):
        """
        Display Name: RSVP Node Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Routeipv6objectclass31ctype2NodeAddressListRsvpNodeAddress"
                ]
            ),
        )

    @property
    def Diagresponseclass32CType1DreqArrivalTime(self):
        """
        Display Name: DREQ Arrival Time
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Diagresponseclass32CType1DreqArrivalTime"]
            ),
        )

    @property
    def Diagresponseclass32CType1IncomingInterfaceAddress(self):
        """
        Display Name: Incoming Interface Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Diagresponseclass32CType1IncomingInterfaceAddress"]
            ),
        )

    @property
    def Diagresponseclass32CType1OutgoingInterfaceAddress(self):
        """
        Display Name: Outgoing Interface Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Diagresponseclass32CType1OutgoingInterfaceAddress"]
            ),
        )

    @property
    def Diagresponseclass32CType1PreviousRSVPHopRouterAddress(self):
        """
        Display Name: Previous-RSVP-Hop Router Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Diagresponseclass32CType1PreviousRSVPHopRouterAddress"
                ]
            ),
        )

    @property
    def Diagresponseclass32CType1Dttl(self):
        """
        Display Name: D-TTL
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Diagresponseclass32CType1Dttl"]),
        )

    @property
    def Diagresponseclass32CType1MBit(self):
        """
        Display Name: M bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Diagresponseclass32CType1MBit"]),
        )

    @property
    def Diagresponseclass32CType1Rerr(self):
        """
        Display Name: R-err
        Default Value: 0
        Value Format: decimal
        Available enum values: no Error, 0, No Path State, 1, packet too big, 2, ROUTE object too big, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Diagresponseclass32CType1Rerr"]),
        )

    @property
    def Diagresponseclass32CType1K(self):
        """
        Display Name: K
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Diagresponseclass32CType1K"])
        )

    @property
    def Diagresponseclass32CType1TimerValue(self):
        """
        Display Name: Timer Value
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Diagresponseclass32CType1TimerValue"]
            ),
        )

    @property
    def DiagresponseIPv6class32CType2DreqArrivalTime(self):
        """
        Display Name: DREQ Arrival Time
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DiagresponseIPv6class32CType2DreqArrivalTime"]
            ),
        )

    @property
    def DiagresponseIPv6class32CType2IncomingInterfaceAddress(self):
        """
        Display Name: Incoming Interface Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "DiagresponseIPv6class32CType2IncomingInterfaceAddress"
                ]
            ),
        )

    @property
    def DiagresponseIPv6class32CType2OutgoingInterfaceAddress(self):
        """
        Display Name: Outgoing Interface Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "DiagresponseIPv6class32CType2OutgoingInterfaceAddress"
                ]
            ),
        )

    @property
    def DiagresponseIPv6class32CType2PreviousRSVPHopRouterAddress(self):
        """
        Display Name: Previous-RSVP-Hop Router Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "DiagresponseIPv6class32CType2PreviousRSVPHopRouterAddress"
                ]
            ),
        )

    @property
    def DiagresponseIPv6class32CType2Dttl(self):
        """
        Display Name: D-TTL
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DiagresponseIPv6class32CType2Dttl"]),
        )

    @property
    def DiagresponseIPv6class32CType2MBit(self):
        """
        Display Name: M bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DiagresponseIPv6class32CType2MBit"]),
        )

    @property
    def DiagresponseIPv6class32CType2Rerr(self):
        """
        Display Name: R-err
        Default Value: 0
        Value Format: decimal
        Available enum values: no Error, 0, No Path State, 1, packet too big, 2, ROUTE object too big, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DiagresponseIPv6class32CType2Rerr"]),
        )

    @property
    def DiagresponseIPv6class32CType2K(self):
        """
        Display Name: K
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DiagresponseIPv6class32CType2K"]),
        )

    @property
    def DiagresponseIPv6class32CType2TimerValue(self):
        """
        Display Name: Timer Value
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DiagresponseIPv6class32CType2TimerValue"]
            ),
        )

    @property
    def S2lsublspipv4Class50CType1Ipv4S2LSubLSPDestinationAddress(self):
        """
        Display Name: IPv4 S2L Sub-LSP destination address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "S2lsublspipv4Class50CType1Ipv4S2LSubLSPDestinationAddress"
                ]
            ),
        )

    @property
    def S2lsublspipv6Class50CType2Ipv6S2LSubLSPDestinationAddress(self):
        """
        Display Name: IPv6 S2L Sub-LSP destination address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "S2lsublspipv6Class50CType2Ipv6S2LSubLSPDestinationAddress"
                ]
            ),
        )

    @property
    def DetourObjectIPv4class63CType7Lengthbytes(self):
        """
        Display Name: Length (bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DetourObjectIPv4class63CType7Lengthbytes"]
            ),
        )

    @property
    def DetourObjectIPv4class63CType7ClassNum(self):
        """
        Display Name: Class-Num
        Default Value: 63
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DetourObjectIPv4class63CType7ClassNum"]
            ),
        )

    @property
    def DetourObjectIPv4class63CType7Ctype(self):
        """
        Display Name: C-Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DetourObjectIPv4class63CType7Ctype"]
            ),
        )

    @property
    def PlrAddressListPlrID(self):
        """
        Display Name: PLR ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PlrAddressListPlrID"])
        )

    @property
    def PlrAddressListAvoidNodeID(self):
        """
        Display Name: Avoid_Node_ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PlrAddressListAvoidNodeID"])
        )

    @property
    def DetourObjectIPv6class63CType8Lengthbytes(self):
        """
        Display Name: Length (bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DetourObjectIPv6class63CType8Lengthbytes"]
            ),
        )

    @property
    def DetourObjectIPv6class63CType8ClassNum(self):
        """
        Display Name: Class-Num
        Default Value: 63
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DetourObjectIPv6class63CType8ClassNum"]
            ),
        )

    @property
    def DetourObjectIPv6class63CType8Ctype(self):
        """
        Display Name: C-Type
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DetourObjectIPv6class63CType8Ctype"]
            ),
        )

    @property
    def Detourobjectipv6class63ctype8PlrAddressListPlrID(self):
        """
        Display Name: PLR ID
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Detourobjectipv6class63ctype8PlrAddressListPlrID"]
            ),
        )

    @property
    def Detourobjectipv6class63ctype8PlrAddressListAvoidNodeID(self):
        """
        Display Name: Avoid_Node_ID
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Detourobjectipv6class63ctype8PlrAddressListAvoidNodeID"
                ]
            ),
        )

    @property
    def ChallengeObjectclass64CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChallengeObjectclass64CType1Reserved"]
            ),
        )

    @property
    def ChallengeObjectclass64CType1KeyId(self):
        """
        Display Name: Key Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ChallengeObjectclass64CType1KeyId"]),
        )

    @property
    def ChallengeObjectclass64CType1ChallengeCookie(self):
        """
        Display Name: Challenge Cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ChallengeObjectclass64CType1ChallengeCookie"]
            ),
        )

    @property
    def DiffservELSPclass65CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DiffservELSPclass65CType1Reserved"]),
        )

    @property
    def DiffservELSPclass65CType1Mapnb(self):
        """
        Display Name: MAPnb
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DiffservELSPclass65CType1Mapnb"]),
        )

    @property
    def MapListReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MapListReserved"])
        )

    @property
    def MapListExp(self):
        """
        Display Name: EXP
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MapListExp"]))

    @property
    def MapListPhbid(self):
        """
        Display Name: PHBID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MapListPhbid"]))

    @property
    def DiffservLLSPclass65CType2Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DiffservLLSPclass65CType2Reserved"]),
        )

    @property
    def DiffservLLSPclass65CType2Psc(self):
        """
        Display Name: PSC
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DiffservLLSPclass65CType2Psc"])
        )

    @property
    def Classtypeclass66CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Classtypeclass66CType1Reserved"]),
        )

    @property
    def Classtypeclass66CType1Ct(self):
        """
        Display Name: CT
        Default Value: 0x001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Classtypeclass66CType1Ct"])
        )

    @property
    def Lsptunnelinterfaceidclass193CType1LsrId(self):
        """
        Display Name: LSR's Router ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelinterfaceidclass193CType1LsrId"]
            ),
        )

    @property
    def Lsptunnelinterfaceidclass193CType1InterfaceID(self):
        """
        Display Name: Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelinterfaceidclass193CType1InterfaceID"]
            ),
        )

    @property
    def SubtypeCtype1LBit(self):
        """
        Display Name: L bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype1LBit"])
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype1Type(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype1Type"
                ]
            ),
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype1Length(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype1Length"
                ]
            ),
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype1Ipv4Address(self):
        """
        Display Name: IPv4 Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype1Ipv4Address"
                ]
            ),
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype1PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype1PrefixLength"
                ]
            ),
        )

    @property
    def SubtypeCtype1Padding(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype1Padding"])
        )

    @property
    def SubtypeCtype2LBit(self):
        """
        Display Name: L bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype2LBit"])
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype2Type(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype2Type"
                ]
            ),
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype2Length(self):
        """
        Display Name: Length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype2Length"
                ]
            ),
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype2Ipv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype2Ipv6Address"
                ]
            ),
        )

    @property
    def Secondaryexplicitrouteclass200ctype2SubtypeCtype2PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryexplicitrouteclass200ctype2SubtypeCtype2PrefixLength"
                ]
            ),
        )

    @property
    def SubtypeCtype2Padding(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype2Padding"])
        )

    @property
    def SubtypeCtype32LBit(self):
        """
        Display Name: L bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype32LBit"])
        )

    @property
    def SubtypeCtype32Type(self):
        """
        Display Name: Type
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype32Type"])
        )

    @property
    def SubtypeCtype32Length(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype32Length"])
        )

    @property
    def SubtypeCtype32AsNumber(self):
        """
        Display Name: AS Number
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype32AsNumber"])
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype1Type(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Secondaryrecordrouteclass201ctype2SubtypeCtype1Type"]
            ),
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype1Length(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryrecordrouteclass201ctype2SubtypeCtype1Length"
                ]
            ),
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype1Ipv4Address(self):
        """
        Display Name: IPv4 Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryrecordrouteclass201ctype2SubtypeCtype1Ipv4Address"
                ]
            ),
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype1PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 32
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryrecordrouteclass201ctype2SubtypeCtype1PrefixLength"
                ]
            ),
        )

    @property
    def SubtypeCtype1Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: Local protection available, 1, Local protection in use, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype1Flags"])
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype2Type(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Secondaryrecordrouteclass201ctype2SubtypeCtype2Type"]
            ),
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype2Length(self):
        """
        Display Name: Length
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryrecordrouteclass201ctype2SubtypeCtype2Length"
                ]
            ),
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype2Ipv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryrecordrouteclass201ctype2SubtypeCtype2Ipv6Address"
                ]
            ),
        )

    @property
    def Secondaryrecordrouteclass201ctype2SubtypeCtype2PrefixLength(self):
        """
        Display Name: Prefix Length
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Secondaryrecordrouteclass201ctype2SubtypeCtype2PrefixLength"
                ]
            ),
        )

    @property
    def SubtypeCtype2Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: Local protection available, 1, Local protection in use, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype2Flags"])
        )

    @property
    def SubtypeCtype3Type(self):
        """
        Display Name: Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype3Type"])
        )

    @property
    def SubtypeCtype3Length(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype3Length"])
        )

    @property
    def SubtypeCtype3Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype3Flags"])
        )

    @property
    def SubtypeCtype3Ctype(self):
        """
        Display Name: C-Type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SubtypeCtype3Ctype"])
        )

    @property
    def SubtypeCtype3ContentsOfLabelObject(self):
        """
        Display Name: Contents of Label Object
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SubtypeCtype3ContentsOfLabelObject"]
            ),
        )

    @property
    def Fastrerouteclass205CType1Lengthbytes(self):
        """
        Display Name: Length (bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType1Lengthbytes"]
            ),
        )

    @property
    def Fastrerouteclass205CType1ClassNum(self):
        """
        Display Name: Class-Num
        Default Value: 205
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType1ClassNum"]),
        )

    @property
    def Fastrerouteclass205CType1Ctype(self):
        """
        Display Name: C-Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType1Ctype"]),
        )

    @property
    def Fastrerouteclass205CType1SetupPrio(self):
        """
        Display Name: Setup Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType1SetupPrio"]
            ),
        )

    @property
    def Fastrerouteclass205CType1HoldingPrio(self):
        """
        Display Name: Holding Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType1HoldingPrio"]
            ),
        )

    @property
    def Fastrerouteclass205CType1Hoplimit(self):
        """
        Display Name: Hop-limit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType1Hoplimit"]),
        )

    @property
    def Fastrerouteclass205CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: One-to-One Backup Desired, 1, Facility Backup Desired, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType1Flags"]),
        )

    @property
    def Fastrerouteclass205CType1Bandwidth(self):
        """
        Display Name: Bandwidth
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType1Bandwidth"]
            ),
        )

    @property
    def Fastrerouteclass205CType1Includeany(self):
        """
        Display Name: Include-any
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType1Includeany"]
            ),
        )

    @property
    def Fastrerouteclass205CType1Excludeany(self):
        """
        Display Name: Exclude-any
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType1Excludeany"]
            ),
        )

    @property
    def Fastrerouteclass205CType1Includeall(self):
        """
        Display Name: Include-all
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType1Includeall"]
            ),
        )

    @property
    def Fastrerouteclass205CType7Lengthbytes(self):
        """
        Display Name: Length (bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType7Lengthbytes"]
            ),
        )

    @property
    def Fastrerouteclass205CType7ClassNum(self):
        """
        Display Name: Class-Num
        Default Value: 205
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType7ClassNum"]),
        )

    @property
    def Fastrerouteclass205CType7Ctype(self):
        """
        Display Name: C-Type
        Default Value: 7
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType7Ctype"]),
        )

    @property
    def Fastrerouteclass205CType7SetupPrio(self):
        """
        Display Name: Setup Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType7SetupPrio"]
            ),
        )

    @property
    def Fastrerouteclass205CType7HoldingPrio(self):
        """
        Display Name: Holding Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType7HoldingPrio"]
            ),
        )

    @property
    def Fastrerouteclass205CType7Hoplimit(self):
        """
        Display Name: Hop-limit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType7Hoplimit"]),
        )

    @property
    def Fastrerouteclass205CType7Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Fastrerouteclass205CType7Reserved"]),
        )

    @property
    def Fastrerouteclass205CType7Bandwidth(self):
        """
        Display Name: Bandwidth
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType7Bandwidth"]
            ),
        )

    @property
    def Fastrerouteclass205CType7Includeany(self):
        """
        Display Name: Include-any
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType7Includeany"]
            ),
        )

    @property
    def Fastrerouteclass205CType7Excludeany(self):
        """
        Display Name: Exclude-any
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Fastrerouteclass205CType7Excludeany"]
            ),
        )

    @property
    def Lsptunnelsessionattributeclass207CType7SetupPrio(self):
        """
        Display Name: Setup Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelsessionattributeclass207CType7SetupPrio"]
            ),
        )

    @property
    def Lsptunnelsessionattributeclass207CType7HoldingPrio(self):
        """
        Display Name: Holding Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelsessionattributeclass207CType7HoldingPrio"]
            ),
        )

    @property
    def Lsptunnelsessionattributeclass207CType7Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: Local protection desired, 1, Local recording desired, 2, SE Style desired, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelsessionattributeclass207CType7Flags"]
            ),
        )

    @property
    def Lsptunnelsessionattributeclass207CType7NameLength(self):
        """
        Display Name: Name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelsessionattributeclass207CType7NameLength"]
            ),
        )

    @property
    def Lsptunnelsessionattributeclass207CType7SessionName(self):
        """
        Display Name: Session Name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelsessionattributeclass207CType7SessionName"]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1Excludeany(self):
        """
        Display Name: Exclude-any
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelrasessionattributeclass207CType1Excludeany"]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1Includeany(self):
        """
        Display Name: Include-any
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelrasessionattributeclass207CType1Includeany"]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1Includeall(self):
        """
        Display Name: Include-all
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelrasessionattributeclass207CType1Includeall"]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1SetupPrio(self):
        """
        Display Name: Setup Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelrasessionattributeclass207CType1SetupPrio"]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1HoldingPrio(self):
        """
        Display Name: Holding Prio
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Lsptunnelrasessionattributeclass207CType1HoldingPrio"
                ]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 1
        Value Format: decimal
        Available enum values: Local protection desired, 1, Local recording desired, 2, SE Style desired, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelrasessionattributeclass207CType1Flags"]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1NameLength(self):
        """
        Display Name: Name Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Lsptunnelrasessionattributeclass207CType1NameLength"]
            ),
        )

    @property
    def Lsptunnelrasessionattributeclass207CType1SessionName(self):
        """
        Display Name: Session Name
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Lsptunnelrasessionattributeclass207CType1SessionName"
                ]
            ),
        )

    @property
    def Atmserviceclassclass227CType1Reserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Atmserviceclassclass227CType1Reserved"]
            ),
        )

    @property
    def Atmserviceclassclass227CType1Flags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        Available enum values: Unspecified Bit Rate, 0, Variable Bit Rate, Non-Real Time, 1, Variable Bit Rate, Real Time, 2, Constant Bit Rate, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Atmserviceclassclass227CType1Flags"]
            ),
        )

    @property
    def CallCapabilityObjectclass228CType2Lengthbytes(self):
        """
        Display Name: Length (bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallCapabilityObjectclass228CType2Lengthbytes"]
            ),
        )

    @property
    def CallCapabilityObjectclass228CType2ClassNum(self):
        """
        Display Name: Class-Num
        Default Value: 228
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallCapabilityObjectclass228CType2ClassNum"]
            ),
        )

    @property
    def CallCapabilityObjectclass228CType2Ctype(self):
        """
        Display Name: C-Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallCapabilityObjectclass228CType2Ctype"]
            ),
        )

    @property
    def CallCapabilityObjectclass228CType2Resv(self):
        """
        Display Name: Resv
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallCapabilityObjectclass228CType2Resv"]
            ),
        )

    @property
    def CallCapabilityObjectclass228CType2CallOpsFlag(self):
        """
        Display Name: Call ops flag
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallCapabilityObjectclass228CType2CallOpsFlag"]
            ),
        )

    @property
    def Ipv4SourceIDUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceIDUBit"])
        )

    @property
    def Ipv4SourceIDFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceIDFBit"])
        )

    @property
    def Ipv4SourceIDSourceIDType(self):
        """
        Display Name: Source ID Type
        Default Value: 0x0960
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceIDSourceIDType"])
        )

    @property
    def Ipv4SourceIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceIDLength"])
        )

    @property
    def Ipv4SourceIDIpv4Address(self):
        """
        Display Name: IPv4 Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceIDIpv4Address"])
        )

    @property
    def Ipv4SourceIDLogicalPortId(self):
        """
        Display Name: Logical PortId
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4SourceIDLogicalPortId"])
        )

    @property
    def Ipv6SourceIDUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceIDUBit"])
        )

    @property
    def Ipv6SourceIDFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceIDFBit"])
        )

    @property
    def Ipv6SourceIDSourceIDType(self):
        """
        Display Name: Source ID Type
        Default Value: 0x0961
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceIDSourceIDType"])
        )

    @property
    def Ipv6SourceIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceIDLength"])
        )

    @property
    def Ipv6SourceIDIpv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceIDIpv6Address"])
        )

    @property
    def Ipv6SourceIDLogicalPortId(self):
        """
        Display Name: Logical PortId
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SourceIDLogicalPortId"])
        )

    @property
    def NsapSourceIDUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapSourceIDUBit"])
        )

    @property
    def NsapSourceIDFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapSourceIDFBit"])
        )

    @property
    def NsapSourceIDSourceIDType(self):
        """
        Display Name: Source ID Type
        Default Value: 0x0962
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapSourceIDSourceIDType"])
        )

    @property
    def NsapSourceIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapSourceIDLength"])
        )

    @property
    def NsapSourceIDDataLength(self):
        """
        Display Name: Data Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapSourceIDDataLength"])
        )

    @property
    def NsapSourceIDNsap(self):
        """
        Display Name: NSAP
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapSourceIDNsap"])
        )

    @property
    def NsapSourceIDLogicalPortId(self):
        """
        Display Name: Logical PortId
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapSourceIDLogicalPortId"])
        )

    @property
    def Ipv4DestIDUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestIDUBit"])
        )

    @property
    def Ipv4DestIDFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestIDFBit"])
        )

    @property
    def Ipv4DestIDDestIDType(self):
        """
        Display Name: Dest ID Type
        Default Value: 0x0963
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestIDDestIDType"])
        )

    @property
    def Ipv4DestIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestIDLength"])
        )

    @property
    def Ipv4DestIDIpv4Address(self):
        """
        Display Name: IPv4 Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestIDIpv4Address"])
        )

    @property
    def Ipv4DestIDLogicalPortId(self):
        """
        Display Name: Logical PortId
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv4DestIDLogicalPortId"])
        )

    @property
    def Ipv6DestIDUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6DestIDUBit"])
        )

    @property
    def Ipv6DestIDFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6DestIDFBit"])
        )

    @property
    def Ipv6DestIDDestIDType(self):
        """
        Display Name: Dest ID Type
        Default Value: 0x0964
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6DestIDDestIDType"])
        )

    @property
    def Ipv6DestIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6DestIDLength"])
        )

    @property
    def Ipv6DestIDIpv6Address(self):
        """
        Display Name: IPv6 Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6DestIDIpv6Address"])
        )

    @property
    def Ipv6DestIDLogicalPortId(self):
        """
        Display Name: Logical PortId
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6DestIDLogicalPortId"])
        )

    @property
    def NsapDestIDUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapDestIDUBit"])
        )

    @property
    def NsapDestIDFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapDestIDFBit"])
        )

    @property
    def NsapDestIDDestIDType(self):
        """
        Display Name: Dest ID Type
        Default Value: 0x0965
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapDestIDDestIDType"])
        )

    @property
    def NsapDestIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapDestIDLength"])
        )

    @property
    def NsapDestIDDataLength(self):
        """
        Display Name: Data Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapDestIDDataLength"])
        )

    @property
    def NsapDestIDNsap(self):
        """
        Display Name: NSAP
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapDestIDNsap"])
        )

    @property
    def NsapDestIDLogicalPortId(self):
        """
        Display Name: Logical PortId
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NsapDestIDLogicalPortId"])
        )

    @property
    def EgressLabelTLVUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVUBit"])
        )

    @property
    def EgressLabelTLVFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVFBit"])
        )

    @property
    def EgressLabelTLVEgressIDType(self):
        """
        Display Name: Egress ID Type
        Default Value: 0x0966
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVEgressIDType"])
        )

    @property
    def EgressLabelTLVLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVLength"])
        )

    @property
    def EgressLabelTLVReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVReserved"])
        )

    @property
    def EgressLabelTLVLbit(self):
        """
        Display Name: L-Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVLbit"])
        )

    @property
    def EgressLabelTLVLogicalPortId(self):
        """
        Display Name: Logical PortId
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVLogicalPortId"])
        )

    @property
    def EgressLabelTLVLabelLength(self):
        """
        Display Name: Label Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVLabelLength"])
        )

    @property
    def EgressLabelTLVLabel(self):
        """
        Display Name: Label
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EgressLabelTLVLabel"])
        )

    @property
    def LocalConnectionIDUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalConnectionIDUBit"])
        )

    @property
    def LocalConnectionIDFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalConnectionIDFBit"])
        )

    @property
    def LocalConnectionIDConnectionIDType(self):
        """
        Display Name: Connection ID Type
        Default Value: 0x0967
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LocalConnectionIDConnectionIDType"]),
        )

    @property
    def LocalConnectionIDLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalConnectionIDLength"])
        )

    @property
    def LocalConnectionIDReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalConnectionIDReserved"])
        )

    @property
    def LocalConnectionIDCbit(self):
        """
        Display Name: C-Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocalConnectionIDCbit"])
        )

    @property
    def LocalConnectionIDLogicalConnectionId(self):
        """
        Display Name: Logical Connection Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LocalConnectionIDLogicalConnectionId"]
            ),
        )

    @property
    def DiversityUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DiversityUBit"]))

    @property
    def DiversityFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DiversityFBit"]))

    @property
    def DiversityDiversityIDType(self):
        """
        Display Name: Diversity ID Type
        Default Value: 0x0968
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DiversityDiversityIDType"])
        )

    @property
    def DiversityLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DiversityLength"])
        )

    @property
    def IteratingListLocalConnectionID(self):
        """
        Display Name: Local Connection ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IteratingListLocalConnectionID"]),
        )

    @property
    def IteratingListReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IteratingListReserved"])
        )

    @property
    def IteratingListDivT(self):
        """
        Display Name: DivT
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IteratingListDivT"])
        )

    @property
    def ContractIdUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ContractIdUBit"])
        )

    @property
    def ContractIdFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ContractIdFBit"])
        )

    @property
    def ContractIdContractIDType(self):
        """
        Display Name: Contract ID Type
        Default Value: 0x0969
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ContractIdContractIDType"])
        )

    @property
    def ContractIdLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ContractIdLength"])
        )

    @property
    def ContractIdContractID(self):
        """
        Display Name: Contract ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ContractIdContractID"])
        )

    @property
    def UniServiceLevelUBit(self):
        """
        Display Name: U Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniServiceLevelUBit"])
        )

    @property
    def UniServiceLevelFBit(self):
        """
        Display Name: F Bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniServiceLevelFBit"])
        )

    @property
    def UniServiceLevelServiceLevelType(self):
        """
        Display Name: Service Level Type
        Default Value: 0x0970
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["UniServiceLevelServiceLevelType"]),
        )

    @property
    def UniServiceLevelLength(self):
        """
        Display Name: Length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniServiceLevelLength"])
        )

    @property
    def UniServiceLevelReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniServiceLevelReserved"])
        )

    @property
    def UniServiceLevelServiceLevel(self):
        """
        Display Name: Service Level
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UniServiceLevelServiceLevel"])
        )

    @property
    def CallIdentifierObjectclass230CType1Lengthbytes(self):
        """
        Display Name: Length (bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallIdentifierObjectclass230CType1Lengthbytes"]
            ),
        )

    @property
    def CallIdentifierObjectclass230CType1ClassNum(self):
        """
        Display Name: Class-Num
        Default Value: 230
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallIdentifierObjectclass230CType1ClassNum"]
            ),
        )

    @property
    def CallIdentifierObjectclass230CType1Ctype(self):
        """
        Display Name: C-Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallIdentifierObjectclass230CType1Ctype"]
            ),
        )

    @property
    def SrcLSRAddressLength4BytesType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength4BytesType"]),
        )

    @property
    def SrcLSRAddressLength4BytesResv(self):
        """
        Display Name: Resv
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength4BytesResv"]),
        )

    @property
    def SrcLSRAddressLength4BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLength4BytesSrcLSRAddress"]
            ),
        )

    @property
    def SrcLSRAddressLength4BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength4BytesLocalId"]),
        )

    @property
    def SrcLSRAddressLength16BytesType(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength16BytesType"]),
        )

    @property
    def SrcLSRAddressLength16BytesResv(self):
        """
        Display Name: Resv
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength16BytesResv"]),
        )

    @property
    def SrcLSRAddressLength16BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLength16BytesSrcLSRAddress"]
            ),
        )

    @property
    def SrcLSRAddressLength16BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength16BytesLocalId"]),
        )

    @property
    def SrcLSRAddressLength20BytesType(self):
        """
        Display Name: Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength20BytesType"]),
        )

    @property
    def SrcLSRAddressLength20BytesResv(self):
        """
        Display Name: Resv
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength20BytesResv"]),
        )

    @property
    def SrcLSRAddressLength20BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLength20BytesSrcLSRAddress"]
            ),
        )

    @property
    def SrcLSRAddressLength20BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength20BytesLocalId"]),
        )

    @property
    def SrcLSRAddressLength6BytesType(self):
        """
        Display Name: Type
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength6BytesType"]),
        )

    @property
    def SrcLSRAddressLength6BytesResv(self):
        """
        Display Name: Resv
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength6BytesResv"]),
        )

    @property
    def SrcLSRAddressLength6BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0:0:0:0:0:0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLength6BytesSrcLSRAddress"]
            ),
        )

    @property
    def SrcLSRAddressLength6BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength6BytesLocalId"]),
        )

    @property
    def SrcLSRAddressLengthVendorDefinedType(self):
        """
        Display Name: Type
        Default Value: 0x7f
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLengthVendorDefinedType"]
            ),
        )

    @property
    def SrcLSRAddressLengthVendorDefinedResv(self):
        """
        Display Name: Resv
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLengthVendorDefinedResv"]
            ),
        )

    @property
    def SrcLSRAddressAddressLength(self):
        """
        Display Name: Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressAddressLength"])
        )

    @property
    def SrcLSRAddressAddressValue(self):
        """
        Display Name: Address Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressAddressValue"])
        )

    @property
    def SrcLSRAddressLengthVendorDefinedLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLengthVendorDefinedLocalId"]
            ),
        )

    @property
    def CallIdentifierObjectclass230CType2Lengthbytes(self):
        """
        Display Name: Length (bytes)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallIdentifierObjectclass230CType2Lengthbytes"]
            ),
        )

    @property
    def CallIdentifierObjectclass230CType2ClassNum(self):
        """
        Display Name: Class-Num
        Default Value: 230
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallIdentifierObjectclass230CType2ClassNum"]
            ),
        )

    @property
    def CallIdentifierObjectclass230CType2Ctype(self):
        """
        Display Name: C-Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallIdentifierObjectclass230CType2Ctype"]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength4BytesType(self):
        """
        Display Name: Type
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength4BytesType"]
            ),
        )

    @property
    def SrcLSRAddressLength4BytesIs(self):
        """
        Display Name: IS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength4BytesIs"])
        )

    @property
    def SrcLSRAddressLength4BytesNs(self):
        """
        Display Name: NS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength4BytesNs"])
        )

    @property
    def CallidentifiersSrcLSRAddressLength4BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CallidentifiersSrcLSRAddressLength4BytesSrcLSRAddress"
                ]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength4BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength4BytesLocalId"]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength16BytesType(self):
        """
        Display Name: Type
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength16BytesType"]
            ),
        )

    @property
    def SrcLSRAddressLength16BytesIs(self):
        """
        Display Name: IS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength16BytesIs"])
        )

    @property
    def SrcLSRAddressLength16BytesNs(self):
        """
        Display Name: NS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength16BytesNs"])
        )

    @property
    def CallidentifiersSrcLSRAddressLength16BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CallidentifiersSrcLSRAddressLength16BytesSrcLSRAddress"
                ]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength16BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength16BytesLocalId"]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength20BytesType(self):
        """
        Display Name: Type
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength20BytesType"]
            ),
        )

    @property
    def SrcLSRAddressLength20BytesIs(self):
        """
        Display Name: IS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength20BytesIs"])
        )

    @property
    def SrcLSRAddressLength20BytesNs(self):
        """
        Display Name: NS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength20BytesNs"])
        )

    @property
    def CallidentifiersSrcLSRAddressLength20BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CallidentifiersSrcLSRAddressLength20BytesSrcLSRAddress"
                ]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength20BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength20BytesLocalId"]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength6BytesType(self):
        """
        Display Name: Type
        Default Value: 0x04
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength6BytesType"]
            ),
        )

    @property
    def SrcLSRAddressLength6BytesIs(self):
        """
        Display Name: IS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength6BytesIs"])
        )

    @property
    def SrcLSRAddressLength6BytesNs(self):
        """
        Display Name: NS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrcLSRAddressLength6BytesNs"])
        )

    @property
    def CallidentifiersSrcLSRAddressLength6BytesSrcLSRAddress(self):
        """
        Display Name: SRC LSR Address
        Default Value: 0:0:0:0:0:0
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CallidentifiersSrcLSRAddressLength6BytesSrcLSRAddress"
                ]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLength6BytesLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLength6BytesLocalId"]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLengthVendorDefinedType(self):
        """
        Display Name: Type
        Default Value: 0x7f
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CallidentifiersSrcLSRAddressLengthVendorDefinedType"]
            ),
        )

    @property
    def SrcLSRAddressLengthVendorDefinedIs(self):
        """
        Display Name: IS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLengthVendorDefinedIs"]
            ),
        )

    @property
    def SrcLSRAddressLengthVendorDefinedNs(self):
        """
        Display Name: NS
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SrcLSRAddressLengthVendorDefinedNs"]
            ),
        )

    @property
    def SrclsraddresslengthvendordefinedSrcLSRAddressAddressLength(self):
        """
        Display Name: Address Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "SrclsraddresslengthvendordefinedSrcLSRAddressAddressLength"
                ]
            ),
        )

    @property
    def SrclsraddresslengthvendordefinedSrcLSRAddressAddressValue(self):
        """
        Display Name: Address Value
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "SrclsraddresslengthvendordefinedSrcLSRAddressAddressValue"
                ]
            ),
        )

    @property
    def CallidentifiersSrcLSRAddressLengthVendorDefinedLocalId(self):
        """
        Display Name: Local Id
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CallidentifiersSrcLSRAddressLengthVendorDefinedLocalId"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
