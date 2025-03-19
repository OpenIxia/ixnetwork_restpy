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


class BgpMVpnSenderSiteSpmsiV4(Base):
    """Bgp MVPN Sender S-PMSI Sites Properties
    The BgpMVpnSenderSiteSpmsiV4 class encapsulates a list of bgpMVpnSenderSiteSpmsiV4 resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpMVpnSenderSiteSpmsiV4.find() method.
    The list can be managed by using the BgpMVpnSenderSiteSpmsiV4.add() and BgpMVpnSenderSiteSpmsiV4.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "bgpMVpnSenderSiteSpmsiV4"
    _SDM_ATT_MAP = {
        "BFRId": "BFRId",
        "BFRIpv4Prefix": "BFRIpv4Prefix",
        "BFRIpv6Prefix": "BFRIpv6Prefix",
        "BFRPrefixType": "BFRPrefixType",
        "BIERSubDomainId": "BIERSubDomainId",
        "SPMSIRouteType": "SPMSIRouteType",
        "AutoConstructBitString": "autoConstructBitString",
        "BierBitStringLength": "bierBitStringLength",
        "BitString": "bitString",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Dscp": "dscp",
        "EnableLIRpFBit": "enableLIRpFBit",
        "EnableTRM": "enableTRM",
        "Entropy": "entropy",
        "ExpectSpecificLeafAdFromDut": "expectSpecificLeafAdFromDut",
        "GroupAddress": "groupAddress",
        "GroupAddressStep": "groupAddressStep",
        "MulticastTunnelType": "multicastTunnelType",
        "Name": "name",
        "NextProtocol": "nextProtocol",
        "Oam": "oam",
        "Rsv": "rsv",
        "SPmsiRsvpP2mpId": "sPmsiRsvpP2mpId",
        "SPmsiRsvpP2mpIdAsNumber": "sPmsiRsvpP2mpIdAsNumber",
        "SPmsiRsvpP2mpIdStep": "sPmsiRsvpP2mpIdStep",
        "SPmsiRsvpTunnelId": "sPmsiRsvpTunnelId",
        "SPmsiRsvpTunnelIdStep": "sPmsiRsvpTunnelIdStep",
        "SPmsiTunnelCount": "sPmsiTunnelCount",
        "SPmsirootAddress": "sPmsirootAddress",
        "SenderAddressPRootNodeAddress": "senderAddressPRootNodeAddress",
        "SenderAddressPRootNodeAddressStep": "senderAddressPRootNodeAddressStep",
        "SetLeafInformationRequiredBit": "setLeafInformationRequiredBit",
        "SiCount": "siCount",
        "SrLabelStart": "srLabelStart",
        "SrLabelStep": "srLabelStep",
        "TrafficBfrId": "trafficBfrId",
        "UpstreamOrDownstreamAssignedLabel": "upstreamOrDownstreamAssignedLabel",
        "UpstreamOrDownstreamAssignedLabelStep": "upstreamOrDownstreamAssignedLabelStep",
        "UseSameBfrIdInTraffic": "useSameBfrIdInTraffic",
        "UseUpstreamOrDownstreamAssignedLabel": "useUpstreamOrDownstreamAssignedLabel",
        "Version": "version",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BgpMVpnSenderSiteSpmsiV4, self).__init__(parent, list_op)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_ecb45bfaef4008cb27346c98c45748b2.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_ecb45bfaef4008cb27346c98c45748b2 import (
            CMacProperties,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CMacProperties", None) is not None:
                return self._properties.get("CMacProperties")
        return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_f9fe868ed341d666199597001888e18d.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_f9fe868ed341d666199597001888e18d import (
            EvpnIPv4PrefixRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnIPv4PrefixRange", None) is not None:
                return self._properties.get("EvpnIPv4PrefixRange")
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_907e82e321deae422b0ee1ed0f82f2f3.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_907e82e321deae422b0ee1ed0f82f2f3 import (
            EvpnIPv6PrefixRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EvpnIPv6PrefixRange", None) is not None:
                return self._properties.get("EvpnIPv6PrefixRange")
        return EvpnIPv6PrefixRange(self)

    @property
    def PnTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57.PnTLVList): An instance of the PnTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57 import (
            PnTLVList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PnTLVList", None) is not None:
                return self._properties.get("PnTLVList")
        return PnTLVList(self)

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
    def BFRId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR-Id
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BFRId"]))

    @property
    def BFRIpv4Prefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR IPv4 Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BFRIpv4Prefix"]))

    @property
    def BFRIpv6Prefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR IPv6 Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BFRIpv6Prefix"]))

    @property
    def BFRPrefixType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFR Prefix Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BFRPrefixType"]))

    @property
    def BIERSubDomainId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BIER Sub-Domain Id
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BIERSubDomainId"])
        )

    @property
    def SPMSIRouteType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI Route Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPMSIRouteType"])
        )

    @property
    def AutoConstructBitString(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use BitString
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AutoConstructBitString"])
        )

    @property
    def BierBitStringLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bit String Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BierBitStringLength"])
        )

    @property
    def BitString(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BitString
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BitString"]))

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
    def Dscp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSCP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Dscp"]))

    @property
    def EnableLIRpFBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable LIR-pF bit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableLIRpFBit"])
        )

    @property
    def EnableTRM(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Multicast Tunnel Type will be PIM-SSM (by default).
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableTRM"])

    @EnableTRM.setter
    def EnableTRM(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableTRM"], value)

    @property
    def Entropy(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Entropy
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Entropy"]))

    @property
    def ExpectSpecificLeafAdFromDut(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Expect Specific Leaf AD From DUT. If false then Ixia expectes Leaf AD in wildcard mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExpectSpecificLeafAdFromDut"])

    @ExpectSpecificLeafAdFromDut.setter
    def ExpectSpecificLeafAdFromDut(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExpectSpecificLeafAdFromDut"], value)

    @property
    def GroupAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GroupAddress"]))

    @property
    def GroupAddressStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["GroupAddressStep"])
        )

    @property
    def MulticastTunnelType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Tunnel Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastTunnelType"])
        )

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
    def NextProtocol(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Next Protocol
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NextProtocol"]))

    @property
    def Oam(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): OAM
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Oam"]))

    @property
    def Rsv(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Rsv
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Rsv"]))

    @property
    def SPmsiRsvpP2mpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI RSVP P2MP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsiRsvpP2mpId"])
        )

    @property
    def SPmsiRsvpP2mpIdAsNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI RSVP P2MP ID as Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsiRsvpP2mpIdAsNumber"])
        )

    @property
    def SPmsiRsvpP2mpIdStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI RSVP P2MP ID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsiRsvpP2mpIdStep"])
        )

    @property
    def SPmsiRsvpTunnelId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI RSVP Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsiRsvpTunnelId"])
        )

    @property
    def SPmsiRsvpTunnelIdStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI RSVP Tunnel ID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsiRsvpTunnelIdStep"])
        )

    @property
    def SPmsiTunnelCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): S-PMSI Tunnel Count
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsiTunnelCount"])
        )

    @property
    def SPmsirootAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SPmsirootAddress"])
        )

    @property
    def SenderAddressPRootNodeAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SenderAddressPRootNodeAddress"]),
        )

    @property
    def SenderAddressPRootNodeAddressStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SenderAddressPRootNodeAddressStep"]),
        )

    @property
    def SetLeafInformationRequiredBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Leaf Information Required Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SetLeafInformationRequiredBit"]),
        )

    @property
    def SiCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Identifier Range
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SiCount"]))

    @property
    def SrLabelStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SR Label Start
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrLabelStart"]))

    @property
    def SrLabelStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SR Label Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrLabelStep"]))

    @property
    def TrafficBfrId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Traffic BFR-Id
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TrafficBfrId"]))

    @property
    def UpstreamOrDownstreamAssignedLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upstream/Downstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["UpstreamOrDownstreamAssignedLabel"]),
        )

    @property
    def UpstreamOrDownstreamAssignedLabelStep(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upstream/Downstream Assigned Label Step
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UpstreamOrDownstreamAssignedLabelStep"]
            ),
        )

    @property
    def UseSameBfrIdInTraffic(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Same BFR-Id in Traffic
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseSameBfrIdInTraffic"])
        )

    @property
    def UseUpstreamOrDownstreamAssignedLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Upstream/Downstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["UseUpstreamOrDownstreamAssignedLabel"]
            ),
        )

    @property
    def Version(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Version
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    def update(self, EnableTRM=None, ExpectSpecificLeafAdFromDut=None, Name=None):
        # type: (bool, bool, str) -> BgpMVpnSenderSiteSpmsiV4
        """Updates bgpMVpnSenderSiteSpmsiV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableTRM (bool): Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Multicast Tunnel Type will be PIM-SSM (by default).
        - ExpectSpecificLeafAdFromDut (bool): Expect Specific Leaf AD From DUT. If false then Ixia expectes Leaf AD in wildcard mode.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableTRM=None, ExpectSpecificLeafAdFromDut=None, Name=None):
        # type: (bool, bool, str) -> BgpMVpnSenderSiteSpmsiV4
        """Adds a new bgpMVpnSenderSiteSpmsiV4 resource on the server and adds it to the container.

        Args
        ----
        - EnableTRM (bool): Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Multicast Tunnel Type will be PIM-SSM (by default).
        - ExpectSpecificLeafAdFromDut (bool): Expect Specific Leaf AD From DUT. If false then Ixia expectes Leaf AD in wildcard mode.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved bgpMVpnSenderSiteSpmsiV4 resources using find and the newly added bgpMVpnSenderSiteSpmsiV4 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpMVpnSenderSiteSpmsiV4 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        EnableTRM=None,
        ExpectSpecificLeafAdFromDut=None,
        Name=None,
    ):
        # type: (int, str, bool, bool, str) -> BgpMVpnSenderSiteSpmsiV4
        """Finds and retrieves bgpMVpnSenderSiteSpmsiV4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpMVpnSenderSiteSpmsiV4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpMVpnSenderSiteSpmsiV4 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableTRM (bool): Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Multicast Tunnel Type will be PIM-SSM (by default).
        - ExpectSpecificLeafAdFromDut (bool): Expect Specific Leaf AD From DUT. If false then Ixia expectes Leaf AD in wildcard mode.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching bgpMVpnSenderSiteSpmsiV4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpMVpnSenderSiteSpmsiV4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpMVpnSenderSiteSpmsiV4 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def get_device_ids(
        self,
        PortNames=None,
        BFRId=None,
        BFRIpv4Prefix=None,
        BFRIpv6Prefix=None,
        BFRPrefixType=None,
        BIERSubDomainId=None,
        SPMSIRouteType=None,
        AutoConstructBitString=None,
        BierBitStringLength=None,
        BitString=None,
        Dscp=None,
        EnableLIRpFBit=None,
        Entropy=None,
        GroupAddress=None,
        GroupAddressStep=None,
        MulticastTunnelType=None,
        NextProtocol=None,
        Oam=None,
        Rsv=None,
        SPmsiRsvpP2mpId=None,
        SPmsiRsvpP2mpIdAsNumber=None,
        SPmsiRsvpP2mpIdStep=None,
        SPmsiRsvpTunnelId=None,
        SPmsiRsvpTunnelIdStep=None,
        SPmsiTunnelCount=None,
        SPmsirootAddress=None,
        SenderAddressPRootNodeAddress=None,
        SenderAddressPRootNodeAddressStep=None,
        SetLeafInformationRequiredBit=None,
        SiCount=None,
        SrLabelStart=None,
        SrLabelStep=None,
        TrafficBfrId=None,
        UpstreamOrDownstreamAssignedLabel=None,
        UpstreamOrDownstreamAssignedLabelStep=None,
        UseSameBfrIdInTraffic=None,
        UseUpstreamOrDownstreamAssignedLabel=None,
        Version=None,
    ):
        """Base class infrastructure that gets a list of bgpMVpnSenderSiteSpmsiV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BFRId (str): optional regex of BFRId
        - BFRIpv4Prefix (str): optional regex of BFRIpv4Prefix
        - BFRIpv6Prefix (str): optional regex of BFRIpv6Prefix
        - BFRPrefixType (str): optional regex of BFRPrefixType
        - BIERSubDomainId (str): optional regex of BIERSubDomainId
        - SPMSIRouteType (str): optional regex of SPMSIRouteType
        - AutoConstructBitString (str): optional regex of autoConstructBitString
        - BierBitStringLength (str): optional regex of bierBitStringLength
        - BitString (str): optional regex of bitString
        - Dscp (str): optional regex of dscp
        - EnableLIRpFBit (str): optional regex of enableLIRpFBit
        - Entropy (str): optional regex of entropy
        - GroupAddress (str): optional regex of groupAddress
        - GroupAddressStep (str): optional regex of groupAddressStep
        - MulticastTunnelType (str): optional regex of multicastTunnelType
        - NextProtocol (str): optional regex of nextProtocol
        - Oam (str): optional regex of oam
        - Rsv (str): optional regex of rsv
        - SPmsiRsvpP2mpId (str): optional regex of sPmsiRsvpP2mpId
        - SPmsiRsvpP2mpIdAsNumber (str): optional regex of sPmsiRsvpP2mpIdAsNumber
        - SPmsiRsvpP2mpIdStep (str): optional regex of sPmsiRsvpP2mpIdStep
        - SPmsiRsvpTunnelId (str): optional regex of sPmsiRsvpTunnelId
        - SPmsiRsvpTunnelIdStep (str): optional regex of sPmsiRsvpTunnelIdStep
        - SPmsiTunnelCount (str): optional regex of sPmsiTunnelCount
        - SPmsirootAddress (str): optional regex of sPmsirootAddress
        - SenderAddressPRootNodeAddress (str): optional regex of senderAddressPRootNodeAddress
        - SenderAddressPRootNodeAddressStep (str): optional regex of senderAddressPRootNodeAddressStep
        - SetLeafInformationRequiredBit (str): optional regex of setLeafInformationRequiredBit
        - SiCount (str): optional regex of siCount
        - SrLabelStart (str): optional regex of srLabelStart
        - SrLabelStep (str): optional regex of srLabelStep
        - TrafficBfrId (str): optional regex of trafficBfrId
        - UpstreamOrDownstreamAssignedLabel (str): optional regex of upstreamOrDownstreamAssignedLabel
        - UpstreamOrDownstreamAssignedLabelStep (str): optional regex of upstreamOrDownstreamAssignedLabelStep
        - UseSameBfrIdInTraffic (str): optional regex of useSameBfrIdInTraffic
        - UseUpstreamOrDownstreamAssignedLabel (str): optional regex of useUpstreamOrDownstreamAssignedLabel
        - Version (str): optional regex of version

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
