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
from typing import List, Any, Union


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
    _SDM_ENUM_MAP = {
        'applyOnTheFlyState': ['allowed', 'notAllowed', 'nothingToApply'],
        'ngpfProtocolRateMode': ['basic', 'smooth'],
        'protocolStackingMode': ['parallel', 'sequential'],
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(Topology, self).__init__(parent, list_op)

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
        if self._properties.get('Ancp', None) is not None:
            return self._properties.get('Ancp')
        else:
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
        if self._properties.get('BfdRouter', None) is not None:
            return self._properties.get('BfdRouter')
        else:
            return BfdRouter(self)._select()

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_3b470f091e80d297b7e766d4fb5475c2.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_3b470f091e80d297b7e766d4fb5475c2 import BgpIpv4Peer
        if self._properties.get('BgpIpv4Peer', None) is not None:
            return self._properties.get('BgpIpv4Peer')
        else:
            return BgpIpv4Peer(self)._select()

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_5867f3e4814dfe7f554ccb03bf0cc68b.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_5867f3e4814dfe7f554ccb03bf0cc68b import BgpIpv6Peer
        if self._properties.get('BgpIpv6Peer', None) is not None:
            return self._properties.get('BgpIpv6Peer')
        else:
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
        if self._properties.get('BondedGRE', None) is not None:
            return self._properties.get('BondedGRE')
        else:
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
        if self._properties.get('CfmBridge', None) is not None:
            return self._properties.get('CfmBridge')
        else:
            return CfmBridge(self)._select()

    @property
    def CuspCP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cuspcp.cuspcp_09917f677121de2d441b03efd10c0992.CuspCP): An instance of the CuspCP class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cuspcp.cuspcp_09917f677121de2d441b03efd10c0992 import CuspCP
        if self._properties.get('CuspCP', None) is not None:
            return self._properties.get('CuspCP')
        else:
            return CuspCP(self)._select()

    @property
    def CuspUP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cuspup.cuspup_985b33e540b199c473b9a9aa9d00f4c4.CuspUP): An instance of the CuspUP class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cuspup.cuspup_985b33e540b199c473b9a9aa9d00f4c4 import CuspUP
        if self._properties.get('CuspUP', None) is not None:
            return self._properties.get('CuspUP')
        else:
            return CuspUP(self)._select()

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
        if self._properties.get('Dhcpv4client', None) is not None:
            return self._properties.get('Dhcpv4client')
        else:
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
        if self._properties.get('Dhcpv4relayAgent', None) is not None:
            return self._properties.get('Dhcpv4relayAgent')
        else:
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
        if self._properties.get('Dhcpv4server', None) is not None:
            return self._properties.get('Dhcpv4server')
        else:
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
        if self._properties.get('Dhcpv6client', None) is not None:
            return self._properties.get('Dhcpv6client')
        else:
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
        if self._properties.get('Dhcpv6relayAgent', None) is not None:
            return self._properties.get('Dhcpv6relayAgent')
        else:
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
        if self._properties.get('Dhcpv6server', None) is not None:
            return self._properties.get('Dhcpv6server')
        else:
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
        if self._properties.get('DotOneX', None) is not None:
            return self._properties.get('DotOneX')
        else:
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
        if self._properties.get('ECpriRe', None) is not None:
            return self._properties.get('ECpriRe')
        else:
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
        if self._properties.get('ECpriRec', None) is not None:
            return self._properties.get('ECpriRec')
        else:
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
        if self._properties.get('EcpriRec', None) is not None:
            return self._properties.get('EcpriRec')
        else:
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
        if self._properties.get('Ere', None) is not None:
            return self._properties.get('Ere')
        else:
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
        if self._properties.get('Esmc', None) is not None:
            return self._properties.get('Esmc')
        else:
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
        if self._properties.get('Ethernet', None) is not None:
            return self._properties.get('Ethernet')
        else:
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
        if self._properties.get('Geneve', None) is not None:
            return self._properties.get('Geneve')
        else:
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
        if self._properties.get('Greoipv4', None) is not None:
            return self._properties.get('Greoipv4')
        else:
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
        if self._properties.get('Greoipv6', None) is not None:
            return self._properties.get('Greoipv6')
        else:
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
        if self._properties.get('IgmpHost', None) is not None:
            return self._properties.get('IgmpHost')
        else:
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
        if self._properties.get('IgmpQuerier', None) is not None:
            return self._properties.get('IgmpQuerier')
        else:
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
        if self._properties.get('Ipv4', None) is not None:
            return self._properties.get('Ipv4')
        else:
            return Ipv4(self)._select()

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_ef62e7d01f88eb0ac20e06be06512826.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_ef62e7d01f88eb0ac20e06be06512826 import Ipv6
        if self._properties.get('Ipv6', None) is not None:
            return self._properties.get('Ipv6')
        else:
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
        if self._properties.get('Ipv6Autoconfiguration', None) is not None:
            return self._properties.get('Ipv6Autoconfiguration')
        else:
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
        if self._properties.get('IsisFabricPathRouter', None) is not None:
            return self._properties.get('IsisFabricPathRouter')
        else:
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
        if self._properties.get('IsisL3Router', None) is not None:
            return self._properties.get('IsisL3Router')
        else:
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
        if self._properties.get('IsisSpbRouter', None) is not None:
            return self._properties.get('IsisSpbRouter')
        else:
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
        if self._properties.get('IsisTrillRouter', None) is not None:
            return self._properties.get('IsisTrillRouter')
        else:
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
        if self._properties.get('Lac', None) is not None:
            return self._properties.get('Lac')
        else:
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
        if self._properties.get('Lacp', None) is not None:
            return self._properties.get('Lacp')
        else:
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
        if self._properties.get('Lagportlacp', None) is not None:
            return self._properties.get('Lagportlacp')
        else:
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
        if self._properties.get('Lagportstaticlag', None) is not None:
            return self._properties.get('Lagportstaticlag')
        else:
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
        if self._properties.get('LdpBasicRouter', None) is not None:
            return self._properties.get('LdpBasicRouter')
        else:
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
        if self._properties.get('LdpBasicRouterV6', None) is not None:
            return self._properties.get('LdpBasicRouterV6')
        else:
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
        if self._properties.get('LdpTargetedRouter', None) is not None:
            return self._properties.get('LdpTargetedRouter')
        else:
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
        if self._properties.get('LdpTargetedRouterV6', None) is not None:
            return self._properties.get('LdpTargetedRouterV6')
        else:
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
        if self._properties.get('LightweightDhcpv6relayAgent', None) is not None:
            return self._properties.get('LightweightDhcpv6relayAgent')
        else:
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
        if self._properties.get('Lns', None) is not None:
            return self._properties.get('Lns')
        else:
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
        if self._properties.get('Macsec', None) is not None:
            return self._properties.get('Macsec')
        else:
            return Macsec(self)._select()

    @property
    def Mka(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_fbbb6ecec94d2879b1165a3f7b0747e7.Mka): An instance of the Mka class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_fbbb6ecec94d2879b1165a3f7b0747e7 import Mka
        if self._properties.get('Mka', None) is not None:
            return self._properties.get('Mka')
        else:
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
        if self._properties.get('MldHost', None) is not None:
            return self._properties.get('MldHost')
        else:
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
        if self._properties.get('MldQuerier', None) is not None:
            return self._properties.get('MldQuerier')
        else:
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
        if self._properties.get('MsrpListener', None) is not None:
            return self._properties.get('MsrpListener')
        else:
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
        if self._properties.get('MsrpTalker', None) is not None:
            return self._properties.get('MsrpTalker')
        else:
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
        if self._properties.get('NetconfClient', None) is not None:
            return self._properties.get('NetconfClient')
        else:
            return NetconfClient(self)._select()

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfserver.netconfserver_12bf8eb804c05df100b307134c571553.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfserver.netconfserver_12bf8eb804c05df100b307134c571553 import NetconfServer
        if self._properties.get('NetconfServer', None) is not None:
            return self._properties.get('NetconfServer')
        else:
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
        if self._properties.get('Ntpclock', None) is not None:
            return self._properties.get('Ntpclock')
        else:
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
        if self._properties.get('OpenFlowChannel', None) is not None:
            return self._properties.get('OpenFlowChannel')
        else:
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
        if self._properties.get('OpenFlowController', None) is not None:
            return self._properties.get('OpenFlowController')
        else:
            return OpenFlowController(self)._select()

    @property
    def Ospfv2Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_fc60e2637a549cc6f1633d0088abb4ee.Ospfv2Router): An instance of the Ospfv2Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_fc60e2637a549cc6f1633d0088abb4ee import Ospfv2Router
        if self._properties.get('Ospfv2Router', None) is not None:
            return self._properties.get('Ospfv2Router')
        else:
            return Ospfv2Router(self)

    @property
    def Ospfv3Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_7372ae367ac5a1ebf0505ed8fc886eb8.Ospfv3Router): An instance of the Ospfv3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_7372ae367ac5a1ebf0505ed8fc886eb8 import Ospfv3Router
        if self._properties.get('Ospfv3Router', None) is not None:
            return self._properties.get('Ospfv3Router')
        else:
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
        if self._properties.get('Ovsdbcontroller', None) is not None:
            return self._properties.get('Ovsdbcontroller')
        else:
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
        if self._properties.get('Ovsdbserver', None) is not None:
            return self._properties.get('Ovsdbserver')
        else:
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
        if self._properties.get('Pcc', None) is not None:
            return self._properties.get('Pcc')
        else:
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
        if self._properties.get('Pce', None) is not None:
            return self._properties.get('Pce')
        else:
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
        if self._properties.get('PimRouter', None) is not None:
            return self._properties.get('PimRouter')
        else:
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
        if self._properties.get('Pppoxclient', None) is not None:
            return self._properties.get('Pppoxclient')
        else:
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
        if self._properties.get('Pppoxserver', None) is not None:
            return self._properties.get('Pppoxserver')
        else:
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
        if self._properties.get('Ptp', None) is not None:
            return self._properties.get('Ptp')
        else:
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
        if self._properties.get('RsvpteIf', None) is not None:
            return self._properties.get('RsvpteIf')
        else:
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
        if self._properties.get('RsvpteLsps', None) is not None:
            return self._properties.get('RsvpteLsps')
        else:
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
        if self._properties.get('StaticLag', None) is not None:
            return self._properties.get('StaticLag')
        else:
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
        if self._properties.get('StaticMacsec', None) is not None:
            return self._properties.get('StaticMacsec')
        else:
            return StaticMacsec(self)._select()

    @property
    def UpGroupInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.upgroupinfo.upgroupinfo_00481e5137e600e738b95cd9c44d367d.UpGroupInfo): An instance of the UpGroupInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.upgroupinfo.upgroupinfo_00481e5137e600e738b95cd9c44d367d import UpGroupInfo
        if self._properties.get('UpGroupInfo', None) is not None:
            return self._properties.get('UpGroupInfo')
        else:
            return UpGroupInfo(self)._select()

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
        if self._properties.get('Vxlan', None) is not None:
            return self._properties.get('Vxlan')
        else:
            return Vxlan(self)._select()

    @property
    def Vxlangpe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlangpe.vxlangpe_d9ba5236670dd27404d1b6b64c942474.Vxlangpe): An instance of the Vxlangpe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlangpe.vxlangpe_d9ba5236670dd27404d1b6b64c942474 import Vxlangpe
        if self._properties.get('Vxlangpe', None) is not None:
            return self._properties.get('Vxlangpe')
        else:
            return Vxlangpe(self)._select()

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
        if self._properties.get('Vxlanv6', None) is not None:
            return self._properties.get('Vxlanv6')
        else:
            return Vxlanv6(self)._select()

    @property
    def Vxlanv6gpe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlanv6gpe.vxlanv6gpe_498d3159ba5a05647434f2adcc138c80.Vxlanv6gpe): An instance of the Vxlanv6gpe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlanv6gpe.vxlanv6gpe_498d3159ba5a05647434f2adcc138c80 import Vxlanv6gpe
        if self._properties.get('Vxlanv6gpe', None) is not None:
            return self._properties.get('Vxlanv6gpe')
        else:
            return Vxlanv6gpe(self)._select()

    @property
    def ApplyOnTheFlyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allowed | notAllowed | nothingToApply): Checks whether the apply changes operation is allowed
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyOnTheFlyState'])

    @property
    def NgpfProtocolRateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(basic | smooth): Decides whether protocol's sessions will started in normal or smooth mode
        """
        return self._get_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'])
    @NgpfProtocolRateMode.setter
    def NgpfProtocolRateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['NgpfProtocolRateMode'], value)

    @property
    def ProtocolActionsInProgress(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Lists all current protocol actions in progress
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolActionsInProgress'])

    @property
    def ProtocolStackingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(parallel | sequential): Decides whether protocol's sessions will started sequentially or parallelly across the layers
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'])
    @ProtocolStackingMode.setter
    def ProtocolStackingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ProtocolStackingMode'], value)

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): The current state of the scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def Vports(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport]): List of virtual ports included in the port level configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vports'])

    def update(self, NgpfProtocolRateMode=None, ProtocolStackingMode=None):
        # type: (str, str) -> Topology
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

    def AbortApplyOnTheFly(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abortApplyOnTheFly operation on the server.

        Aborts any on the fly changes that are outstanding

        abortApplyOnTheFly(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abortApplyOnTheFly', payload=payload, response_object=None)

    def ApplyOnTheFly(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the applyOnTheFly operation on the server.

        Apply any outstanding on the fly changes

        applyOnTheFly(async_operation=bool)string
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Details about the operation's state.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('applyOnTheFly', payload=payload, response_object=None)

    def ConfigureAll(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the configureAll operation on the server.

        Configures all protocols in current scenario

        configureAll(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('configureAll', payload=payload, response_object=None)

    def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the fetchAndUpdateConfigFromCloud operation on the server.

        Learn MAC / IP address for a topology running on VM ports, deployed in AWS.

        fetchAndUpdateConfigFromCloud(Mode=string, async_operation=bool)
        ----------------------------------------------------------------
        - Mode (str): Mode. Options are: cmdrefreshall, cmdrefreshmac, cmdrefreshipv4
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)
