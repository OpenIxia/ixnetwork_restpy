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


class MulticastSenderSite(Base):
    """Configures the values for the multicast sender site.
    The MulticastSenderSite class encapsulates a list of multicastSenderSite resources that are managed by the user.
    A list of resources can be retrieved from the server using the MulticastSenderSite.find() method.
    The list can be managed by using the MulticastSenderSite.add() and MulticastSenderSite.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'multicastSenderSite'
    _SDM_ATT_MAP = {
        'AddressFamilyType': 'addressFamilyType',
        'Enabled': 'enabled',
        'GroupAddressCount': 'groupAddressCount',
        'GroupMaskWidth': 'groupMaskWidth',
        'IncludeIpv6ExplicitNullLabel': 'includeIpv6ExplicitNullLabel',
        'MplsAssignedUpstreamLabel': 'mplsAssignedUpstreamLabel',
        'MplsAssignedUpstreamLabelStep': 'mplsAssignedUpstreamLabelStep',
        'SPmsiRsvpP2mpId': 'sPmsiRsvpP2mpId',
        'SPmsiRsvpP2mpIdAsNumber': 'sPmsiRsvpP2mpIdAsNumber',
        'SPmsiRsvpP2mpIdStep': 'sPmsiRsvpP2mpIdStep',
        'SPmsiRsvpTunnelCount': 'sPmsiRsvpTunnelCount',
        'SPmsiRsvpTunnelId': 'sPmsiRsvpTunnelId',
        'SPmsiRsvpTunnelIdStep': 'sPmsiRsvpTunnelIdStep',
        'SPmsiTrafficGroupId': 'sPmsiTrafficGroupId',
        'SPmsiTunnelCount': 'sPmsiTunnelCount',
        'SendTriggeredSourceActiveAdRoute': 'sendTriggeredSourceActiveAdRoute',
        'SetLeafInformationRequiredBit': 'setLeafInformationRequiredBit',
        'SourceAddressCount': 'sourceAddressCount',
        'SourceGroupMapping': 'sourceGroupMapping',
        'SourceMaskWidth': 'sourceMaskWidth',
        'StartGroupAddress': 'startGroupAddress',
        'StartSourceAddress': 'startSourceAddress',
        'TuunelType': 'tuunelType',
        'UseUpstreamAssignedLabel': 'useUpstreamAssignedLabel',
    }

    def __init__(self, parent):
        super(MulticastSenderSite, self).__init__(parent)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_0125173541665eff2bf2844a26c5299f.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_0125173541665eff2bf2844a26c5299f import OpaqueValueElement
        return OpaqueValueElement(self)

    @property
    def AddressFamilyType(self):
        """
        Returns
        -------
        - str(addressFamilyIpv4 | addressFamilyIpv6): Indicates the IPv4/IPv6 interface id of the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AddressFamilyType'])
    @AddressFamilyType.setter
    def AddressFamilyType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AddressFamilyType'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables use of the multicast Sender site.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def GroupAddressCount(self):
        """
        Returns
        -------
        - number: The number of group addresses to be included in the Register message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupAddressCount'])
    @GroupAddressCount.setter
    def GroupAddressCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupAddressCount'], value)

    @property
    def GroupMaskWidth(self):
        """
        Returns
        -------
        - number: The number of bits in the network mask used with the Group Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupMaskWidth'])
    @GroupMaskWidth.setter
    def GroupMaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GroupMaskWidth'], value)

    @property
    def IncludeIpv6ExplicitNullLabel(self):
        """
        Returns
        -------
        - bool: If true, allows to include Explicit NULL label (2) in I-PMSI IPv6 PE-to-CE Traffic.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeIpv6ExplicitNullLabel'])
    @IncludeIpv6ExplicitNullLabel.setter
    def IncludeIpv6ExplicitNullLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeIpv6ExplicitNullLabel'], value)

    @property
    def MplsAssignedUpstreamLabel(self):
        """
        Returns
        -------
        - number: This helps to assign unique upstream assigned label for each flow. This is applicable only if Use Upstream Assigned Label is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsAssignedUpstreamLabel'])
    @MplsAssignedUpstreamLabel.setter
    def MplsAssignedUpstreamLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsAssignedUpstreamLabel'], value)

    @property
    def MplsAssignedUpstreamLabelStep(self):
        """
        Returns
        -------
        - number: S-PMSI A-D route is sent with this Upstream Label. This is applicable only if Use Upstream Assigned Label is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MplsAssignedUpstreamLabelStep'])
    @MplsAssignedUpstreamLabelStep.setter
    def MplsAssignedUpstreamLabelStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MplsAssignedUpstreamLabelStep'], value)

    @property
    def SPmsiRsvpP2mpId(self):
        """
        Returns
        -------
        - str: The P2MP Id represented in IP address format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiRsvpP2mpId'])
    @SPmsiRsvpP2mpId.setter
    def SPmsiRsvpP2mpId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiRsvpP2mpId'], value)

    @property
    def SPmsiRsvpP2mpIdAsNumber(self):
        """
        Returns
        -------
        - number: The P2MP Id represented in integer format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiRsvpP2mpIdAsNumber'])
    @SPmsiRsvpP2mpIdAsNumber.setter
    def SPmsiRsvpP2mpIdAsNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiRsvpP2mpIdAsNumber'], value)

    @property
    def SPmsiRsvpP2mpIdStep(self):
        """
        Returns
        -------
        - number: Indicates the P2MP ID. This accepts only integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiRsvpP2mpIdStep'])
    @SPmsiRsvpP2mpIdStep.setter
    def SPmsiRsvpP2mpIdStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiRsvpP2mpIdStep'], value)

    @property
    def SPmsiRsvpTunnelCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: The total count of the S-PMSI RSVP Tunnel Count.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiRsvpTunnelCount'])
    @SPmsiRsvpTunnelCount.setter
    def SPmsiRsvpTunnelCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiRsvpTunnelCount'], value)

    @property
    def SPmsiRsvpTunnelId(self):
        """
        Returns
        -------
        - number: The first Tunnel ID value in the range of Tunnel IDs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiRsvpTunnelId'])
    @SPmsiRsvpTunnelId.setter
    def SPmsiRsvpTunnelId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiRsvpTunnelId'], value)

    @property
    def SPmsiRsvpTunnelIdStep(self):
        """
        Returns
        -------
        - number: Indicates the P2MP ID. This accepts only integer values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiRsvpTunnelIdStep'])
    @SPmsiRsvpTunnelIdStep.setter
    def SPmsiRsvpTunnelIdStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiRsvpTunnelIdStep'], value)

    @property
    def SPmsiTrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): Creates traffic using MPLS Labels of S-PMSI Tunnel and S-PMSI Upstream Assigned Label.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiTrafficGroupId'])
    @SPmsiTrafficGroupId.setter
    def SPmsiTrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiTrafficGroupId'], value)

    @property
    def SPmsiTunnelCount(self):
        """
        Returns
        -------
        - number: Signifies the SPMSI tunnel count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SPmsiTunnelCount'])
    @SPmsiTunnelCount.setter
    def SPmsiTunnelCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SPmsiTunnelCount'], value)

    @property
    def SendTriggeredSourceActiveAdRoute(self):
        """
        Returns
        -------
        - bool: If true, allows to send the Source Active A-D Route after receiving Source Tree Join C-Multicast route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendTriggeredSourceActiveAdRoute'])
    @SendTriggeredSourceActiveAdRoute.setter
    def SendTriggeredSourceActiveAdRoute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendTriggeredSourceActiveAdRoute'], value)

    @property
    def SetLeafInformationRequiredBit(self):
        """
        Returns
        -------
        - bool: his is used to send S-PMSI A-D Route with Leaf Information Required bit Set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetLeafInformationRequiredBit'])
    @SetLeafInformationRequiredBit.setter
    def SetLeafInformationRequiredBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetLeafInformationRequiredBit'], value)

    @property
    def SourceAddressCount(self):
        """
        Returns
        -------
        - number: The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values of the Source Address and the Source Mask Width.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddressCount'])
    @SourceAddressCount.setter
    def SourceAddressCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAddressCount'], value)

    @property
    def SourceGroupMapping(self):
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne): Indicates the source group mapping.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceGroupMapping'])
    @SourceGroupMapping.setter
    def SourceGroupMapping(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceGroupMapping'], value)

    @property
    def SourceMaskWidth(self):
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceMaskWidth'])
    @SourceMaskWidth.setter
    def SourceMaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceMaskWidth'], value)

    @property
    def StartGroupAddress(self):
        """
        Returns
        -------
        - str: The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartGroupAddress'])
    @StartGroupAddress.setter
    def StartGroupAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartGroupAddress'], value)

    @property
    def StartSourceAddress(self):
        """
        Returns
        -------
        - str: The first IPv4 or IPv6 source address to be included in this Register message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSourceAddress'])
    @StartSourceAddress.setter
    def StartSourceAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSourceAddress'], value)

    @property
    def TuunelType(self):
        """
        Returns
        -------
        - str(): the tunnel type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TuunelType'])
    @TuunelType.setter
    def TuunelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TuunelType'], value)

    @property
    def UseUpstreamAssignedLabel(self):
        """
        Returns
        -------
        - bool: Indicates whether upstream label as configured be used or not. If this field is false, then MPLS Assigned Upstream Label and MPLS Assigned Upstream Label Step fields are disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseUpstreamAssignedLabel'])
    @UseUpstreamAssignedLabel.setter
    def UseUpstreamAssignedLabel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseUpstreamAssignedLabel'], value)

    def update(self, AddressFamilyType=None, Enabled=None, GroupAddressCount=None, GroupMaskWidth=None, IncludeIpv6ExplicitNullLabel=None, MplsAssignedUpstreamLabel=None, MplsAssignedUpstreamLabelStep=None, SPmsiRsvpP2mpId=None, SPmsiRsvpP2mpIdAsNumber=None, SPmsiRsvpP2mpIdStep=None, SPmsiRsvpTunnelCount=None, SPmsiRsvpTunnelId=None, SPmsiRsvpTunnelIdStep=None, SPmsiTrafficGroupId=None, SPmsiTunnelCount=None, SendTriggeredSourceActiveAdRoute=None, SetLeafInformationRequiredBit=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddress=None, StartSourceAddress=None, TuunelType=None, UseUpstreamAssignedLabel=None):
        """Updates multicastSenderSite resource on the server.

        Args
        ----
        - AddressFamilyType (str(addressFamilyIpv4 | addressFamilyIpv6)): Indicates the IPv4/IPv6 interface id of the router.
        - Enabled (bool): Enables or disables use of the multicast Sender site.
        - GroupAddressCount (number): The number of group addresses to be included in the Register message.
        - GroupMaskWidth (number): The number of bits in the network mask used with the Group Address.
        - IncludeIpv6ExplicitNullLabel (bool): If true, allows to include Explicit NULL label (2) in I-PMSI IPv6 PE-to-CE Traffic.
        - MplsAssignedUpstreamLabel (number): This helps to assign unique upstream assigned label for each flow. This is applicable only if Use Upstream Assigned Label is true.
        - MplsAssignedUpstreamLabelStep (number): S-PMSI A-D route is sent with this Upstream Label. This is applicable only if Use Upstream Assigned Label is true.
        - SPmsiRsvpP2mpId (str): The P2MP Id represented in IP address format.
        - SPmsiRsvpP2mpIdAsNumber (number): The P2MP Id represented in integer format.
        - SPmsiRsvpP2mpIdStep (number): Indicates the P2MP ID. This accepts only integer values.
        - SPmsiRsvpTunnelCount (number): The total count of the S-PMSI RSVP Tunnel Count.
        - SPmsiRsvpTunnelId (number): The first Tunnel ID value in the range of Tunnel IDs.
        - SPmsiRsvpTunnelIdStep (number): Indicates the P2MP ID. This accepts only integer values.
        - SPmsiTrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Creates traffic using MPLS Labels of S-PMSI Tunnel and S-PMSI Upstream Assigned Label.
        - SPmsiTunnelCount (number): Signifies the SPMSI tunnel count
        - SendTriggeredSourceActiveAdRoute (bool): If true, allows to send the Source Active A-D Route after receiving Source Tree Join C-Multicast route.
        - SetLeafInformationRequiredBit (bool): his is used to send S-PMSI A-D Route with Leaf Information Required bit Set.
        - SourceAddressCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values of the Source Address and the Source Mask Width.
        - SourceGroupMapping (str(fullyMeshed | oneToOne)): Indicates the source group mapping.
        - SourceMaskWidth (number): The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        - StartGroupAddress (str): The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        - StartSourceAddress (str): The first IPv4 or IPv6 source address to be included in this Register message.
        - TuunelType (str()): the tunnel type.
        - UseUpstreamAssignedLabel (bool): Indicates whether upstream label as configured be used or not. If this field is false, then MPLS Assigned Upstream Label and MPLS Assigned Upstream Label Step fields are disabled.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AddressFamilyType=None, Enabled=None, GroupAddressCount=None, GroupMaskWidth=None, IncludeIpv6ExplicitNullLabel=None, MplsAssignedUpstreamLabel=None, MplsAssignedUpstreamLabelStep=None, SPmsiRsvpP2mpId=None, SPmsiRsvpP2mpIdAsNumber=None, SPmsiRsvpP2mpIdStep=None, SPmsiRsvpTunnelCount=None, SPmsiRsvpTunnelId=None, SPmsiRsvpTunnelIdStep=None, SPmsiTrafficGroupId=None, SPmsiTunnelCount=None, SendTriggeredSourceActiveAdRoute=None, SetLeafInformationRequiredBit=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddress=None, StartSourceAddress=None, TuunelType=None, UseUpstreamAssignedLabel=None):
        """Adds a new multicastSenderSite resource on the server and adds it to the container.

        Args
        ----
        - AddressFamilyType (str(addressFamilyIpv4 | addressFamilyIpv6)): Indicates the IPv4/IPv6 interface id of the router.
        - Enabled (bool): Enables or disables use of the multicast Sender site.
        - GroupAddressCount (number): The number of group addresses to be included in the Register message.
        - GroupMaskWidth (number): The number of bits in the network mask used with the Group Address.
        - IncludeIpv6ExplicitNullLabel (bool): If true, allows to include Explicit NULL label (2) in I-PMSI IPv6 PE-to-CE Traffic.
        - MplsAssignedUpstreamLabel (number): This helps to assign unique upstream assigned label for each flow. This is applicable only if Use Upstream Assigned Label is true.
        - MplsAssignedUpstreamLabelStep (number): S-PMSI A-D route is sent with this Upstream Label. This is applicable only if Use Upstream Assigned Label is true.
        - SPmsiRsvpP2mpId (str): The P2MP Id represented in IP address format.
        - SPmsiRsvpP2mpIdAsNumber (number): The P2MP Id represented in integer format.
        - SPmsiRsvpP2mpIdStep (number): Indicates the P2MP ID. This accepts only integer values.
        - SPmsiRsvpTunnelCount (number): The total count of the S-PMSI RSVP Tunnel Count.
        - SPmsiRsvpTunnelId (number): The first Tunnel ID value in the range of Tunnel IDs.
        - SPmsiRsvpTunnelIdStep (number): Indicates the P2MP ID. This accepts only integer values.
        - SPmsiTrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Creates traffic using MPLS Labels of S-PMSI Tunnel and S-PMSI Upstream Assigned Label.
        - SPmsiTunnelCount (number): Signifies the SPMSI tunnel count
        - SendTriggeredSourceActiveAdRoute (bool): If true, allows to send the Source Active A-D Route after receiving Source Tree Join C-Multicast route.
        - SetLeafInformationRequiredBit (bool): his is used to send S-PMSI A-D Route with Leaf Information Required bit Set.
        - SourceAddressCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values of the Source Address and the Source Mask Width.
        - SourceGroupMapping (str(fullyMeshed | oneToOne)): Indicates the source group mapping.
        - SourceMaskWidth (number): The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        - StartGroupAddress (str): The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        - StartSourceAddress (str): The first IPv4 or IPv6 source address to be included in this Register message.
        - TuunelType (str()): the tunnel type.
        - UseUpstreamAssignedLabel (bool): Indicates whether upstream label as configured be used or not. If this field is false, then MPLS Assigned Upstream Label and MPLS Assigned Upstream Label Step fields are disabled.

        Returns
        -------
        - self: This instance with all currently retrieved multicastSenderSite resources using find and the newly added multicastSenderSite resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained multicastSenderSite resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AddressFamilyType=None, Enabled=None, GroupAddressCount=None, GroupMaskWidth=None, IncludeIpv6ExplicitNullLabel=None, MplsAssignedUpstreamLabel=None, MplsAssignedUpstreamLabelStep=None, SPmsiRsvpP2mpId=None, SPmsiRsvpP2mpIdAsNumber=None, SPmsiRsvpP2mpIdStep=None, SPmsiRsvpTunnelCount=None, SPmsiRsvpTunnelId=None, SPmsiRsvpTunnelIdStep=None, SPmsiTrafficGroupId=None, SPmsiTunnelCount=None, SendTriggeredSourceActiveAdRoute=None, SetLeafInformationRequiredBit=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddress=None, StartSourceAddress=None, TuunelType=None, UseUpstreamAssignedLabel=None):
        """Finds and retrieves multicastSenderSite resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastSenderSite resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastSenderSite resources from the server.

        Args
        ----
        - AddressFamilyType (str(addressFamilyIpv4 | addressFamilyIpv6)): Indicates the IPv4/IPv6 interface id of the router.
        - Enabled (bool): Enables or disables use of the multicast Sender site.
        - GroupAddressCount (number): The number of group addresses to be included in the Register message.
        - GroupMaskWidth (number): The number of bits in the network mask used with the Group Address.
        - IncludeIpv6ExplicitNullLabel (bool): If true, allows to include Explicit NULL label (2) in I-PMSI IPv6 PE-to-CE Traffic.
        - MplsAssignedUpstreamLabel (number): This helps to assign unique upstream assigned label for each flow. This is applicable only if Use Upstream Assigned Label is true.
        - MplsAssignedUpstreamLabelStep (number): S-PMSI A-D route is sent with this Upstream Label. This is applicable only if Use Upstream Assigned Label is true.
        - SPmsiRsvpP2mpId (str): The P2MP Id represented in IP address format.
        - SPmsiRsvpP2mpIdAsNumber (number): The P2MP Id represented in integer format.
        - SPmsiRsvpP2mpIdStep (number): Indicates the P2MP ID. This accepts only integer values.
        - SPmsiRsvpTunnelCount (number): The total count of the S-PMSI RSVP Tunnel Count.
        - SPmsiRsvpTunnelId (number): The first Tunnel ID value in the range of Tunnel IDs.
        - SPmsiRsvpTunnelIdStep (number): Indicates the P2MP ID. This accepts only integer values.
        - SPmsiTrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Creates traffic using MPLS Labels of S-PMSI Tunnel and S-PMSI Upstream Assigned Label.
        - SPmsiTunnelCount (number): Signifies the SPMSI tunnel count
        - SendTriggeredSourceActiveAdRoute (bool): If true, allows to send the Source Active A-D Route after receiving Source Tree Join C-Multicast route.
        - SetLeafInformationRequiredBit (bool): his is used to send S-PMSI A-D Route with Leaf Information Required bit Set.
        - SourceAddressCount (number): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values of the Source Address and the Source Mask Width.
        - SourceGroupMapping (str(fullyMeshed | oneToOne)): Indicates the source group mapping.
        - SourceMaskWidth (number): The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.The default value is 32. The valid range is 1 to 128, depending on address family type.Used for (S,G) Type and (S,G, rpt) only.
        - StartGroupAddress (str): The first IPv4 or IPv6 Multicast group address in the range of group addresses included in this Register message.
        - StartSourceAddress (str): The first IPv4 or IPv6 source address to be included in this Register message.
        - TuunelType (str()): the tunnel type.
        - UseUpstreamAssignedLabel (bool): Indicates whether upstream label as configured be used or not. If this field is false, then MPLS Assigned Upstream Label and MPLS Assigned Upstream Label Step fields are disabled.

        Returns
        -------
        - self: This instance with matching multicastSenderSite resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastSenderSite data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastSenderSite resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def SwitchToSpmsi(self):
        """Executes the switchToSpmsi operation on the server.

        This exec switches the tunnel to sPMSI.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('switchToSpmsi', payload=payload, response_object=None)
