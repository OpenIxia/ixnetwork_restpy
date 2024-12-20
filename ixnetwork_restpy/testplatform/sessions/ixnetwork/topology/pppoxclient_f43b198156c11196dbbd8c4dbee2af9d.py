# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Pppoxclient(Base):
    """PPPoX Client
    The Pppoxclient class encapsulates a list of pppoxclient resources that are managed by the user.
    A list of resources can be retrieved from the server using the Pppoxclient.find() method.
    The list can be managed by using the Pppoxclient.add() and Pppoxclient.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "pppoxclient"
    _SDM_ATT_MAP = {
        "AcMatchMac": "acMatchMac",
        "AcMatchName": "acMatchName",
        "AcOptions": "acOptions",
        "ActualRateDownstream": "actualRateDownstream",
        "ActualRateUpstream": "actualRateUpstream",
        "AgentAccessAggregationCircuitId": "agentAccessAggregationCircuitId",
        "AgentCircuitId": "agentCircuitId",
        "AgentRemoteId": "agentRemoteId",
        "AuthRetries": "authRetries",
        "AuthTimeout": "authTimeout",
        "AuthType": "authType",
        "CalledNum": "calledNum",
        "CallingNum": "callingNum",
        "ChapName": "chapName",
        "ChapSecret": "chapSecret",
        "ClientDnsOptions": "clientDnsOptions",
        "ClientLocalIp": "clientLocalIp",
        "ClientLocalIpv6Iid": "clientLocalIpv6Iid",
        "ClientNcpOptions": "clientNcpOptions",
        "ClientNetmask": "clientNetmask",
        "ClientNetmaskOptions": "clientNetmaskOptions",
        "ClientPrimaryDnsAddress": "clientPrimaryDnsAddress",
        "ClientSecondaryDnsAddress": "clientSecondaryDnsAddress",
        "ClientSignalIWF": "clientSignalIWF",
        "ClientSignalLoopChar": "clientSignalLoopChar",
        "ClientSignalLoopEncapsulation": "clientSignalLoopEncapsulation",
        "ClientSignalLoopId": "clientSignalLoopId",
        "ClientV6NcpOptions": "clientV6NcpOptions",
        "ClientWinsOptions": "clientWinsOptions",
        "ClientWinsPrimaryAddress": "clientWinsPrimaryAddress",
        "ClientWinsSecondaryAddress": "clientWinsSecondaryAddress",
        "CompMaxHeader": "compMaxHeader",
        "CompSuboptions": "compSuboptions",
        "ConnectSpeedUpdateEnable": "connectSpeedUpdateEnable",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "CustomAction": "customAction",
        "DataLink": "dataLink",
        "DescriptiveName": "descriptiveName",
        "DiscoveredIpv4Addresses": "discoveredIpv4Addresses",
        "DiscoveredIpv6Addresses": "discoveredIpv6Addresses",
        "DiscoveredMacs": "discoveredMacs",
        "DiscoveredRemoteSessionIds": "discoveredRemoteSessionIds",
        "DiscoveredRemoteTunnelIds": "discoveredRemoteTunnelIds",
        "DiscoveredSessionIds": "discoveredSessionIds",
        "DiscoveredTunnelIPs": "discoveredTunnelIPs",
        "DiscoveredTunnelIds": "discoveredTunnelIds",
        "DomainList": "domainList",
        "DslTypeTlv": "dslTypeTlv",
        "EchoReqInterval": "echoReqInterval",
        "EnableDomainGroups": "enableDomainGroups",
        "EnableEchoReq": "enableEchoReq",
        "EnableEchoRsp": "enableEchoRsp",
        "EnableHostUniq": "enableHostUniq",
        "EnableMaxPayload": "enableMaxPayload",
        "EnableRedial": "enableRedial",
        "Encaps1": "encaps1",
        "Encaps2": "encaps2",
        "EndpointDiscNegotiation": "endpointDiscNegotiation",
        "EndpointDiscriminatorClass": "endpointDiscriminatorClass",
        "Errors": "errors",
        "FcsAltOption": "fcsAltOption",
        "HostUniq": "hostUniq",
        "HostUniqLength": "hostUniqLength",
        "IphcFMaxPeriod": "iphcFMaxPeriod",
        "IphcFMaxTime": "iphcFMaxTime",
        "IphcNonTcpSpace": "iphcNonTcpSpace",
        "IphcTcpSpace": "iphcTcpSpace",
        "LastRxLcpReq": "lastRxLcpReq",
        "LastSentLcpReq": "lastSentLcpReq",
        "LcpAccm": "lcpAccm",
        "LcpConfReqInterval": "lcpConfReqInterval",
        "LcpConfReqMode": "lcpConfReqMode",
        "LcpConfReqRetries": "lcpConfReqRetries",
        "LcpEnableAccm": "lcpEnableAccm",
        "LcpEnableAcfc": "lcpEnableAcfc",
        "LcpEnableFcsAlternatives": "lcpEnableFcsAlternatives",
        "LcpEnablePfc": "lcpEnablePfc",
        "LcpMaxFailure": "lcpMaxFailure",
        "LcpRetries": "lcpRetries",
        "LcpStartDelay": "lcpStartDelay",
        "LcpTermRetries": "lcpTermRetries",
        "LcpTimeout": "lcpTimeout",
        "MaxPayload": "maxPayload",
        "MlpppIPAddress": "mlpppIPAddress",
        "MlpppMACAddress": "mlpppMACAddress",
        "Mrru": "mrru",
        "MrruNegotiation": "mrruNegotiation",
        "MruNegotiation": "mruNegotiation",
        "Mtu": "mtu",
        "Multiplier": "multiplier",
        "Name": "name",
        "NcpConfReqInterval": "ncpConfReqInterval",
        "NcpConfReqMode": "ncpConfReqMode",
        "NcpConfReqRetries": "ncpConfReqRetries",
        "NcpEnableIPComp": "ncpEnableIPComp",
        "NcpIPCompProtocol": "ncpIPCompProtocol",
        "NcpRetries": "ncpRetries",
        "NcpTimeout": "ncpTimeout",
        "NcpType": "ncpType",
        "PadiRetries": "padiRetries",
        "PadiTimeout": "padiTimeout",
        "PadrRetries": "padrRetries",
        "PadrTimeout": "padrTimeout",
        "PapPassword": "papPassword",
        "PapUser": "papUser",
        "PonTypeTlv": "ponTypeTlv",
        "ProxyAuthChal": "proxyAuthChal",
        "ProxyAuthId": "proxyAuthId",
        "ProxyAuthName": "proxyAuthName",
        "ProxyAuthRes": "proxyAuthRes",
        "ProxyAuthType": "proxyAuthType",
        "RedialMax": "redialMax",
        "RedialTimeout": "redialTimeout",
        "RohcMaxCid": "rohcMaxCid",
        "RohcMrru": "rohcMrru",
        "RxConnectSpeed": "rxConnectSpeed",
        "ServiceName": "serviceName",
        "ServiceOptions": "serviceOptions",
        "SessionInfo": "sessionInfo",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "TxConnectSpeed": "txConnectSpeed",
        "UnlimitedRedialAttempts": "unlimitedRedialAttempts",
        "UserDefinedDslType": "userDefinedDslType",
        "UserDefinedPonType": "userDefinedPonType",
        "VjCompSlotId": "vjCompSlotId",
        "VjMaxSlotId": "vjMaxSlotId",
    }
    _SDM_ENUM_MAP = {
        "status": [
            "configured",
            "error",
            "mixed",
            "notStarted",
            "started",
            "starting",
            "stopping",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Pppoxclient, self).__init__(parent, list_op)

    @property
    def Bfdv4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e.Bfdv4Interface): An instance of the Bfdv4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e import (
            Bfdv4Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Bfdv4Interface", None) is not None:
                return self._properties.get("Bfdv4Interface")
        return Bfdv4Interface(self)

    @property
    def Bfdv6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface_b9a91920db1b70c8c6410d2de0b438d3.Bfdv6Interface): An instance of the Bfdv6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface_b9a91920db1b70c8c6410d2de0b438d3 import (
            Bfdv6Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Bfdv6Interface", None) is not None:
                return self._properties.get("Bfdv6Interface")
        return Bfdv6Interface(self)

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer_6f0423477064be24e0493341e399bee9.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer_6f0423477064be24e0493341e399bee9 import (
            BgpIpv4Peer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIpv4Peer", None) is not None:
                return self._properties.get("BgpIpv4Peer")
        return BgpIpv4Peer(self)

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer_8b9aa9838ebd53702954aa471913ed1e.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer_8b9aa9838ebd53702954aa471913ed1e import (
            BgpIpv6Peer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIpv6Peer", None) is not None:
                return self._properties.get("BgpIpv6Peer")
        return BgpIpv6Peer(self)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import (
            Connector,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Connector", None) is not None:
                return self._properties.get("Connector")
        return Connector(self)

    @property
    def Dhcpv6client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client_64480d87e9c578f0a0b7d3415d792d7e.Dhcpv6client): An instance of the Dhcpv6client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client_64480d87e9c578f0a0b7d3415d792d7e import (
            Dhcpv6client,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6client", None) is not None:
                return self._properties.get("Dhcpv6client")
        return Dhcpv6client(self)

    @property
    def ECpriRe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011.ECpriRe): An instance of the ECpriRe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011 import (
            ECpriRe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ECpriRe", None) is not None:
                return self._properties.get("ECpriRe")
        return ECpriRe(self)

    @property
    def ECpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255.ECpriRec): An instance of the ECpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255 import (
            ECpriRec,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ECpriRec", None) is not None:
                return self._properties.get("ECpriRec")
        return ECpriRec(self)

    @property
    def Geneve(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve_14ab6f140956b4fc77d1d0f03c5e7514.Geneve): An instance of the Geneve class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve_14ab6f140956b4fc77d1d0f03c5e7514 import (
            Geneve,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Geneve", None) is not None:
                return self._properties.get("Geneve")
        return Geneve(self)

    @property
    def IgmpHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost_8940887674c0387469423e8df3a33854.IgmpHost): An instance of the IgmpHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost_8940887674c0387469423e8df3a33854 import (
            IgmpHost,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpHost", None) is not None:
                return self._properties.get("IgmpHost")
        return IgmpHost(self)

    @property
    def IgmpQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier_38c883b0cec7ffb5405af90bf1b8cda5.IgmpQuerier): An instance of the IgmpQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier_38c883b0cec7ffb5405af90bf1b8cda5 import (
            IgmpQuerier,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpQuerier", None) is not None:
                return self._properties.get("IgmpQuerier")
        return IgmpQuerier(self)

    @property
    def MldHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost_824a1bed927138d4bb32f7d2631197a5.MldHost): An instance of the MldHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost_824a1bed927138d4bb32f7d2631197a5 import (
            MldHost,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldHost", None) is not None:
                return self._properties.get("MldHost")
        return MldHost(self)

    @property
    def MldQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier_e20671d730d138d65036e88d7cad63ac.MldQuerier): An instance of the MldQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier_e20671d730d138d65036e88d7cad63ac import (
            MldQuerier,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldQuerier", None) is not None:
                return self._properties.get("MldQuerier")
        return MldQuerier(self)

    @property
    def MplsOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam_e01bb6affe899a4731aa60619f4aeadc.MplsOam): An instance of the MplsOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam_e01bb6affe899a4731aa60619f4aeadc import (
            MplsOam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MplsOam", None) is not None:
                return self._properties.get("MplsOam")
        return MplsOam(self)

    @property
    def NetconfClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient_41816a47b6ef7550649c9682748ade71.NetconfClient): An instance of the NetconfClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient_41816a47b6ef7550649c9682748ade71 import (
            NetconfClient,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetconfClient", None) is not None:
                return self._properties.get("NetconfClient")
        return NetconfClient(self)

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver_2cdfea14e3c87592db77c4a646f1cdc1.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver_2cdfea14e3c87592db77c4a646f1cdc1 import (
            NetconfServer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetconfServer", None) is not None:
                return self._properties.get("NetconfServer")
        return NetconfServer(self)

    @property
    def Ospfv2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2_eb5737de1e17134d62e78286b93d24ac.Ospfv2): An instance of the Ospfv2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2_eb5737de1e17134d62e78286b93d24ac import (
            Ospfv2,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ospfv2", None) is not None:
                return self._properties.get("Ospfv2")
        return Ospfv2(self)

    @property
    def Ospfv3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3_3fea0f5606ed503cbf2020d4f305b6fa.Ospfv3): An instance of the Ospfv3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3_3fea0f5606ed503cbf2020d4f305b6fa import (
            Ospfv3,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ospfv3", None) is not None:
                return self._properties.get("Ospfv3")
        return Ospfv3(self)

    @property
    def Pcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc_f8f4f7c4bc41b0a9d3332c9aa5dc3ef6.Pcc): An instance of the Pcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc_f8f4f7c4bc41b0a9d3332c9aa5dc3ef6 import (
            Pcc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pcc", None) is not None:
                return self._properties.get("Pcc")
        return Pcc(self)

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce_bd5f6a11078a4f0deb5d56bef8e9674f.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce_bd5f6a11078a4f0deb5d56bef8e9674f import (
            Pce,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pce", None) is not None:
                return self._properties.get("Pce")
        return Pce(self)

    @property
    def PimV4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface_ed04aa4e4b8704acfae296adbf02aa3c.PimV4Interface): An instance of the PimV4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface_ed04aa4e4b8704acfae296adbf02aa3c import (
            PimV4Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimV4Interface", None) is not None:
                return self._properties.get("PimV4Interface")
        return PimV4Interface(self)

    @property
    def PimV6Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface_d2951dd353b66739101751a9f48226b9.PimV6Interface): An instance of the PimV6Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface_d2951dd353b66739101751a9f48226b9 import (
            PimV6Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimV6Interface", None) is not None:
                return self._properties.get("PimV6Interface")
        return PimV6Interface(self)

    @property
    def Ptprobeinstancesrv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptprobeinstancesrv6_79ffe5c7f81290d2749e262cddea5618.Ptprobeinstancesrv6): An instance of the Ptprobeinstancesrv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptprobeinstancesrv6_79ffe5c7f81290d2749e262cddea5618 import (
            Ptprobeinstancesrv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ptprobeinstancesrv6", None) is not None:
                return self._properties.get("Ptprobeinstancesrv6")
        return Ptprobeinstancesrv6(self)

    @property
    def Rocev2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rocev2_31d57573c11ba80c7909f6e453915e71.Rocev2): An instance of the Rocev2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rocev2_31d57573c11ba80c7909f6e453915e71 import (
            Rocev2,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rocev2", None) is not None:
                return self._properties.get("Rocev2")
        return Rocev2(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import (
            Tag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Tag", None) is not None:
                return self._properties.get("Tag")
        return Tag(self)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_421be1db953efaf826fe146cf9700e26.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_421be1db953efaf826fe146cf9700e26 import (
            TlvProfile,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TlvProfile", None) is not None:
                return self._properties.get("TlvProfile")
        return TlvProfile(self)

    @property
    def Vxlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan_ed3df6fe7146492fc5fe0f77f53f9473.Vxlan): An instance of the Vxlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan_ed3df6fe7146492fc5fe0f77f53f9473 import (
            Vxlan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlan", None) is not None:
                return self._properties.get("Vxlan")
        return Vxlan(self)

    @property
    def Vxlangpe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlangpe_e779e9783907b2c61304fff3bae70291.Vxlangpe): An instance of the Vxlangpe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlangpe_e779e9783907b2c61304fff3bae70291 import (
            Vxlangpe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlangpe", None) is not None:
                return self._properties.get("Vxlangpe")
        return Vxlangpe(self)

    @property
    def Vxlanv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6_c18187deccae3db44b9e9de30ad538ec.Vxlanv6): An instance of the Vxlanv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6_c18187deccae3db44b9e9de30ad538ec import (
            Vxlanv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlanv6", None) is not None:
                return self._properties.get("Vxlanv6")
        return Vxlanv6(self)

    @property
    def Vxlanv6gpe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6gpe_c816572194cd020274b16a0978c849fa.Vxlanv6gpe): An instance of the Vxlanv6gpe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6gpe_c816572194cd020274b16a0978c849fa import (
            Vxlanv6gpe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlanv6gpe", None) is not None:
                return self._properties.get("Vxlanv6gpe")
        return Vxlanv6gpe(self)

    @property
    def AcMatchMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AcMatchMac"]))

    @property
    def AcMatchName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AcMatchName"]))

    @property
    def AcOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates PPPoE AC retrieval mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AcOptions"]))

    @property
    def ActualRateDownstream(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual downstream data rate (sub-option 0x81), in kbps.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActualRateDownstream"])
        )

    @property
    def ActualRateUpstream(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual upstream data rate (sub-option 0x82), in kbps.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ActualRateUpstream"])
        )

    @property
    def AgentAccessAggregationCircuitId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Access-Aggregation-Circuit-ID-ASCII-Value field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["AgentAccessAggregationCircuitId"]),
        )

    @property
    def AgentCircuitId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Circuit ID field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AgentCircuitId"])
        )

    @property
    def AgentRemoteId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value to be inserted into the Agent Remote ID field of the PPPoX tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AgentRemoteId"]))

    @property
    def AuthRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PPP authentication retries
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AuthRetries"]))

    @property
    def AuthTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PPP authentication, in seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AuthTimeout"]))

    @property
    def AuthType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The authentication type to use during link setup.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AuthType"]))

    @property
    def CalledNum(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Calling Number AVP in ICRQ
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CalledNum"]))

    @property
    def CallingNum(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Calling Number AVP in ICRQ
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CallingNum"]))

    @property
    def ChapName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ChapName"]))

    @property
    def ChapSecret(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Secret when CHAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ChapSecret"]))

    @property
    def ClientDnsOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The client DNS options.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientDnsOptions"])
        )

    @property
    def ClientLocalIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The requested IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientLocalIp"]))

    @property
    def ClientLocalIpv6Iid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The requested IPv6 Interface Identifier (IID).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientLocalIpv6Iid"])
        )

    @property
    def ClientNcpOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The NCP configuration mode for IPv4 addressing.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientNcpOptions"])
        )

    @property
    def ClientNetmask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The netmask that the client will use with the assigned IP address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientNetmask"]))

    @property
    def ClientNetmaskOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The client netmask option.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientNetmaskOptions"])
        )

    @property
    def ClientPrimaryDnsAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the primary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary only' or 'Request Primary and Secondary'.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientPrimaryDnsAddress"])
        )

    @property
    def ClientSecondaryDnsAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the secondary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary and Secondary'.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientSecondaryDnsAddress"])
        )

    @property
    def ClientSignalIWF(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientSignalIWF"])
        )

    @property
    def ClientSignalLoopChar(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientSignalLoopChar"])
        )

    @property
    def ClientSignalLoopEncapsulation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ClientSignalLoopEncapsulation"]),
        )

    @property
    def ClientSignalLoopId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x01 , 0x02, 0x03 (Remote ID,Circuit ID and Access Aggregation Circuit ID) into the DSL tag in PADI and PADR packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientSignalLoopId"])
        )

    @property
    def ClientV6NcpOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The NCP configuration mode for IPv6 addressing.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientV6NcpOptions"])
        )

    @property
    def ClientWinsOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the mode in which WINS host addresses are configured.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientWinsOptions"])
        )

    @property
    def ClientWinsPrimaryAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the primary WINS address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientWinsPrimaryAddress"])
        )

    @property
    def ClientWinsSecondaryAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the secondary WINS address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ClientWinsSecondaryAddress"])
        )

    @property
    def CompMaxHeader(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The largest header size in octets that may be compressed.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CompMaxHeader"]))

    @property
    def CompSuboptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field contain suboptions data in hex format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CompSuboptions"])
        )

    @property
    def ConnectSpeedUpdateEnable(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, LAC will send Connect Speed Update Enable AVP in ICRQ control message
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConnectSpeedUpdateEnable"])
        )

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedVia"])

    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedVia"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def CustomAction(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Custom action to be executed as per the configuration value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CustomAction"]))

    @property
    def DataLink(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DataLink"]))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DiscoveredIpv4Addresses(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered IPv4 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredIpv4Addresses"])

    @property
    def DiscoveredIpv6Addresses(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredIpv6Addresses"])

    @property
    def DiscoveredMacs(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered remote MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredMacs"])

    @property
    def DiscoveredRemoteSessionIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Remote session ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredRemoteSessionIds"])

    @property
    def DiscoveredRemoteTunnelIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Remote tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredRemoteTunnelIds"])

    @property
    def DiscoveredSessionIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The negotiated session ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredSessionIds"])

    @property
    def DiscoveredTunnelIPs(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered remote tunnel IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredTunnelIPs"])

    @property
    def DiscoveredTunnelIds(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): The negotiated tunnel ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredTunnelIds"])

    @property
    def DomainList(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure domain group settings
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DomainList"]))

    @property
    def DslTypeTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSL Type to be advertised in PPPoE VSA Tag. For undefined DSL type user has to select User-defined DSL Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DslTypeTlv"]))

    @property
    def EchoReqInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Keep alive interval, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EchoReqInterval"])
        )

    @property
    def EnableDomainGroups(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable domain groups
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableDomainGroups"])
        )

    @property
    def EnableEchoReq(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableEchoReq"]))

    @property
    def EnableEchoRsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ?
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableEchoRsp"]))

    @property
    def EnableHostUniq(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables PPPoE Host-Uniq tag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableHostUniq"])
        )

    @property
    def EnableMaxPayload(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables PPPoE Max Payload tag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableMaxPayload"])
        )

    @property
    def EnableRedial(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, PPPoE redial is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableRedial"]))

    @property
    def Encaps1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Encaps1"]))

    @property
    def Encaps2(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A one-byte field included with sub-option 0x90.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Encaps2"]))

    @property
    def EndpointDiscNegotiation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Endpoint Discriminator Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointDiscNegotiation"])
        )

    @property
    def EndpointDiscriminatorClass(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Endpoint Discriminator for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EndpointDiscriminatorClass"])
        )

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def FcsAltOption(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FCS Alternatives Configuration Options.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcsAltOption"]))

    @property
    def HostUniq(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates Host-Uniq Tag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostUniq"]))

    @property
    def HostUniqLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host-Uniq Length, in bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HostUniqLength"])
        )

    @property
    def IphcFMaxPeriod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum interval between full headers.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IphcFMaxPeriod"])
        )

    @property
    def IphcFMaxTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum time interval between full headers.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IphcFMaxTime"]))

    @property
    def IphcNonTcpSpace(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The NON_TCP_SPACE field is two octets and indicates the maximum value of a context identifier in the space of context identifiers allocated for non-TCP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IphcNonTcpSpace"])
        )

    @property
    def IphcTcpSpace(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The TCP_SPACE field is two octets and indicates the maximum value of a context identifier in the space of context identifiers allocated for TCP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IphcTcpSpace"]))

    @property
    def LastRxLcpReq(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value configured (Hex format) in this field will be sent under AVP type 28 in ICCN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LastRxLcpReq"]))

    @property
    def LastSentLcpReq(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value configured (Hex format) in this field will be sent under AVP type 27 in ICCN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LastSentLcpReq"])
        )

    @property
    def LcpAccm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Async-Control-Character-Map
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpAccm"]))

    @property
    def LcpConfReqInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time interval between config-reject received and config-request with same local options sent in response, in seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LcpConfReqInterval"])
        )

    @property
    def LcpConfReqMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This dropdown determines the behavior of LCP Config-Request on receiving config-reject. None or Default - Default workflow. Local and Close Connection - this will allow PPPoE client/server to ignore config-reject and will send config-req with the same local options in response to config-reject till the counter configured in LCP Config-Req Retries after which the connection will close by sending PADT.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LcpConfReqMode"])
        )

    @property
    def LcpConfReqRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of config-request retries with same local options in response to config-reject after which the connection will close.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LcpConfReqRetries"])
        )

    @property
    def LcpEnableAccm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Async-Control-Character-Map
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpEnableAccm"]))

    @property
    def LcpEnableAcfc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Address and Control Field Compression (Option 8)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpEnableAcfc"]))

    @property
    def LcpEnableFcsAlternatives(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable FCS Alternatives (Option 9)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LcpEnableFcsAlternatives"])
        )

    @property
    def LcpEnablePfc(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Protocol Field Compression (Option 7)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpEnablePfc"]))

    @property
    def LcpMaxFailure(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Configure-Nak packets sent without sending a Configure-Ack before assuming that configuration is not converging. Any further Configure-Nak packets for peer requested options are converted to Configure-Reject packets
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpMaxFailure"]))

    @property
    def LcpRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of LCP retries
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpRetries"]))

    @property
    def LcpStartDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Delay time in milliseconds to wait before sending LCP Config Request packet
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpStartDelay"]))

    @property
    def LcpTermRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of LCP Termination Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LcpTermRetries"])
        )

    @property
    def LcpTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for LCP phase, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LcpTimeout"]))

    @property
    def MaxPayload(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Payload
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxPayload"]))

    @property
    def MlpppIPAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address used in the ML-PPP endpoint discriminator option of the LCP configure request sent by PPP clients
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MlpppIPAddress"])
        )

    @property
    def MlpppMACAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The MAC addresses are automatically derived from the local MAC address. An address in this class contains an IEEE 802.1 MAC address is canonical (802.3) format
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MlpppMACAddress"])
        )

    @property
    def Mrru(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Receive Reconstructed Unit for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mrru"]))

    @property
    def MrruNegotiation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MRRU Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MrruNegotiation"])
        )

    @property
    def MruNegotiation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MRU Negotiation
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MruNegotiation"])
        )

    @property
    def Mtu(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Transmit Unit for PPP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mtu"]))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NcpConfReqInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time interval between config-nak received and config-request with same local options sent in response, in seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NcpConfReqInterval"])
        )

    @property
    def NcpConfReqMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This dropdown determines the behavior of NCP Config-Request on receiving config-nak. None or Default - Default workflow. Local and Close Connection - this will allow PPPoE client/server to ignore IPCP config-nak and will send config-req with the same local options in response to config-nak till the counter configured in NCP Config-Req Retries after which the connection will close by sending termination/PADT. This option is limited to only IPCP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NcpConfReqMode"])
        )

    @property
    def NcpConfReqRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of config-request retries with same local options in response to config-nak after which the connection will close.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NcpConfReqRetries"])
        )

    @property
    def NcpEnableIPComp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IP Compression Protocol
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NcpEnableIPComp"])
        )

    @property
    def NcpIPCompProtocol(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select IP Compression Protocol
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NcpIPCompProtocol"])
        )

    @property
    def NcpRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of NCP retries
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NcpRetries"]))

    @property
    def NcpTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for NCP phase, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NcpTimeout"]))

    @property
    def NcpType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP address type (IPv4 or IPv6) for Network Control Protocol
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NcpType"]))

    @property
    def PadiRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PADI Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadiRetries"]))

    @property
    def PadiTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PADI no response, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadiTimeout"]))

    @property
    def PadrRetries(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of PADR Retries
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadrRetries"]))

    @property
    def PadrTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Timeout for PADR no response, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadrTimeout"]))

    @property
    def PapPassword(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PapPassword"]))

    @property
    def PapUser(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User name when PAP Authentication is being used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PapUser"]))

    @property
    def PonTypeTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PON Type to be advertised in PPPoE VSA Tag. For undefined PON type user has to select User-defined PON Type.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PonTypeTlv"]))

    @property
    def ProxyAuthChal(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value configured (String format) in this field will be sent under AVP type 31 in ICCN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProxyAuthChal"]))

    @property
    def ProxyAuthId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value configured (Decimal format) in this field will be sent under AVP type 32 in ICCN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProxyAuthId"]))

    @property
    def ProxyAuthName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value configured (String format) in this field will be sent under AVP type 30 in ICCN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProxyAuthName"]))

    @property
    def ProxyAuthRes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value configured (String format) in this field will be sent under AVP type 33 in ICCN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProxyAuthRes"]))

    @property
    def ProxyAuthType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Used to determine Proxy Authentication Type AVP 29 that will be sent in ICCN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ProxyAuthType"]))

    @property
    def RedialMax(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of PPPoE redials
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RedialMax"]))

    @property
    def RedialTimeout(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PPPoE redial timeout, in seconds
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RedialTimeout"]))

    @property
    def RohcMaxCid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The MAX_CID field is two octets and indicates the maximum value of a context identifier.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RohcMaxCid"]))

    @property
    def RohcMrru(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The MRRU field is two octets and indicates the maximum reconstructed reception unit for Robust Header Compression.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RohcMrru"]))

    @property
    def RxConnectSpeed(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Rx Connection Speed
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RxConnectSpeed"])
        )

    @property
    def ServiceName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Access Concentrator Service Name - this option is only available for PPP servers.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServiceName"]))

    @property
    def ServiceOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates PPPoE service retrieval mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServiceOptions"])
        )

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[cLS_CFG_REJ_AUTH | cLS_CHAP_PEER_DET_FAIL | cLS_CHAP_PEER_RESP_BAD | cLS_CODE_REJ_IPCP | cLS_CODE_REJ_IPV6CP | cLS_CODE_REJ_LCP | cLS_ERR_PPP_NO_BUF | cLS_ERR_PPP_SEND_PKT | cLS_LINK_DISABLE | cLS_LOC_IPADDR_BROADCAST | cLS_LOC_IPADDR_CLASS_E | cLS_LOC_IPADDR_INVAL_ACKS_0 | cLS_LOC_IPADDR_INVAL_ACKS_DIFF | cLS_LOC_IPADDR_LOOPBACK | cLS_LOC_IPADDR_PEER_MATCH_LOC | cLS_LOC_IPADDR_PEER_NO_GIVE | cLS_LOC_IPADDR_PEER_NO_HELP | cLS_LOC_IPADDR_PEER_NO_TAKE | cLS_LOC_IPADDR_PEER_REJ | cLS_LOOPBACK_DETECT | cLS_NO_NCP | cLS_NONE | cLS_PAP_BAD_PASSWD | cLS_PEER_DISCONNECTED | cLS_PEER_DISCONNECTED_NEGO | cLS_PEER_IPADDR_MATCH_LOC | cLS_PEER_IPADDR_PEER_NO_SET | cLS_PPOE_AC_SYSTEM_ERROR | cLS_PPOE_GENERIC_ERROR | cLS_PPP_DISABLE | cLS_PPPOE_NO_HOST_UNIQ | cLS_PPPOE_PADI_TIMEOUT | cLS_PPPOE_PADO_TIMEOUT | cLS_PPPOE_PADR_TIMEOUT | cLS_PROTO_REJ_IPCP | cLS_PROTO_REJ_IPv6CP | cLS_TIMEOUT_CHAP_CHAL | cLS_TIMEOUT_CHAP_RESP | cLS_TIMEOUT_IPCP_CFG_REQ | cLS_TIMEOUT_IPV6CP_CFG_REQ | cLS_TIMEOUT_IPV6CP_RA | cLS_TIMEOUT_LCP_CFG_REQ | cLS_TIMEOUT_LCP_ECHO_REQ | cLS_TIMEOUT_PAP_AUTH_REQ | cLS_TUN_AUTH_FAILED | cLS_TUN_NO_RESOURCES | cLS_TUN_TIMEOUT_ICRQ | cLS_TUN_TIMEOUT_SCCRQ | cLS_TUN_VENDOR_SPECIFIC_ERR]): Logs additional information about the session state
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionInfo"])

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateCounts"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @property
    def TxConnectSpeed(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tx Connection Speed
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TxConnectSpeed"])
        )

    @property
    def UnlimitedRedialAttempts(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If checked, PPPoE unlimited redial attempts is enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnlimitedRedialAttempts"])
        )

    @property
    def UserDefinedDslType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined DSL-Type Value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedDslType"])
        )

    @property
    def UserDefinedPonType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User Defined PON-Type Value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedPonType"])
        )

    @property
    def VjCompSlotId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field indicates whether the slot identifier field may be compressed. 0 The slot identifier must not be compressed. 1 The slot identifer may be compressed.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VjCompSlotId"]))

    @property
    def VjMaxSlotId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field indicates the maximum slot identifier.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VjMaxSlotId"]))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        # type: (List[str], int, str, List[str]) -> Pppoxclient
        """Updates pppoxclient resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        # type: (List[str], int, str, List[str]) -> Pppoxclient
        """Adds a new pppoxclient resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved pppoxclient resources using find and the newly added pppoxclient resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pppoxclient resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        DiscoveredIpv4Addresses=None,
        DiscoveredIpv6Addresses=None,
        DiscoveredMacs=None,
        DiscoveredRemoteSessionIds=None,
        DiscoveredRemoteTunnelIds=None,
        DiscoveredSessionIds=None,
        DiscoveredTunnelIPs=None,
        DiscoveredTunnelIds=None,
        Errors=None,
        Multiplier=None,
        Name=None,
        SessionInfo=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves pppoxclient resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pppoxclient resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pppoxclient resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DiscoveredIpv4Addresses (list(str)): The discovered IPv4 addresses.
        - DiscoveredIpv6Addresses (list(str)): The discovered IPv6 addresses.
        - DiscoveredMacs (list(str)): The discovered remote MAC address.
        - DiscoveredRemoteSessionIds (list(number)): Remote session ID.
        - DiscoveredRemoteTunnelIds (list(number)): Remote tunnel ID.
        - DiscoveredSessionIds (list(number)): The negotiated session ID.
        - DiscoveredTunnelIPs (list(str)): The discovered remote tunnel IP.
        - DiscoveredTunnelIds (list(number)): The negotiated tunnel ID.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionInfo (list(str[cLS_CFG_REJ_AUTH | cLS_CHAP_PEER_DET_FAIL | cLS_CHAP_PEER_RESP_BAD | cLS_CODE_REJ_IPCP | cLS_CODE_REJ_IPV6CP | cLS_CODE_REJ_LCP | cLS_ERR_PPP_NO_BUF | cLS_ERR_PPP_SEND_PKT | cLS_LINK_DISABLE | cLS_LOC_IPADDR_BROADCAST | cLS_LOC_IPADDR_CLASS_E | cLS_LOC_IPADDR_INVAL_ACKS_0 | cLS_LOC_IPADDR_INVAL_ACKS_DIFF | cLS_LOC_IPADDR_LOOPBACK | cLS_LOC_IPADDR_PEER_MATCH_LOC | cLS_LOC_IPADDR_PEER_NO_GIVE | cLS_LOC_IPADDR_PEER_NO_HELP | cLS_LOC_IPADDR_PEER_NO_TAKE | cLS_LOC_IPADDR_PEER_REJ | cLS_LOOPBACK_DETECT | cLS_NO_NCP | cLS_NONE | cLS_PAP_BAD_PASSWD | cLS_PEER_DISCONNECTED | cLS_PEER_DISCONNECTED_NEGO | cLS_PEER_IPADDR_MATCH_LOC | cLS_PEER_IPADDR_PEER_NO_SET | cLS_PPOE_AC_SYSTEM_ERROR | cLS_PPOE_GENERIC_ERROR | cLS_PPP_DISABLE | cLS_PPPOE_NO_HOST_UNIQ | cLS_PPPOE_PADI_TIMEOUT | cLS_PPPOE_PADO_TIMEOUT | cLS_PPPOE_PADR_TIMEOUT | cLS_PROTO_REJ_IPCP | cLS_PROTO_REJ_IPv6CP | cLS_TIMEOUT_CHAP_CHAL | cLS_TIMEOUT_CHAP_RESP | cLS_TIMEOUT_IPCP_CFG_REQ | cLS_TIMEOUT_IPV6CP_CFG_REQ | cLS_TIMEOUT_IPV6CP_RA | cLS_TIMEOUT_LCP_CFG_REQ | cLS_TIMEOUT_LCP_ECHO_REQ | cLS_TIMEOUT_PAP_AUTH_REQ | cLS_TUN_AUTH_FAILED | cLS_TUN_NO_RESOURCES | cLS_TUN_TIMEOUT_ICRQ | cLS_TUN_TIMEOUT_SCCRQ | cLS_TUN_VENDOR_SPECIFIC_ERR])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching pppoxclient resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pppoxclient data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pppoxclient resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def CloseIpcp(self, *args, **kwargs):
        """Executes the closeIpcp operation on the server.

        Close IPCP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeIpcp(async_operation=bool)list
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        closeIpcp(SessionIndices=list, async_operation=bool)list
        --------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        closeIpcp(SessionIndices=string, async_operation=bool)list
        ----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("closeIpcp", payload=payload, response_object=None)

    def CloseIpv6cp(self, *args, **kwargs):
        """Executes the closeIpv6cp operation on the server.

        Close IPv6CP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        closeIpv6cp(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        closeIpv6cp(SessionIndices=list, async_operation=bool)list
        ----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        closeIpv6cp(SessionIndices=string, async_operation=bool)list
        ------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("closeIpv6cp", payload=payload, response_object=None)

    def OpenIpcp(self, *args, **kwargs):
        """Executes the openIpcp operation on the server.

        Open IPCP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        openIpcp(async_operation=bool)list
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        openIpcp(SessionIndices=list, async_operation=bool)list
        -------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        openIpcp(SessionIndices=string, async_operation=bool)list
        ---------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("openIpcp", payload=payload, response_object=None)

    def OpenIpv6cp(self, *args, **kwargs):
        """Executes the openIpv6cp operation on the server.

        Open IPv6CP for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        openIpv6cp(async_operation=bool)list
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        openIpv6cp(SessionIndices=list, async_operation=bool)list
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        openIpv6cp(SessionIndices=string, async_operation=bool)list
        -----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("openIpv6cp", payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("restartDown", payload=payload, response_object=None)

    def SendPing(self, *args, **kwargs):
        """Executes the sendPing operation on the server.

        Send Ping IPv4 for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing(DestIp=string, async_operation=bool)list
        -------------------------------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(DestIp=string, SessionIndices=list, async_operation=bool)list
        ----------------------------------------------------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(SessionIndices=string, DestIp=string, async_operation=bool)list
        ------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a destIp of type kString
        - DestIp (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("sendPing", payload=payload, response_object=None)

    def SendPing6(self, *args, **kwargs):
        """Executes the sendPing6 operation on the server.

        Send Ping IPv6 for selected PPPoX items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing6(DestIp=string, async_operation=bool)list
        --------------------------------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing6(DestIp=string, SessionIndices=list, async_operation=bool)list
        -----------------------------------------------------------------------
        - DestIp (str): This parameter requires a destIp of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing6(SessionIndices=string, DestIp=string, async_operation=bool)list
        -------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a destIp of type kString
        - DestIp (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("sendPing6", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        AcMatchMac=None,
        AcMatchName=None,
        AcOptions=None,
        ActualRateDownstream=None,
        ActualRateUpstream=None,
        AgentAccessAggregationCircuitId=None,
        AgentCircuitId=None,
        AgentRemoteId=None,
        AuthRetries=None,
        AuthTimeout=None,
        AuthType=None,
        CalledNum=None,
        CallingNum=None,
        ChapName=None,
        ChapSecret=None,
        ClientDnsOptions=None,
        ClientLocalIp=None,
        ClientLocalIpv6Iid=None,
        ClientNcpOptions=None,
        ClientNetmask=None,
        ClientNetmaskOptions=None,
        ClientPrimaryDnsAddress=None,
        ClientSecondaryDnsAddress=None,
        ClientSignalIWF=None,
        ClientSignalLoopChar=None,
        ClientSignalLoopEncapsulation=None,
        ClientSignalLoopId=None,
        ClientV6NcpOptions=None,
        ClientWinsOptions=None,
        ClientWinsPrimaryAddress=None,
        ClientWinsSecondaryAddress=None,
        CompMaxHeader=None,
        CompSuboptions=None,
        ConnectSpeedUpdateEnable=None,
        CustomAction=None,
        DataLink=None,
        DomainList=None,
        DslTypeTlv=None,
        EchoReqInterval=None,
        EnableDomainGroups=None,
        EnableEchoReq=None,
        EnableEchoRsp=None,
        EnableHostUniq=None,
        EnableMaxPayload=None,
        EnableRedial=None,
        Encaps1=None,
        Encaps2=None,
        EndpointDiscNegotiation=None,
        EndpointDiscriminatorClass=None,
        FcsAltOption=None,
        HostUniq=None,
        HostUniqLength=None,
        IphcFMaxPeriod=None,
        IphcFMaxTime=None,
        IphcNonTcpSpace=None,
        IphcTcpSpace=None,
        LastRxLcpReq=None,
        LastSentLcpReq=None,
        LcpAccm=None,
        LcpConfReqInterval=None,
        LcpConfReqMode=None,
        LcpConfReqRetries=None,
        LcpEnableAccm=None,
        LcpEnableAcfc=None,
        LcpEnableFcsAlternatives=None,
        LcpEnablePfc=None,
        LcpMaxFailure=None,
        LcpRetries=None,
        LcpStartDelay=None,
        LcpTermRetries=None,
        LcpTimeout=None,
        MaxPayload=None,
        MlpppIPAddress=None,
        MlpppMACAddress=None,
        Mrru=None,
        MrruNegotiation=None,
        MruNegotiation=None,
        Mtu=None,
        NcpConfReqInterval=None,
        NcpConfReqMode=None,
        NcpConfReqRetries=None,
        NcpEnableIPComp=None,
        NcpIPCompProtocol=None,
        NcpRetries=None,
        NcpTimeout=None,
        NcpType=None,
        PadiRetries=None,
        PadiTimeout=None,
        PadrRetries=None,
        PadrTimeout=None,
        PapPassword=None,
        PapUser=None,
        PonTypeTlv=None,
        ProxyAuthChal=None,
        ProxyAuthId=None,
        ProxyAuthName=None,
        ProxyAuthRes=None,
        ProxyAuthType=None,
        RedialMax=None,
        RedialTimeout=None,
        RohcMaxCid=None,
        RohcMrru=None,
        RxConnectSpeed=None,
        ServiceName=None,
        ServiceOptions=None,
        TxConnectSpeed=None,
        UnlimitedRedialAttempts=None,
        UserDefinedDslType=None,
        UserDefinedPonType=None,
        VjCompSlotId=None,
        VjMaxSlotId=None,
    ):
        """Base class infrastructure that gets a list of pppoxclient device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AcMatchMac (str): optional regex of acMatchMac
        - AcMatchName (str): optional regex of acMatchName
        - AcOptions (str): optional regex of acOptions
        - ActualRateDownstream (str): optional regex of actualRateDownstream
        - ActualRateUpstream (str): optional regex of actualRateUpstream
        - AgentAccessAggregationCircuitId (str): optional regex of agentAccessAggregationCircuitId
        - AgentCircuitId (str): optional regex of agentCircuitId
        - AgentRemoteId (str): optional regex of agentRemoteId
        - AuthRetries (str): optional regex of authRetries
        - AuthTimeout (str): optional regex of authTimeout
        - AuthType (str): optional regex of authType
        - CalledNum (str): optional regex of calledNum
        - CallingNum (str): optional regex of callingNum
        - ChapName (str): optional regex of chapName
        - ChapSecret (str): optional regex of chapSecret
        - ClientDnsOptions (str): optional regex of clientDnsOptions
        - ClientLocalIp (str): optional regex of clientLocalIp
        - ClientLocalIpv6Iid (str): optional regex of clientLocalIpv6Iid
        - ClientNcpOptions (str): optional regex of clientNcpOptions
        - ClientNetmask (str): optional regex of clientNetmask
        - ClientNetmaskOptions (str): optional regex of clientNetmaskOptions
        - ClientPrimaryDnsAddress (str): optional regex of clientPrimaryDnsAddress
        - ClientSecondaryDnsAddress (str): optional regex of clientSecondaryDnsAddress
        - ClientSignalIWF (str): optional regex of clientSignalIWF
        - ClientSignalLoopChar (str): optional regex of clientSignalLoopChar
        - ClientSignalLoopEncapsulation (str): optional regex of clientSignalLoopEncapsulation
        - ClientSignalLoopId (str): optional regex of clientSignalLoopId
        - ClientV6NcpOptions (str): optional regex of clientV6NcpOptions
        - ClientWinsOptions (str): optional regex of clientWinsOptions
        - ClientWinsPrimaryAddress (str): optional regex of clientWinsPrimaryAddress
        - ClientWinsSecondaryAddress (str): optional regex of clientWinsSecondaryAddress
        - CompMaxHeader (str): optional regex of compMaxHeader
        - CompSuboptions (str): optional regex of compSuboptions
        - ConnectSpeedUpdateEnable (str): optional regex of connectSpeedUpdateEnable
        - CustomAction (str): optional regex of customAction
        - DataLink (str): optional regex of dataLink
        - DomainList (str): optional regex of domainList
        - DslTypeTlv (str): optional regex of dslTypeTlv
        - EchoReqInterval (str): optional regex of echoReqInterval
        - EnableDomainGroups (str): optional regex of enableDomainGroups
        - EnableEchoReq (str): optional regex of enableEchoReq
        - EnableEchoRsp (str): optional regex of enableEchoRsp
        - EnableHostUniq (str): optional regex of enableHostUniq
        - EnableMaxPayload (str): optional regex of enableMaxPayload
        - EnableRedial (str): optional regex of enableRedial
        - Encaps1 (str): optional regex of encaps1
        - Encaps2 (str): optional regex of encaps2
        - EndpointDiscNegotiation (str): optional regex of endpointDiscNegotiation
        - EndpointDiscriminatorClass (str): optional regex of endpointDiscriminatorClass
        - FcsAltOption (str): optional regex of fcsAltOption
        - HostUniq (str): optional regex of hostUniq
        - HostUniqLength (str): optional regex of hostUniqLength
        - IphcFMaxPeriod (str): optional regex of iphcFMaxPeriod
        - IphcFMaxTime (str): optional regex of iphcFMaxTime
        - IphcNonTcpSpace (str): optional regex of iphcNonTcpSpace
        - IphcTcpSpace (str): optional regex of iphcTcpSpace
        - LastRxLcpReq (str): optional regex of lastRxLcpReq
        - LastSentLcpReq (str): optional regex of lastSentLcpReq
        - LcpAccm (str): optional regex of lcpAccm
        - LcpConfReqInterval (str): optional regex of lcpConfReqInterval
        - LcpConfReqMode (str): optional regex of lcpConfReqMode
        - LcpConfReqRetries (str): optional regex of lcpConfReqRetries
        - LcpEnableAccm (str): optional regex of lcpEnableAccm
        - LcpEnableAcfc (str): optional regex of lcpEnableAcfc
        - LcpEnableFcsAlternatives (str): optional regex of lcpEnableFcsAlternatives
        - LcpEnablePfc (str): optional regex of lcpEnablePfc
        - LcpMaxFailure (str): optional regex of lcpMaxFailure
        - LcpRetries (str): optional regex of lcpRetries
        - LcpStartDelay (str): optional regex of lcpStartDelay
        - LcpTermRetries (str): optional regex of lcpTermRetries
        - LcpTimeout (str): optional regex of lcpTimeout
        - MaxPayload (str): optional regex of maxPayload
        - MlpppIPAddress (str): optional regex of mlpppIPAddress
        - MlpppMACAddress (str): optional regex of mlpppMACAddress
        - Mrru (str): optional regex of mrru
        - MrruNegotiation (str): optional regex of mrruNegotiation
        - MruNegotiation (str): optional regex of mruNegotiation
        - Mtu (str): optional regex of mtu
        - NcpConfReqInterval (str): optional regex of ncpConfReqInterval
        - NcpConfReqMode (str): optional regex of ncpConfReqMode
        - NcpConfReqRetries (str): optional regex of ncpConfReqRetries
        - NcpEnableIPComp (str): optional regex of ncpEnableIPComp
        - NcpIPCompProtocol (str): optional regex of ncpIPCompProtocol
        - NcpRetries (str): optional regex of ncpRetries
        - NcpTimeout (str): optional regex of ncpTimeout
        - NcpType (str): optional regex of ncpType
        - PadiRetries (str): optional regex of padiRetries
        - PadiTimeout (str): optional regex of padiTimeout
        - PadrRetries (str): optional regex of padrRetries
        - PadrTimeout (str): optional regex of padrTimeout
        - PapPassword (str): optional regex of papPassword
        - PapUser (str): optional regex of papUser
        - PonTypeTlv (str): optional regex of ponTypeTlv
        - ProxyAuthChal (str): optional regex of proxyAuthChal
        - ProxyAuthId (str): optional regex of proxyAuthId
        - ProxyAuthName (str): optional regex of proxyAuthName
        - ProxyAuthRes (str): optional regex of proxyAuthRes
        - ProxyAuthType (str): optional regex of proxyAuthType
        - RedialMax (str): optional regex of redialMax
        - RedialTimeout (str): optional regex of redialTimeout
        - RohcMaxCid (str): optional regex of rohcMaxCid
        - RohcMrru (str): optional regex of rohcMrru
        - RxConnectSpeed (str): optional regex of rxConnectSpeed
        - ServiceName (str): optional regex of serviceName
        - ServiceOptions (str): optional regex of serviceOptions
        - TxConnectSpeed (str): optional regex of txConnectSpeed
        - UnlimitedRedialAttempts (str): optional regex of unlimitedRedialAttempts
        - UserDefinedDslType (str): optional regex of userDefinedDslType
        - UserDefinedPonType (str): optional regex of userDefinedPonType
        - VjCompSlotId (str): optional regex of vjCompSlotId
        - VjMaxSlotId (str): optional regex of vjMaxSlotId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
