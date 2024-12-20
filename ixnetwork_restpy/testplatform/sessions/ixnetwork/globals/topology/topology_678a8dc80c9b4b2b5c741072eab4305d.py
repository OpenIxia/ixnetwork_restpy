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


class Topology(Base):
    """Topology port level configuration
    The Topology class encapsulates a required topology resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "topology"
    _SDM_ATT_MAP = {
        "ApplyOnTheFlyState": "applyOnTheFlyState",
        "NgpfProtocolRateMode": "ngpfProtocolRateMode",
        "ProtocolActionsInProgress": "protocolActionsInProgress",
        "ProtocolStackingMode": "protocolStackingMode",
        "Status": "status",
        "Vports": "vports",
    }
    _SDM_ENUM_MAP = {
        "applyOnTheFlyState": ["allowed", "notAllowed", "nothingToApply"],
        "ngpfProtocolRateMode": ["basic", "smooth"],
        "protocolStackingMode": ["parallel", "sequential"],
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ancp.ancp_ff7c65534887bffdbaff1aefad2051e6 import (
            Ancp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ancp", None) is not None:
                return self._properties.get("Ancp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bfdrouter.bfdrouter_b0c139a26d47ac8a6ee154cb005bf240 import (
            BfdRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BfdRouter", None) is not None:
                return self._properties.get("BfdRouter")
        return BfdRouter(self)._select()

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_df91734757c6c41add55223a2e168060.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv4peer.bgpipv4peer_df91734757c6c41add55223a2e168060 import (
            BgpIpv4Peer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIpv4Peer", None) is not None:
                return self._properties.get("BgpIpv4Peer")
        return BgpIpv4Peer(self)._select()

    @property
    def BgpIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_72282fe6d1d67beba231ba2980997352.BgpIpv6Peer): An instance of the BgpIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bgpipv6peer.bgpipv6peer_72282fe6d1d67beba231ba2980997352 import (
            BgpIpv6Peer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpIpv6Peer", None) is not None:
                return self._properties.get("BgpIpv6Peer")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.bondedgre.bondedgre_0a904fed3442eacc276cae46d48c1750 import (
            BondedGRE,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BondedGRE", None) is not None:
                return self._properties.get("BondedGRE")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cfmbridge.cfmbridge_9363686425d10105a01699246014d27d import (
            CfmBridge,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CfmBridge", None) is not None:
                return self._properties.get("CfmBridge")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cuspcp.cuspcp_09917f677121de2d441b03efd10c0992 import (
            CuspCP,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CuspCP", None) is not None:
                return self._properties.get("CuspCP")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.cuspup.cuspup_985b33e540b199c473b9a9aa9d00f4c4 import (
            CuspUP,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CuspUP", None) is not None:
                return self._properties.get("CuspUP")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.dhcpv4client_177a83e0b1208125d8f1210a0eeccf9e import (
            Dhcpv4client,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv4client", None) is not None:
                return self._properties.get("Dhcpv4client")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4relayagent.dhcpv4relayagent_0505d30995689ae96b30b284ac888f41 import (
            Dhcpv4relayAgent,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv4relayAgent", None) is not None:
                return self._properties.get("Dhcpv4relayAgent")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4server.dhcpv4server_4e72811319e14b12cbdf5ee077d49332 import (
            Dhcpv4server,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv4server", None) is not None:
                return self._properties.get("Dhcpv4server")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6client.dhcpv6client_dfdae0e3c18486de2d035a82acbaf6d1 import (
            Dhcpv6client,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6client", None) is not None:
                return self._properties.get("Dhcpv6client")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6relayagent.dhcpv6relayagent_3ce0fea2045102397de9e3f84c8cfdcd import (
            Dhcpv6relayAgent,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6relayAgent", None) is not None:
                return self._properties.get("Dhcpv6relayAgent")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv6server.dhcpv6server_5ecd1ab7ae85632367976a63d9909c05 import (
            Dhcpv6server,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6server", None) is not None:
                return self._properties.get("Dhcpv6server")
        return Dhcpv6server(self)._select()

    @property
    def DotOneX(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dotonex.dotonex_0022a5422a7b5d939bb7a351340e1963.DotOneX): An instance of the DotOneX class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dotonex.dotonex_0022a5422a7b5d939bb7a351340e1963 import (
            DotOneX,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DotOneX", None) is not None:
                return self._properties.get("DotOneX")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprire.ecprire_9d6b48cf3a20de96e1aee98275bb8971 import (
            ECpriRe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ECpriRe", None) is not None:
                return self._properties.get("ECpriRe")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprirec.ecprirec_80ed3cc8a41439f6adf914cf9995b127 import (
            ECpriRec,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ECpriRec", None) is not None:
                return self._properties.get("ECpriRec")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ecprirec.ecprirec_6b5325dd78ee80055b43c5d6e69df33e import (
            EcpriRec,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EcpriRec", None) is not None:
                return self._properties.get("EcpriRec")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ere.ere_789c83954739b60cea624081f35f8161 import (
            Ere,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ere", None) is not None:
                return self._properties.get("Ere")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.esmc.esmc_a6e91ae9ab0a9252a7e1dbcd069fcc86 import (
            Esmc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Esmc", None) is not None:
                return self._properties.get("Esmc")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.ethernet_ccd3a65106ab16a2364be51d1a412f05 import (
            Ethernet,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ethernet", None) is not None:
                return self._properties.get("Ethernet")
        return Ethernet(self)._select()

    @property
    def GRIBIClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.gribiclient.gribiclient_3cd2070ad07638a9370aa9054bc38516.GRIBIClient): An instance of the GRIBIClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.gribiclient.gribiclient_3cd2070ad07638a9370aa9054bc38516 import (
            GRIBIClient,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GRIBIClient", None) is not None:
                return self._properties.get("GRIBIClient")
        return GRIBIClient(self)._select()

    @property
    def GRPCClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.grpcclient.grpcclient_6743ae6e031e52a1629f0930a672ebc9.GRPCClient): An instance of the GRPCClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.grpcclient.grpcclient_6743ae6e031e52a1629f0930a672ebc9 import (
            GRPCClient,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GRPCClient", None) is not None:
                return self._properties.get("GRPCClient")
        return GRPCClient(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.geneve.geneve_a488a10a6d48e959563f1aca2792a26d import (
            Geneve,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Geneve", None) is not None:
                return self._properties.get("Geneve")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.greoipv4.greoipv4_bfe88b9922d2e84deca2bbeaf25f303f import (
            Greoipv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Greoipv4", None) is not None:
                return self._properties.get("Greoipv4")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.greoipv6.greoipv6_c83bf0ee8707452690be75b94867fcf9 import (
            Greoipv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Greoipv6", None) is not None:
                return self._properties.get("Greoipv6")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.igmphost.igmphost_645f95b3e8385de64cf69a7b7e61e397 import (
            IgmpHost,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpHost", None) is not None:
                return self._properties.get("IgmpHost")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.igmpquerier.igmpquerier_df3eea6185ecfa4bea0ad48a29577a8d import (
            IgmpQuerier,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpQuerier", None) is not None:
                return self._properties.get("IgmpQuerier")
        return IgmpQuerier(self)._select()

    @property
    def Ipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_9f2d3c4082b38a75137161eceb450ab1.Ipv4): An instance of the Ipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.ipv4_9f2d3c4082b38a75137161eceb450ab1 import (
            Ipv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4", None) is not None:
                return self._properties.get("Ipv4")
        return Ipv4(self)._select()

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_ab6c81b5b300b4621ca50e4da7d5db2a.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6.ipv6_ab6c81b5b300b4621ca50e4da7d5db2a import (
            Ipv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6", None) is not None:
                return self._properties.get("Ipv6")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv6autoconfiguration.ipv6autoconfiguration_186fdf3eb8d47323f28ec9e4d4c3e927 import (
            Ipv6Autoconfiguration,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Autoconfiguration", None) is not None:
                return self._properties.get("Ipv6Autoconfiguration")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisfabricpathrouter.isisfabricpathrouter_b5fd74ea8bb28a8238ccce4a47cbb980 import (
            IsisFabricPathRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisFabricPathRouter", None) is not None:
                return self._properties.get("IsisFabricPathRouter")
        return IsisFabricPathRouter(self)

    @property
    def IsisL3Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_9768fe1f600aea196e895480f3c204d6.IsisL3Router): An instance of the IsisL3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisl3router.isisl3router_9768fe1f600aea196e895480f3c204d6 import (
            IsisL3Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisL3Router", None) is not None:
                return self._properties.get("IsisL3Router")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isisspbrouter.isisspbrouter_c88de4431424c89626da1d081531f662 import (
            IsisSpbRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSpbRouter", None) is not None:
                return self._properties.get("IsisSpbRouter")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.isistrillrouter.isistrillrouter_ea0bdac1569ccf8ad0a233d5ddf6c84e import (
            IsisTrillRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisTrillRouter", None) is not None:
                return self._properties.get("IsisTrillRouter")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lac.lac_8a6ae7a66f1fba21c9a7af820795ad38 import (
            Lac,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lac", None) is not None:
                return self._properties.get("Lac")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lacp.lacp_8a53bc5dca056354ad9594ab602dbf11 import (
            Lacp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lacp", None) is not None:
                return self._properties.get("Lacp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportlacp.lagportlacp_7a4a0d1aa284610bc44568a967d49355 import (
            Lagportlacp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lagportlacp", None) is not None:
                return self._properties.get("Lagportlacp")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lagportstaticlag.lagportstaticlag_e722ffdff0d9b2f5175aa99e8f6c6166 import (
            Lagportstaticlag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lagportstaticlag", None) is not None:
                return self._properties.get("Lagportstaticlag")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldpbasicrouter.ldpbasicrouter_e9428e9f101cf2a89e54a270d4e5a5fd import (
            LdpBasicRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpBasicRouter", None) is not None:
                return self._properties.get("LdpBasicRouter")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldpbasicrouterv6.ldpbasicrouterv6_1e2c5e9e2f178b1ee66235537827556e import (
            LdpBasicRouterV6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpBasicRouterV6", None) is not None:
                return self._properties.get("LdpBasicRouterV6")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldptargetedrouter.ldptargetedrouter_349e833eaf6311e7d96c33c94aa3422d import (
            LdpTargetedRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpTargetedRouter", None) is not None:
                return self._properties.get("LdpTargetedRouter")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ldptargetedrouterv6.ldptargetedrouterv6_a4eb01d937371cdb3d812b66f18e1ce9 import (
            LdpTargetedRouterV6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpTargetedRouterV6", None) is not None:
                return self._properties.get("LdpTargetedRouterV6")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lightweightdhcpv6relayagent.lightweightdhcpv6relayagent_63fbf8e8df0af8e405e1da5d43ae1bf7 import (
            LightweightDhcpv6relayAgent,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LightweightDhcpv6relayAgent", None) is not None:
                return self._properties.get("LightweightDhcpv6relayAgent")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.lns.lns_14b5a82b54457c522a1ed86b71521526 import (
            Lns,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lns", None) is not None:
                return self._properties.get("Lns")
        return Lns(self)._select()

    @property
    def Macsec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_b93abc2847815d89651f09c37d6efa2f.Macsec): An instance of the Macsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.macsec.macsec_b93abc2847815d89651f09c37d6efa2f import (
            Macsec,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Macsec", None) is not None:
                return self._properties.get("Macsec")
        return Macsec(self)._select()

    @property
    def Mka(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_290c0bc15e05e906e69ccccc0fe53e72.Mka): An instance of the Mka class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mka.mka_290c0bc15e05e906e69ccccc0fe53e72 import (
            Mka,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Mka", None) is not None:
                return self._properties.get("Mka")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mldhost.mldhost_a3143c5453f0fb60d35e1b3bc9c9a6c5 import (
            MldHost,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldHost", None) is not None:
                return self._properties.get("MldHost")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.mldquerier.mldquerier_d640dcc1bb991ffab41b80f626f60956 import (
            MldQuerier,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldQuerier", None) is not None:
                return self._properties.get("MldQuerier")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.msrplistener.msrplistener_8dc30853f9acb06c9e848a9841108c86 import (
            MsrpListener,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MsrpListener", None) is not None:
                return self._properties.get("MsrpListener")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.msrptalker.msrptalker_1cf2e428b92779ea5a5b07763ad23e37 import (
            MsrpTalker,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MsrpTalker", None) is not None:
                return self._properties.get("MsrpTalker")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfclient.netconfclient_45b3879edfc7e7ac69fa5fa74e9b93ed import (
            NetconfClient,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetconfClient", None) is not None:
                return self._properties.get("NetconfClient")
        return NetconfClient(self)._select()

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfserver.netconfserver_cdfdf0a2ca5fc25352bc3bb0b147bbfc.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.netconfserver.netconfserver_cdfdf0a2ca5fc25352bc3bb0b147bbfc import (
            NetconfServer,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetconfServer", None) is not None:
                return self._properties.get("NetconfServer")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ntpclock.ntpclock_3eae35d9041be46ad02835c1125fdbcc import (
            Ntpclock,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ntpclock", None) is not None:
                return self._properties.get("Ntpclock")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowchannel.openflowchannel_8ec1f01f10da89a528ff9caaa6cebe92 import (
            OpenFlowChannel,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenFlowChannel", None) is not None:
                return self._properties.get("OpenFlowChannel")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.openflowcontroller_e0a495604f848478428f1aea1ec3455d import (
            OpenFlowController,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenFlowController", None) is not None:
                return self._properties.get("OpenFlowController")
        return OpenFlowController(self)._select()

    @property
    def Ospfv2Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_269014fa4008b7e81a251725fc2ca6bf.Ospfv2Router): An instance of the Ospfv2Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv2router.ospfv2router_269014fa4008b7e81a251725fc2ca6bf import (
            Ospfv2Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ospfv2Router", None) is not None:
                return self._properties.get("Ospfv2Router")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ospfv3router.ospfv3router_7372ae367ac5a1ebf0505ed8fc886eb8 import (
            Ospfv3Router,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ospfv3Router", None) is not None:
                return self._properties.get("Ospfv3Router")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ovsdbcontroller.ovsdbcontroller_c5e1dbb109b53449b511bb3f4f1f67c3 import (
            Ovsdbcontroller,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ovsdbcontroller", None) is not None:
                return self._properties.get("Ovsdbcontroller")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ovsdbserver.ovsdbserver_81a9ab01d7e6a6258b63347f69239169 import (
            Ovsdbserver,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ovsdbserver", None) is not None:
                return self._properties.get("Ovsdbserver")
        return Ovsdbserver(self)._select()

    @property
    def Pcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pcc.pcc_b9da1d5a5cf31906067f29bdfc78e860.Pcc): An instance of the Pcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pcc.pcc_b9da1d5a5cf31906067f29bdfc78e860 import (
            Pcc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pcc", None) is not None:
                return self._properties.get("Pcc")
        return Pcc(self)._select()

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_01d903d1ebbc310362aec8b4e7dc8176.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pce.pce_01d903d1ebbc310362aec8b4e7dc8176 import (
            Pce,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pce", None) is not None:
                return self._properties.get("Pce")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pimrouter.pimrouter_39524eebf8e4ea0724ec1feb3d8b789b import (
            PimRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimRouter", None) is not None:
                return self._properties.get("PimRouter")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pppoxclient.pppoxclient_5dc1f66a565b5f159bb9b76e6267101c import (
            Pppoxclient,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pppoxclient", None) is not None:
                return self._properties.get("Pppoxclient")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.pppoxserver.pppoxserver_fdced8fd52e32218efb5f2597593d410 import (
            Pppoxserver,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pppoxserver", None) is not None:
                return self._properties.get("Pppoxserver")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ptp.ptp_9b33e1dd881757ed391df3bdd54c280a import (
            Ptp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ptp", None) is not None:
                return self._properties.get("Ptp")
        return Ptp(self)._select()

    @property
    def Ptprobeinstancesrv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ptprobeinstancesrv6.ptprobeinstancesrv6_42465f189e48f32cc2859230c2df9e11.Ptprobeinstancesrv6): An instance of the Ptprobeinstancesrv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ptprobeinstancesrv6.ptprobeinstancesrv6_42465f189e48f32cc2859230c2df9e11 import (
            Ptprobeinstancesrv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ptprobeinstancesrv6", None) is not None:
                return self._properties.get("Ptprobeinstancesrv6")
        return Ptprobeinstancesrv6(self)._select()

    @property
    def Roce6v2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.roce6v2.roce6v2_c10c727ab6238f40d0d75af5804e65fd.Roce6v2): An instance of the Roce6v2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.roce6v2.roce6v2_c10c727ab6238f40d0d75af5804e65fd import (
            Roce6v2,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Roce6v2", None) is not None:
                return self._properties.get("Roce6v2")
        return Roce6v2(self)._select()

    @property
    def Rocev2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rocev2.rocev2_16221c79cb9987f68933e5578c282eb6.Rocev2): An instance of the Rocev2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rocev2.rocev2_16221c79cb9987f68933e5578c282eb6 import (
            Rocev2,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Rocev2", None) is not None:
                return self._properties.get("Rocev2")
        return Rocev2(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rsvpteif.rsvpteif_77b8bc06c494a745387b31dc60177eee import (
            RsvpteIf,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpteIf", None) is not None:
                return self._properties.get("RsvpteIf")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.rsvptelsps.rsvptelsps_6e179efaa8c1b35d09f6aec22096d186 import (
            RsvpteLsps,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpteLsps", None) is not None:
                return self._properties.get("RsvpteLsps")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.staticlag.staticlag_bb394020ab7d7a51040dbbf42e2f75d1 import (
            StaticLag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StaticLag", None) is not None:
                return self._properties.get("StaticLag")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.staticmacsec.staticmacsec_9ab47bdf2b3b33d22965d0aa28f2bb3d import (
            StaticMacsec,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StaticMacsec", None) is not None:
                return self._properties.get("StaticMacsec")
        return StaticMacsec(self)._select()

    @property
    def TwampIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.twampipv4.twampipv4_83456029c1debac8b6bdcdd43fd80f00.TwampIpv4): An instance of the TwampIpv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.twampipv4.twampipv4_83456029c1debac8b6bdcdd43fd80f00 import (
            TwampIpv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TwampIpv4", None) is not None:
                return self._properties.get("TwampIpv4")
        return TwampIpv4(self)._select()

    @property
    def TwampIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.twampipv6.twampipv6_38ebcf9adafea940a522a0879aa08fb0.TwampIpv6): An instance of the TwampIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.twampipv6.twampipv6_38ebcf9adafea940a522a0879aa08fb0 import (
            TwampIpv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TwampIpv6", None) is not None:
                return self._properties.get("TwampIpv6")
        return TwampIpv6(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.upgroupinfo.upgroupinfo_00481e5137e600e738b95cd9c44d367d import (
            UpGroupInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UpGroupInfo", None) is not None:
                return self._properties.get("UpGroupInfo")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlan.vxlan_c36b365204d25eec87b15250f75a383e import (
            Vxlan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlan", None) is not None:
                return self._properties.get("Vxlan")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlangpe.vxlangpe_d9ba5236670dd27404d1b6b64c942474 import (
            Vxlangpe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlangpe", None) is not None:
                return self._properties.get("Vxlangpe")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlanv6.vxlanv6_342acd1ce35073333be5a63be5b86440 import (
            Vxlanv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlanv6", None) is not None:
                return self._properties.get("Vxlanv6")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.vxlanv6gpe.vxlanv6gpe_498d3159ba5a05647434f2adcc138c80 import (
            Vxlanv6gpe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Vxlanv6gpe", None) is not None:
                return self._properties.get("Vxlanv6gpe")
        return Vxlanv6gpe(self)._select()

    @property
    def ApplyOnTheFlyState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allowed | notAllowed | nothingToApply): Checks whether the apply changes operation is allowed
        """
        return self._get_attribute(self._SDM_ATT_MAP["ApplyOnTheFlyState"])

    @property
    def NgpfProtocolRateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(basic | smooth): Decides whether protocol's sessions will started in normal or smooth mode
        """
        return self._get_attribute(self._SDM_ATT_MAP["NgpfProtocolRateMode"])

    @NgpfProtocolRateMode.setter
    def NgpfProtocolRateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["NgpfProtocolRateMode"], value)

    @property
    def ProtocolActionsInProgress(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Lists all current protocol actions in progress
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolActionsInProgress"])

    @property
    def ProtocolStackingMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(parallel | sequential): Decides whether protocol's sessions will started sequentially or parallelly across the layers
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolStackingMode"])

    @ProtocolStackingMode.setter
    def ProtocolStackingMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolStackingMode"], value)

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): The current state of the scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @property
    def Vports(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport]): List of virtual ports included in the port level configuration
        """
        return self._get_attribute(self._SDM_ATT_MAP["Vports"])

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

    def find(
        self,
        ApplyOnTheFlyState=None,
        NgpfProtocolRateMode=None,
        ProtocolActionsInProgress=None,
        ProtocolStackingMode=None,
        Status=None,
        Vports=None,
    ):
        # type: (str, str, List[str], str, str, List[str]) -> Topology
        """Finds and retrieves topology resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve topology resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all topology resources from the server.

        Args
        ----
        - ApplyOnTheFlyState (str(allowed | notAllowed | nothingToApply)): Checks whether the apply changes operation is allowed
        - NgpfProtocolRateMode (str(basic | smooth)): Decides whether protocol's sessions will started in normal or smooth mode
        - ProtocolActionsInProgress (list(str)): Lists all current protocol actions in progress
        - ProtocolStackingMode (str(parallel | sequential)): Decides whether protocol's sessions will started sequentially or parallelly across the layers
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): The current state of the scenario
        - Vports (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): List of virtual ports included in the port level configuration

        Returns
        -------
        - self: This instance with matching topology resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of topology data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the topology resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "abortApplyOnTheFly", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyOnTheFly", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("configureAll", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "fetchAndUpdateConfigFromCloud", payload=payload, response_object=None
        )

    def FetchDeviceGroupCount(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the fetchDeviceGroupCount operation on the server.

        Get Device Group Count for the Entire Scenario

        fetchDeviceGroupCount(async_operation=bool)number
        -------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: Device Group Count for the Entire Scenario

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
        return self._execute(
            "fetchDeviceGroupCount", payload=payload, response_object=None
        )

    def FetchScenarioObjectsShortenedNames(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the fetchScenarioObjectsShortenedNames operation on the server.

        Get shortened Topology/Device Group/Network Group names in case of ver long names

        fetchScenarioObjectsShortenedNames(Arg2=href, Arg3=number, async_operation=bool)string
        --------------------------------------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/topology | /api/v1/sessions/1/ixnetwork/topology/.../deviceGroup | /api/v1/sessions/1/ixnetwork/topology/.../networkGroup | /api/v1/sessions/1/ixnetwork/topology/deviceGroup | /api/v1/sessions/1/ixnetwork/topology/deviceGroup/networkGroup)): objref to /topology or device group or network group
        - Arg3 (number): Max number of characters to display
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: shortened Topology/Device Group/Network Group names in case of ver long names

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
        return self._execute(
            "fetchScenarioObjectsShortenedNames", payload=payload, response_object=None
        )

    def SendArpGlobal(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the sendArpGlobal operation on the server.

        Send ARP for a Topology or all Topologies

        sendArpGlobal(async_operation=bool)string
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
        return self._execute("sendArpGlobal", payload=payload, response_object=None)

    def SendNsGlobal(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the sendNsGlobal operation on the server.

        Send NS for a Topology or all Topologies

        sendNsGlobal(async_operation=bool)string
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

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
        return self._execute("sendNsGlobal", payload=payload, response_object=None)
