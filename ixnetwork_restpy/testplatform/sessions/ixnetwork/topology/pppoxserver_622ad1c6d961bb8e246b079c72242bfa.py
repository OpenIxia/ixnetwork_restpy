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


class Pppoxserver(Base):
    """PPPoX Server
    The Pppoxserver class encapsulates a list of pppoxserver resources that are managed by the user.
    A list of resources can be retrieved from the server using the Pppoxserver.find() method.
    The list can be managed by using the Pppoxserver.add() and Pppoxserver.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "pppoxserver"
    _SDM_ATT_MAP = {
        "AcName": "acName",
        "AcceptAnyAuthValue": "acceptAnyAuthValue",
        "AuthRetries": "authRetries",
        "AuthTimeout": "authTimeout",
        "AuthType": "authType",
        "ClientBaseIID": "clientBaseIID",
        "ClientBaseIp": "clientBaseIp",
        "ClientIID": "clientIID",
        "ClientIIDIncr": "clientIIDIncr",
        "ClientIpIncr": "clientIpIncr",
        "CompMaxHeader": "compMaxHeader",
        "CompSuboptions": "compSuboptions",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DnsServerList": "dnsServerList",
        "EchoReqInterval": "echoReqInterval",
        "EnableDnsRa": "enableDnsRa",
        "EnableEchoReq": "enableEchoReq",
        "EnableEchoRsp": "enableEchoRsp",
        "EnableMaxPayload": "enableMaxPayload",
        "EnableRaMFlag": "enableRaMFlag",
        "EnableRaOFlag": "enableRaOFlag",
        "EndpointDiscNegotiation": "endpointDiscNegotiation",
        "EndpointDiscriminatorClass": "endpointDiscriminatorClass",
        "Errors": "errors",
        "FcsAltOption": "fcsAltOption",
        "IphcFMaxPeriod": "iphcFMaxPeriod",
        "IphcFMaxTime": "iphcFMaxTime",
        "IphcNonTcpSpace": "iphcNonTcpSpace",
        "IphcTcpSpace": "iphcTcpSpace",
        "Ipv6AddrPrefixLen": "ipv6AddrPrefixLen",
        "Ipv6PoolPrefix": "ipv6PoolPrefix",
        "Ipv6PoolPrefixLen": "ipv6PoolPrefixLen",
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
        "PppoxServerGlobalAndPortData": "pppoxServerGlobalAndPortData",
        "RohcMaxCid": "rohcMaxCid",
        "RohcMrru": "rohcMrru",
        "ServerBaseIID": "serverBaseIID",
        "ServerBaseIp": "serverBaseIp",
        "ServerDnsOptions": "serverDnsOptions",
        "ServerIID": "serverIID",
        "ServerIIDIncr": "serverIIDIncr",
        "ServerIpIncr": "serverIpIncr",
        "ServerNcpOptions": "serverNcpOptions",
        "ServerNetmask": "serverNetmask",
        "ServerNetmaskOptions": "serverNetmaskOptions",
        "ServerPrimaryDnsAddress": "serverPrimaryDnsAddress",
        "ServerSecondaryDnsAddress": "serverSecondaryDnsAddress",
        "ServerSignalDslTypeTlv": "serverSignalDslTypeTlv",
        "ServerSignalIWF": "serverSignalIWF",
        "ServerSignalLoopChar": "serverSignalLoopChar",
        "ServerSignalLoopEncapsulation": "serverSignalLoopEncapsulation",
        "ServerSignalLoopId": "serverSignalLoopId",
        "ServerSignalPonTypeTlv": "serverSignalPonTypeTlv",
        "ServerV6NcpOptions": "serverV6NcpOptions",
        "ServerWinsOptions": "serverWinsOptions",
        "ServerWinsPrimaryAddress": "serverWinsPrimaryAddress",
        "ServerWinsSecondaryAddress": "serverWinsSecondaryAddress",
        "ServiceName": "serviceName",
        "SessionStatus": "sessionStatus",
        "SessionsCount": "sessionsCount",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
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
        super(Pppoxserver, self).__init__(parent, list_op)

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
    def Dhcpv6server(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6server_df745f3926c8653c96b69175854d0c80.Dhcpv6server): An instance of the Dhcpv6server class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6server_df745f3926c8653c96b69175854d0c80 import (
            Dhcpv6server,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6server", None) is not None:
                return self._properties.get("Dhcpv6server")
        return Dhcpv6server(self)

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
    def PppoxServerSessions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserversessions_34f51eaa47353aae9b360c64589d7c32.PppoxServerSessions): An instance of the PppoxServerSessions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserversessions_34f51eaa47353aae9b360c64589d7c32 import (
            PppoxServerSessions,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoxServerSessions", None) is not None:
                return self._properties.get("PppoxServerSessions")
        return PppoxServerSessions(self)._select()

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
    def AcName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Access Concentrator Name - this option is only available for PPP servers.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AcName"]))

    @property
    def AcceptAnyAuthValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configures a PAP/CHAP authenticator to accept all offered usernames, passwords, and base domain names
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AcceptAnyAuthValue"])
        )

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
    def ClientBaseIID(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Obsolete - use clientIID instead.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientBaseIID"]))

    @property
    def ClientBaseIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The base IP address to be used when creating PPP client addresses. This property is used as an incrementor for the 'clientIpIncr' property
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientBaseIp"]))

    @property
    def ClientIID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The base IPv6CP (RFC5072) interface identifier for the PPP client. Used in conjunction with 'clientIIDIncr' as its incrementor. Valid for IPv6 only. The identifier is used in assigned global and local scope addresses created after negotiation.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientIID"]))

    @property
    def ClientIIDIncr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Client IPv6CP interface identifier increment, used in conjuction with the base identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientIIDIncr"]))

    @property
    def ClientIpIncr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The incrementor for the clientBaseIp property address when multiple PPP addresses are created.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ClientIpIncr"]))

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
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DnsServerList(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DNS server list separacted by semicolon
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DnsServerList"]))

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
    def EnableDnsRa(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable RDNSS routing advertisments
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableDnsRa"]))

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
    def EnableMaxPayload(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables PPP Max Payload tag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableMaxPayload"])
        )

    @property
    def EnableRaMFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, Managed address configuration flag will be set in Router Advertisement.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableRaMFlag"]))

    @property
    def EnableRaOFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, Other configuration flag will be set in Router Advertisement.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableRaOFlag"]))

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
    def Ipv6AddrPrefixLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Address prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6AddrPrefixLen"])
        )

    @property
    def Ipv6PoolPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Pool prefix for the IPv6 IP pool.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefix"])
        )

    @property
    def Ipv6PoolPrefixLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Pool prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6PoolPrefixLen"])
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
    def PppoxServerGlobalAndPortData(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology): Global and Port Settings
        """
        return self._get_attribute(self._SDM_ATT_MAP["PppoxServerGlobalAndPortData"])

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
    def ServerBaseIID(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Obsolete - use serverIID instead.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerBaseIID"]))

    @property
    def ServerBaseIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The base IP address to be used when create PPP server addresses. This property is used in conjunction with the 'IPv4 Server IP Increment By' property.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerBaseIp"]))

    @property
    def ServerDnsOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The server DNS options.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerDnsOptions"])
        )

    @property
    def ServerIID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The base IPv6CP (RFC5072) interface identifier for the PPP server, used in conjunction with 'serverIIDIncr' as incrementor. Valid for IPv6 only.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerIID"]))

    @property
    def ServerIIDIncr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Server IPv6CP interface identifier increment, used in conjuction with the base identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerIIDIncr"]))

    @property
    def ServerIpIncr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Server IP increment, used in conjuction with 'IPv4 Server IP' property
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerIpIncr"]))

    @property
    def ServerNcpOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the NCP configuration mode.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerNcpOptions"])
        )

    @property
    def ServerNetmask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The netmask that the server will assign to the client when the Server Netmask Options parameter is set to Supply Netmask.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerNetmask"]))

    @property
    def ServerNetmaskOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The server netmask option.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerNetmaskOptions"])
        )

    @property
    def ServerPrimaryDnsAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The primary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerPrimaryDnsAddress"])
        )

    @property
    def ServerSecondaryDnsAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The secondary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to Supply Primary and Secondary.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerSecondaryDnsAddress"])
        )

    @property
    def ServerSignalDslTypeTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSL-Type TLV to be inserted in PPPoE VSA Tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerSignalDslTypeTlv"])
        )

    @property
    def ServerSignalIWF(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADO and PADS packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerSignalIWF"])
        )

    @property
    def ServerSignalLoopChar(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADO and PADS packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerSignalLoopChar"])
        )

    @property
    def ServerSignalLoopEncapsulation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADO and PADS packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ServerSignalLoopEncapsulation"]),
        )

    @property
    def ServerSignalLoopId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This parameter enables or disables the insertion of sub-options 0x01 and 0x02 (Remote ID and Circuit ID) into the DSL tag in PADO and PADS packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerSignalLoopId"])
        )

    @property
    def ServerSignalPonTypeTlv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PON-Type TLV to be inserted in PPPoE VSA Tag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerSignalPonTypeTlv"])
        )

    @property
    def ServerV6NcpOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies the NCP configuration mode.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerV6NcpOptions"])
        )

    @property
    def ServerWinsOptions(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The WINS server discovery mode.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerWinsOptions"])
        )

    @property
    def ServerWinsPrimaryAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The primary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerWinsPrimaryAddress"])
        )

    @property
    def ServerWinsSecondaryAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The secondary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to Supply Primary and Secondary.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerWinsSecondaryAddress"])
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
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def SessionsCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of PPP clients a single server can accept (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionsCount"])

    @SessionsCount.setter
    def SessionsCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionsCount"], value)

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

    def update(
        self,
        ConnectedVia=None,
        Multiplier=None,
        Name=None,
        SessionsCount=None,
        StackedLayers=None,
    ):
        # type: (List[str], int, str, int, List[str]) -> Pppoxserver
        """Updates pppoxserver resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionsCount (number): Number of PPP clients a single server can accept (multiplier)
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        Multiplier=None,
        Name=None,
        SessionsCount=None,
        StackedLayers=None,
    ):
        # type: (List[str], int, str, int, List[str]) -> Pppoxserver
        """Adds a new pppoxserver resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionsCount (number): Number of PPP clients a single server can accept (multiplier)
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved pppoxserver resources using find and the newly added pppoxserver resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pppoxserver resources in this instance from the server.

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
        Errors=None,
        Multiplier=None,
        Name=None,
        PppoxServerGlobalAndPortData=None,
        SessionStatus=None,
        SessionsCount=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves pppoxserver resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pppoxserver resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pppoxserver resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PppoxServerGlobalAndPortData (str(None | /api/v1/sessions/1/ixnetwork/topology)): Global and Port Settings
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SessionsCount (number): Number of PPP clients a single server can accept (multiplier)
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching pppoxserver resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pppoxserver data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pppoxserver resources from the server available through an iterator or index

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
        AcName=None,
        AcceptAnyAuthValue=None,
        AuthRetries=None,
        AuthTimeout=None,
        AuthType=None,
        ClientBaseIID=None,
        ClientBaseIp=None,
        ClientIID=None,
        ClientIIDIncr=None,
        ClientIpIncr=None,
        CompMaxHeader=None,
        CompSuboptions=None,
        DnsServerList=None,
        EchoReqInterval=None,
        EnableDnsRa=None,
        EnableEchoReq=None,
        EnableEchoRsp=None,
        EnableMaxPayload=None,
        EnableRaMFlag=None,
        EnableRaOFlag=None,
        EndpointDiscNegotiation=None,
        EndpointDiscriminatorClass=None,
        FcsAltOption=None,
        IphcFMaxPeriod=None,
        IphcFMaxTime=None,
        IphcNonTcpSpace=None,
        IphcTcpSpace=None,
        Ipv6AddrPrefixLen=None,
        Ipv6PoolPrefix=None,
        Ipv6PoolPrefixLen=None,
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
        RohcMaxCid=None,
        RohcMrru=None,
        ServerBaseIID=None,
        ServerBaseIp=None,
        ServerDnsOptions=None,
        ServerIID=None,
        ServerIIDIncr=None,
        ServerIpIncr=None,
        ServerNcpOptions=None,
        ServerNetmask=None,
        ServerNetmaskOptions=None,
        ServerPrimaryDnsAddress=None,
        ServerSecondaryDnsAddress=None,
        ServerSignalDslTypeTlv=None,
        ServerSignalIWF=None,
        ServerSignalLoopChar=None,
        ServerSignalLoopEncapsulation=None,
        ServerSignalLoopId=None,
        ServerSignalPonTypeTlv=None,
        ServerV6NcpOptions=None,
        ServerWinsOptions=None,
        ServerWinsPrimaryAddress=None,
        ServerWinsSecondaryAddress=None,
        ServiceName=None,
        VjCompSlotId=None,
        VjMaxSlotId=None,
    ):
        """Base class infrastructure that gets a list of pppoxserver device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AcName (str): optional regex of acName
        - AcceptAnyAuthValue (str): optional regex of acceptAnyAuthValue
        - AuthRetries (str): optional regex of authRetries
        - AuthTimeout (str): optional regex of authTimeout
        - AuthType (str): optional regex of authType
        - ClientBaseIID (str): optional regex of clientBaseIID
        - ClientBaseIp (str): optional regex of clientBaseIp
        - ClientIID (str): optional regex of clientIID
        - ClientIIDIncr (str): optional regex of clientIIDIncr
        - ClientIpIncr (str): optional regex of clientIpIncr
        - CompMaxHeader (str): optional regex of compMaxHeader
        - CompSuboptions (str): optional regex of compSuboptions
        - DnsServerList (str): optional regex of dnsServerList
        - EchoReqInterval (str): optional regex of echoReqInterval
        - EnableDnsRa (str): optional regex of enableDnsRa
        - EnableEchoReq (str): optional regex of enableEchoReq
        - EnableEchoRsp (str): optional regex of enableEchoRsp
        - EnableMaxPayload (str): optional regex of enableMaxPayload
        - EnableRaMFlag (str): optional regex of enableRaMFlag
        - EnableRaOFlag (str): optional regex of enableRaOFlag
        - EndpointDiscNegotiation (str): optional regex of endpointDiscNegotiation
        - EndpointDiscriminatorClass (str): optional regex of endpointDiscriminatorClass
        - FcsAltOption (str): optional regex of fcsAltOption
        - IphcFMaxPeriod (str): optional regex of iphcFMaxPeriod
        - IphcFMaxTime (str): optional regex of iphcFMaxTime
        - IphcNonTcpSpace (str): optional regex of iphcNonTcpSpace
        - IphcTcpSpace (str): optional regex of iphcTcpSpace
        - Ipv6AddrPrefixLen (str): optional regex of ipv6AddrPrefixLen
        - Ipv6PoolPrefix (str): optional regex of ipv6PoolPrefix
        - Ipv6PoolPrefixLen (str): optional regex of ipv6PoolPrefixLen
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
        - RohcMaxCid (str): optional regex of rohcMaxCid
        - RohcMrru (str): optional regex of rohcMrru
        - ServerBaseIID (str): optional regex of serverBaseIID
        - ServerBaseIp (str): optional regex of serverBaseIp
        - ServerDnsOptions (str): optional regex of serverDnsOptions
        - ServerIID (str): optional regex of serverIID
        - ServerIIDIncr (str): optional regex of serverIIDIncr
        - ServerIpIncr (str): optional regex of serverIpIncr
        - ServerNcpOptions (str): optional regex of serverNcpOptions
        - ServerNetmask (str): optional regex of serverNetmask
        - ServerNetmaskOptions (str): optional regex of serverNetmaskOptions
        - ServerPrimaryDnsAddress (str): optional regex of serverPrimaryDnsAddress
        - ServerSecondaryDnsAddress (str): optional regex of serverSecondaryDnsAddress
        - ServerSignalDslTypeTlv (str): optional regex of serverSignalDslTypeTlv
        - ServerSignalIWF (str): optional regex of serverSignalIWF
        - ServerSignalLoopChar (str): optional regex of serverSignalLoopChar
        - ServerSignalLoopEncapsulation (str): optional regex of serverSignalLoopEncapsulation
        - ServerSignalLoopId (str): optional regex of serverSignalLoopId
        - ServerSignalPonTypeTlv (str): optional regex of serverSignalPonTypeTlv
        - ServerV6NcpOptions (str): optional regex of serverV6NcpOptions
        - ServerWinsOptions (str): optional regex of serverWinsOptions
        - ServerWinsPrimaryAddress (str): optional regex of serverWinsPrimaryAddress
        - ServerWinsSecondaryAddress (str): optional regex of serverWinsSecondaryAddress
        - ServiceName (str): optional regex of serviceName
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
