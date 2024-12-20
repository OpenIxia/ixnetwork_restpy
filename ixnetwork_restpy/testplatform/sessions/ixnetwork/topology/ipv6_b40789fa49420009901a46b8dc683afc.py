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


class Ipv6(Base):
    """Static IPV6
    The Ipv6 class encapsulates a list of ipv6 resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ipv6.find() method.
    The list can be managed by using the Ipv6.add() and Ipv6.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "ipv6"
    _SDM_ATT_MAP = {
        "Address": "address",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "CustomLinkLocalAddress": "customLinkLocalAddress",
        "DescriptiveName": "descriptiveName",
        "DiscoverGatewayIp": "discoverGatewayIp",
        "DiscoveredGatewayIp": "discoveredGatewayIp",
        "Errors": "errors",
        "GatewayDiscoveryOpt": "gatewayDiscoveryOpt",
        "GatewayIp": "gatewayIp",
        "IncludeRaPrefix": "includeRaPrefix",
        "LearnNeighbors": "learnNeighbors",
        "LinkLocalAddress": "linkLocalAddress",
        "ManualGatewayMac": "manualGatewayMac",
        "Multiplier": "multiplier",
        "Name": "name",
        "Prefix": "prefix",
        "ResolveGateway": "resolveGateway",
        "ResolvedGatewayMac": "resolvedGatewayMac",
        "SendRa": "sendRa",
        "SessionInfo": "sessionInfo",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "UseCustomLinkLocalAddress": "useCustomLinkLocalAddress",
    }
    _SDM_ENUM_MAP = {
        "gatewayDiscoveryOpt": ["ra", "nsNa"],
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
        super(Ipv6, self).__init__(parent, list_op)

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
    def CuspCP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcp_1ab532ec5eaeec746678378f2443dafe.CuspCP): An instance of the CuspCP class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcp_1ab532ec5eaeec746678378f2443dafe import (
            CuspCP,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CuspCP", None) is not None:
                return self._properties.get("CuspCP")
        return CuspCP(self)

    @property
    def CuspUP(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspup_a452407df164d641b27491106f32c6de.CuspUP): An instance of the CuspUP class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspup_a452407df164d641b27491106f32c6de import (
            CuspUP,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CuspUP", None) is not None:
                return self._properties.get("CuspUP")
        return CuspUP(self)

    @property
    def Dhcpv6relayAgent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6relayagent_98152227df750678a31eb6776380facc.Dhcpv6relayAgent): An instance of the Dhcpv6relayAgent class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6relayagent_98152227df750678a31eb6776380facc import (
            Dhcpv6relayAgent,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dhcpv6relayAgent", None) is not None:
                return self._properties.get("Dhcpv6relayAgent")
        return Dhcpv6relayAgent(self)

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
    def Greoipv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv6_aad01583ffa3746a541812fe996bbcd0.Greoipv6): An instance of the Greoipv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv6_aad01583ffa3746a541812fe996bbcd0 import (
            Greoipv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Greoipv6", None) is not None:
                return self._properties.get("Greoipv6")
        return Greoipv6(self)

    @property
    def Ipv6sr(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6sr_5d596ce1a2d00c8f120ae357d45b9a46.Ipv6sr): An instance of the Ipv6sr class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6sr_5d596ce1a2d00c8f120ae357d45b9a46 import (
            Ipv6sr,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ipv6sr", None) is not None:
                return self._properties.get("Ipv6sr")
        return Ipv6sr(self)

    @property
    def LdpBasicRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c.LdpBasicRouterV6): An instance of the LdpBasicRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c import (
            LdpBasicRouterV6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpBasicRouterV6", None) is not None:
                return self._properties.get("LdpBasicRouterV6")
        return LdpBasicRouterV6(self)

    @property
    def LdpTargetedRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf.LdpTargetedRouterV6): An instance of the LdpTargetedRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf import (
            LdpTargetedRouterV6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpTargetedRouterV6", None) is not None:
                return self._properties.get("LdpTargetedRouterV6")
        return LdpTargetedRouterV6(self)

    @property
    def Ldpv6ConnectedInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6connectedinterface_c2cbc5e29b8ad12450804681ee48ce22.Ldpv6ConnectedInterface): An instance of the Ldpv6ConnectedInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6connectedinterface_c2cbc5e29b8ad12450804681ee48ce22 import (
            Ldpv6ConnectedInterface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ldpv6ConnectedInterface", None) is not None:
                return self._properties.get("Ldpv6ConnectedInterface")
        return Ldpv6ConnectedInterface(self)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

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
    def Ntpclock(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock_0d879e81ae3d4c658c1fddb7e0bca059.Ntpclock): An instance of the Ntpclock class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock_0d879e81ae3d4c658c1fddb7e0bca059 import (
            Ntpclock,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ntpclock", None) is not None:
                return self._properties.get("Ntpclock")
        return Ntpclock(self)

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
    def Ptp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp_c3eec87ebde27dac796b6c44a242310f.Ptp): An instance of the Ptp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp_c3eec87ebde27dac796b6c44a242310f import (
            Ptp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ptp", None) is not None:
                return self._properties.get("Ptp")
        return Ptp(self)

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
    def Roce6v2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.roce6v2_c5bf003ba7756e74c6e5da9fd6ee6a9b.Roce6v2): An instance of the Roce6v2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.roce6v2_c5bf003ba7756e74c6e5da9fd6ee6a9b import (
            Roce6v2,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Roce6v2", None) is not None:
                return self._properties.get("Roce6v2")
        return Roce6v2(self)

    @property
    def Srv6Oam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oam_677f5b387d62a13791d7d97f690e2b56.Srv6Oam): An instance of the Srv6Oam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oam_677f5b387d62a13791d7d97f690e2b56 import (
            Srv6Oam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Srv6Oam", None) is not None:
                return self._properties.get("Srv6Oam")
        return Srv6Oam(self)

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
    def TwampIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.twampipv6_72c7939993683cf2a1b8b4518a76974c.TwampIpv6): An instance of the TwampIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.twampipv6_72c7939993683cf2a1b8b4518a76974c import (
            TwampIpv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TwampIpv6", None) is not None:
                return self._properties.get("TwampIpv6")
        return TwampIpv6(self)

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
    def Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 addresses of the devices
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Address"]))

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
    def CustomLinkLocalAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Attribute to configure Custom Link Local Address(s).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CustomLinkLocalAddress"])
        )

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
    def DiscoverGatewayIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables gateway IP address discovery.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DiscoverGatewayIp"])
        )

    @property
    def DiscoveredGatewayIp(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The discovered gateway IP addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscoveredGatewayIp"])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def GatewayDiscoveryOpt(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ra | nsNa): Options to discover the gateway IP.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GatewayDiscoveryOpt"])

    @GatewayDiscoveryOpt.setter
    def GatewayDiscoveryOpt(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["GatewayDiscoveryOpt"], value)

    @property
    def GatewayIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Gateways of the layer
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GatewayIp"]))

    @property
    def IncludeRaPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When enabled, prefix will be added in RA option.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeRaPrefix"])
        )

    @property
    def LearnNeighbors(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable or disable the discover or learn neighbor(s) option.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LearnNeighbors"])

    @LearnNeighbors.setter
    def LearnNeighbors(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LearnNeighbors"], value)

    @property
    def LinkLocalAddress(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Attribute to retrieve the configured Link Local Address(s).
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkLocalAddress"])

    @property
    def ManualGatewayMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User specified Gateway MAC addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ManualGatewayMac"])
        )

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
    def Prefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Prefix"]))

    @property
    def ResolveGateway(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables the gateway MAC address discovery.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ResolveGateway"])
        )

    @property
    def ResolvedGatewayMac(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The resolved gateway's MAC addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP["ResolvedGatewayMac"])

    @property
    def SendRa(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, periodic Router Advertisements will be sent from this interface.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SendRa"]))

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[discoverIpFailed | duplicateAddress | interfaceRemoved | none | resolveMacFailed]): Logs additional information about the session state.
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
    def UseCustomLinkLocalAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to determine whether the custom Link Local Address is enabled. By default, it is set to false.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseCustomLinkLocalAddress"])

    @UseCustomLinkLocalAddress.setter
    def UseCustomLinkLocalAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseCustomLinkLocalAddress"], value)

    def update(
        self,
        ConnectedVia=None,
        GatewayDiscoveryOpt=None,
        LearnNeighbors=None,
        Multiplier=None,
        Name=None,
        StackedLayers=None,
        UseCustomLinkLocalAddress=None,
    ):
        # type: (List[str], str, bool, int, str, List[str], bool) -> Ipv6
        """Updates ipv6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - GatewayDiscoveryOpt (str(ra | nsNa)): Options to discover the gateway IP.
        - LearnNeighbors (bool): Enable or disable the discover or learn neighbor(s) option.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - UseCustomLinkLocalAddress (bool): Flag to determine whether the custom Link Local Address is enabled. By default, it is set to false.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        GatewayDiscoveryOpt=None,
        LearnNeighbors=None,
        Multiplier=None,
        Name=None,
        StackedLayers=None,
        UseCustomLinkLocalAddress=None,
    ):
        # type: (List[str], str, bool, int, str, List[str], bool) -> Ipv6
        """Adds a new ipv6 resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - GatewayDiscoveryOpt (str(ra | nsNa)): Options to discover the gateway IP.
        - LearnNeighbors (bool): Enable or disable the discover or learn neighbor(s) option.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - UseCustomLinkLocalAddress (bool): Flag to determine whether the custom Link Local Address is enabled. By default, it is set to false.

        Returns
        -------
        - self: This instance with all currently retrieved ipv6 resources using find and the newly added ipv6 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ipv6 resources in this instance from the server.

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
        DiscoveredGatewayIp=None,
        Errors=None,
        GatewayDiscoveryOpt=None,
        LearnNeighbors=None,
        LinkLocalAddress=None,
        Multiplier=None,
        Name=None,
        ResolvedGatewayMac=None,
        SessionInfo=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        UseCustomLinkLocalAddress=None,
    ):
        """Finds and retrieves ipv6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv6 resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DiscoveredGatewayIp (list(str)): The discovered gateway IP addresses.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - GatewayDiscoveryOpt (str(ra | nsNa)): Options to discover the gateway IP.
        - LearnNeighbors (bool): Enable or disable the discover or learn neighbor(s) option.
        - LinkLocalAddress (list(str)): Attribute to retrieve the configured Link Local Address(s).
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ResolvedGatewayMac (list(str)): The resolved gateway's MAC addresses
        - SessionInfo (list(str[discoverIpFailed | duplicateAddress | interfaceRemoved | none | resolveMacFailed])): Logs additional information about the session state.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - UseCustomLinkLocalAddress (bool): Flag to determine whether the custom Link Local Address is enabled. By default, it is set to false.

        Returns
        -------
        - self: This instance with matching ipv6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv6 resources from the server available through an iterator or index

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

    def CancelPing(self, *args, **kwargs):
        """Executes the cancelPing operation on the server.

        Cancel Non-Blocking Send Ping Requests for selected IPv6 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        cancelPing(async_operation=bool)list
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        cancelPing(SessionIndices=list, async_operation=bool)list
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        cancelPing(SessionIndices=string, async_operation=bool)list
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
        return self._execute("cancelPing", payload=payload, response_object=None)

    def ClearLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearLearnedInfo operation on the server.

        Clear Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearLearnedInfo(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearLearnedInfo(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearLearnedInfo(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of configured device indices. An empty list indicates all the instances.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("clearLearnedInfo", payload=payload, response_object=None)

    def GetNeighborInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getNeighborInfo operation on the server.

        Get Neighbor Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getNeighborInfo(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getNeighborInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getNeighborInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getNeighborInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices to fetch the learned info
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("getNeighborInfo", payload=payload, response_object=None)

    def PingStatus(self, *args, **kwargs):
        """Executes the pingStatus operation on the server.

        Status of Non-Blocking Send Ping Requests for selected IPv6 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pingStatus(async_operation=bool)list
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        pingStatus(SessionIndices=list, async_operation=bool)list
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        pingStatus(SessionIndices=string, async_operation=bool)list
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
        return self._execute("pingStatus", payload=payload, response_object=None)

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

    def SendNs(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendNs operation on the server.

        Send Neighbor Solicitation request to configured gateway IP address to resolve Gateway MAC for selected items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendNs(async_operation=bool)
        ----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendNs(SessionIndices=list, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendNs(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------
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
        return self._execute("sendNs", payload=payload, response_object=None)

    def SendNsManual(self, *args, **kwargs):
        """Executes the sendNsManual operation on the server.

        Send Neighbor Solicitation request to specified IP address for selected items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendNsManual(DestIP=string, async_operation=bool)list
        -----------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendNsManual(DestIP=string, SessionIndices=list, async_operation=bool)list
        --------------------------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendNsManual(SessionIndices=string, DestIP=string, async_operation=bool)list
        ----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a destIP of type kString
        - DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("sendNsManual", payload=payload, response_object=None)

    def SendPing(self, *args, **kwargs):
        """Executes the sendPing operation on the server.

        Send ping for selected IPv6 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing(DestIP=string, async_operation=bool)list
        -------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(DestIP=string, SessionIndices=list, async_operation=bool)list
        ----------------------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(SessionIndices=string, DestIP=string, async_operation=bool)list
        ------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a destIP of type kString
        - DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12
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

    def SendPingAsync(self, *args, **kwargs):
        """Executes the sendPingAsync operation on the server.

        Non-Blocking Send ping request for selected IPv6 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPingAsync(DestIP=string, async_operation=bool)list
        ------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPingAsync(DestIP=string, SessionIndices=list, async_operation=bool)list
        ---------------------------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPingAsync(SessionIndices=string, DestIP=string, async_operation=bool)list
        -----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a destIP of type kString
        - DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute("sendPingAsync", payload=payload, response_object=None)

    def SendPingWithCountAndPayload(self, *args, **kwargs):
        """Executes the sendPingWithCountAndPayload operation on the server.

        Blocking Send ping request for selected IPv6 items with Ping Count and Payload size.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPingWithCountAndPayload(DestIP=string, PingCount=number, PingInterval=number, PayloadSize=number, async_operation=bool)list
        -------------------------------------------------------------------------------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - PingCount (number): This parameter requires a pingCount of type kInteger
        - PingInterval (number): This parameter requires a pingInterval of type kInteger
        - PayloadSize (number): This parameter requires a payloadSize of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPingWithCountAndPayload(DestIP=string, PingCount=number, PingInterval=number, PayloadSize=number, SessionIndices=list, async_operation=bool)list
        ----------------------------------------------------------------------------------------------------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - PingCount (number): This parameter requires a pingCount of type kInteger
        - PingInterval (number): This parameter requires a pingInterval of type kInteger
        - PayloadSize (number): This parameter requires a payloadSize of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPingWithCountAndPayload(SessionIndices=string, DestIP=string, PingCount=number, PingInterval=number, PayloadSize=number, async_operation=bool)list
        ------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a destIP of type kString
        - DestIP (str): This parameter requires a pingCount of type kInteger
        - PingCount (number): This parameter requires a pingInterval of type kInteger
        - PingInterval (number): This parameter requires a payloadSize of type kInteger
        - PayloadSize (number): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute(
            "sendPingWithCountAndPayload", payload=payload, response_object=None
        )

    def SendPingWithCountAndPayloadAsync(self, *args, **kwargs):
        """Executes the sendPingWithCountAndPayloadAsync operation on the server.

        Blocking Send ping request for selected IPv6 items with Ping Count and Payload size.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPingWithCountAndPayloadAsync(DestIP=string, PingCount=number, PingInterval=number, PayloadSize=number, async_operation=bool)list
        ------------------------------------------------------------------------------------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - PingCount (number): This parameter requires a pingCount of type kInteger
        - PingInterval (number): This parameter requires a pingInterval of type kInteger
        - PayloadSize (number): This parameter requires a payloadSize of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPingWithCountAndPayloadAsync(DestIP=string, PingCount=number, PingInterval=number, PayloadSize=number, SessionIndices=list, async_operation=bool)list
        ---------------------------------------------------------------------------------------------------------------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - PingCount (number): This parameter requires a pingCount of type kInteger
        - PingInterval (number): This parameter requires a pingInterval of type kInteger
        - PayloadSize (number): This parameter requires a payloadSize of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPingWithCountAndPayloadAsync(SessionIndices=string, DestIP=string, PingCount=number, PingInterval=number, PayloadSize=number, async_operation=bool)list
        -----------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a destIP of type kString
        - DestIP (str): This parameter requires a pingCount of type kInteger
        - PingCount (number): This parameter requires a pingInterval of type kInteger
        - PingInterval (number): This parameter requires a payloadSize of type kInteger
        - PayloadSize (number): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute(
            "sendPingWithCountAndPayloadAsync", payload=payload, response_object=None
        )

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
        Address=None,
        CustomLinkLocalAddress=None,
        DiscoverGatewayIp=None,
        GatewayIp=None,
        IncludeRaPrefix=None,
        ManualGatewayMac=None,
        Prefix=None,
        ResolveGateway=None,
        SendRa=None,
    ):
        """Base class infrastructure that gets a list of ipv6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Address (str): optional regex of address
        - CustomLinkLocalAddress (str): optional regex of customLinkLocalAddress
        - DiscoverGatewayIp (str): optional regex of discoverGatewayIp
        - GatewayIp (str): optional regex of gatewayIp
        - IncludeRaPrefix (str): optional regex of includeRaPrefix
        - ManualGatewayMac (str): optional regex of manualGatewayMac
        - Prefix (str): optional regex of prefix
        - ResolveGateway (str): optional regex of resolveGateway
        - SendRa (str): optional regex of sendRa

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
