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


class BgpIpv4MVrf(Base):
    """BGP IPv4 Peer mVRF Configuration
    The BgpIpv4MVrf class encapsulates a list of bgpIpv4MVrf resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpIpv4MVrf.find() method.
    The list can be managed by using the BgpIpv4MVrf.add() and BgpIpv4MVrf.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "bgpIpv4MVrf"
    _SDM_ATT_MAP = {
        "BFRId": "BFRId",
        "BFRIpv4Prefix": "BFRIpv4Prefix",
        "BFRIpv6Prefix": "BFRIpv6Prefix",
        "BFRPrefixType": "BFRPrefixType",
        "BIERSubDomainId": "BIERSubDomainId",
        "BslMismatchHandlingOption": "BslMismatchHandlingOption",
        "LeafInfoRequiredBit": "LeafInfoRequiredBit",
        "LeafInfoRequiredPerFlow": "LeafInfoRequiredPerFlow",
        "Active": "active",
        "AdvertiseIPMSIRoutes": "advertiseIPMSIRoutes",
        "AutoConstructBitString": "autoConstructBitString",
        "BierBitStringLength": "bierBitStringLength",
        "BitString": "bitString",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Dscp": "dscp",
        "DutIpv4": "dutIpv4",
        "EnableTRM": "enableTRM",
        "Entropy": "entropy",
        "Errors": "errors",
        "GroupAddress": "groupAddress",
        "ImportRtListSameAsExportRtList": "importRtListSameAsExportRtList",
        "IncludeBierPTAinLeafAD": "includeBierPTAinLeafAD",
        "IncludePmsiTunnelAttribute": "includePmsiTunnelAttribute",
        "LocalIpv4": "localIpv4",
        "LocalRouterID": "localRouterID",
        "MulticastDistinguisherAs4Number": "multicastDistinguisherAs4Number",
        "MulticastDistinguisherAsNumber": "multicastDistinguisherAsNumber",
        "MulticastDistinguisherAssignedNumber": "multicastDistinguisherAssignedNumber",
        "MulticastDistinguisherIpAddress": "multicastDistinguisherIpAddress",
        "MulticastDistinguisherType": "multicastDistinguisherType",
        "MulticastTunnelType": "multicastTunnelType",
        "Multiplier": "multiplier",
        "Name": "name",
        "NextProtocol": "nextProtocol",
        "NumRtInExportRouteTargetList": "numRtInExportRouteTargetList",
        "NumRtInImportRouteTargetList": "numRtInImportRouteTargetList",
        "NumRtInUmhExportRouteTargetList": "numRtInUmhExportRouteTargetList",
        "NumRtInUmhImportRouteTargetList": "numRtInUmhImportRouteTargetList",
        "Oam": "oam",
        "RootAddress": "rootAddress",
        "Rsv": "rsv",
        "RsvpP2mpId": "rsvpP2mpId",
        "RsvpP2mpIdAsNumber": "rsvpP2mpIdAsNumber",
        "RsvpTunnelId": "rsvpTunnelId",
        "SameAsExportRT": "sameAsExportRT",
        "SameAsImportRT": "sameAsImportRT",
        "SenderAddressPRootNodeAddress": "senderAddressPRootNodeAddress",
        "SessionStatus": "sessionStatus",
        "SiCount": "siCount",
        "SrLabelStart": "srLabelStart",
        "SrLabelStep": "srLabelStep",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "SupportLeafADRoutesSending": "supportLeafADRoutesSending",
        "TrafficBfrId": "trafficBfrId",
        "UpOrDownStreamAssignedLabel": "upOrDownStreamAssignedLabel",
        "UseSameBfrIdInTraffic": "useSameBfrIdInTraffic",
        "UseUpOrDownStreamAssigneLabel": "useUpOrDownStreamAssigneLabel",
        "Version": "version",
        "VrfName": "vrfName",
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
        super(BgpIpv4MVrf, self).__init__(parent, list_op)

    @property
    def BgpExportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist_ce93ce056c01eaf7643c31a7fd67768c.BgpExportRouteTargetList): An instance of the BgpExportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist_ce93ce056c01eaf7643c31a7fd67768c import (
            BgpExportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpExportRouteTargetList", None) is not None:
                return self._properties.get("BgpExportRouteTargetList")
        return BgpExportRouteTargetList(self)

    @property
    def BgpImportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist_99470595cc13238e15b19c07b8af6021.BgpImportRouteTargetList): An instance of the BgpImportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist_99470595cc13238e15b19c07b8af6021 import (
            BgpImportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpImportRouteTargetList", None) is not None:
                return self._properties.get("BgpImportRouteTargetList")
        return BgpImportRouteTargetList(self)

    @property
    def BgpUmhExportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhexportroutetargetlist_536e8a485efae5ffcda5cfc4f848255b.BgpUmhExportRouteTargetList): An instance of the BgpUmhExportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhexportroutetargetlist_536e8a485efae5ffcda5cfc4f848255b import (
            BgpUmhExportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpUmhExportRouteTargetList", None) is not None:
                return self._properties.get("BgpUmhExportRouteTargetList")
        return BgpUmhExportRouteTargetList(self)

    @property
    def BgpUmhImportRouteTargetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhimportroutetargetlist_02ef98778defb99b99d0de435c533ff0.BgpUmhImportRouteTargetList): An instance of the BgpUmhImportRouteTargetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhimportroutetargetlist_02ef98778defb99b99d0de435c533ff0 import (
            BgpUmhImportRouteTargetList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpUmhImportRouteTargetList", None) is not None:
                return self._properties.get("BgpUmhImportRouteTargetList")
        return BgpUmhImportRouteTargetList(self)

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
    def BslMismatchHandlingOption(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BIER BSL Mismatch Handling Option
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BslMismatchHandlingOption"])
        )

    @property
    def LeafInfoRequiredBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Leaf Info Required Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LeafInfoRequiredBit"])
        )

    @property
    def LeafInfoRequiredPerFlow(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Leaf Info Required Per Flow(LIR-PF)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LeafInfoRequiredPerFlow"])
        )

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
    def AdvertiseIPMSIRoutes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables I-PMSI Route Advertisement for MVPN (if True). Disables I-PMSI Route Advertisement for MVPN (if False). - Set to False when Enable TRM is Enabled (by deafult).
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvertiseIPMSIRoutes"])

    @AdvertiseIPMSIRoutes.setter
    def AdvertiseIPMSIRoutes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvertiseIPMSIRoutes"], value)

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
    def DutIpv4(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): DUT IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["DutIpv4"])

    @property
    def EnableTRM(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Advertise I-PMSI Routes will be disabled (by default). - Multicast Tunnel Type will be PIM-SSM (by default). - VRF Route Import Extended Community is sent with EVPN Route Type 2 & 5 (always).
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
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

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
    def ImportRtListSameAsExportRtList(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Import RT List Same As Export RT List
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImportRtListSameAsExportRtList"])

    @ImportRtListSameAsExportRtList.setter
    def ImportRtListSameAsExportRtList(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ImportRtListSameAsExportRtList"], value)

    @property
    def IncludeBierPTAinLeafAD(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Bier PTA in Leaf A-D
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeBierPTAinLeafAD"])
        )

    @property
    def IncludePmsiTunnelAttribute(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include PMSI Tunnel Attribute
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludePmsiTunnelAttribute"])
        )

    @property
    def LocalIpv4(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIpv4"])

    @property
    def LocalRouterID(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalRouterID"])

    @property
    def MulticastDistinguisherAs4Number(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VMulticast Distinguisher AS4 Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastDistinguisherAs4Number"]),
        )

    @property
    def MulticastDistinguisherAsNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VMulticast Distinguisher AS Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastDistinguisherAsNumber"]),
        )

    @property
    def MulticastDistinguisherAssignedNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Distinguisher Assigned Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MulticastDistinguisherAssignedNumber"]
            ),
        )

    @property
    def MulticastDistinguisherIpAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Distinguisher IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MulticastDistinguisherIpAddress"]),
        )

    @property
    def MulticastDistinguisherType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast Distinguisher Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MulticastDistinguisherType"])
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
    def NumRtInExportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in Export Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRtInExportRouteTargetList"])

    @NumRtInExportRouteTargetList.setter
    def NumRtInExportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRtInExportRouteTargetList"], value)

    @property
    def NumRtInImportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in Import Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRtInImportRouteTargetList"])

    @NumRtInImportRouteTargetList.setter
    def NumRtInImportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRtInImportRouteTargetList"], value)

    @property
    def NumRtInUmhExportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in Export Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRtInUmhExportRouteTargetList"])

    @NumRtInUmhExportRouteTargetList.setter
    def NumRtInUmhExportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRtInUmhExportRouteTargetList"], value)

    @property
    def NumRtInUmhImportRouteTargetList(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of RTs in Import Route Target List(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumRtInUmhImportRouteTargetList"])

    @NumRtInUmhImportRouteTargetList.setter
    def NumRtInUmhImportRouteTargetList(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumRtInUmhImportRouteTargetList"], value)

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
    def RootAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RootAddress"]))

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
    def RsvpP2mpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RsvpP2mpId"]))

    @property
    def RsvpP2mpIdAsNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID as Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpP2mpIdAsNumber"])
        )

    @property
    def RsvpTunnelId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RsvpTunnelId"]))

    @property
    def SameAsExportRT(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Same As Export RT Attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP["SameAsExportRT"])

    @SameAsExportRT.setter
    def SameAsExportRT(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SameAsExportRT"], value)

    @property
    def SameAsImportRT(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Same As Import RT Attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP["SameAsImportRT"])

    @SameAsImportRT.setter
    def SameAsImportRT(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SameAsImportRT"], value)

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
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

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
    def SupportLeafADRoutesSending(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support Leaf A-D Routes Sending
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SupportLeafADRoutesSending"])
        )

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
    def UpOrDownStreamAssignedLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Upstream/Downstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UpOrDownStreamAssignedLabel"])
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
    def UseUpOrDownStreamAssigneLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Upstream/Downstream Assigned Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["UseUpOrDownStreamAssigneLabel"]),
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

    @property
    def VrfName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ID of the identified VRF.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VrfName"]))

    def update(
        self,
        AdvertiseIPMSIRoutes=None,
        ConnectedVia=None,
        EnableTRM=None,
        ImportRtListSameAsExportRtList=None,
        Multiplier=None,
        Name=None,
        NumRtInExportRouteTargetList=None,
        NumRtInImportRouteTargetList=None,
        NumRtInUmhExportRouteTargetList=None,
        NumRtInUmhImportRouteTargetList=None,
        SameAsExportRT=None,
        SameAsImportRT=None,
        StackedLayers=None,
    ):
        # type: (bool, List[str], bool, bool, int, str, int, int, int, int, bool, bool, List[str]) -> BgpIpv4MVrf
        """Updates bgpIpv4MVrf resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AdvertiseIPMSIRoutes (bool): Enables I-PMSI Route Advertisement for MVPN (if True). Disables I-PMSI Route Advertisement for MVPN (if False). - Set to False when Enable TRM is Enabled (by deafult).
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableTRM (bool): Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Advertise I-PMSI Routes will be disabled (by default). - Multicast Tunnel Type will be PIM-SSM (by default). - VRF Route Import Extended Community is sent with EVPN Route Type 2 & 5 (always).
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - SameAsExportRT (bool): Same As Export RT Attribute
        - SameAsImportRT (bool): Same As Import RT Attribute
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AdvertiseIPMSIRoutes=None,
        ConnectedVia=None,
        EnableTRM=None,
        ImportRtListSameAsExportRtList=None,
        Multiplier=None,
        Name=None,
        NumRtInExportRouteTargetList=None,
        NumRtInImportRouteTargetList=None,
        NumRtInUmhExportRouteTargetList=None,
        NumRtInUmhImportRouteTargetList=None,
        SameAsExportRT=None,
        SameAsImportRT=None,
        StackedLayers=None,
    ):
        # type: (bool, List[str], bool, bool, int, str, int, int, int, int, bool, bool, List[str]) -> BgpIpv4MVrf
        """Adds a new bgpIpv4MVrf resource on the server and adds it to the container.

        Args
        ----
        - AdvertiseIPMSIRoutes (bool): Enables I-PMSI Route Advertisement for MVPN (if True). Disables I-PMSI Route Advertisement for MVPN (if False). - Set to False when Enable TRM is Enabled (by deafult).
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableTRM (bool): Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Advertise I-PMSI Routes will be disabled (by default). - Multicast Tunnel Type will be PIM-SSM (by default). - VRF Route Import Extended Community is sent with EVPN Route Type 2 & 5 (always).
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - SameAsExportRT (bool): Same As Export RT Attribute
        - SameAsImportRT (bool): Same As Import RT Attribute
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved bgpIpv4MVrf resources using find and the newly added bgpIpv4MVrf resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpIpv4MVrf resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AdvertiseIPMSIRoutes=None,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        DutIpv4=None,
        EnableTRM=None,
        Errors=None,
        ImportRtListSameAsExportRtList=None,
        LocalIpv4=None,
        LocalRouterID=None,
        Multiplier=None,
        Name=None,
        NumRtInExportRouteTargetList=None,
        NumRtInImportRouteTargetList=None,
        NumRtInUmhExportRouteTargetList=None,
        NumRtInUmhImportRouteTargetList=None,
        SameAsExportRT=None,
        SameAsImportRT=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves bgpIpv4MVrf resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpIpv4MVrf resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpIpv4MVrf resources from the server.

        Args
        ----
        - AdvertiseIPMSIRoutes (bool): Enables I-PMSI Route Advertisement for MVPN (if True). Disables I-PMSI Route Advertisement for MVPN (if False). - Set to False when Enable TRM is Enabled (by deafult).
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DutIpv4 (list(str)): DUT IP
        - EnableTRM (bool): Enables Tenant Routed Multicast support in EVPN. Upon Enabling, - Advertise I-PMSI Routes will be disabled (by default). - Multicast Tunnel Type will be PIM-SSM (by default). - VRF Route Import Extended Community is sent with EVPN Route Type 2 & 5 (always).
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
        - LocalIpv4 (list(str)): Local IP
        - LocalRouterID (list(str)): Router ID
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
        - NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
        - SameAsExportRT (bool): Same As Export RT Attribute
        - SameAsImportRT (bool): Same As Import RT Attribute
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching bgpIpv4MVrf resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpIpv4MVrf data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpIpv4MVrf resources from the server available through an iterator or index

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

    def ClearAllBgpVRFLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearAllBgpVRFLearnedInfo operation on the server.

        Clear All BGP VRF Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllBgpVRFLearnedInfo(async_operation=bool)
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllBgpVRFLearnedInfo(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllBgpVRFLearnedInfo(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------------
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
        return self._execute(
            "clearAllBgpVRFLearnedInfo", payload=payload, response_object=None
        )

    def ClearAllBgpVRFLearnedInfoInClient(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearAllBgpVRFLearnedInfoInClient operation on the server.

        Clears ALL routes from GUI grid for the selected BGP Peers.

        clearAllBgpVRFLearnedInfoInClient(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute(
            "clearAllBgpVRFLearnedInfoInClient", payload=payload, response_object=None
        )

    def GetIPv4VpnLearnedInfoPerVRF(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv4VpnLearnedInfoPerVRF operation on the server.

        Get IPv4 Vpn Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv4VpnLearnedInfoPerVRF(async_operation=bool)
        -------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4VpnLearnedInfoPerVRF(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4VpnLearnedInfoPerVRF(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4VpnLearnedInfoPerVRF(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute(
            "getIPv4VpnLearnedInfoPerVRF", payload=payload, response_object=None
        )

    def GetIPv6VpnLearnedInfoPerVRF(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv6VpnLearnedInfoPerVRF operation on the server.

        Get IPv6 Vpn Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv6VpnLearnedInfoPerVRF(async_operation=bool)
        -------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6VpnLearnedInfoPerVRF(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6VpnLearnedInfoPerVRF(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6VpnLearnedInfoPerVRF(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute(
            "getIPv6VpnLearnedInfoPerVRF", payload=payload, response_object=None
        )

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

    def get_device_ids(
        self,
        PortNames=None,
        BFRId=None,
        BFRIpv4Prefix=None,
        BFRIpv6Prefix=None,
        BFRPrefixType=None,
        BIERSubDomainId=None,
        BslMismatchHandlingOption=None,
        LeafInfoRequiredBit=None,
        LeafInfoRequiredPerFlow=None,
        Active=None,
        AutoConstructBitString=None,
        BierBitStringLength=None,
        BitString=None,
        Dscp=None,
        Entropy=None,
        GroupAddress=None,
        IncludeBierPTAinLeafAD=None,
        IncludePmsiTunnelAttribute=None,
        MulticastDistinguisherAs4Number=None,
        MulticastDistinguisherAsNumber=None,
        MulticastDistinguisherAssignedNumber=None,
        MulticastDistinguisherIpAddress=None,
        MulticastDistinguisherType=None,
        MulticastTunnelType=None,
        NextProtocol=None,
        Oam=None,
        RootAddress=None,
        Rsv=None,
        RsvpP2mpId=None,
        RsvpP2mpIdAsNumber=None,
        RsvpTunnelId=None,
        SenderAddressPRootNodeAddress=None,
        SiCount=None,
        SrLabelStart=None,
        SrLabelStep=None,
        SupportLeafADRoutesSending=None,
        TrafficBfrId=None,
        UpOrDownStreamAssignedLabel=None,
        UseSameBfrIdInTraffic=None,
        UseUpOrDownStreamAssigneLabel=None,
        Version=None,
        VrfName=None,
    ):
        """Base class infrastructure that gets a list of bgpIpv4MVrf device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BFRId (str): optional regex of BFRId
        - BFRIpv4Prefix (str): optional regex of BFRIpv4Prefix
        - BFRIpv6Prefix (str): optional regex of BFRIpv6Prefix
        - BFRPrefixType (str): optional regex of BFRPrefixType
        - BIERSubDomainId (str): optional regex of BIERSubDomainId
        - BslMismatchHandlingOption (str): optional regex of BslMismatchHandlingOption
        - LeafInfoRequiredBit (str): optional regex of LeafInfoRequiredBit
        - LeafInfoRequiredPerFlow (str): optional regex of LeafInfoRequiredPerFlow
        - Active (str): optional regex of active
        - AutoConstructBitString (str): optional regex of autoConstructBitString
        - BierBitStringLength (str): optional regex of bierBitStringLength
        - BitString (str): optional regex of bitString
        - Dscp (str): optional regex of dscp
        - Entropy (str): optional regex of entropy
        - GroupAddress (str): optional regex of groupAddress
        - IncludeBierPTAinLeafAD (str): optional regex of includeBierPTAinLeafAD
        - IncludePmsiTunnelAttribute (str): optional regex of includePmsiTunnelAttribute
        - MulticastDistinguisherAs4Number (str): optional regex of multicastDistinguisherAs4Number
        - MulticastDistinguisherAsNumber (str): optional regex of multicastDistinguisherAsNumber
        - MulticastDistinguisherAssignedNumber (str): optional regex of multicastDistinguisherAssignedNumber
        - MulticastDistinguisherIpAddress (str): optional regex of multicastDistinguisherIpAddress
        - MulticastDistinguisherType (str): optional regex of multicastDistinguisherType
        - MulticastTunnelType (str): optional regex of multicastTunnelType
        - NextProtocol (str): optional regex of nextProtocol
        - Oam (str): optional regex of oam
        - RootAddress (str): optional regex of rootAddress
        - Rsv (str): optional regex of rsv
        - RsvpP2mpId (str): optional regex of rsvpP2mpId
        - RsvpP2mpIdAsNumber (str): optional regex of rsvpP2mpIdAsNumber
        - RsvpTunnelId (str): optional regex of rsvpTunnelId
        - SenderAddressPRootNodeAddress (str): optional regex of senderAddressPRootNodeAddress
        - SiCount (str): optional regex of siCount
        - SrLabelStart (str): optional regex of srLabelStart
        - SrLabelStep (str): optional regex of srLabelStep
        - SupportLeafADRoutesSending (str): optional regex of supportLeafADRoutesSending
        - TrafficBfrId (str): optional regex of trafficBfrId
        - UpOrDownStreamAssignedLabel (str): optional regex of upOrDownStreamAssignedLabel
        - UseSameBfrIdInTraffic (str): optional regex of useSameBfrIdInTraffic
        - UseUpOrDownStreamAssigneLabel (str): optional regex of useUpOrDownStreamAssigneLabel
        - Version (str): optional regex of version
        - VrfName (str): optional regex of vrfName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
