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


class Mpls(Base):
    """MPLS protocol.
    The Mpls class encapsulates a list of mpls resources that are managed by the user.
    A list of resources can be retrieved from the server using the Mpls.find() method.
    The list can be managed by using the Mpls.add() and Mpls.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "mpls"
    _SDM_ATT_MAP = {
        "Bos": "bos",
        "ConnectedVia": "connectedVia",
        "Cos": "cos",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "DestMac": "destMac",
        "Enablecw": "enablecw",
        "Errors": "errors",
        "Multiplier": "multiplier",
        "Name": "name",
        "Overridecos": "overridecos",
        "RxLabelValue": "rxLabelValue",
        "SessionInfo": "sessionInfo",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "TransportType": "transportType",
        "Ttl": "ttl",
        "TxLabelValue": "txLabelValue",
        "UpperLayer": "upperLayer",
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
        "transportType": ["overMac", "overTunnel"],
        "upperLayer": ["nhEthernet", "nhIp"],
    }

    def __init__(self, parent, list_op=False):
        super(Mpls, self).__init__(parent, list_op)

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
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635 import (
            Ethernet,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ethernet", None) is not None:
                return self._properties.get("Ethernet")
        return Ethernet(self)

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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3_2471ee7fdf32e67045bfc6c9e14f54d6.IsisL3): An instance of the IsisL3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3_2471ee7fdf32e67045bfc6c9e14f54d6 import (
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
    def Bos(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): bos
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Bos"]))

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
    def Cos(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EXP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Cos"]))

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
    def DestMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination Mac.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DestMac"]))

    @property
    def Enablecw(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable Control Word
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enablecw"])

    @Enablecw.setter
    def Enablecw(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enablecw"], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

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
    def Overridecos(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Override Cos
        """
        return self._get_attribute(self._SDM_ATT_MAP["Overridecos"])

    @Overridecos.setter
    def Overridecos(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Overridecos"], value)

    @property
    def RxLabelValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Rx Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RxLabelValue"]))

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[interfaceCreationFailed | interfaceDeletionFailed | interfaceInternalProblem | none]): Logs additional information about the session state
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
    def TransportType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(overMac | overTunnel): TransportType
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransportType"])

    @TransportType.setter
    def TransportType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransportType"], value)

    @property
    def Ttl(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TTL
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ttl"]))

    @property
    def TxLabelValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tx Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TxLabelValue"]))

    @property
    def UpperLayer(self):
        # type: () -> str
        """
        Returns
        -------
        - str(nhEthernet | nhIp): Value to Determine who is upper Layer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpperLayer"])

    @UpperLayer.setter
    def UpperLayer(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpperLayer"], value)

    def update(
        self,
        ConnectedVia=None,
        Enablecw=None,
        Multiplier=None,
        Name=None,
        Overridecos=None,
        StackedLayers=None,
        TransportType=None,
        UpperLayer=None,
    ):
        # type: (List[str], bool, int, str, bool, List[str], str, str) -> Mpls
        """Updates mpls resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Enablecw (bool): Enable Control Word
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Overridecos (bool): Override Cos
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - TransportType (str(overMac | overTunnel)): TransportType
        - UpperLayer (str(nhEthernet | nhIp)): Value to Determine who is upper Layer.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        Enablecw=None,
        Multiplier=None,
        Name=None,
        Overridecos=None,
        StackedLayers=None,
        TransportType=None,
        UpperLayer=None,
    ):
        # type: (List[str], bool, int, str, bool, List[str], str, str) -> Mpls
        """Adds a new mpls resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Enablecw (bool): Enable Control Word
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Overridecos (bool): Override Cos
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - TransportType (str(overMac | overTunnel)): TransportType
        - UpperLayer (str(nhEthernet | nhIp)): Value to Determine who is upper Layer.

        Returns
        -------
        - self: This instance with all currently retrieved mpls resources using find and the newly added mpls resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mpls resources in this instance from the server.

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
        Enablecw=None,
        Errors=None,
        Multiplier=None,
        Name=None,
        Overridecos=None,
        SessionInfo=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        TransportType=None,
        UpperLayer=None,
    ):
        """Finds and retrieves mpls resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mpls resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mpls resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Enablecw (bool): Enable Control Word
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Overridecos (bool): Override Cos
        - SessionInfo (list(str[interfaceCreationFailed | interfaceDeletionFailed | interfaceInternalProblem | none])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TransportType (str(overMac | overTunnel)): TransportType
        - UpperLayer (str(nhEthernet | nhIp)): Value to Determine who is upper Layer.

        Returns
        -------
        - self: This instance with matching mpls resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mpls data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mpls resources from the server available through an iterator or index

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
        Bos=None,
        Cos=None,
        DestMac=None,
        RxLabelValue=None,
        Ttl=None,
        TxLabelValue=None,
    ):
        """Base class infrastructure that gets a list of mpls device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Bos (str): optional regex of bos
        - Cos (str): optional regex of cos
        - DestMac (str): optional regex of destMac
        - RxLabelValue (str): optional regex of rxLabelValue
        - Ttl (str): optional regex of ttl
        - TxLabelValue (str): optional regex of txLabelValue

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
