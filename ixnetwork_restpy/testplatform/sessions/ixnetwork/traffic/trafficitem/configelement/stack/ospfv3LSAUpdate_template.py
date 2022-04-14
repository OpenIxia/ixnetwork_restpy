from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv3LSAUpdate(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv3LSAUpdate"
    _SDM_ATT_MAP = {
        "Ospfv3PacketHeaderOspfVersion": "ospfv3LSAUpdate.header.ospfv3PacketHeader.ospfVersion-1",
        "Ospfv3PacketHeaderPacketType": "ospfv3LSAUpdate.header.ospfv3PacketHeader.packetType-2",
        "Ospfv3PacketHeaderPacketLength": "ospfv3LSAUpdate.header.ospfv3PacketHeader.packetLength-3",
        "Ospfv3PacketHeaderRouterID": "ospfv3LSAUpdate.header.ospfv3PacketHeader.routerID-4",
        "Ospfv3PacketHeaderAreaID": "ospfv3LSAUpdate.header.ospfv3PacketHeader.areaID-5",
        "Ospfv3PacketHeaderOspfPacketChecksum": "ospfv3LSAUpdate.header.ospfv3PacketHeader.ospfPacketChecksum-6",
        "Ospfv3PacketHeaderInstanceID": "ospfv3LSAUpdate.header.ospfv3PacketHeader.instanceID-7",
        "Ospfv3PacketHeaderReserved": "ospfv3LSAUpdate.header.ospfv3PacketHeader.reserved-8",
        "LinkStateUpdateBodyNumLsa": "ospfv3LSAUpdate.header.linkStateUpdateBody.numLsa-9",
        "VariableHeaderLinkStateAge": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAge-10",
        "LinkStateTypeUnrecognizedLSTypeAction": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateType.unrecognizedLSTypeAction-11",
        "LinkStateTypeLsaFloodingScope": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateType.lsaFloodingScope-12",
        "LinkStateTypeLsaFunctionCode": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateType.lsaFunctionCode-13",
        "VariableHeaderLinkStateID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateID-14",
        "VariableHeaderLinkStateAdvertisingRouter": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisingRouter-15",
        "VariableHeaderLinkStateSequenceNumber": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateSequenceNumber-16",
        "VariableHeaderLinkStateChecksum": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateChecksum-17",
        "VariableHeaderLinkStateLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateLength-18",
        "RouterLSAReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.reserved-19",
        "RouterLSARouterLSAFlags": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerLSAFlags-20",
        "RouterLSAOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.options-21",
        "RouterInterfaceInterfaceType": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.nextRouterInterface.routerInterface.interfaceType-22",
        "RouterInterfaceReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.nextRouterInterface.routerInterface.reserved-23",
        "RouterInterfaceInterfaceMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.nextRouterInterface.routerInterface.interfaceMetric-24",
        "RouterInterfaceInterfaceID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.nextRouterInterface.routerInterface.interfaceID-25",
        "RouterInterfaceNeighborInterfaceID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.nextRouterInterface.routerInterface.neighborInterfaceID-26",
        "RouterInterfaceNeighborRouterID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.nextRouterInterface.routerInterface.neighborRouterID-27",
        "NetworkLSAReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkLSA.reserved-28",
        "NetworkLSAOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkLSA.options-29",
        "AttachedRouterListAttachedRouterID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkLSA.attachedRouterList.attachedRouterID-30",
        "InterAreaPrefixLSAReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaPrefixLSA.reserved-31",
        "InterAreaPrefixLSARouteMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaPrefixLSA.routeMetric-32",
        "AddressPrefixPrefixLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaPrefixLSA.addressPrefix.prefixLength-33",
        "AddressPrefixPrefixOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaPrefixLSA.addressPrefix.prefixOptions-34",
        "AddressPrefixPrefixMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaPrefixLSA.addressPrefix.prefixMetric-35",
        "AddressPrefixDataLengthoctets": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaPrefixLSA.addressPrefix.dataLengthoctets-36",
        "AddressPrefixIpv6AddressPrefix": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaPrefixLSA.addressPrefix.ipv6AddressPrefix-37",
        "InterAreaRouterLSAReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaRouterLSA.reserved-38",
        "InterAreaRouterLSAOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaRouterLSA.options-39",
        "LinkstateadvertisementbodyInterAreaRouterLSAReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaRouterLSA.reserved-40",
        "InterAreaRouterLSARouteMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaRouterLSA.routeMetric-41",
        "InterAreaRouterLSADestinationRouterID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.interAreaRouterLSA.destinationRouterID-42",
        "Grace_period_tlvType": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.graceLSA.grace_period_tlv.type-43",
        "Grace_period_tlvLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.graceLSA.grace_period_tlv.length-44",
        "Grace_period_tlvValue": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.graceLSA.grace_period_tlv.value-45",
        "Graceful_restart_reason_tlvType": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.graceLSA.graceful_restart_reason_tlv.type-46",
        "Graceful_restart_reason_tlvLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.graceLSA.graceful_restart_reason_tlv.length-47",
        "Graceful_restart_reason_tlvValue": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.graceLSA.graceful_restart_reason_tlv.value-48",
        "Graceful_restart_reason_tlvPad": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.graceLSA.graceful_restart_reason_tlv.pad-49",
        "ExternalLSAReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.reserved-50",
        "ExternalLSAOptionsTbit": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalLSAOptions.tbit-51",
        "ExternalLSAOptionsFbit": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalLSAOptions.fbit-52",
        "ExternalLSAOptionsEbit": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalLSAOptions.ebit-53",
        "ExternalLSARouteMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.routeMetric-54",
        "ExternallsaAddressPrefixPrefixLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.addressPrefix.prefixLength-55",
        "ExternallsaAddressPrefixPrefixOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.addressPrefix.prefixOptions-56",
        "ReferencedLSTypeUnrecognizedLSTypeAction": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.addressPrefix.referencedLSType.unrecognizedLSTypeAction-57",
        "ReferencedLSTypeLsaFloodingScope": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.addressPrefix.referencedLSType.lsaFloodingScope-58",
        "ReferencedLSTypeLsaFunctionCode": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.addressPrefix.referencedLSType.lsaFunctionCode-59",
        "ExternallsaAddressPrefixDataLengthoctets": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.addressPrefix.dataLengthoctets-60",
        "ExternallsaAddressPrefixIpv6AddressPrefix": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.addressPrefix.ipv6AddressPrefix-61",
        "ExternalLSAForwardingAddress": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.forwardingAddress-62",
        "ExternalLSAExternalRouteTag": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRouteTag-63",
        "ExternalLSAReferencedLinkStateID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.referencedLinkStateID-64",
        "Type7NSSAExternalLSAReserved": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.reserved-65",
        "Type7nssaexternallsaExternalLSAOptionsTbit": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalLSAOptions.tbit-66",
        "Type7nssaexternallsaExternalLSAOptionsFbit": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalLSAOptions.fbit-67",
        "Type7nssaexternallsaExternalLSAOptionsEbit": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalLSAOptions.ebit-68",
        "Type7NSSAExternalLSARouteMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.routeMetric-69",
        "Type7nssaexternallsaAddressPrefixPrefixLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.addressPrefix.prefixLength-70",
        "Type7nssaexternallsaAddressPrefixPrefixOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.addressPrefix.prefixOptions-71",
        "AddressprefixReferencedLSTypeUnrecognizedLSTypeAction": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.addressPrefix.referencedLSType.unrecognizedLSTypeAction-72",
        "AddressprefixReferencedLSTypeLsaFloodingScope": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.addressPrefix.referencedLSType.lsaFloodingScope-73",
        "AddressprefixReferencedLSTypeLsaFunctionCode": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.addressPrefix.referencedLSType.lsaFunctionCode-74",
        "Type7nssaexternallsaAddressPrefixDataLengthoctets": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.addressPrefix.dataLengthoctets-75",
        "Type7nssaexternallsaAddressPrefixIpv6AddressPrefix": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.addressPrefix.ipv6AddressPrefix-76",
        "Type7NSSAExternalLSAForwardingAddress": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.forwardingAddress-77",
        "Type7NSSAExternalLSAExternalRouteTag": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRouteTag-78",
        "Type7NSSAExternalLSAReferencedLinkStateID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.referencedLinkStateID-79",
        "LinkLSARouterPriority": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.routerPriority-80",
        "LinkLSAOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.options-81",
        "LinkLSALinkLocalInterfaceAddress": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.linkLocalInterfaceAddress-82",
        "LinkLSANumberOfPrefixes": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.numberOfPrefixes-83",
        "AddressprefixesAddressPrefixPrefixLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.addressPrefixes.addressPrefix.prefixLength-84",
        "AddressprefixesAddressPrefixPrefixOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.addressPrefixes.addressPrefix.prefixOptions-85",
        "AddressprefixesAddressPrefixPrefixMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.addressPrefixes.addressPrefix.prefixMetric-86",
        "AddressprefixesAddressPrefixDataLengthoctets": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.addressPrefixes.addressPrefix.dataLengthoctets-87",
        "AddressprefixesAddressPrefixIpv6AddressPrefix": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.linkLSA.addressPrefixes.addressPrefix.ipv6AddressPrefix-88",
        "IntraAreaPrefixLSANumberOfPrefixes": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.numberOfPrefixes-89",
        "IntraareaprefixlsaReferencedLSTypeUnrecognizedLSTypeAction": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.referencedLSType.unrecognizedLSTypeAction-90",
        "IntraareaprefixlsaReferencedLSTypeLsaFloodingScope": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.referencedLSType.lsaFloodingScope-91",
        "IntraareaprefixlsaReferencedLSTypeLsaFunctionCode": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.referencedLSType.lsaFunctionCode-92",
        "IntraAreaPrefixLSAReferencedLinkStateID": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.referencedLinkStateID-93",
        "IntraAreaPrefixLSAReferencedLinkStateAdvertisingRouter": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.referencedLinkStateAdvertisingRouter-94",
        "IntraareaprefixlsaAddressprefixesAddressPrefixPrefixLength": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.addressPrefixes.addressPrefix.prefixLength-95",
        "IntraareaprefixlsaAddressprefixesAddressPrefixPrefixOptions": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.addressPrefixes.addressPrefix.prefixOptions-96",
        "IntraareaprefixlsaAddressprefixesAddressPrefixPrefixMetric": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.addressPrefixes.addressPrefix.prefixMetric-97",
        "IntraareaprefixlsaAddressprefixesAddressPrefixDataLengthoctets": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.addressPrefixes.addressPrefix.dataLengthoctets-98",
        "IntraareaprefixlsaAddressprefixesAddressPrefixIpv6AddressPrefix": "ospfv3LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.intraAreaPrefixLSA.addressPrefixes.addressPrefix.ipv6AddressPrefix-99",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv3LSAUpdate, self).__init__(parent, list_op)

    @property
    def Ospfv3PacketHeaderOspfVersion(self):
        """
        Display Name: OSPF Version
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderOspfVersion"]),
        )

    @property
    def Ospfv3PacketHeaderPacketType(self):
        """
        Display Name: Packet Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderPacketType"])
        )

    @property
    def Ospfv3PacketHeaderPacketLength(self):
        """
        Display Name: Packet length
        Default Value: 48
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderPacketLength"]),
        )

    @property
    def Ospfv3PacketHeaderRouterID(self):
        """
        Display Name: Router ID
        Default Value: 1.1.1.1
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderRouterID"])
        )

    @property
    def Ospfv3PacketHeaderAreaID(self):
        """
        Display Name: Area ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderAreaID"])
        )

    @property
    def Ospfv3PacketHeaderOspfPacketChecksum(self):
        """
        Display Name: OSPF packet checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ospfv3PacketHeaderOspfPacketChecksum"]
            ),
        )

    @property
    def Ospfv3PacketHeaderInstanceID(self):
        """
        Display Name: Instance ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderInstanceID"])
        )

    @property
    def Ospfv3PacketHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv3PacketHeaderReserved"])
        )

    @property
    def LinkStateUpdateBodyNumLsa(self):
        """
        Display Name: # LSAs
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkStateUpdateBodyNumLsa"])
        )

    @property
    def VariableHeaderLinkStateAge(self):
        """
        Display Name: Link-State age
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateAge"])
        )

    @property
    def LinkStateTypeUnrecognizedLSTypeAction(self):
        """
        Display Name: Unrecognized LS Type Action
        Default Value: 0
        Value Format: decimal
        Available enum values: Treat the LSA as if it had link-local flooding scope, 0, Store and flood the LSA, as if type understood, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LinkStateTypeUnrecognizedLSTypeAction"]
            ),
        )

    @property
    def LinkStateTypeLsaFloodingScope(self):
        """
        Display Name: LSA flooding scope
        Default Value: 1
        Value Format: decimal
        Available enum values: Link-Local Scoping. Flooded only on link it is originating on., 0, Area Scoping. Flooded to all routers in the originating area., 1, AS Scoping. Flooded to all routers in the AS., 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LinkStateTypeLsaFloodingScope"]),
        )

    @property
    def LinkStateTypeLsaFunctionCode(self):
        """
        Display Name: LSA function code
        Default Value: 1
        Value Format: decimal
        Available enum values: Router-LSA, 1, Network-LSA., 2, Inter-Area-Prefix-LSA, 3, Inter-Area-Router-LSA, 4, AS-External-LSA, 5, Group-membership-LSA, 6, Type-7-LSA, 7, Link-LSA, 8, Intra-Area-Prefix-LSA, 9, Grace-LSA, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkStateTypeLsaFunctionCode"])
        )

    @property
    def VariableHeaderLinkStateID(self):
        """
        Display Name: Link-State ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateID"])
        )

    @property
    def VariableHeaderLinkStateAdvertisingRouter(self):
        """
        Display Name: Link-State advertising router
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VariableHeaderLinkStateAdvertisingRouter"]
            ),
        )

    @property
    def VariableHeaderLinkStateSequenceNumber(self):
        """
        Display Name: Link-State Sequence Number
        Default Value: 0x80000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["VariableHeaderLinkStateSequenceNumber"]
            ),
        )

    @property
    def VariableHeaderLinkStateChecksum(self):
        """
        Display Name: Link-State checksum
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateChecksum"]),
        )

    @property
    def VariableHeaderLinkStateLength(self):
        """
        Display Name: Link-State length
        Default Value: 30
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateLength"]),
        )

    @property
    def RouterLSAReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RouterLSAReserved"])
        )

    @property
    def RouterLSARouterLSAFlags(self):
        """
        Display Name: Router LSA flags
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RouterLSARouterLSAFlags"])
        )

    @property
    def RouterLSAOptions(self):
        """
        Display Name: Options
        Default Value: 0x13
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RouterLSAOptions"])
        )

    @property
    def RouterInterfaceInterfaceType(self):
        """
        Display Name: Interface type
        Default Value: 1
        Value Format: decimal
        Available enum values: Point-to-point connection to another router, 1, Connection to a transit network, 2, Connection to a stub network , 3, Virtual link, 4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RouterInterfaceInterfaceType"])
        )

    @property
    def RouterInterfaceReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RouterInterfaceReserved"])
        )

    @property
    def RouterInterfaceInterfaceMetric(self):
        """
        Display Name: Interface metric
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RouterInterfaceInterfaceMetric"]),
        )

    @property
    def RouterInterfaceInterfaceID(self):
        """
        Display Name: Interface ID
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RouterInterfaceInterfaceID"])
        )

    @property
    def RouterInterfaceNeighborInterfaceID(self):
        """
        Display Name: Neighbor Interface ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouterInterfaceNeighborInterfaceID"]
            ),
        )

    @property
    def RouterInterfaceNeighborRouterID(self):
        """
        Display Name: Neighbor Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RouterInterfaceNeighborRouterID"]),
        )

    @property
    def NetworkLSAReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NetworkLSAReserved"])
        )

    @property
    def NetworkLSAOptions(self):
        """
        Display Name: Options
        Default Value: 0x13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NetworkLSAOptions"])
        )

    @property
    def AttachedRouterListAttachedRouterID(self):
        """
        Display Name: Attached Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AttachedRouterListAttachedRouterID"]
            ),
        )

    @property
    def InterAreaPrefixLSAReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterAreaPrefixLSAReserved"])
        )

    @property
    def InterAreaPrefixLSARouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["InterAreaPrefixLSARouteMetric"]),
        )

    @property
    def AddressPrefixPrefixLength(self):
        """
        Display Name: Prefix length
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressPrefixPrefixLength"])
        )

    @property
    def AddressPrefixPrefixOptions(self):
        """
        Display Name: Prefix options
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressPrefixPrefixOptions"])
        )

    @property
    def AddressPrefixPrefixMetric(self):
        """
        Display Name: Prefix metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddressPrefixPrefixMetric"])
        )

    @property
    def AddressPrefixDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AddressPrefixDataLengthoctets"]),
        )

    @property
    def AddressPrefixIpv6AddressPrefix(self):
        """
        Display Name: IPv6 address prefix
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AddressPrefixIpv6AddressPrefix"]),
        )

    @property
    def InterAreaRouterLSAReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterAreaRouterLSAReserved"])
        )

    @property
    def InterAreaRouterLSAOptions(self):
        """
        Display Name: Options
        Default Value: 0x13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterAreaRouterLSAOptions"])
        )

    @property
    def LinkstateadvertisementbodyInterAreaRouterLSAReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "LinkstateadvertisementbodyInterAreaRouterLSAReserved"
                ]
            ),
        )

    @property
    def InterAreaRouterLSARouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["InterAreaRouterLSARouteMetric"]),
        )

    @property
    def InterAreaRouterLSADestinationRouterID(self):
        """
        Display Name: Destination Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["InterAreaRouterLSADestinationRouterID"]
            ),
        )

    @property
    def Grace_period_tlvType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Grace_period_tlvType"])
        )

    @property
    def Grace_period_tlvLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Grace_period_tlvLength"])
        )

    @property
    def Grace_period_tlvValue(self):
        """
        Display Name: Value
        Default Value: 120
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Grace_period_tlvValue"])
        )

    @property
    def Graceful_restart_reason_tlvType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Graceful_restart_reason_tlvType"]),
        )

    @property
    def Graceful_restart_reason_tlvLength(self):
        """
        Display Name: Length
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Graceful_restart_reason_tlvLength"]),
        )

    @property
    def Graceful_restart_reason_tlvValue(self):
        """
        Display Name: Value
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Graceful_restart_reason_tlvValue"]),
        )

    @property
    def Graceful_restart_reason_tlvPad(self):
        """
        Display Name: pad
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Graceful_restart_reason_tlvPad"]),
        )

    @property
    def ExternalLSAReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalLSAReserved"])
        )

    @property
    def ExternalLSAOptionsTbit(self):
        """
        Display Name: T-bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalLSAOptionsTbit"])
        )

    @property
    def ExternalLSAOptionsFbit(self):
        """
        Display Name: F-bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalLSAOptionsFbit"])
        )

    @property
    def ExternalLSAOptionsEbit(self):
        """
        Display Name: E-bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalLSAOptionsEbit"])
        )

    @property
    def ExternalLSARouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalLSARouteMetric"])
        )

    @property
    def ExternallsaAddressPrefixPrefixLength(self):
        """
        Display Name: Prefix length
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExternallsaAddressPrefixPrefixLength"]
            ),
        )

    @property
    def ExternallsaAddressPrefixPrefixOptions(self):
        """
        Display Name: Prefix options
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExternallsaAddressPrefixPrefixOptions"]
            ),
        )

    @property
    def ReferencedLSTypeUnrecognizedLSTypeAction(self):
        """
        Display Name: Unrecognized LS Type Action
        Default Value: 0
        Value Format: decimal
        Available enum values: Treat the LSA as if it had link-local flooding scope, 0, Store and flood the LSA, as if type understood, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ReferencedLSTypeUnrecognizedLSTypeAction"]
            ),
        )

    @property
    def ReferencedLSTypeLsaFloodingScope(self):
        """
        Display Name: LSA flooding scope
        Default Value: 1
        Value Format: decimal
        Available enum values: Link-Local Scoping. Flooded only on link it is originating on., 0, Area Scoping. Flooded to all routers in the originating area., 1, AS Scoping. Flooded to all routers in the AS., 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReferencedLSTypeLsaFloodingScope"]),
        )

    @property
    def ReferencedLSTypeLsaFunctionCode(self):
        """
        Display Name: LSA function code
        Default Value: 1
        Value Format: decimal
        Available enum values: Router-LSA, 1, Network-LSA., 2, Inter-Area-Prefix-LSA, 3, Inter-Area-Router-LSA, 4, AS-External-LSA, 5, Group-membership-LSA, 6, Type-7-LSA, 7, Link-LSA, 8, Intra-Area-Prefix-LSA, 9, Grace-LSA, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReferencedLSTypeLsaFunctionCode"]),
        )

    @property
    def ExternallsaAddressPrefixDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExternallsaAddressPrefixDataLengthoctets"]
            ),
        )

    @property
    def ExternallsaAddressPrefixIpv6AddressPrefix(self):
        """
        Display Name: IPv6 address prefix
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExternallsaAddressPrefixIpv6AddressPrefix"]
            ),
        )

    @property
    def ExternalLSAForwardingAddress(self):
        """
        Display Name: Forwarding address
        Default Value: 1:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalLSAForwardingAddress"])
        )

    @property
    def ExternalLSAExternalRouteTag(self):
        """
        Display Name: External route tag
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalLSAExternalRouteTag"])
        )

    @property
    def ExternalLSAReferencedLinkStateID(self):
        """
        Display Name: Referenced Link-State ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ExternalLSAReferencedLinkStateID"]),
        )

    @property
    def Type7NSSAExternalLSAReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Type7NSSAExternalLSAReserved"])
        )

    @property
    def Type7nssaexternallsaExternalLSAOptionsTbit(self):
        """
        Display Name: T-bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalLSAOptionsTbit"]
            ),
        )

    @property
    def Type7nssaexternallsaExternalLSAOptionsFbit(self):
        """
        Display Name: F-bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalLSAOptionsFbit"]
            ),
        )

    @property
    def Type7nssaexternallsaExternalLSAOptionsEbit(self):
        """
        Display Name: E-bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalLSAOptionsEbit"]
            ),
        )

    @property
    def Type7NSSAExternalLSARouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Type7NSSAExternalLSARouteMetric"]),
        )

    @property
    def Type7nssaexternallsaAddressPrefixPrefixLength(self):
        """
        Display Name: Prefix length
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaAddressPrefixPrefixLength"]
            ),
        )

    @property
    def Type7nssaexternallsaAddressPrefixPrefixOptions(self):
        """
        Display Name: Prefix options
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaAddressPrefixPrefixOptions"]
            ),
        )

    @property
    def AddressprefixReferencedLSTypeUnrecognizedLSTypeAction(self):
        """
        Display Name: Unrecognized LS Type Action
        Default Value: 0
        Value Format: decimal
        Available enum values: Treat the LSA as if it had link-local flooding scope, 0, Store and flood the LSA, as if type understood, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "AddressprefixReferencedLSTypeUnrecognizedLSTypeAction"
                ]
            ),
        )

    @property
    def AddressprefixReferencedLSTypeLsaFloodingScope(self):
        """
        Display Name: LSA flooding scope
        Default Value: 1
        Value Format: decimal
        Available enum values: Link-Local Scoping. Flooded only on link it is originating on., 0, Area Scoping. Flooded to all routers in the originating area., 1, AS Scoping. Flooded to all routers in the AS., 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AddressprefixReferencedLSTypeLsaFloodingScope"]
            ),
        )

    @property
    def AddressprefixReferencedLSTypeLsaFunctionCode(self):
        """
        Display Name: LSA function code
        Default Value: 1
        Value Format: decimal
        Available enum values: Router-LSA, 1, Network-LSA., 2, Inter-Area-Prefix-LSA, 3, Inter-Area-Router-LSA, 4, AS-External-LSA, 5, Group-membership-LSA, 6, Type-7-LSA, 7, Link-LSA, 8, Intra-Area-Prefix-LSA, 9, Grace-LSA, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AddressprefixReferencedLSTypeLsaFunctionCode"]
            ),
        )

    @property
    def Type7nssaexternallsaAddressPrefixDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaAddressPrefixDataLengthoctets"]
            ),
        )

    @property
    def Type7nssaexternallsaAddressPrefixIpv6AddressPrefix(self):
        """
        Display Name: IPv6 address prefix
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaAddressPrefixIpv6AddressPrefix"]
            ),
        )

    @property
    def Type7NSSAExternalLSAForwardingAddress(self):
        """
        Display Name: Forwarding address
        Default Value: 1:0:0:0:0:0:0:0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7NSSAExternalLSAForwardingAddress"]
            ),
        )

    @property
    def Type7NSSAExternalLSAExternalRouteTag(self):
        """
        Display Name: External route tag
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7NSSAExternalLSAExternalRouteTag"]
            ),
        )

    @property
    def Type7NSSAExternalLSAReferencedLinkStateID(self):
        """
        Display Name: Referenced Link-State ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7NSSAExternalLSAReferencedLinkStateID"]
            ),
        )

    @property
    def LinkLSARouterPriority(self):
        """
        Display Name: Router priority
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkLSARouterPriority"])
        )

    @property
    def LinkLSAOptions(self):
        """
        Display Name: Options
        Default Value: 0x13
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkLSAOptions"])
        )

    @property
    def LinkLSALinkLocalInterfaceAddress(self):
        """
        Display Name: Link-Local Interface Address
        Default Value: 0::0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LinkLSALinkLocalInterfaceAddress"]),
        )

    @property
    def LinkLSANumberOfPrefixes(self):
        """
        Display Name: Number of prefixes
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkLSANumberOfPrefixes"])
        )

    @property
    def AddressprefixesAddressPrefixPrefixLength(self):
        """
        Display Name: Prefix length
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AddressprefixesAddressPrefixPrefixLength"]
            ),
        )

    @property
    def AddressprefixesAddressPrefixPrefixOptions(self):
        """
        Display Name: Prefix options
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AddressprefixesAddressPrefixPrefixOptions"]
            ),
        )

    @property
    def AddressprefixesAddressPrefixPrefixMetric(self):
        """
        Display Name: Prefix metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AddressprefixesAddressPrefixPrefixMetric"]
            ),
        )

    @property
    def AddressprefixesAddressPrefixDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AddressprefixesAddressPrefixDataLengthoctets"]
            ),
        )

    @property
    def AddressprefixesAddressPrefixIpv6AddressPrefix(self):
        """
        Display Name: IPv6 address prefix
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AddressprefixesAddressPrefixIpv6AddressPrefix"]
            ),
        )

    @property
    def IntraAreaPrefixLSANumberOfPrefixes(self):
        """
        Display Name: Number of prefixes
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntraAreaPrefixLSANumberOfPrefixes"]
            ),
        )

    @property
    def IntraareaprefixlsaReferencedLSTypeUnrecognizedLSTypeAction(self):
        """
        Display Name: Unrecognized LS Type Action
        Default Value: 0
        Value Format: decimal
        Available enum values: Treat the LSA as if it had link-local flooding scope, 0, Store and flood the LSA, as if type understood, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntraareaprefixlsaReferencedLSTypeUnrecognizedLSTypeAction"
                ]
            ),
        )

    @property
    def IntraareaprefixlsaReferencedLSTypeLsaFloodingScope(self):
        """
        Display Name: LSA flooding scope
        Default Value: 1
        Value Format: decimal
        Available enum values: Link-Local Scoping. Flooded only on link it is originating on., 0, Area Scoping. Flooded to all routers in the originating area., 1, AS Scoping. Flooded to all routers in the AS., 2, Reserved, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntraareaprefixlsaReferencedLSTypeLsaFloodingScope"]
            ),
        )

    @property
    def IntraareaprefixlsaReferencedLSTypeLsaFunctionCode(self):
        """
        Display Name: LSA function code
        Default Value: 1
        Value Format: decimal
        Available enum values: Router-LSA, 1, Network-LSA., 2, Inter-Area-Prefix-LSA, 3, Inter-Area-Router-LSA, 4, AS-External-LSA, 5, Group-membership-LSA, 6, Type-7-LSA, 7, Link-LSA, 8, Intra-Area-Prefix-LSA, 9, Grace-LSA, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntraareaprefixlsaReferencedLSTypeLsaFunctionCode"]
            ),
        )

    @property
    def IntraAreaPrefixLSAReferencedLinkStateID(self):
        """
        Display Name: Referenced Link-State ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IntraAreaPrefixLSAReferencedLinkStateID"]
            ),
        )

    @property
    def IntraAreaPrefixLSAReferencedLinkStateAdvertisingRouter(self):
        """
        Display Name: Referenced Link-State Advertising Router
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntraAreaPrefixLSAReferencedLinkStateAdvertisingRouter"
                ]
            ),
        )

    @property
    def IntraareaprefixlsaAddressprefixesAddressPrefixPrefixLength(self):
        """
        Display Name: Prefix length
        Default Value: 64
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntraareaprefixlsaAddressprefixesAddressPrefixPrefixLength"
                ]
            ),
        )

    @property
    def IntraareaprefixlsaAddressprefixesAddressPrefixPrefixOptions(self):
        """
        Display Name: Prefix options
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntraareaprefixlsaAddressprefixesAddressPrefixPrefixOptions"
                ]
            ),
        )

    @property
    def IntraareaprefixlsaAddressprefixesAddressPrefixPrefixMetric(self):
        """
        Display Name: Prefix metric
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntraareaprefixlsaAddressprefixesAddressPrefixPrefixMetric"
                ]
            ),
        )

    @property
    def IntraareaprefixlsaAddressprefixesAddressPrefixDataLengthoctets(self):
        """
        Display Name: data length (octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntraareaprefixlsaAddressprefixesAddressPrefixDataLengthoctets"
                ]
            ),
        )

    @property
    def IntraareaprefixlsaAddressprefixesAddressPrefixIpv6AddressPrefix(self):
        """
        Display Name: IPv6 address prefix
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "IntraareaprefixlsaAddressprefixesAddressPrefixIpv6AddressPrefix"
                ]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
