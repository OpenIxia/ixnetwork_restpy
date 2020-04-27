# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class L3Site(Base):
    """This object represents a VPN layer 3 site to be used with internal neighbors.
    The L3Site class encapsulates a list of l3Site resources that are managed by the user.
    A list of resources can be retrieved from the server using the L3Site.find() method.
    The list can be managed by using the L3Site.add() and L3Site.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l3Site'

    def __init__(self, parent):
        super(L3Site, self).__init__(parent)

    @property
    def ImportTarget(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.importtarget_52aba3cb7f6338c2feccae080a25e976.ImportTarget): An instance of the ImportTarget class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.importtarget_52aba3cb7f6338c2feccae080a25e976 import ImportTarget
        return ImportTarget(self)._select()

    @property
    def LearnedRoute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_6f88f1d1d3e4c2d419cc616fa12fdc2d.LearnedRoute): An instance of the LearnedRoute class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_6f88f1d1d3e4c2d419cc616fa12fdc2d import LearnedRoute
        return LearnedRoute(self)

    @property
    def LearnedRouteIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedrouteipv6_fdef4758ad13bb42ae07821a7635e378.LearnedRouteIpv6): An instance of the LearnedRouteIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedrouteipv6_fdef4758ad13bb42ae07821a7635e378 import LearnedRouteIpv6
        return LearnedRouteIpv6(self)

    @property
    def Multicast(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicast_8ef6164921af4904d2878f04e4dbf9cf.Multicast): An instance of the Multicast class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicast_8ef6164921af4904d2878f04e4dbf9cf import Multicast
        return Multicast(self)._select()

    @property
    def MulticastReceiverSite(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastreceiversite_a6dd0f4602c1c6f74114129cf93afe3d.MulticastReceiverSite): An instance of the MulticastReceiverSite class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastreceiversite_a6dd0f4602c1c6f74114129cf93afe3d import MulticastReceiverSite
        return MulticastReceiverSite(self)

    @property
    def MulticastSenderSite(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastsendersite_c0ab83b7e5f56c74a62506fef05b9425.MulticastSenderSite): An instance of the MulticastSenderSite class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastsendersite_c0ab83b7e5f56c74a62506fef05b9425 import MulticastSenderSite
        return MulticastSenderSite(self)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_7c2e4f761727ffdf05fdff9d4a3947b0.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_7c2e4f761727ffdf05fdff9d4a3947b0 import OpaqueValueElement
        return OpaqueValueElement(self)

    @property
    def Target(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.target_293cbb2af232bf58a8625cc4ede579a1.Target): An instance of the Target class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.target_293cbb2af232bf58a8625cc4ede579a1 import Target
        return Target(self)._select()

    @property
    def UmhImportTarget(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhimporttarget_55ae39453aafd245655d33ffdf8b3cf3.UmhImportTarget): An instance of the UmhImportTarget class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhimporttarget_55ae39453aafd245655d33ffdf8b3cf3 import UmhImportTarget
        return UmhImportTarget(self)._select()

    @property
    def UmhSelectionRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhselectionrouterange_12592a8223aec2b7fb2f42f5d293639c.UmhSelectionRouteRange): An instance of the UmhSelectionRouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhselectionrouterange_12592a8223aec2b7fb2f42f5d293639c import UmhSelectionRouteRange
        return UmhSelectionRouteRange(self)

    @property
    def UmhTarget(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhtarget_96930b1a7c273f4e65165aeb74613631.UmhTarget): An instance of the UmhTarget class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.umhtarget_96930b1a7c273f4e65165aeb74613631 import UmhTarget
        return UmhTarget(self)._select()

    @property
    def VpnRouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpnrouterange_f5e2875a8bf43ac9b0985ff5ce186b07.VpnRouteRange): An instance of the VpnRouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vpnrouterange_f5e2875a8bf43ac9b0985ff5ce186b07 import VpnRouteRange
        return VpnRouteRange(self)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the L3 site is enabled.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def ExposeEachVrfAsTrafficEndpoint(self):
        """
        Returns
        -------
        - bool: If true, exposes each VRF as traffic endpoints.
        """
        return self._get_attribute('exposeEachVrfAsTrafficEndpoint')
    @ExposeEachVrfAsTrafficEndpoint.setter
    def ExposeEachVrfAsTrafficEndpoint(self, value):
        self._set_attribute('exposeEachVrfAsTrafficEndpoint', value)

    @property
    def IncludePmsiTunnelAttribute(self):
        """
        Returns
        -------
        - bool: If true, this will cause Ixia to include PMSI Tunnel Attribute inside the Intra-AS A-D route containing tunnel information to bind a mVPN to a particular RSVP-TE P2MP LSP. This attribute is not needed only when the user wants to setup S-PMSI only and also does not want to bind the PMSI to any particular P-Tunnel (P2MP LSP).
        """
        return self._get_attribute('includePmsiTunnelAttribute')
    @IncludePmsiTunnelAttribute.setter
    def IncludePmsiTunnelAttribute(self, value):
        self._set_attribute('includePmsiTunnelAttribute', value)

    @property
    def IsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, the L3 site learned information is refreshed.
        """
        return self._get_attribute('isLearnedInfoRefreshed')

    @property
    def MplsAssignedUpstreamLabel(self):
        """
        Returns
        -------
        - number: This label is used when Include PMSI Tunnel Attribute inside Intra-AS A-D Route is enabled. The PMSI Tunnel Identifier will contain this label value.
        """
        return self._get_attribute('mplsAssignedUpstreamLabel')
    @MplsAssignedUpstreamLabel.setter
    def MplsAssignedUpstreamLabel(self, value):
        self._set_attribute('mplsAssignedUpstreamLabel', value)

    @property
    def MulticastGroupAddressStep(self):
        """
        Returns
        -------
        - str: The increment step to be added to each additional Multicast Group Address.
        """
        return self._get_attribute('multicastGroupAddressStep')
    @MulticastGroupAddressStep.setter
    def MulticastGroupAddressStep(self, value):
        self._set_attribute('multicastGroupAddressStep', value)

    @property
    def RsvpP2mpId(self):
        """
        Returns
        -------
        - str: The P2MP Id represented in IP address format.
        """
        return self._get_attribute('rsvpP2mpId')
    @RsvpP2mpId.setter
    def RsvpP2mpId(self, value):
        self._set_attribute('rsvpP2mpId', value)

    @property
    def RsvpTunnelId(self):
        """
        Returns
        -------
        - number: This allows to select the P2MP LSP that can be used for this particular mVPN. An LSP is uniquely identified by P2MP-Id, Tunnel Id and Extended Tunnel ID (Tunnel Head Address
        """
        return self._get_attribute('rsvpTunnelId')
    @RsvpTunnelId.setter
    def RsvpTunnelId(self, value):
        self._set_attribute('rsvpTunnelId', value)

    @property
    def SameRtAsL3SiteRt(self):
        """
        Returns
        -------
        - bool: If enabled, this allows UMH VRF to use same RT as configured in l3 site
        """
        return self._get_attribute('sameRtAsL3SiteRt')
    @SameRtAsL3SiteRt.setter
    def SameRtAsL3SiteRt(self, value):
        self._set_attribute('sameRtAsL3SiteRt', value)

    @property
    def SameTargetListAsL3SiteTargetList(self):
        """
        Returns
        -------
        - bool: If enabled, this allows UMH VRF to use same target list as configured in l3 site
        """
        return self._get_attribute('sameTargetListAsL3SiteTargetList')
    @SameTargetListAsL3SiteTargetList.setter
    def SameTargetListAsL3SiteTargetList(self, value):
        self._set_attribute('sameTargetListAsL3SiteTargetList', value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        """
        return self._get_attribute('trafficGroupId')
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute('trafficGroupId', value)

    @property
    def TunnelType(self):
        """
        Returns
        -------
        - str(tunnelTypePimGreRosenDraft | tunnelTypeRsvpP2mp | tunnelTypeMldpP2mp): The tunnel type.
        """
        return self._get_attribute('tunnelType')
    @TunnelType.setter
    def TunnelType(self, value):
        self._set_attribute('tunnelType', value)

    @property
    def UseUpstreamAssignedLabel(self):
        """
        Returns
        -------
        - bool: This field indicates whether the configured upstream label AS needs to be used. If false, the Upstream Assigned Label field is disabled.
        """
        return self._get_attribute('useUpstreamAssignedLabel')
    @UseUpstreamAssignedLabel.setter
    def UseUpstreamAssignedLabel(self, value):
        self._set_attribute('useUpstreamAssignedLabel', value)

    @property
    def VrfCount(self):
        """
        Returns
        -------
        - number: Number of VRFs within the VRF Range.
        """
        return self._get_attribute('vrfCount')
    @VrfCount.setter
    def VrfCount(self, value):
        self._set_attribute('vrfCount', value)

    def update(self, Enabled=None, ExposeEachVrfAsTrafficEndpoint=None, IncludePmsiTunnelAttribute=None, MplsAssignedUpstreamLabel=None, MulticastGroupAddressStep=None, RsvpP2mpId=None, RsvpTunnelId=None, SameRtAsL3SiteRt=None, SameTargetListAsL3SiteTargetList=None, TrafficGroupId=None, TunnelType=None, UseUpstreamAssignedLabel=None, VrfCount=None):
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
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        - TunnelType (str(tunnelTypePimGreRosenDraft | tunnelTypeRsvpP2mp | tunnelTypeMldpP2mp)): The tunnel type.
        - UseUpstreamAssignedLabel (bool): This field indicates whether the configured upstream label AS needs to be used. If false, the Upstream Assigned Label field is disabled.
        - VrfCount (number): Number of VRFs within the VRF Range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, Enabled=None, ExposeEachVrfAsTrafficEndpoint=None, IncludePmsiTunnelAttribute=None, MplsAssignedUpstreamLabel=None, MulticastGroupAddressStep=None, RsvpP2mpId=None, RsvpTunnelId=None, SameRtAsL3SiteRt=None, SameTargetListAsL3SiteTargetList=None, TrafficGroupId=None, TunnelType=None, UseUpstreamAssignedLabel=None, VrfCount=None):
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
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
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
        return self._create(locals())

    def remove(self):
        """Deletes all the contained l3Site resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, ExposeEachVrfAsTrafficEndpoint=None, IncludePmsiTunnelAttribute=None, IsLearnedInfoRefreshed=None, MplsAssignedUpstreamLabel=None, MulticastGroupAddressStep=None, RsvpP2mpId=None, RsvpTunnelId=None, SameRtAsL3SiteRt=None, SameTargetListAsL3SiteTargetList=None, TrafficGroupId=None, TunnelType=None, UseUpstreamAssignedLabel=None, VrfCount=None):
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
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
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
        return self._select(locals())

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

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        This function allows to refresh the BGP learned information from the DUT.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
