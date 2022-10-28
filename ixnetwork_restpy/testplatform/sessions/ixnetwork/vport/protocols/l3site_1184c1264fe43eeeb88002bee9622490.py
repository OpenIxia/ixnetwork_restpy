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


class L3Site(Base):
    """This object represents a VPN layer 3 site to be used with internal neighbors.
    The L3Site class encapsulates a list of l3Site resources that are managed by the user.
    A list of resources can be retrieved from the server using the L3Site.find() method.
    The list can be managed by using the L3Site.add() and L3Site.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "l3Site"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "ExposeEachVrfAsTrafficEndpoint": "exposeEachVrfAsTrafficEndpoint",
        "IncludePmsiTunnelAttribute": "includePmsiTunnelAttribute",
        "IsLearnedInfoRefreshed": "isLearnedInfoRefreshed",
        "MplsAssignedUpstreamLabel": "mplsAssignedUpstreamLabel",
        "MulticastGroupAddressStep": "multicastGroupAddressStep",
        "RsvpP2mpId": "rsvpP2mpId",
        "RsvpTunnelId": "rsvpTunnelId",
        "SameRtAsL3SiteRt": "sameRtAsL3SiteRt",
        "SameTargetListAsL3SiteTargetList": "sameTargetListAsL3SiteTargetList",
        "TrafficGroupId": "trafficGroupId",
        "TunnelType": "tunnelType",
        "UseUpstreamAssignedLabel": "useUpstreamAssignedLabel",
        "VrfCount": "vrfCount",
    }
    _SDM_ENUM_MAP = {
        "tunnelType": [
            "tunnelTypePimGreRosenDraft",
            "tunnelTypeRsvpP2mp",
            "tunnelTypeMldpP2mp",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(L3Site, self).__init__(parent, list_op)

    @property
    def ImportTarget(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.importtarget_5de62449ab162506e7d4343bed6cdae9.ImportTarget): An instance of the ImportTarget class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.importtarget_5de62449ab162506e7d4343bed6cdae9 import (
            ImportTarget,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ImportTarget", None) is not None:
                return self._properties.get("ImportTarget")
        return ImportTarget(self)._select()

    @property
    def LearnedRoute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_bf92411e6ec4c496c037ba0073ceb01c.LearnedRoute): An instance of the LearnedRoute class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_bf92411e6ec4c496c037ba0073ceb01c import (
            LearnedRoute,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedRoute", None) is not None:
                return self._properties.get("LearnedRoute")
        return LearnedRoute(self)

    @property
    def LearnedRouteIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedrouteipv6_e146efad7b2709c72b7ef3489e6a153e.LearnedRouteIpv6): An instance of the LearnedRouteIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedrouteipv6_e146efad7b2709c72b7ef3489e6a153e import (
            LearnedRouteIpv6,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedRouteIpv6", None) is not None:
                return self._properties.get("LearnedRouteIpv6")
        return LearnedRouteIpv6(self)

    @property
    def Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicast_753c518b5f1dc0635a787650b6627859.Multicast): An instance of the Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicast_753c518b5f1dc0635a787650b6627859 import (
            Multicast,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Multicast", None) is not None:
                return self._properties.get("Multicast")
        return Multicast(self)._select()

    @property
    def MulticastReceiverSite(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastreceiversite_cac2a5b53ffba8f61d029919a79e1343.MulticastReceiverSite): An instance of the MulticastReceiverSite class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastreceiversite_cac2a5b53ffba8f61d029919a79e1343 import (
            MulticastReceiverSite,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastReceiverSite", None) is not None:
                return self._properties.get("MulticastReceiverSite")
        return MulticastReceiverSite(self)

    @property
    def MulticastSenderSite(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastsendersite_83f523e9811617a00cbff1d57dcf5a27.MulticastSenderSite): An instance of the MulticastSenderSite class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastsendersite_83f523e9811617a00cbff1d57dcf5a27 import (
            MulticastSenderSite,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastSenderSite", None) is not None:
                return self._properties.get("MulticastSenderSite")
        return MulticastSenderSite(self)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_09e1c3fa84ec75f297eac04830ce7156.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_09e1c3fa84ec75f297eac04830ce7156 import (
            OpaqueValueElement,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpaqueValueElement", None) is not None:
                return self._properties.get("OpaqueValueElement")
        return OpaqueValueElement(self)

    @property
    def Target(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.target_c6cbdddc7771a9b67858085e8d346456.Target): An instance of the Target class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.target_c6cbdddc7771a9b67858085e8d346456 import (
            Target,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Target", None) is not None:
                return self._properties.get("Target")
        return Target(self)._select()

    @property
    def UmhImportTarget(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhimporttarget_6c3dc34540c306cc15b2ab9bf4d49565.UmhImportTarget): An instance of the UmhImportTarget class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhimporttarget_6c3dc34540c306cc15b2ab9bf4d49565 import (
            UmhImportTarget,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UmhImportTarget", None) is not None:
                return self._properties.get("UmhImportTarget")
        return UmhImportTarget(self)._select()

    @property
    def UmhSelectionRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhselectionrouterange_b1fb332d421ad602bbe1bf5ee8bdc230.UmhSelectionRouteRange): An instance of the UmhSelectionRouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhselectionrouterange_b1fb332d421ad602bbe1bf5ee8bdc230 import (
            UmhSelectionRouteRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UmhSelectionRouteRange", None) is not None:
                return self._properties.get("UmhSelectionRouteRange")
        return UmhSelectionRouteRange(self)

    @property
    def UmhTarget(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhtarget_7fd706c876de38f4f7aea952e9a68a18.UmhTarget): An instance of the UmhTarget class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhtarget_7fd706c876de38f4f7aea952e9a68a18 import (
            UmhTarget,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UmhTarget", None) is not None:
                return self._properties.get("UmhTarget")
        return UmhTarget(self)._select()

    @property
    def VpnRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpnrouterange_63f34e6d80ef976eee3f8513cd149760.VpnRouteRange): An instance of the VpnRouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpnrouterange_63f34e6d80ef976eee3f8513cd149760 import (
            VpnRouteRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("VpnRouteRange", None) is not None:
                return self._properties.get("VpnRouteRange")
        return VpnRouteRange(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the L3 site is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ExposeEachVrfAsTrafficEndpoint(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, exposes each VRF as traffic endpoints.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExposeEachVrfAsTrafficEndpoint"])

    @ExposeEachVrfAsTrafficEndpoint.setter
    def ExposeEachVrfAsTrafficEndpoint(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExposeEachVrfAsTrafficEndpoint"], value)

    @property
    def IncludePmsiTunnelAttribute(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this will cause Ixia to include PMSI Tunnel Attribute inside the Intra-AS A-D route containing tunnel information to bind a mVPN to a particular RSVP-TE P2MP LSP. This attribute is not needed only when the user wants to setup S-PMSI only and also does not want to bind the PMSI to any particular P-Tunnel (P2MP LSP).
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludePmsiTunnelAttribute"])

    @IncludePmsiTunnelAttribute.setter
    def IncludePmsiTunnelAttribute(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludePmsiTunnelAttribute"], value)

    @property
    def IsLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the L3 site learned information is refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLearnedInfoRefreshed"])

    @property
    def MplsAssignedUpstreamLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This label is used when Include PMSI Tunnel Attribute inside Intra-AS A-D Route is enabled. The PMSI Tunnel Identifier will contain this label value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MplsAssignedUpstreamLabel"])

    @MplsAssignedUpstreamLabel.setter
    def MplsAssignedUpstreamLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MplsAssignedUpstreamLabel"], value)

    @property
    def MulticastGroupAddressStep(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The increment step to be added to each additional Multicast Group Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastGroupAddressStep"])

    @MulticastGroupAddressStep.setter
    def MulticastGroupAddressStep(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastGroupAddressStep"], value)

    @property
    def RsvpP2mpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The P2MP Id represented in IP address format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpP2mpId"])

    @RsvpP2mpId.setter
    def RsvpP2mpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpP2mpId"], value)

    @property
    def RsvpTunnelId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This allows to select the P2MP LSP that can be used for this particular mVPN. An LSP is uniquely identified by P2MP-Id, Tunnel Id and Extended Tunnel ID (Tunnel Head Address
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpTunnelId"])

    @RsvpTunnelId.setter
    def RsvpTunnelId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpTunnelId"], value)

    @property
    def SameRtAsL3SiteRt(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this allows UMH VRF to use same RT as configured in l3 site
        """
        return self._get_attribute(self._SDM_ATT_MAP["SameRtAsL3SiteRt"])

    @SameRtAsL3SiteRt.setter
    def SameRtAsL3SiteRt(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SameRtAsL3SiteRt"], value)

    @property
    def SameTargetListAsL3SiteTargetList(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, this allows UMH VRF to use same target list as configured in l3 site
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["SameTargetListAsL3SiteTargetList"]
        )

    @SameTargetListAsL3SiteTargetList.setter
    def SameTargetListAsL3SiteTargetList(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["SameTargetListAsL3SiteTargetList"], value
        )

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    @property
    def TunnelType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(tunnelTypePimGreRosenDraft | tunnelTypeRsvpP2mp | tunnelTypeMldpP2mp): The tunnel type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TunnelType"])

    @TunnelType.setter
    def TunnelType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TunnelType"], value)

    @property
    def UseUpstreamAssignedLabel(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This field indicates whether the configured upstream label AS needs to be used. If false, the Upstream Assigned Label field is disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseUpstreamAssignedLabel"])

    @UseUpstreamAssignedLabel.setter
    def UseUpstreamAssignedLabel(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseUpstreamAssignedLabel"], value)

    @property
    def VrfCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of VRFs within the VRF Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VrfCount"])

    @VrfCount.setter
    def VrfCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VrfCount"], value)

    def update(
        self,
        Enabled=None,
        ExposeEachVrfAsTrafficEndpoint=None,
        IncludePmsiTunnelAttribute=None,
        MplsAssignedUpstreamLabel=None,
        MulticastGroupAddressStep=None,
        RsvpP2mpId=None,
        RsvpTunnelId=None,
        SameRtAsL3SiteRt=None,
        SameTargetListAsL3SiteTargetList=None,
        TrafficGroupId=None,
        TunnelType=None,
        UseUpstreamAssignedLabel=None,
        VrfCount=None,
    ):
        # type: (bool, bool, bool, int, str, str, int, bool, bool, str, str, bool, int) -> L3Site
        """Updates l3Site resource on the server.

        Args
        ----
        - Enabled (bool): If true, the L3 site is enabled.
        - ExposeEachVrfAsTrafficEndpoint (bool): If true, exposes each VRF as traffic endpoints.
        - IncludePmsiTunnelAttribute (bool): If true, this will cause Ixia to include PMSI Tunnel Attribute inside the Intra-AS A-D route containing tunnel information to bind a mVPN to a particular RSVP-TE P2MP LSP. This attribute is not needed only when the user wants to setup S-PMSI only and also does not want to bind the PMSI to any particular P-Tunnel (P2MP LSP).
        - MplsAssignedUpstreamLabel (number): This label is used when Include PMSI Tunnel Attribute inside Intra-AS A-D Route is enabled. The PMSI Tunnel Identifier will contain this label value.
        - MulticastGroupAddressStep (str): The increment step to be added to each additional Multicast Group Address.
        - RsvpP2mpId (str): The P2MP Id represented in IP address format.
        - RsvpTunnelId (number): This allows to select the P2MP LSP that can be used for this particular mVPN. An LSP is uniquely identified by P2MP-Id, Tunnel Id and Extended Tunnel ID (Tunnel Head Address
        - SameRtAsL3SiteRt (bool): If enabled, this allows UMH VRF to use same RT as configured in l3 site
        - SameTargetListAsL3SiteTargetList (bool): If enabled, this allows UMH VRF to use same target list as configured in l3 site
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        - TunnelType (str(tunnelTypePimGreRosenDraft | tunnelTypeRsvpP2mp | tunnelTypeMldpP2mp)): The tunnel type.
        - UseUpstreamAssignedLabel (bool): This field indicates whether the configured upstream label AS needs to be used. If false, the Upstream Assigned Label field is disabled.
        - VrfCount (number): Number of VRFs within the VRF Range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        ExposeEachVrfAsTrafficEndpoint=None,
        IncludePmsiTunnelAttribute=None,
        MplsAssignedUpstreamLabel=None,
        MulticastGroupAddressStep=None,
        RsvpP2mpId=None,
        RsvpTunnelId=None,
        SameRtAsL3SiteRt=None,
        SameTargetListAsL3SiteTargetList=None,
        TrafficGroupId=None,
        TunnelType=None,
        UseUpstreamAssignedLabel=None,
        VrfCount=None,
    ):
        # type: (bool, bool, bool, int, str, str, int, bool, bool, str, str, bool, int) -> L3Site
        """Adds a new l3Site resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, the L3 site is enabled.
        - ExposeEachVrfAsTrafficEndpoint (bool): If true, exposes each VRF as traffic endpoints.
        - IncludePmsiTunnelAttribute (bool): If true, this will cause Ixia to include PMSI Tunnel Attribute inside the Intra-AS A-D route containing tunnel information to bind a mVPN to a particular RSVP-TE P2MP LSP. This attribute is not needed only when the user wants to setup S-PMSI only and also does not want to bind the PMSI to any particular P-Tunnel (P2MP LSP).
        - MplsAssignedUpstreamLabel (number): This label is used when Include PMSI Tunnel Attribute inside Intra-AS A-D Route is enabled. The PMSI Tunnel Identifier will contain this label value.
        - MulticastGroupAddressStep (str): The increment step to be added to each additional Multicast Group Address.
        - RsvpP2mpId (str): The P2MP Id represented in IP address format.
        - RsvpTunnelId (number): This allows to select the P2MP LSP that can be used for this particular mVPN. An LSP is uniquely identified by P2MP-Id, Tunnel Id and Extended Tunnel ID (Tunnel Head Address
        - SameRtAsL3SiteRt (bool): If enabled, this allows UMH VRF to use same RT as configured in l3 site
        - SameTargetListAsL3SiteTargetList (bool): If enabled, this allows UMH VRF to use same target list as configured in l3 site
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        - TunnelType (str(tunnelTypePimGreRosenDraft | tunnelTypeRsvpP2mp | tunnelTypeMldpP2mp)): The tunnel type.
        - UseUpstreamAssignedLabel (bool): This field indicates whether the configured upstream label AS needs to be used. If false, the Upstream Assigned Label field is disabled.
        - VrfCount (number): Number of VRFs within the VRF Range.

        Returns
        -------
        - self: This instance with all currently retrieved l3Site resources using find and the newly added l3Site resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained l3Site resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        ExposeEachVrfAsTrafficEndpoint=None,
        IncludePmsiTunnelAttribute=None,
        IsLearnedInfoRefreshed=None,
        MplsAssignedUpstreamLabel=None,
        MulticastGroupAddressStep=None,
        RsvpP2mpId=None,
        RsvpTunnelId=None,
        SameRtAsL3SiteRt=None,
        SameTargetListAsL3SiteTargetList=None,
        TrafficGroupId=None,
        TunnelType=None,
        UseUpstreamAssignedLabel=None,
        VrfCount=None,
    ):
        # type: (bool, bool, bool, bool, int, str, str, int, bool, bool, str, str, bool, int) -> L3Site
        """Finds and retrieves l3Site resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l3Site resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l3Site resources from the server.

        Args
        ----
        - Enabled (bool): If true, the L3 site is enabled.
        - ExposeEachVrfAsTrafficEndpoint (bool): If true, exposes each VRF as traffic endpoints.
        - IncludePmsiTunnelAttribute (bool): If true, this will cause Ixia to include PMSI Tunnel Attribute inside the Intra-AS A-D route containing tunnel information to bind a mVPN to a particular RSVP-TE P2MP LSP. This attribute is not needed only when the user wants to setup S-PMSI only and also does not want to bind the PMSI to any particular P-Tunnel (P2MP LSP).
        - IsLearnedInfoRefreshed (bool): If true, the L3 site learned information is refreshed.
        - MplsAssignedUpstreamLabel (number): This label is used when Include PMSI Tunnel Attribute inside Intra-AS A-D Route is enabled. The PMSI Tunnel Identifier will contain this label value.
        - MulticastGroupAddressStep (str): The increment step to be added to each additional Multicast Group Address.
        - RsvpP2mpId (str): The P2MP Id represented in IP address format.
        - RsvpTunnelId (number): This allows to select the P2MP LSP that can be used for this particular mVPN. An LSP is uniquely identified by P2MP-Id, Tunnel Id and Extended Tunnel ID (Tunnel Head Address
        - SameRtAsL3SiteRt (bool): If enabled, this allows UMH VRF to use same RT as configured in l3 site
        - SameTargetListAsL3SiteTargetList (bool): If enabled, this allows UMH VRF to use same target list as configured in l3 site
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        - TunnelType (str(tunnelTypePimGreRosenDraft | tunnelTypeRsvpP2mp | tunnelTypeMldpP2mp)): The tunnel type.
        - UseUpstreamAssignedLabel (bool): This field indicates whether the configured upstream label AS needs to be used. If false, the Upstream Assigned Label field is disabled.
        - VrfCount (number): Number of VRFs within the VRF Range.

        Returns
        -------
        - self: This instance with matching l3Site resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l3Site data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l3Site resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedInfo operation on the server.

        This function allows to refresh the BGP learned information from the DUT.

        refreshLearnedInfo(async_operation=bool)bool
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshLearnedInfo", payload=payload, response_object=None
        )
