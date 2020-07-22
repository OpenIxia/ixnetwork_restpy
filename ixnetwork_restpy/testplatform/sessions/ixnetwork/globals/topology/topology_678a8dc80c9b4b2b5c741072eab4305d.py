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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Topology(Base):
    """Topology port level configuration
    The Topology class encapsulates a required topology resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'topology'
    _SDM_ATT_MAP = {
        'ApplyOnTheFlyState': 'applyOnTheFlyState',
        'NgpfProtocolRateMode': 'ngpfProtocolRateMode',
        'ProtocolActionsInProgress': 'protocolActionsInProgress',
        'ProtocolStackingMode': 'protocolStackingMode',
        'Status': 'status',
        'Vports': 'vports',
    }

    def __init__(self, parent):
        super(Topology, self).__init__(parent)

    @property
    def Ancp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ancp.ancp_ff7c65534887bffdbaff1aefad2051e6.Ancp): An instance of the Ancp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ancp.ancp_ff7c65534887bffdbaff1aefad2051e6 import Ancp
        return Ancp(self)._select()

    @property
    def BfdRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bfdrouter.bfdrouter_b0c139a26d47ac8a6ee154cb005bf240.BfdRouter): An instance of the BfdRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bfdrouter.bfdrouter_b0c139a26d47ac8a6ee154cb005bf240 import BfdRouter
        return BfdRouter(self)._select()

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_439a44dd340bf6fd724df996ab26569d.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_439a44dd340bf6fd724df996ab26569d import BgpIpv4Peer
        return BgpIpv4Peer(self)._select()

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_7e5e36454dedaa483fd7dd20abef422b.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_7e5e36454dedaa483fd7dd20abef422b import BgpIpv6Peer
        return BgpIpv6Peer(self)._select()

    @property
    def BondedGRE(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bondedgre.bondedgre_0a904fed3442eacc276cae46d48c1750.BondedGRE): An instance of the BondedGRE class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bondedgre.bondedgre_0a904fed3442eacc276cae46d48c1750 import BondedGRE
        return BondedGRE(self)._select()

    @property
    def CfmBridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cfmbridge.cfmbridge_9363686425d10105a01699246014d27d.CfmBridge): An instance of the CfmBridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cfmbridge.cfmbridge_9363686425d10105a01699246014d27d import CfmBridge
        return CfmBridge(self)._select()

    @property
    def Dhcpv4client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.dhcpv4client_177a83e0b1208125d8f1210a0eeccf9e.Dhcpv4client): An instance of the Dhcpv4client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.dhcpv4client_177a83e0b1208125d8f1210a0eeccf9e import Dhcpv4client
        return Dhcpv4client(self)._select()

    @property
    def Dhcpv4relayAgent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4relayagent.dhcpv4relayagent_0505d30995689ae96b30b284ac888f41.Dhcpv4relayAgent): An instance of the Dhcpv4relayAgent class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4relayagent.dhcpv4relayagent_0505d30995689ae96b30b284ac888f41 import Dhcpv4relayAgent
        return Dhcpv4relayAgent(self)._select()

    @property
    def Dhcpv4server(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4server.dhcpv4server_4e72811319e14b12cbdf5ee077d49332.Dhcpv4server): An instance of the Dhcpv4server class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4server.dhcpv4server_4e72811319e14b12cbdf5ee077d49332 import Dhcpv4server
        return Dhcpv4server(self)._select()

    @property
    def Dhcpv6client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6client.dhcpv6client_dfdae0e3c18486de2d035a82acbaf6d1.Dhcpv6client): An instance of the Dhcpv6client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6client.dhcpv6client_dfdae0e3c18486de2d035a82acbaf6d1 import Dhcpv6client
        return Dhcpv6client(self)._select()

    @property
    def Dhcpv6relayAgent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6relayagent.dhcpv6relayagent_3ce0fea2045102397de9e3f84c8cfdcd.Dhcpv6relayAgent): An instance of the Dhcpv6relayAgent class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6relayagent.dhcpv6relayagent_3ce0fea2045102397de9e3f84c8cfdcd import Dhcpv6relayAgent
        return Dhcpv6relayAgent(self)._select()

    @property
    def Dhcpv6server(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6server.dhcpv6server_5ecd1ab7ae85632367976a63d9909c05.Dhcpv6server): An instance of the Dhcpv6server class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6server.dhcpv6server_5ecd1ab7ae85632367976a63d9909c05 import Dhcpv6server
        return Dhcpv6server(self)._select()

    @property
    def DotOneX(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dotonex.dotonex_10d3ebb1f176536ccbf2a6c27585cb8b.DotOneX): An instance of the DotOneX class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dotonex.dotonex_10d3ebb1f176536ccbf2a6c27585cb8b import DotOneX
        return DotOneX(self)._select()

    @property
    def ECpriRe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprire.ecprire_9d6b48cf3a20de96e1aee98275bb8971.ECpriRe): An instance of the ECpriRe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprire.ecprire_9d6b48cf3a20de96e1aee98275bb8971 import ECpriRe
        return ECpriRe(self)._select()

    @property
    def ECpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprirec.ecprirec_80ed3cc8a41439f6adf914cf9995b127.ECpriRec): An instance of the ECpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprirec.ecprirec_80ed3cc8a41439f6adf914cf9995b127 import ECpriRec
        return ECpriRec(self)._select()

    @property
    def EcpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprirec.ecprirec_6b5325dd78ee80055b43c5d6e69df33e.EcpriRec): An instance of the EcpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprirec.ecprirec_6b5325dd78ee80055b43c5d6e69df33e import EcpriRec
        return EcpriRec(self)._select()

    @property
    def Ere(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ere.ere_789c83954739b60cea624081f35f8161.Ere): An instance of the Ere class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ere.ere_789c83954739b60cea624081f35f8161 import Ere
        return Ere(self)._select()

    @property
    def Esmc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.esmc_a6e91ae9ab0a9252a7e1dbcd069fcc86.Esmc): An instance of the Esmc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.esmc_a6e91ae9ab0a9252a7e1dbcd069fcc86 import Esmc
        return Esmc(self)._select()

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.ethernet_ccd3a65106ab16a2364be51d1a412f05.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.ethernet_ccd3a65106ab16a2364be51d1a412f05 import Ethernet
        return Ethernet(self)._select()

    @property
    def Geneve(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.geneve.geneve_a488a10a6d48e959563f1aca2792a26d.Geneve): An instance of the Geneve class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.geneve.geneve_a488a10a6d48e959563f1aca2792a26d import Geneve
        return Geneve(self)._select()

    @property
    def Greoipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.greoipv4.greoipv4_bfe88b9922d2e84deca2bbeaf25f303f.Greoipv4): An instance of the Greoipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.greoipv4.greoipv4_bfe88b9922d2e84deca2bbeaf25f303f import Greoipv4
        return Greoipv4(self)._select()

    @property
    def Greoipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.greoipv6.greoipv6_c83bf0ee8707452690be75b94867fcf9.Greoipv6): An instance of the Greoipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.greoipv6.greoipv6_c83bf0ee8707452690be75b94867fcf9 import Greoipv6
        return Greoipv6(self)._select()

    @property
    def IgmpHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.igmphost.igmphost_645f95b3e8385de64cf69a7b7e61e397.IgmpHost): An instance of the IgmpHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.igmphost.igmphost_645f95b3e8385de64cf69a7b7e61e397 import IgmpHost
        return IgmpHost(self)._select()

    @property
    def IgmpQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.igmpquerier.igmpquerier_df3eea6185ecfa4bea0ad48a29577a8d.IgmpQuerier): An instance of the IgmpQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.igmpquerier.igmpquerier_df3eea6185ecfa4bea0ad48a29577a8d import IgmpQuerier
        return IgmpQuerier(self)._select()

    @property
    def Ipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_d3982d161b434ec799d31ef7237a4b96.Ipv4): An instance of the Ipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_d3982d161b434ec799d31ef7237a4b96 import Ipv4
        return Ipv4(self)._select()

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_a9f2dfb33a5d9c10d60b9830b8455095.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_a9f2dfb33a5d9c10d60b9830b8455095 import Ipv6
        return Ipv6(self)._select()

    @property
    def Ipv6Autoconfiguration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.ipv6autoconfiguration_186fdf3eb8d47323f28ec9e4d4c3e927.Ipv6Autoconfiguration): An instance of the Ipv6Autoconfiguration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.ipv6autoconfiguration_186fdf3eb8d47323f28ec9e4d4c3e927 import Ipv6Autoconfiguration
        return Ipv6Autoconfiguration(self)._select()

    @property
    def IsisFabricPathRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisfabricpathrouter.isisfabricpathrouter_b5fd74ea8bb28a8238ccce4a47cbb980.IsisFabricPathRouter): An instance of the IsisFabricPathRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisfabricpathrouter.isisfabricpathrouter_b5fd74ea8bb28a8238ccce4a47cbb980 import IsisFabricPathRouter
        return IsisFabricPathRouter(self)

    @property
    def IsisL3Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_b5c245f4973246022b20f2613546d45a.IsisL3Router): An instance of the IsisL3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_b5c245f4973246022b20f2613546d45a import IsisL3Router
        return IsisL3Router(self)

    @property
    def IsisSpbRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisspbrouter.isisspbrouter_c88de4431424c89626da1d081531f662.IsisSpbRouter): An instance of the IsisSpbRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisspbrouter.isisspbrouter_c88de4431424c89626da1d081531f662 import IsisSpbRouter
        return IsisSpbRouter(self)._select()

    @property
    def IsisTrillRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isistrillrouter.isistrillrouter_ea0bdac1569ccf8ad0a233d5ddf6c84e.IsisTrillRouter): An instance of the IsisTrillRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isistrillrouter.isistrillrouter_ea0bdac1569ccf8ad0a233d5ddf6c84e import IsisTrillRouter
        return IsisTrillRouter(self)

    @property
    def Lac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lac.lac_8a6ae7a66f1fba21c9a7af820795ad38.Lac): An instance of the Lac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lac.lac_8a6ae7a66f1fba21c9a7af820795ad38 import Lac
        return Lac(self)._select()

    @property
    def Lacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lacp.lacp_8a53bc5dca056354ad9594ab602dbf11.Lacp): An instance of the Lacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lacp.lacp_8a53bc5dca056354ad9594ab602dbf11 import Lacp
        return Lacp(self)._select()

    @property
    def Lagportlacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportlacp.lagportlacp_7a4a0d1aa284610bc44568a967d49355.Lagportlacp): An instance of the Lagportlacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportlacp.lagportlacp_7a4a0d1aa284610bc44568a967d49355 import Lagportlacp
        return Lagportlacp(self)._select()

    @property
    def Lagportstaticlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportstaticlag.lagportstaticlag_e722ffdff0d9b2f5175aa99e8f6c6166.Lagportstaticlag): An instance of the Lagportstaticlag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportstaticlag.lagportstaticlag_e722ffdff0d9b2f5175aa99e8f6c6166 import Lagportstaticlag
        return Lagportstaticlag(self)._select()

    @property
    def LdpBasicRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldpbasicrouter.ldpbasicrouter_e9428e9f101cf2a89e54a270d4e5a5fd.LdpBasicRouter): An instance of the LdpBasicRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldpbasicrouter.ldpbasicrouter_e9428e9f101cf2a89e54a270d4e5a5fd import LdpBasicRouter
        return LdpBasicRouter(self)._select()

    @property
    def LdpBasicRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldpbasicrouterv6.ldpbasicrouterv6_1e2c5e9e2f178b1ee66235537827556e.LdpBasicRouterV6): An instance of the LdpBasicRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldpbasicrouterv6.ldpbasicrouterv6_1e2c5e9e2f178b1ee66235537827556e import LdpBasicRouterV6
        return LdpBasicRouterV6(self)._select()

    @property
    def LdpTargetedRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldptargetedrouter.ldptargetedrouter_349e833eaf6311e7d96c33c94aa3422d.LdpTargetedRouter): An instance of the LdpTargetedRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldptargetedrouter.ldptargetedrouter_349e833eaf6311e7d96c33c94aa3422d import LdpTargetedRouter
        return LdpTargetedRouter(self)._select()

    @property
    def LdpTargetedRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldptargetedrouterv6.ldptargetedrouterv6_a4eb01d937371cdb3d812b66f18e1ce9.LdpTargetedRouterV6): An instance of the LdpTargetedRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldptargetedrouterv6.ldptargetedrouterv6_a4eb01d937371cdb3d812b66f18e1ce9 import LdpTargetedRouterV6
        return LdpTargetedRouterV6(self)._select()

    @property
    def LightweightDhcpv6relayAgent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lightweightdhcpv6relayagent.lightweightdhcpv6relayagent_63fbf8e8df0af8e405e1da5d43ae1bf7.LightweightDhcpv6relayAgent): An instance of the LightweightDhcpv6relayAgent class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lightweightdhcpv6relayagent.lightweightdhcpv6relayagent_63fbf8e8df0af8e405e1da5d43ae1bf7 import LightweightDhcpv6relayAgent
        return LightweightDhcpv6relayAgent(self)._select()

    @property
    def Lns(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lns.lns_14b5a82b54457c522a1ed86b71521526.Lns): An instance of the Lns class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lns.lns_14b5a82b54457c522a1ed86b71521526 import Lns
        return Lns(self)._select()

    @property
    def Macsec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_8998c1b41f29384c2c688534cb45d85d.Macsec): An instance of the Macsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_8998c1b41f29384c2c688534cb45d85d import Macsec
        return Macsec(self)._select()

    @property
    def Mka(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_aedde1a3ca5c00a7f6b976a4fce2c20d.Mka): An instance of the Mka class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_aedde1a3ca5c00a7f6b976a4fce2c20d import Mka
        return Mka(self)._select()

    @property
    def MldHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mldhost.mldhost_a3143c5453f0fb60d35e1b3bc9c9a6c5.MldHost): An instance of the MldHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mldhost.mldhost_a3143c5453f0fb60d35e1b3bc9c9a6c5 import MldHost
        return MldHost(self)._select()

    @property
    def MldQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mldquerier.mldquerier_d640dcc1bb991ffab41b80f626f60956.MldQuerier): An instance of the MldQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mldquerier.mldquerier_d640dcc1bb991ffab41b80f626f60956 import MldQuerier
        return MldQuerier(self)._select()

    @property
    def MsrpListener(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.msrplistener.msrplistener_8dc30853f9acb06c9e848a9841108c86.MsrpListener): An instance of the MsrpListener class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.msrplistener.msrplistener_8dc30853f9acb06c9e848a9841108c86 import MsrpListener
        return MsrpListener(self)._select()

    @property
    def MsrpTalker(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.msrptalker.msrptalker_1cf2e428b92779ea5a5b07763ad23e37.MsrpTalker): An instance of the MsrpTalker class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.msrptalker.msrptalker_1cf2e428b92779ea5a5b07763ad23e37 import MsrpTalker
        return MsrpTalker(self)._select()

    @property
    def NetconfClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfclient.netconfclient_45b3879edfc7e7ac69fa5fa74e9b93ed.NetconfClient): An instance of the NetconfClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfclient.netconfclient_45b3879edfc7e7ac69fa5fa74e9b93ed import NetconfClient
        return NetconfClient(self)._select()

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfserver.netconfserver_a0a29db48af83ed4d6cc5c2febf83313.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfserver.netconfserver_a0a29db48af83ed4d6cc5c2febf83313 import NetconfServer
        return NetconfServer(self)._select()

    @property
    def Ntpclock(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ntpclock.ntpclock_3eae35d9041be46ad02835c1125fdbcc.Ntpclock): An instance of the Ntpclock class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ntpclock.ntpclock_3eae35d9041be46ad02835c1125fdbcc import Ntpclock
        return Ntpclock(self)._select()

    @property
    def OpenFlowChannel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.openflowchannel_8ec1f01f10da89a528ff9caaa6cebe92.OpenFlowChannel): An instance of the OpenFlowChannel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.openflowchannel_8ec1f01f10da89a528ff9caaa6cebe92 import OpenFlowChannel
        return OpenFlowChannel(self)._select()

    @property
    def OpenFlowController(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.openflowcontroller_e0a495604f848478428f1aea1ec3455d.OpenFlowController): An instance of the OpenFlowController class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.openflowcontroller_e0a495604f848478428f1aea1ec3455d import OpenFlowController
        return OpenFlowController(self)._select()

    @property
    def Ospfv2Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_74c05cad626e75b691d6431d3166eb2c.Ospfv2Router): An instance of the Ospfv2Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_74c05cad626e75b691d6431d3166eb2c import Ospfv2Router
        return Ospfv2Router(self)

    @property
    def Ospfv3Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_4c45a88f00fdf201bca989331894ee2f.Ospfv3Router): An instance of the Ospfv3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_4c45a88f00fdf201bca989331894ee2f import Ospfv3Router
        return Ospfv3Router(self)._select()

    @property
    def Ovsdbcontroller(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ovsdbcontroller.ovsdbcontroller_c5e1dbb109b53449b511bb3f4f1f67c3.Ovsdbcontroller): An instance of the Ovsdbcontroller class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ovsdbcontroller.ovsdbcontroller_c5e1dbb109b53449b511bb3f4f1f67c3 import Ovsdbcontroller
        return Ovsdbcontroller(self)._select()

    @property
    def Ovsdbserver(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ovsdbserver.ovsdbserver_81a9ab01d7e6a6258b63347f69239169.Ovsdbserver): An instance of the Ovsdbserver class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ovsdbserver.ovsdbserver_81a9ab01d7e6a6258b63347f69239169 import Ovsdbserver
        return Ovsdbserver(self)._select()

    @property
    def Pcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pcc.pcc_91c1343cca1ebf407382f361cdaac3e7.Pcc): An instance of the Pcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pcc.pcc_91c1343cca1ebf407382f361cdaac3e7 import Pcc
        return Pcc(self)._select()

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_5defd13c57ea406c73fd4b2cb010a30f.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_5defd13c57ea406c73fd4b2cb010a30f import Pce
        return Pce(self)._select()

    @property
    def PimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pimrouter.pimrouter_39524eebf8e4ea0724ec1feb3d8b789b.PimRouter): An instance of the PimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pimrouter.pimrouter_39524eebf8e4ea0724ec1feb3d8b789b import PimRouter
        return PimRouter(self)._select()

    @property
    def Pppoxclient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pppoxclient.pppoxclient_5dc1f66a565b5f159bb9b76e6267101c.Pppoxclient): An instance of the Pppoxclient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pppoxclient.pppoxclient_5dc1f66a565b5f159bb9b76e6267101c import Pppoxclient
        return Pppoxclient(self)._select()

    @property
    def Pppoxserver(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pppoxserver.pppoxserver_fdced8fd52e32218efb5f2597593d410.Pppoxserver): An instance of the Pppoxserver class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pppoxserver.pppoxserver_fdced8fd52e32218efb5f2597593d410 import Pppoxserver
        return Pppoxserver(self)._select()

    @property
    def Ptp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ptp.ptp_9b33e1dd881757ed391df3bdd54c280a.Ptp): An instance of the Ptp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ptp.ptp_9b33e1dd881757ed391df3bdd54c280a import Ptp
        return Ptp(self)._select()

    @property
    def RsvpteIf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rsvpteif.rsvpteif_77b8bc06c494a745387b31dc60177eee.RsvpteIf): An instance of the RsvpteIf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rsvpteif.rsvpteif_77b8bc06c494a745387b31dc60177eee import RsvpteIf
        return RsvpteIf(self)._select()

    @property
    def RsvpteLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rsvptelsps.rsvptelsps_6e179efaa8c1b35d09f6aec22096d186.RsvpteLsps): An instance of the RsvpteLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rsvptelsps.rsvptelsps_6e179efaa8c1b35d09f6aec22096d186 import RsvpteLsps
        return RsvpteLsps(self)._select()

    @property
    def StaticLag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.staticlag.staticlag_bb394020ab7d7a51040dbbf42e2f75d1.StaticLag): An instance of the StaticLag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.staticlag.staticlag_bb394020ab7d7a51040dbbf42e2f75d1 import StaticLag
        return StaticLag(self)._select()

    @property
    def StaticMacsec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.staticmacsec.staticmacsec_9ab47bdf2b3b33d22965d0aa28f2bb3d.StaticMacsec): An instance of the StaticMacsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.staticmacsec.staticmacsec_9ab47bdf2b3b33d22965d0aa28f2bb3d import StaticMacsec
        return StaticMacsec(self)._select()

    @property
    def Vxlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlan.vxlan_c36b365204d25eec87b15250f75a383e.Vxlan): An instance of the Vxlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlan.vxlan_c36b365204d25eec87b15250f75a383e import Vxlan
        return Vxlan(self)._select()

    @property
    def Vxlanv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlanv6.vxlanv6_342acd1ce35073333be5a63be5b86440.Vxlanv6): An instance of the Vxlanv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlanv6.vxlanv6_342acd1ce35073333be5a63be5b86440 import Vxlanv6
        return Vxlanv6(self)._select()

    @property
    def ApplyOnTheFlyState(self):
        """
        Returns
        -------
        - str(allowed | notAllowed | nothingToApply): Checks whether the apply changes operation is allowed
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyOnTheFlyState'])

    @property
    def NgpfProtocolRateMode(self):
        """
        Returns
        -------
        - str(basic | smooth): Decides whether protocol's sessions will started in normal or smooth mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'])
    @NgpfProtocolRateMode.setter
    def NgpfProtocolRateMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'], value)

    @property
    def ProtocolActionsInProgress(self):
        """
        Returns
        -------
        - list(str): Lists all current protocol actions in progress
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolActionsInProgress'])

    @property
    def ProtocolStackingMode(self):
        """
        Returns
        -------
        - str(parallel | sequential): Decides whether protocol's sessions will started sequentially or parallelly across the layers
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'])
    @ProtocolStackingMode.setter
    def ProtocolStackingMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'], value)

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): The current state of the scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def Vports(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport]): List of virtual ports included in the port level configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vports'])

    def update(self, NgpfProtocolRateMode=None, ProtocolStackingMode=None):
        """Updates topology resource on the server.

        Args
        ----
        - NgpfProtocolRateMode (str(basic | smooth)): Decides whether protocol's sessions will started in normal or smooth mode
        - ProtocolStackingMode (str(parallel | sequential)): Decides whether protocol's sessions will started sequentially or parallelly across the layers

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def AbortApplyOnTheFly(self):
        """Executes the abortApplyOnTheFly operation on the server.

        Aborts any on the fly changes that are outstanding

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('abortApplyOnTheFly', payload=payload, response_object=None)

    def ApplyOnTheFly(self):
        """Executes the applyOnTheFly operation on the server.

        Apply any outstanding on the fly changes

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyOnTheFly', payload=payload, response_object=None)

    def ConfigureAll(self):
        """Executes the configureAll operation on the server.

        Configures all protocols in current scenario

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('configureAll', payload=payload, response_object=None)

    def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
        """Executes the fetchAndUpdateConfigFromCloud operation on the server.

        Learn MAC / IP address for a topology running on VM ports, deployed in AWS.

        fetchAndUpdateConfigFromCloud(Mode=string)
        ------------------------------------------
        - Mode (str): Mode. Options are: cmdrefreshall, cmdrefreshmac, cmdrefreshipv4

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)
