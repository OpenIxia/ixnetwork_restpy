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


class BroadcastDomainV4(Base):
    """BGP V4 Broadcast Domain Configuration
    The BroadcastDomainV4 class encapsulates a required broadcastDomainV4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "broadcastDomainV4"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AdRouteLabel": "adRouteLabel",
        "AsNumber2Bytes": "asNumber2Bytes",
        "AsNumber4Bytes": "asNumber4Bytes",
        "BVlanId": "bVlanId",
        "BVlanPriority": "bVlanPriority",
        "BVlanTpid": "bVlanTpid",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableVlanAwareService": "enableVlanAwareService",
        "EthernetTagId": "ethernetTagId",
        "ExportEviRTAssignedNumber": "exportEviRTAssignedNumber",
        "ExportRTIpv4Address": "exportRTIpv4Address",
        "ExportRTSubType": "exportRTSubType",
        "ExportRTType": "exportRTType",
        "ExportRTValueSameAsExportRT": "exportRTValueSameAsExportRT",
        "GroupAddress": "groupAddress",
        "ImportEviRTAssignedNumber": "importEviRTAssignedNumber",
        "ImportRTIpv4Address": "importRTIpv4Address",
        "ImportRTSubType": "importRTSubType",
        "ImportRTType": "importRTType",
        "ImportRTValueSameAsExportEVIRT": "importRTValueSameAsExportEVIRT",
        "Name": "name",
        "NoOfMacPools": "noOfMacPools",
        "NumJoinSynchIgmpRoutes": "numJoinSynchIgmpRoutes",
        "NumJoinSynchMldRoutes": "numJoinSynchMldRoutes",
        "NumLeaveSynchIgmpRoutes": "numLeaveSynchIgmpRoutes",
        "NumLeaveSynchMldRoutes": "numLeaveSynchMldRoutes",
        "NumSmetIgmpRoutes": "numSmetIgmpRoutes",
        "NumSmetMldRoutes": "numSmetMldRoutes",
        "NumSpmsiV4Routes": "numSpmsiV4Routes",
        "RootAddress": "rootAddress",
        "RsvpP2mpId": "rsvpP2mpId",
        "RsvpP2mpIdAsNumber": "rsvpP2mpIdAsNumber",
        "RsvpTunnelId": "rsvpTunnelId",
        "SenderAddressPRootNodeAddress": "senderAddressPRootNodeAddress",
        "UsebVlan": "usebVlan",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BroadcastDomainV4, self).__init__(parent, list_op)

    @property
    def BgpEvpnJoinSynchIgmp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnjoinsynchigmp_f89f38fca85b1442229391afe5b95e76.BgpEvpnJoinSynchIgmp): An instance of the BgpEvpnJoinSynchIgmp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnjoinsynchigmp_f89f38fca85b1442229391afe5b95e76 import (
            BgpEvpnJoinSynchIgmp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEvpnJoinSynchIgmp", None) is not None:
                return self._properties.get("BgpEvpnJoinSynchIgmp")
        return BgpEvpnJoinSynchIgmp(self)._select()

    @property
    def BgpEvpnJoinSynchMld(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnjoinsynchmld_4f5a831aa8e923cbdbff69a4f078837d.BgpEvpnJoinSynchMld): An instance of the BgpEvpnJoinSynchMld class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnjoinsynchmld_4f5a831aa8e923cbdbff69a4f078837d import (
            BgpEvpnJoinSynchMld,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEvpnJoinSynchMld", None) is not None:
                return self._properties.get("BgpEvpnJoinSynchMld")
        return BgpEvpnJoinSynchMld(self)._select()

    @property
    def BgpEvpnLeaveSynchIgmp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnleavesynchigmp_411f258090ec14c0d716cabc5159977e.BgpEvpnLeaveSynchIgmp): An instance of the BgpEvpnLeaveSynchIgmp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnleavesynchigmp_411f258090ec14c0d716cabc5159977e import (
            BgpEvpnLeaveSynchIgmp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEvpnLeaveSynchIgmp", None) is not None:
                return self._properties.get("BgpEvpnLeaveSynchIgmp")
        return BgpEvpnLeaveSynchIgmp(self)._select()

    @property
    def BgpEvpnLeaveSynchMld(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnleavesynchmld_226fbb8fe75f87a6460aecae872f059a.BgpEvpnLeaveSynchMld): An instance of the BgpEvpnLeaveSynchMld class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnleavesynchmld_226fbb8fe75f87a6460aecae872f059a import (
            BgpEvpnLeaveSynchMld,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEvpnLeaveSynchMld", None) is not None:
                return self._properties.get("BgpEvpnLeaveSynchMld")
        return BgpEvpnLeaveSynchMld(self)._select()

    @property
    def BgpEvpnSmetIgmp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnsmetigmp_68fa5fa63ce581945025c1253038bccb.BgpEvpnSmetIgmp): An instance of the BgpEvpnSmetIgmp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnsmetigmp_68fa5fa63ce581945025c1253038bccb import (
            BgpEvpnSmetIgmp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEvpnSmetIgmp", None) is not None:
                return self._properties.get("BgpEvpnSmetIgmp")
        return BgpEvpnSmetIgmp(self)._select()

    @property
    def BgpEvpnSmetMld(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnsmetmld_8d81cf97f583ad4547c03c6110c5168a.BgpEvpnSmetMld): An instance of the BgpEvpnSmetMld class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnsmetmld_8d81cf97f583ad4547c03c6110c5168a import (
            BgpEvpnSmetMld,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEvpnSmetMld", None) is not None:
                return self._properties.get("BgpEvpnSmetMld")
        return BgpEvpnSmetMld(self)._select()

    @property
    def BgpEvpnSpmsiV4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnspmsiv4_1a04dcc2041028074ff091c8cf9f0f9c.BgpEvpnSpmsiV4): An instance of the BgpEvpnSpmsiV4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpevpnspmsiv4_1a04dcc2041028074ff091c8cf9f0f9c import (
            BgpEvpnSpmsiV4,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpEvpnSpmsiV4", None) is not None:
                return self._properties.get("BgpEvpnSpmsiV4")
        return BgpEvpnSpmsiV4(self)._select()

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
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AdRouteLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AD Route Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdRouteLabel"]))

    @property
    def AsNumber2Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS 2-Bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsNumber2Bytes"])
        )

    @property
    def AsNumber4Bytes(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS 4-Bytes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AsNumber4Bytes"])
        )

    @property
    def BVlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BVlanId"]))

    @property
    def BVlanPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BVlanPriority"]))

    @property
    def BVlanTpid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BVlanTpid"]))

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
    def EnableVlanAwareService(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable VLAN Aware Service
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableVlanAwareService"])
        )

    @property
    def EthernetTagId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ethernet Tag ID. For VPWS, this acts as VPWS Service ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EthernetTagId"]))

    @property
    def ExportEviRTAssignedNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Export Route Target Assigned Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExportEviRTAssignedNumber"])
        )

    @property
    def ExportRTIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExportRTIpv4Address"])
        )

    @property
    def ExportRTSubType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SubType
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExportRTSubType"])
        )

    @property
    def ExportRTType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExportRTType"]))

    @property
    def ExportRTValueSameAsExportRT(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Same value as the Export RT configured in EVI.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExportRTValueSameAsExportRT"])
        )

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
    def ImportEviRTAssignedNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Import Route Target Assigned Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ImportEviRTAssignedNumber"])
        )

    @property
    def ImportRTIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IP
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ImportRTIpv4Address"])
        )

    @property
    def ImportRTSubType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SubType
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ImportRTSubType"])
        )

    @property
    def ImportRTType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ImportRTType"]))

    @property
    def ImportRTValueSameAsExportEVIRT(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Same value as the Export EVI-RT configured in broadcastdomain
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ImportRTValueSameAsExportEVIRT"]),
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
    def NoOfMacPools(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Mac Pools
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfMacPools"])

    @NoOfMacPools.setter
    def NoOfMacPools(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfMacPools"], value)

    @property
    def NumJoinSynchIgmpRoutes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of JoinSnch (IGMP) Routes to be configured under Broadcast Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumJoinSynchIgmpRoutes"])

    @NumJoinSynchIgmpRoutes.setter
    def NumJoinSynchIgmpRoutes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumJoinSynchIgmpRoutes"], value)

    @property
    def NumJoinSynchMldRoutes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of JoinSynch (MLD) Routes to be configured under Broadcast Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumJoinSynchMldRoutes"])

    @NumJoinSynchMldRoutes.setter
    def NumJoinSynchMldRoutes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumJoinSynchMldRoutes"], value)

    @property
    def NumLeaveSynchIgmpRoutes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of LeaveSynch (IGMP) Routes to be configured under Broadcast Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumLeaveSynchIgmpRoutes"])

    @NumLeaveSynchIgmpRoutes.setter
    def NumLeaveSynchIgmpRoutes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumLeaveSynchIgmpRoutes"], value)

    @property
    def NumLeaveSynchMldRoutes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of LeaveSynch (MLD) Routes to be configured under Broadcast Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumLeaveSynchMldRoutes"])

    @NumLeaveSynchMldRoutes.setter
    def NumLeaveSynchMldRoutes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumLeaveSynchMldRoutes"], value)

    @property
    def NumSmetIgmpRoutes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of SMET (IGMP) Routes to be configured under Broadcast Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumSmetIgmpRoutes"])

    @NumSmetIgmpRoutes.setter
    def NumSmetIgmpRoutes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumSmetIgmpRoutes"], value)

    @property
    def NumSmetMldRoutes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of SMET (MLD) Routes to be configured under Broadcast Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumSmetMldRoutes"])

    @NumSmetMldRoutes.setter
    def NumSmetMldRoutes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumSmetMldRoutes"], value)

    @property
    def NumSpmsiV4Routes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of S-PMSI A-D Routes to be configured under Broadcast Domain
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumSpmsiV4Routes"])

    @NumSpmsiV4Routes.setter
    def NumSpmsiV4Routes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumSpmsiV4Routes"], value)

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
    def UsebVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use B-VLAN
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsebVlan"])

    @UsebVlan.setter
    def UsebVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsebVlan"], value)

    def update(
        self,
        Name=None,
        NoOfMacPools=None,
        NumJoinSynchIgmpRoutes=None,
        NumJoinSynchMldRoutes=None,
        NumLeaveSynchIgmpRoutes=None,
        NumLeaveSynchMldRoutes=None,
        NumSmetIgmpRoutes=None,
        NumSmetMldRoutes=None,
        NumSpmsiV4Routes=None,
        UsebVlan=None,
    ):
        # type: (str, int, int, int, int, int, int, int, int, bool) -> BroadcastDomainV4
        """Updates broadcastDomainV4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMacPools (number): Number of Mac Pools
        - NumJoinSynchIgmpRoutes (number): The number of JoinSnch (IGMP) Routes to be configured under Broadcast Domain
        - NumJoinSynchMldRoutes (number): The number of JoinSynch (MLD) Routes to be configured under Broadcast Domain
        - NumLeaveSynchIgmpRoutes (number): The number of LeaveSynch (IGMP) Routes to be configured under Broadcast Domain
        - NumLeaveSynchMldRoutes (number): The number of LeaveSynch (MLD) Routes to be configured under Broadcast Domain
        - NumSmetIgmpRoutes (number): The number of SMET (IGMP) Routes to be configured under Broadcast Domain
        - NumSmetMldRoutes (number): The number of SMET (MLD) Routes to be configured under Broadcast Domain
        - NumSpmsiV4Routes (number): The number of S-PMSI A-D Routes to be configured under Broadcast Domain
        - UsebVlan (bool): Use B-VLAN

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Name=None,
        NoOfMacPools=None,
        NumJoinSynchIgmpRoutes=None,
        NumJoinSynchMldRoutes=None,
        NumLeaveSynchIgmpRoutes=None,
        NumLeaveSynchMldRoutes=None,
        NumSmetIgmpRoutes=None,
        NumSmetMldRoutes=None,
        NumSpmsiV4Routes=None,
        UsebVlan=None,
    ):
        # type: (int, str, str, int, int, int, int, int, int, int, int, bool) -> BroadcastDomainV4
        """Finds and retrieves broadcastDomainV4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve broadcastDomainV4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all broadcastDomainV4 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMacPools (number): Number of Mac Pools
        - NumJoinSynchIgmpRoutes (number): The number of JoinSnch (IGMP) Routes to be configured under Broadcast Domain
        - NumJoinSynchMldRoutes (number): The number of JoinSynch (MLD) Routes to be configured under Broadcast Domain
        - NumLeaveSynchIgmpRoutes (number): The number of LeaveSynch (IGMP) Routes to be configured under Broadcast Domain
        - NumLeaveSynchMldRoutes (number): The number of LeaveSynch (MLD) Routes to be configured under Broadcast Domain
        - NumSmetIgmpRoutes (number): The number of SMET (IGMP) Routes to be configured under Broadcast Domain
        - NumSmetMldRoutes (number): The number of SMET (MLD) Routes to be configured under Broadcast Domain
        - NumSpmsiV4Routes (number): The number of S-PMSI A-D Routes to be configured under Broadcast Domain
        - UsebVlan (bool): Use B-VLAN

        Returns
        -------
        - self: This instance with matching broadcastDomainV4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of broadcastDomainV4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the broadcastDomainV4 resources from the server available through an iterator or index

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

    def AdvertiseAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the advertiseAliasing operation on the server.

        Advertise Aliasing Per Broadcast Domain.

        advertiseAliasing(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute("advertiseAliasing", payload=payload, response_object=None)

    def AdvertiseAliasingPerBroadcastDomain(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the advertiseAliasingPerBroadcastDomain operation on the server.

        Advertise Aliasing Per Broadcast Domain

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        advertiseAliasingPerBroadcastDomain(async_operation=bool)
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        advertiseAliasingPerBroadcastDomain(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        advertiseAliasingPerBroadcastDomain(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------
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
            "advertiseAliasingPerBroadcastDomain", payload=payload, response_object=None
        )

    def WithdrawAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the withdrawAliasing operation on the server.

        Withdraw Aliasing Per Broadcast Domain.

        withdrawAliasing(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute("withdrawAliasing", payload=payload, response_object=None)

    def WithdrawAliasingPerBroadcastDomain(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the withdrawAliasingPerBroadcastDomain operation on the server.

        Advertise Aliasing Per Broadcast Domain

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        withdrawAliasingPerBroadcastDomain(async_operation=bool)
        --------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawAliasingPerBroadcastDomain(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawAliasingPerBroadcastDomain(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------------------------
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
            "withdrawAliasingPerBroadcastDomain", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AdRouteLabel=None,
        AsNumber2Bytes=None,
        AsNumber4Bytes=None,
        BVlanId=None,
        BVlanPriority=None,
        BVlanTpid=None,
        EnableVlanAwareService=None,
        EthernetTagId=None,
        ExportEviRTAssignedNumber=None,
        ExportRTIpv4Address=None,
        ExportRTSubType=None,
        ExportRTType=None,
        ExportRTValueSameAsExportRT=None,
        GroupAddress=None,
        ImportEviRTAssignedNumber=None,
        ImportRTIpv4Address=None,
        ImportRTSubType=None,
        ImportRTType=None,
        ImportRTValueSameAsExportEVIRT=None,
        RootAddress=None,
        RsvpP2mpId=None,
        RsvpP2mpIdAsNumber=None,
        RsvpTunnelId=None,
        SenderAddressPRootNodeAddress=None,
    ):
        """Base class infrastructure that gets a list of broadcastDomainV4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdRouteLabel (str): optional regex of adRouteLabel
        - AsNumber2Bytes (str): optional regex of asNumber2Bytes
        - AsNumber4Bytes (str): optional regex of asNumber4Bytes
        - BVlanId (str): optional regex of bVlanId
        - BVlanPriority (str): optional regex of bVlanPriority
        - BVlanTpid (str): optional regex of bVlanTpid
        - EnableVlanAwareService (str): optional regex of enableVlanAwareService
        - EthernetTagId (str): optional regex of ethernetTagId
        - ExportEviRTAssignedNumber (str): optional regex of exportEviRTAssignedNumber
        - ExportRTIpv4Address (str): optional regex of exportRTIpv4Address
        - ExportRTSubType (str): optional regex of exportRTSubType
        - ExportRTType (str): optional regex of exportRTType
        - ExportRTValueSameAsExportRT (str): optional regex of exportRTValueSameAsExportRT
        - GroupAddress (str): optional regex of groupAddress
        - ImportEviRTAssignedNumber (str): optional regex of importEviRTAssignedNumber
        - ImportRTIpv4Address (str): optional regex of importRTIpv4Address
        - ImportRTSubType (str): optional regex of importRTSubType
        - ImportRTType (str): optional regex of importRTType
        - ImportRTValueSameAsExportEVIRT (str): optional regex of importRTValueSameAsExportEVIRT
        - RootAddress (str): optional regex of rootAddress
        - RsvpP2mpId (str): optional regex of rsvpP2mpId
        - RsvpP2mpIdAsNumber (str): optional regex of rsvpP2mpIdAsNumber
        - RsvpTunnelId (str): optional regex of rsvpTunnelId
        - SenderAddressPRootNodeAddress (str): optional regex of senderAddressPRootNodeAddress

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
