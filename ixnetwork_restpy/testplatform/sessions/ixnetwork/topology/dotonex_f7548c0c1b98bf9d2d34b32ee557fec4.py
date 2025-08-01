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


class DotOneX(Base):
    """
    The DotOneX class encapsulates a list of dotOneX resources that are managed by the user.
    A list of resources can be retrieved from the server using the DotOneX.find() method.
    The list can be managed by using the DotOneX.add() and DotOneX.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "dotOneX"
    _SDM_ATT_MAP = {
        "Active": "active",
        "CaCert": "caCert",
        "CertDir": "certDir",
        "CertificateKeySameFile": "certificateKeySameFile",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EapolVersion": "eapolVersion",
        "Errors": "errors",
        "FastInnerMethod": "fastInnerMethod",
        "FastProMode": "fastProMode",
        "Faststateless": "faststateless",
        "HostAuthMode": "hostAuthMode",
        "HostCert": "hostCert",
        "HostKey": "hostKey",
        "HostName": "hostName",
        "HostPwd": "hostPwd",
        "IgnoreAuthEapolVer": "ignoreAuthEapolVer",
        "InnerTunnel": "innerTunnel",
        "Multiplier": "multiplier",
        "Name": "name",
        "ParentEth": "parentEth",
        "PeerCert": "peerCert",
        "PrivateKey": "privateKey",
        "Protocol": "protocol",
        "RunTimeCertGen": "runTimeCertGen",
        "SendCACertOnly": "sendCACertOnly",
        "SessionInfo": "sessionInfo",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "TlsVersion": "tlsVersion",
        "UserName": "userName",
        "UserPwd": "userPwd",
        "VerifyPeer": "verifyPeer",
        "WaitId": "waitId",
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
        super(DotOneX, self).__init__(parent, list_op)

    @property
    def BondedGRE(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bondedgre_09eda4ea678bfaf1026122797df45443.BondedGRE): An instance of the BondedGRE class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bondedgre_09eda4ea678bfaf1026122797df45443 import (
            BondedGRE,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BondedGRE", None) is not None:
                return self._properties.get("BondedGRE")
        return BondedGRE(self)

    @property
    def CfmBridge(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge_0d1f83a1e9fee8ee7d444b2a33a0e03b.CfmBridge): An instance of the CfmBridge class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge_0d1f83a1e9fee8ee7d444b2a33a0e03b import (
            CfmBridge,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CfmBridge", None) is not None:
                return self._properties.get("CfmBridge")
        return CfmBridge(self)

    @property
    def Dhcpv4client(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client_51940f357e701f382297f94c99af7a22.Dhcpv4client): An instance of the Dhcpv4client class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client_51940f357e701f382297f94c99af7a22 import (
            Dhcpv4client,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv4client", None) is not None:
                return self._properties.get("Dhcpv4client")
        return Dhcpv4client(self)

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
    def Esmc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.esmc_4d9a2f8edc72794b61857303b0afb00d.Esmc): An instance of the Esmc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.esmc_4d9a2f8edc72794b61857303b0afb00d import (
            Esmc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Esmc", None) is not None:
                return self._properties.get("Esmc")
        return Esmc(self)

    @property
    def Ipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4_8cb960b62ae85a03e1b40a57bfaeb7bb.Ipv4): An instance of the Ipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4_8cb960b62ae85a03e1b40a57bfaeb7bb import (
            Ipv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv4", None) is not None:
                return self._properties.get("Ipv4")
        return Ipv4(self)

    @property
    def Ipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6_b40789fa49420009901a46b8dc683afc.Ipv6): An instance of the Ipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6_b40789fa49420009901a46b8dc683afc import (
            Ipv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6", None) is not None:
                return self._properties.get("Ipv6")
        return Ipv6(self)

    @property
    def Ipv6Autoconfiguration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration_30e04d0136286f29e3d34b2c9405e01e.Ipv6Autoconfiguration): An instance of the Ipv6Autoconfiguration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration_30e04d0136286f29e3d34b2c9405e01e import (
            Ipv6Autoconfiguration,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6Autoconfiguration", None) is not None:
                return self._properties.get("Ipv6Autoconfiguration")
        return Ipv6Autoconfiguration(self)

    @property
    def IsisDceSimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter_92c9662fb6421c6639f138f508faf4d4.IsisDceSimRouter): An instance of the IsisDceSimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter_92c9662fb6421c6639f138f508faf4d4 import (
            IsisDceSimRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisDceSimRouter", None) is not None:
                return self._properties.get("IsisDceSimRouter")
        return IsisDceSimRouter(self)

    @property
    def IsisFabricPath(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath_49ed8317c28295615f21a4a8362c2b95.IsisFabricPath): An instance of the IsisFabricPath class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath_49ed8317c28295615f21a4a8362c2b95 import (
            IsisFabricPath,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisFabricPath", None) is not None:
                return self._properties.get("IsisFabricPath")
        return IsisFabricPath(self)

    @property
    def IsisL3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3_fc556e45abed3a66fda411498eb8b6a4.IsisL3): An instance of the IsisL3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3_fc556e45abed3a66fda411498eb8b6a4 import (
            IsisL3,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisL3", None) is not None:
                return self._properties.get("IsisL3")
        return IsisL3(self)

    @property
    def IsisSpbBcb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb_d576c38717539c1b1768a3a9f8ab5670.IsisSpbBcb): An instance of the IsisSpbBcb class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb_d576c38717539c1b1768a3a9f8ab5670 import (
            IsisSpbBcb,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSpbBcb", None) is not None:
                return self._properties.get("IsisSpbBcb")
        return IsisSpbBcb(self)

    @property
    def IsisSpbBeb(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb_82771ae7e9ec8dfc9848a0c0aa078da2.IsisSpbBeb): An instance of the IsisSpbBeb class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb_82771ae7e9ec8dfc9848a0c0aa078da2 import (
            IsisSpbBeb,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSpbBeb", None) is not None:
                return self._properties.get("IsisSpbBeb")
        return IsisSpbBeb(self)

    @property
    def IsisSpbSimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter_4d8d2b3596c2f006afcd75a76b6934ff.IsisSpbSimRouter): An instance of the IsisSpbSimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter_4d8d2b3596c2f006afcd75a76b6934ff import (
            IsisSpbSimRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSpbSimRouter", None) is not None:
                return self._properties.get("IsisSpbSimRouter")
        return IsisSpbSimRouter(self)

    @property
    def IsisTrill(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill_e1cc1866688f861871e06513525d235b.IsisTrill): An instance of the IsisTrill class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill_e1cc1866688f861871e06513525d235b import (
            IsisTrill,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisTrill", None) is not None:
                return self._properties.get("IsisTrill")
        return IsisTrill(self)

    @property
    def IsisTrillSimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter_7f0721f1a50df44db865ccea96c8f735.IsisTrillSimRouter): An instance of the IsisTrillSimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter_7f0721f1a50df44db865ccea96c8f735 import (
            IsisTrillSimRouter,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisTrillSimRouter", None) is not None:
                return self._properties.get("IsisTrillSimRouter")
        return IsisTrillSimRouter(self)

    @property
    def Lacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp_b6b488f98125e4a7318076cb1375941b.Lacp): An instance of the Lacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp_b6b488f98125e4a7318076cb1375941b import (
            Lacp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lacp", None) is not None:
                return self._properties.get("Lacp")
        return Lacp(self)

    @property
    def Lagportlacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportlacp_ed42d76e076cab1a6c2369b757a5d616.Lagportlacp): An instance of the Lagportlacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportlacp_ed42d76e076cab1a6c2369b757a5d616 import (
            Lagportlacp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lagportlacp", None) is not None:
                return self._properties.get("Lagportlacp")
        return Lagportlacp(self)

    @property
    def Lagportstaticlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportstaticlag_f67759421ceee90b665b41bf19b8202d.Lagportstaticlag): An instance of the Lagportstaticlag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lagportstaticlag_f67759421ceee90b665b41bf19b8202d import (
            Lagportstaticlag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Lagportstaticlag", None) is not None:
                return self._properties.get("Lagportstaticlag")
        return Lagportstaticlag(self)

    @property
    def LightweightDhcpv6relayAgent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lightweightdhcpv6relayagent_f435ed323783b3dadd80a122fef5c031.LightweightDhcpv6relayAgent): An instance of the LightweightDhcpv6relayAgent class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lightweightdhcpv6relayagent_f435ed323783b3dadd80a122fef5c031 import (
            LightweightDhcpv6relayAgent,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LightweightDhcpv6relayAgent", None) is not None:
                return self._properties.get("LightweightDhcpv6relayAgent")
        return LightweightDhcpv6relayAgent(self)

    @property
    def Macsec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macsec_8816f28c50db5a9224d83bc7b8e0744d.Macsec): An instance of the Macsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macsec_8816f28c50db5a9224d83bc7b8e0744d import (
            Macsec,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Macsec", None) is not None:
                return self._properties.get("Macsec")
        return Macsec(self)

    @property
    def Microbfdv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.microbfdv4_141c58b1c08e07212b7c46d9ec8495c1.Microbfdv4): An instance of the Microbfdv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.microbfdv4_141c58b1c08e07212b7c46d9ec8495c1 import (
            Microbfdv4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Microbfdv4", None) is not None:
                return self._properties.get("Microbfdv4")
        return Microbfdv4(self)

    @property
    def Microbfdv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.microbfdv6_6b0c1a370d37aab2ddafd875d7778d93.Microbfdv6): An instance of the Microbfdv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.microbfdv6_6b0c1a370d37aab2ddafd875d7778d93 import (
            Microbfdv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Microbfdv6", None) is not None:
                return self._properties.get("Microbfdv6")
        return Microbfdv6(self)

    @property
    def Mka(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mka_78bbec2a0b33a75a2bd662bf23b07c3d.Mka): An instance of the Mka class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mka_78bbec2a0b33a75a2bd662bf23b07c3d import (
            Mka,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Mka", None) is not None:
                return self._properties.get("Mka")
        return Mka(self)

    @property
    def Mpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls_ffaab24246ff53741a201b0a48e8e3f1.Mpls): An instance of the Mpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls_ffaab24246ff53741a201b0a48e8e3f1 import (
            Mpls,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Mpls", None) is not None:
                return self._properties.get("Mpls")
        return Mpls(self)

    @property
    def MsrpListener(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener_e4c5ef0942a99c83ab955893f78633c0.MsrpListener): An instance of the MsrpListener class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener_e4c5ef0942a99c83ab955893f78633c0 import (
            MsrpListener,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MsrpListener", None) is not None:
                return self._properties.get("MsrpListener")
        return MsrpListener(self)

    @property
    def MsrpTalker(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker_ac4e61374b0b4d8500aef7076a2cda89.MsrpTalker): An instance of the MsrpTalker class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker_ac4e61374b0b4d8500aef7076a2cda89 import (
            MsrpTalker,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MsrpTalker", None) is not None:
                return self._properties.get("MsrpTalker")
        return MsrpTalker(self)

    @property
    def Pppoxclient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxclient_f43b198156c11196dbbd8c4dbee2af9d.Pppoxclient): An instance of the Pppoxclient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxclient_f43b198156c11196dbbd8c4dbee2af9d import (
            Pppoxclient,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pppoxclient", None) is not None:
                return self._properties.get("Pppoxclient")
        return Pppoxclient(self)

    @property
    def Pppoxserver(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver_622ad1c6d961bb8e246b079c72242bfa.Pppoxserver): An instance of the Pppoxserver class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver_622ad1c6d961bb8e246b079c72242bfa import (
            Pppoxserver,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pppoxserver", None) is not None:
                return self._properties.get("Pppoxserver")
        return Pppoxserver(self)

    @property
    def Ptp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp_c1137d7a86f153ce202396614c8f5e6a.Ptp): An instance of the Ptp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp_c1137d7a86f153ce202396614c8f5e6a import (
            Ptp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ptp", None) is not None:
                return self._properties.get("Ptp")
        return Ptp(self)

    @property
    def StaticLag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag_d16a8997708d466db9c9f007ce04724e.StaticLag): An instance of the StaticLag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag_d16a8997708d466db9c9f007ce04724e import (
            StaticLag,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StaticLag", None) is not None:
                return self._properties.get("StaticLag")
        return StaticLag(self)

    @property
    def StaticMacsec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticmacsec_1fc553ada89d0fcad13e14f944ba6854.StaticMacsec): An instance of the StaticMacsec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticmacsec_1fc553ada89d0fcad13e14f944ba6854 import (
            StaticMacsec,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StaticMacsec", None) is not None:
                return self._properties.get("StaticMacsec")
        return StaticMacsec(self)

    @property
    def Streams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams_dcd5bdb9e0099c6354f7bed1be55d8f6.Streams): An instance of the Streams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams_dcd5bdb9e0099c6354f7bed1be55d8f6 import (
            Streams,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Streams", None) is not None:
                return self._properties.get("Streams")
        return Streams(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def CaCert(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The CA certificate to be used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CaCert"]))

    @property
    def CertDir(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The location to the saved certificates
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CertDir"]))

    @property
    def CertificateKeySameFile(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): flag to determine whether to use same Certificate file for both Private Key and User Certificate
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CertificateKeySameFile"])
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
    def EapolVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 802.1x EAPOL authentication version.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EapolVersion"]))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def FastInnerMethod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAST Inner Method
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FastInnerMethod"])
        )

    @property
    def FastProMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAST Provision Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FastProMode"]))

    @property
    def Faststateless(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAST Stateless Resume
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Faststateless"]))

    @property
    def HostAuthMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host Authentication Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostAuthMode"]))

    @property
    def HostCert(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Peer certificate to be used by the host
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostCert"]))

    @property
    def HostKey(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The private key certificate to be used by the host
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostKey"]))

    @property
    def HostName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Credential of the host for authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostName"]))

    @property
    def HostPwd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password of the host for authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostPwd"]))

    @property
    def IgnoreAuthEapolVer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable to ignore authenticator EAPOL version.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IgnoreAuthEapolVer"])
        )

    @property
    def InnerTunnel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Inner tunnel selection for EAP-TTLS. Supported choices being MSCHAPv2 and PAP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["InnerTunnel"]))

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
    def ParentEth(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ParentEth"])

    @ParentEth.setter
    def ParentEth(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ParentEth"], value)

    @property
    def PeerCert(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Peer certificate to be used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PeerCert"]))

    @property
    def PrivateKey(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The private key certificate to be used
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrivateKey"]))

    @property
    def Protocol(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): protocol for authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Protocol"]))

    @property
    def RunTimeCertGen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Generate Certificate during Run time. Configure details in Global parameters. Common Name will be User Name. Certificate and Key file names will be generated based on corresponding Client User name. Eg: If Client User name is IxiaUser1 then Certificate File will be IxiaUser1.pem, Key File will be IxiaUser1_key.pem, CA certificate File will be root.pem
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RunTimeCertGen"])
        )

    @property
    def SendCACertOnly(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use this option to send CA Certificate only to Port. Eg: For PEAPv0/v1 case there is no need to send User Certificate to port.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendCACertOnly"])
        )

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[acquired | authenticated | authenticating | configured | connecting | disconnected | eapFailure | forceAuth | forceUnAuth | genFailure | held | initFailure | invalidFailure | loadFailure | logoff | restart | unconfigured]): Current 802.1x session state: Log Off - Supplicant has been sent EAPOL-Logoff message. Stopped - Supplicant disconnected succesfully. Authenticating - Supplicant is being authenticated. but negotiation didn't complete yet. Held - Supplicant ignores and discards all EAPOL packets. Authenticated - Authenticator has successfully authenticated the Supplicant. Restart - Supplicant is entered Restart state. Force Authentication - This state is entered because DUT's portControl is set to force-authorized. Force UnAuthentication - This state is entered because DUT's portControl is set to force-unauthorized. Unconfigured - Supplicant Unconfigured state. Configured - Supplicant initilize state. Authentication Failure - Supplicant's authentication failed. CA Cert Load Failed - Supplicant's unable to load CA certificate. Failed To Load Certificate/Key - Failed to load certificate or certificate key. Invalid EAP - Invalid EAP. Generic EAP Failure - Generic EAP Failure.
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
    def TlsVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TLS version selecction
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TlsVersion"]))

    @property
    def UserName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Credential of the user for authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UserName"]))

    @property
    def UserPwd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password of the user for authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UserPwd"]))

    @property
    def VerifyPeer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Verifies the provided peer certificate
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VerifyPeer"]))

    @property
    def WaitId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When enabled, the supplicant does not send the initial EAPOL Start message. Instead, it waits for the authenticator (the DUT) to send an EAPOL Request / Identity message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["WaitId"]))

    def update(
        self,
        ConnectedVia=None,
        Multiplier=None,
        Name=None,
        ParentEth=None,
        StackedLayers=None,
    ):
        # type: (List[str], int, str, str, List[str]) -> DotOneX
        """Updates dotOneX resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ParentEth (str(None | /api/v1/sessions/1/ixnetwork/topology)):
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
        ParentEth=None,
        StackedLayers=None,
    ):
        # type: (List[str], int, str, str, List[str]) -> DotOneX
        """Adds a new dotOneX resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ParentEth (str(None | /api/v1/sessions/1/ixnetwork/topology)):
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved dotOneX resources using find and the newly added dotOneX resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dotOneX resources in this instance from the server.

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
        ParentEth=None,
        SessionInfo=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves dotOneX resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dotOneX resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dotOneX resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ParentEth (str(None | /api/v1/sessions/1/ixnetwork/topology)):
        - SessionInfo (list(str[acquired | authenticated | authenticating | configured | connecting | disconnected | eapFailure | forceAuth | forceUnAuth | genFailure | held | initFailure | invalidFailure | loadFailure | logoff | restart | unconfigured])): Current 802.1x session state: Log Off - Supplicant has been sent EAPOL-Logoff message. Stopped - Supplicant disconnected succesfully. Authenticating - Supplicant is being authenticated. but negotiation didn't complete yet. Held - Supplicant ignores and discards all EAPOL packets. Authenticated - Authenticator has successfully authenticated the Supplicant. Restart - Supplicant is entered Restart state. Force Authentication - This state is entered because DUT's portControl is set to force-authorized. Force UnAuthentication - This state is entered because DUT's portControl is set to force-unauthorized. Unconfigured - Supplicant Unconfigured state. Configured - Supplicant initilize state. Authentication Failure - Supplicant's authentication failed. CA Cert Load Failed - Supplicant's unable to load CA certificate. Failed To Load Certificate/Key - Failed to load certificate or certificate key. Invalid EAP - Invalid EAP. Generic EAP Failure - Generic EAP Failure.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching dotOneX resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dotOneX data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dotOneX resources from the server available through an iterator or index

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

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
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

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
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
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

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

    def UploadFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the uploadFile operation on the server.

        For secure sessions, upload necessary certificate files to chassis before test is run.

        uploadFile(Arg2=list, Arg3=number, Arg4=href, async_operation=bool)list
        -----------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Arg3 (number):
        - Arg4 (obj(ixnetwork_restpy.files.Files)): Select files(s) to upload.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("uploadFile", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        CaCert=None,
        CertDir=None,
        CertificateKeySameFile=None,
        EapolVersion=None,
        FastInnerMethod=None,
        FastProMode=None,
        Faststateless=None,
        HostAuthMode=None,
        HostCert=None,
        HostKey=None,
        HostName=None,
        HostPwd=None,
        IgnoreAuthEapolVer=None,
        InnerTunnel=None,
        PeerCert=None,
        PrivateKey=None,
        Protocol=None,
        RunTimeCertGen=None,
        SendCACertOnly=None,
        TlsVersion=None,
        UserName=None,
        UserPwd=None,
        VerifyPeer=None,
        WaitId=None,
    ):
        """Base class infrastructure that gets a list of dotOneX device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CaCert (str): optional regex of caCert
        - CertDir (str): optional regex of certDir
        - CertificateKeySameFile (str): optional regex of certificateKeySameFile
        - EapolVersion (str): optional regex of eapolVersion
        - FastInnerMethod (str): optional regex of fastInnerMethod
        - FastProMode (str): optional regex of fastProMode
        - Faststateless (str): optional regex of faststateless
        - HostAuthMode (str): optional regex of hostAuthMode
        - HostCert (str): optional regex of hostCert
        - HostKey (str): optional regex of hostKey
        - HostName (str): optional regex of hostName
        - HostPwd (str): optional regex of hostPwd
        - IgnoreAuthEapolVer (str): optional regex of ignoreAuthEapolVer
        - InnerTunnel (str): optional regex of innerTunnel
        - PeerCert (str): optional regex of peerCert
        - PrivateKey (str): optional regex of privateKey
        - Protocol (str): optional regex of protocol
        - RunTimeCertGen (str): optional regex of runTimeCertGen
        - SendCACertOnly (str): optional regex of sendCACertOnly
        - TlsVersion (str): optional regex of tlsVersion
        - UserName (str): optional regex of userName
        - UserPwd (str): optional regex of userPwd
        - VerifyPeer (str): optional regex of verifyPeer
        - WaitId (str): optional regex of waitId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
