from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv2LSAUpdate(Base):
    __slots__ = ()
    _SDM_NAME = "ospfv2LSAUpdate"
    _SDM_ATT_MAP = {
        "Ospfv2PacketHeaderOspfVersion": "ospfv2LSAUpdate.header.ospfv2PacketHeader.ospfVersion-1",
        "Ospfv2PacketHeaderPacketType": "ospfv2LSAUpdate.header.ospfv2PacketHeader.packetType-2",
        "Ospfv2PacketHeaderPacketLength": "ospfv2LSAUpdate.header.ospfv2PacketHeader.packetLength-3",
        "Ospfv2PacketHeaderRouterID": "ospfv2LSAUpdate.header.ospfv2PacketHeader.routerID-4",
        "Ospfv2PacketHeaderAreaID": "ospfv2LSAUpdate.header.ospfv2PacketHeader.areaID-5",
        "Ospfv2PacketHeaderChecksum": "ospfv2LSAUpdate.header.ospfv2PacketHeader.checksum-6",
        "Ospfv2PacketHeaderAuthenticationType": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationType-7",
        "AuthenticationDataNullAuthentication": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationData.nullAuthentication-8",
        "AuthenticationDataSimplePassword": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationData.simplePassword-9",
        "CryptographicAuthenticationDataReserved": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.reserved-10",
        "CryptographicAuthenticationDataKeyID": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.keyID-11",
        "CryptographicAuthenticationDataAuthenticationDataLength": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.authenticationDataLength-12",
        "CryptographicAuthenticationDataCryptographicSequenceNumber": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationData.cryptographicAuthenticationData.cryptographicSequenceNumber-13",
        "UserDefinedAuthenticationDataUserDefinedAuthData": "ospfv2LSAUpdate.header.ospfv2PacketHeader.authenticationData.userDefinedAuthenticationData.userDefinedAuthData-14",
        "LinkStateUpdateBodyNumberOfLSAs": "ospfv2LSAUpdate.header.linkStateUpdateBody.numberOfLSAs-15",
        "VariableHeaderLinkStateAge": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAge-16",
        "VariableHeaderOptions": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.options-17",
        "VariableHeaderLinkStateType": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateType-18",
        "VariableHeaderLinkStateID": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateID-19",
        "VariableHeaderLinkStateAdvertisingRouter": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisingRouter-20",
        "VariableHeaderLinkStateSequenceNumber": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateSequenceNumber-21",
        "VariableHeaderLinkStateChecksum": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateChecksum-22",
        "VariableHeaderLinkStateLength": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateLength-23",
        "RouterLSAReserved": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.reserved-24",
        "RouterLSARouterLSAFlags": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerLSAFlags-25",
        "RouterLSAPad": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.pad-26",
        "RouterLSANumberOfRouterInterfaceLinks": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.numberOfRouterInterfaceLinks-27",
        "RouterInterfaceRouterInterfaceLinkID": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.routerInterfaceLinkID-28",
        "RouterInterfaceRouterInterfaceLinkData": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.routerInterfaceLinkData-29",
        "RouterInterfaceInterfaceType": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.interfaceType-30",
        "RouterInterfaceNumberOfTOSEntries": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.numberOfTOSEntries-31",
        "RouterInterfaceInterfaceMetric": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.interfaceMetric-32",
        "TosEntryTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.tosList.tosEntry.typeOfService-33",
        "TosEntryReserved": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.tosList.tosEntry.reserved-34",
        "TosEntryMetricForCorrespondingTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.routerLSA.routerInterfacesList.routerInterface.tosList.tosEntry.metricForCorrespondingTypeOfService-35",
        "NetworkLSANetworkMask": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkLSA.networkMask-36",
        "AttachedRouterListAttachedRouterID": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkLSA.attachedRouterList.attachedRouterID-37",
        "SummaryRouteNetworkMask": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkSummaryLSA.summaryRoute.networkMask-38",
        "SummaryRouteReserved": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkSummaryLSA.summaryRoute.reserved-39",
        "SummaryRouteRouteMetric": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkSummaryLSA.summaryRoute.routeMetric-40",
        "ToslistTosEntryTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkSummaryLSA.summaryRoute.tosList.tosEntry.typeOfService-41",
        "ToslistTosEntryMetricForCorrespondingTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.networkSummaryLSA.summaryRoute.tosList.tosEntry.metricForCorrespondingTypeOfService-42",
        "AsborderroutersummarylsaSummaryRouteNetworkMask": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.asBorderRouterSummaryLSA.summaryRoute.networkMask-43",
        "AsborderroutersummarylsaSummaryRouteReserved": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.asBorderRouterSummaryLSA.summaryRoute.reserved-44",
        "AsborderroutersummarylsaSummaryRouteRouteMetric": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.asBorderRouterSummaryLSA.summaryRoute.routeMetric-45",
        "SummaryrouteToslistTosEntryTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.asBorderRouterSummaryLSA.summaryRoute.tosList.tosEntry.typeOfService-46",
        "SummaryrouteToslistTosEntryMetricForCorrespondingTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.asBorderRouterSummaryLSA.summaryRoute.tosList.tosEntry.metricForCorrespondingTypeOfService-47",
        "ExternalRouteNetworkMask": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.networkMask-48",
        "ExternalRouteEbit": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.ebit-49",
        "ExternalRouteReserved": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.reserved-50",
        "ExternalRouteRouteMetric": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.routeMetric-51",
        "ExternalRouteForwardingAddress": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.forwardingAddress-52",
        "ExternalRouteExternalRouteTag": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.externalRouteTag-53",
        "TosEntryEbit": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.tosList.tosEntry.ebit-54",
        "ExternalrouteToslistTosEntryTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.tosList.tosEntry.typeOfService-55",
        "ExternalrouteToslistTosEntryMetricForCorrespondingTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.tosList.tosEntry.metricForCorrespondingTypeOfService-56",
        "TosEntryForwardingAddress": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.externalLSA.externalRoute.tosList.tosEntry.forwardingAddress-57",
        "Type7nssaexternallsaExternalRouteNetworkMask": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.networkMask-58",
        "Type7nssaexternallsaExternalRouteEbit": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.ebit-59",
        "Type7nssaexternallsaExternalRouteReserved": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.reserved-60",
        "Type7nssaexternallsaExternalRouteRouteMetric": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.routeMetric-61",
        "Type7nssaexternallsaExternalRouteForwardingAddress": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.forwardingAddress-62",
        "Type7nssaexternallsaExternalRouteExternalRouteTag": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.externalRouteTag-63",
        "ToslistTosEntryEbit": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.tosList.tosEntry.ebit-64",
        "Type7nssaexternallsaExternalrouteToslistTosEntryTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.tosList.tosEntry.typeOfService-65",
        "Type7nssaexternallsaExternalrouteToslistTosEntryMetricForCorrespondingTypeOfService": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.tosList.tosEntry.metricForCorrespondingTypeOfService-66",
        "ToslistTosEntryForwardingAddress": "ospfv2LSAUpdate.header.linkStateUpdateBody.lsaList.linkStateAdvertisement.variableHeader.linkStateAdvertisementBody.type7NSSAExternalLSA.externalRoute.tosList.tosEntry.forwardingAddress-67",
    }

    def __init__(self, parent, list_op=False):
        super(Ospfv2LSAUpdate, self).__init__(parent, list_op)

    @property
    def Ospfv2PacketHeaderOspfVersion(self):
        """
        Display Name: OSPF Version
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderOspfVersion"]),
        )

    @property
    def Ospfv2PacketHeaderPacketType(self):
        """
        Display Name: Packet Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderPacketType"])
        )

    @property
    def Ospfv2PacketHeaderPacketLength(self):
        """
        Display Name: Packet length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderPacketLength"]),
        )

    @property
    def Ospfv2PacketHeaderRouterID(self):
        """
        Display Name: Router ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderRouterID"])
        )

    @property
    def Ospfv2PacketHeaderAreaID(self):
        """
        Display Name: Area ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderAreaID"])
        )

    @property
    def Ospfv2PacketHeaderChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ospfv2PacketHeaderChecksum"])
        )

    @property
    def Ospfv2PacketHeaderAuthenticationType(self):
        """
        Display Name: Authentication type
        Default Value: 0
        Value Format: decimal
        Available enum values: Null authentication, 0, Simple password, 1, Cryptographic Authentication, 2, User defined Authentication, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ospfv2PacketHeaderAuthenticationType"]
            ),
        )

    @property
    def AuthenticationDataNullAuthentication(self):
        """
        Display Name: Null authentication
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AuthenticationDataNullAuthentication"]
            ),
        )

    @property
    def AuthenticationDataSimplePassword(self):
        """
        Display Name: Simple password
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AuthenticationDataSimplePassword"]),
        )

    @property
    def CryptographicAuthenticationDataReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CryptographicAuthenticationDataReserved"]
            ),
        )

    @property
    def CryptographicAuthenticationDataKeyID(self):
        """
        Display Name: Key ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["CryptographicAuthenticationDataKeyID"]
            ),
        )

    @property
    def CryptographicAuthenticationDataAuthenticationDataLength(self):
        """
        Display Name: Authentication data length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CryptographicAuthenticationDataAuthenticationDataLength"
                ]
            ),
        )

    @property
    def CryptographicAuthenticationDataCryptographicSequenceNumber(self):
        """
        Display Name: Cryptographic sequence number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "CryptographicAuthenticationDataCryptographicSequenceNumber"
                ]
            ),
        )

    @property
    def UserDefinedAuthenticationDataUserDefinedAuthData(self):
        """
        Display Name: User defined Auth Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UserDefinedAuthenticationDataUserDefinedAuthData"]
            ),
        )

    @property
    def LinkStateUpdateBodyNumberOfLSAs(self):
        """
        Display Name: Number of LSAs
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["LinkStateUpdateBodyNumberOfLSAs"]),
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
    def VariableHeaderOptions(self):
        """
        Display Name: Options
        Default Value: 0x42
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderOptions"])
        )

    @property
    def VariableHeaderLinkStateType(self):
        """
        Display Name: Link-State type
        Default Value: 1
        Value Format: decimal
        Available enum values: Router LSA, 1, Network LSA, 2, Summary LSA, Routers to Networks, 3, Summary LSA, Routers to AS Boundary, 4, AS-External-LSA, 5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VariableHeaderLinkStateType"])
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
        Default Value: 0x1234
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
        Default Value: 20
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
        Default Value: 0
        Value Format: decimal
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
    def RouterLSAPad(self):
        """
        Display Name: Pad
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RouterLSAPad"]))

    @property
    def RouterLSANumberOfRouterInterfaceLinks(self):
        """
        Display Name: Number of Router Interface Links
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouterLSANumberOfRouterInterfaceLinks"]
            ),
        )

    @property
    def RouterInterfaceRouterInterfaceLinkID(self):
        """
        Display Name: Router Interface Link ID
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouterInterfaceRouterInterfaceLinkID"]
            ),
        )

    @property
    def RouterInterfaceRouterInterfaceLinkData(self):
        """
        Display Name: Router Interface Link Data
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RouterInterfaceRouterInterfaceLinkData"]
            ),
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
    def RouterInterfaceNumberOfTOSEntries(self):
        """
        Display Name: Number of TOS Entries
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RouterInterfaceNumberOfTOSEntries"]),
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
    def TosEntryTypeOfService(self):
        """
        Display Name: Type-Of-Service
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TosEntryTypeOfService"])
        )

    @property
    def TosEntryReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TosEntryReserved"])
        )

    @property
    def TosEntryMetricForCorrespondingTypeOfService(self):
        """
        Display Name: Metric for corresponding Type-Of-Service
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["TosEntryMetricForCorrespondingTypeOfService"]
            ),
        )

    @property
    def NetworkLSANetworkMask(self):
        """
        Display Name: Network mask
        Default Value: 255.255.255.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NetworkLSANetworkMask"])
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
    def SummaryRouteNetworkMask(self):
        """
        Display Name: Network mask
        Default Value: 255.255.255.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SummaryRouteNetworkMask"])
        )

    @property
    def SummaryRouteReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SummaryRouteReserved"])
        )

    @property
    def SummaryRouteRouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SummaryRouteRouteMetric"])
        )

    @property
    def ToslistTosEntryTypeOfService(self):
        """
        Display Name: Type-Of-Service
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ToslistTosEntryTypeOfService"])
        )

    @property
    def ToslistTosEntryMetricForCorrespondingTypeOfService(self):
        """
        Display Name: Metric for corresponding Type-Of-Service
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ToslistTosEntryMetricForCorrespondingTypeOfService"]
            ),
        )

    @property
    def AsborderroutersummarylsaSummaryRouteNetworkMask(self):
        """
        Display Name: Network mask
        Default Value: 255.255.255.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AsborderroutersummarylsaSummaryRouteNetworkMask"]
            ),
        )

    @property
    def AsborderroutersummarylsaSummaryRouteReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AsborderroutersummarylsaSummaryRouteReserved"]
            ),
        )

    @property
    def AsborderroutersummarylsaSummaryRouteRouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AsborderroutersummarylsaSummaryRouteRouteMetric"]
            ),
        )

    @property
    def SummaryrouteToslistTosEntryTypeOfService(self):
        """
        Display Name: Type-Of-Service
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["SummaryrouteToslistTosEntryTypeOfService"]
            ),
        )

    @property
    def SummaryrouteToslistTosEntryMetricForCorrespondingTypeOfService(self):
        """
        Display Name: Metric for corresponding Type-Of-Service
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "SummaryrouteToslistTosEntryMetricForCorrespondingTypeOfService"
                ]
            ),
        )

    @property
    def ExternalRouteNetworkMask(self):
        """
        Display Name: Network mask
        Default Value: 255.255.255.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalRouteNetworkMask"])
        )

    @property
    def ExternalRouteEbit(self):
        """
        Display Name: E-Bit
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalRouteEbit"])
        )

    @property
    def ExternalRouteReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalRouteReserved"])
        )

    @property
    def ExternalRouteRouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExternalRouteRouteMetric"])
        )

    @property
    def ExternalRouteForwardingAddress(self):
        """
        Display Name: Forwarding Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ExternalRouteForwardingAddress"]),
        )

    @property
    def ExternalRouteExternalRouteTag(self):
        """
        Display Name: External Route Tag
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ExternalRouteExternalRouteTag"]),
        )

    @property
    def TosEntryEbit(self):
        """
        Display Name: E-Bit
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TosEntryEbit"]))

    @property
    def ExternalrouteToslistTosEntryTypeOfService(self):
        """
        Display Name: Type-Of-Service
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["ExternalrouteToslistTosEntryTypeOfService"]
            ),
        )

    @property
    def ExternalrouteToslistTosEntryMetricForCorrespondingTypeOfService(self):
        """
        Display Name: Metric for corresponding Type-Of-Service
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "ExternalrouteToslistTosEntryMetricForCorrespondingTypeOfService"
                ]
            ),
        )

    @property
    def TosEntryForwardingAddress(self):
        """
        Display Name: Forwarding Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TosEntryForwardingAddress"])
        )

    @property
    def Type7nssaexternallsaExternalRouteNetworkMask(self):
        """
        Display Name: Network mask
        Default Value: 255.255.255.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalRouteNetworkMask"]
            ),
        )

    @property
    def Type7nssaexternallsaExternalRouteEbit(self):
        """
        Display Name: E-Bit
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalRouteEbit"]
            ),
        )

    @property
    def Type7nssaexternallsaExternalRouteReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalRouteReserved"]
            ),
        )

    @property
    def Type7nssaexternallsaExternalRouteRouteMetric(self):
        """
        Display Name: Route Metric
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalRouteRouteMetric"]
            ),
        )

    @property
    def Type7nssaexternallsaExternalRouteForwardingAddress(self):
        """
        Display Name: Forwarding Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalRouteForwardingAddress"]
            ),
        )

    @property
    def Type7nssaexternallsaExternalRouteExternalRouteTag(self):
        """
        Display Name: External Route Tag
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Type7nssaexternallsaExternalRouteExternalRouteTag"]
            ),
        )

    @property
    def ToslistTosEntryEbit(self):
        """
        Display Name: E-Bit
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ToslistTosEntryEbit"])
        )

    @property
    def Type7nssaexternallsaExternalrouteToslistTosEntryTypeOfService(self):
        """
        Display Name: Type-Of-Service
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Type7nssaexternallsaExternalrouteToslistTosEntryTypeOfService"
                ]
            ),
        )

    @property
    def Type7nssaexternallsaExternalrouteToslistTosEntryMetricForCorrespondingTypeOfService(
        self,
    ):
        """
        Display Name: Metric for corresponding Type-Of-Service
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Type7nssaexternallsaExternalrouteToslistTosEntryMetricForCorrespondingTypeOfService"
                ]
            ),
        )

    @property
    def ToslistTosEntryForwardingAddress(self):
        """
        Display Name: Forwarding Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ToslistTosEntryForwardingAddress"]),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
