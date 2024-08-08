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


class OspfPseudoInterface(Base):
    """Information for Simulated Router Interfaces
    The OspfPseudoInterface class encapsulates a list of ospfPseudoInterface resources that are managed by the system.
    A list of resources can be retrieved from the server using the OspfPseudoInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ospfPseudoInterface"
    _SDM_ATT_MAP = {
        "AdjSID": "adjSID",
        "AdministratorGroup": "administratorGroup",
        "AdministratorGroupTo": "administratorGroupTo",
        "BFlag": "bFlag",
        "BandwidthPriority0": "bandwidthPriority0",
        "BandwidthPriority0To": "bandwidthPriority0To",
        "BandwidthPriority1": "bandwidthPriority1",
        "BandwidthPriority1To": "bandwidthPriority1To",
        "BandwidthPriority2": "bandwidthPriority2",
        "BandwidthPriority2To": "bandwidthPriority2To",
        "BandwidthPriority3": "bandwidthPriority3",
        "BandwidthPriority3To": "bandwidthPriority3To",
        "BandwidthPriority4": "bandwidthPriority4",
        "BandwidthPriority4To": "bandwidthPriority4To",
        "BandwidthPriority5": "bandwidthPriority5",
        "BandwidthPriority5To": "bandwidthPriority5To",
        "BandwidthPriority6": "bandwidthPriority6",
        "BandwidthPriority6To": "bandwidthPriority6To",
        "BandwidthPriority7": "bandwidthPriority7",
        "BandwidthPriority7To": "bandwidthPriority7To",
        "Count": "count",
        "Dedicated1Plus1": "dedicated1Plus1",
        "Dedicated1To1": "dedicated1To1",
        "DescriptiveName": "descriptiveName",
        "EnLinkProtection": "enLinkProtection",
        "Enable": "enable",
        "EnableAdjSID": "enableAdjSID",
        "EnableSRLG": "enableSRLG",
        "Enhanced": "enhanced",
        "ExtraTraffic": "extraTraffic",
        "LFlag": "lFlag",
        "MaxBandwidth": "maxBandwidth",
        "MaxBandwidthTo": "maxBandwidthTo",
        "MaxReservableBandwidth": "maxReservableBandwidth",
        "MaxReservableBandwidthTo": "maxReservableBandwidthTo",
        "Metric": "metric",
        "MetricLevel": "metricLevel",
        "MetricLevelTo": "metricLevelTo",
        "MetricTo": "metricTo",
        "Name": "name",
        "NoOfTeProfile": "noOfTeProfile",
        "PFlag": "pFlag",
        "Reserved40": "reserved40",
        "Reserved80": "reserved80",
        "SFlag": "sFlag",
        "Shared": "shared",
        "SrlgCount": "srlgCount",
        "Unprotected": "unprotected",
        "VFlag": "vFlag",
        "Weight": "weight",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(OspfPseudoInterface, self).__init__(parent, list_op)

    @property
    def OspfPseudoTrafficEngineeringProfileList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudotrafficengineeringprofilelist_06278d34a5e26dd304ee8c97bdf5f67b.OspfPseudoTrafficEngineeringProfileList): An instance of the OspfPseudoTrafficEngineeringProfileList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudotrafficengineeringprofilelist_06278d34a5e26dd304ee8c97bdf5f67b import (
            OspfPseudoTrafficEngineeringProfileList,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("OspfPseudoTrafficEngineeringProfileList", None)
                is not None
            ):
                return self._properties.get("OspfPseudoTrafficEngineeringProfileList")
        return OspfPseudoTrafficEngineeringProfileList(self)._select()

    @property
    def SrlgValueList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist_355b617a5f46ce90d800290d21158418.SrlgValueList): An instance of the SrlgValueList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist_355b617a5f46ce90d800290d21158418 import (
            SrlgValueList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SrlgValueList", None) is not None:
                return self._properties.get("SrlgValueList")
        return SrlgValueList(self)

    @property
    def AdjSID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Adjacency SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdjSID"]))

    @property
    def AdministratorGroup(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Administrator Group
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdministratorGroup"])
        )

    @property
    def AdministratorGroupTo(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Administrator Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdministratorGroupTo"])
        )

    @property
    def BFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BFlag"]))

    @property
    def BandwidthPriority0(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority0"])
        )

    @property
    def BandwidthPriority0To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 0 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority0To"])
        )

    @property
    def BandwidthPriority1(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority1"])
        )

    @property
    def BandwidthPriority1To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 1 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority1To"])
        )

    @property
    def BandwidthPriority2(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority2"])
        )

    @property
    def BandwidthPriority2To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 2 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority2To"])
        )

    @property
    def BandwidthPriority3(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority3"])
        )

    @property
    def BandwidthPriority3To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 3 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority3To"])
        )

    @property
    def BandwidthPriority4(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority4"])
        )

    @property
    def BandwidthPriority4To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 4 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority4To"])
        )

    @property
    def BandwidthPriority5(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority5"])
        )

    @property
    def BandwidthPriority5To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 5 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority5To"])
        )

    @property
    def BandwidthPriority6(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority6"])
        )

    @property
    def BandwidthPriority6To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 6 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority6To"])
        )

    @property
    def BandwidthPriority7(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority7"])
        )

    @property
    def BandwidthPriority7To(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Bandwidth for Priority 7 (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority7To"])
        )

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
    def Dedicated1Plus1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Dedicated1Plus1"])
        )

    @property
    def Dedicated1To1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Dedicated1To1"]))

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
    def EnLinkProtection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the link protection on the OSPF link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnLinkProtection"])
        )

    @property
    def Enable(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE Enabled
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Enable"]))

    @property
    def EnableAdjSID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Adj SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableAdjSID"]))

    @property
    def EnableSRLG(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the SRLG on the OSPF link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableSRLG"]))

    @property
    def Enhanced(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Enhanced"]))

    @property
    def ExtraTraffic(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExtraTraffic"]))

    @property
    def LFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local/Global Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LFlag"]))

    @property
    def MaxBandwidth(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxBandwidth"]))

    @property
    def MaxBandwidthTo(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Maximum Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxBandwidthTo"])
        )

    @property
    def MaxReservableBandwidth(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReservableBandwidth"])
        )

    @property
    def MaxReservableBandwidthTo(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Maximum Reservable Bandwidth (B/sec).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReservableBandwidthTo"])
        )

    @property
    def Metric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node to To Node, Link Metric.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Metric"]))

    @property
    def MetricLevel(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE Metric Level
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MetricLevel"]))

    @property
    def MetricLevelTo(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, TE Metric Level.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MetricLevelTo"]))

    @property
    def MetricTo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node to From Node, Link Metric.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MetricTo"]))

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
    def NoOfTeProfile(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of TE Profile
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfTeProfile"])

    @NoOfTeProfile.setter
    def NoOfTeProfile(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfTeProfile"], value)

    @property
    def PFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Persistent Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PFlag"]))

    @property
    def Reserved40(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved40"]))

    @property
    def Reserved80(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x80.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved80"]))

    @property
    def SFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set/Group Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SFlag"]))

    @property
    def Shared(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Shared"]))

    @property
    def SrlgCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This field value shows how many SRLG Value columns would be there in the GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrlgCount"])

    @SrlgCount.setter
    def SrlgCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrlgCount"], value)

    @property
    def Unprotected(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Unprotected"]))

    @property
    def VFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value/Index Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VFlag"]))

    @property
    def Weight(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Weight"]))

    def update(self, Name=None, NoOfTeProfile=None, SrlgCount=None):
        # type: (str, int, int) -> OspfPseudoInterface
        """Updates ospfPseudoInterface resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None, NoOfTeProfile=None, SrlgCount=None):
        # type: (str, int, int) -> OspfPseudoInterface
        """Adds a new ospfPseudoInterface resource on the json, only valid with batch add utility

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Returns
        -------
        - self: This instance with all currently retrieved ospfPseudoInterface resources using find and the newly added ospfPseudoInterface resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Name=None,
        NoOfTeProfile=None,
        SrlgCount=None,
    ):
        # type: (int, str, str, int, int) -> OspfPseudoInterface
        """Finds and retrieves ospfPseudoInterface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfPseudoInterface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfPseudoInterface resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Returns
        -------
        - self: This instance with matching ospfPseudoInterface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfPseudoInterface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfPseudoInterface resources from the server available through an iterator or index

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

        abort(async_operation=bool)
        ---------------------------
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

    def Disconnect(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the disconnect operation on the server.

        Disconnect Simulated Interface

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        disconnect(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        disconnect(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        disconnect(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------
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
        return self._execute("disconnect", payload=payload, response_object=None)

    def Reconnect(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the reconnect operation on the server.

        Reconnect Simulated Interface

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        reconnect(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        reconnect(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        reconnect(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------
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
        return self._execute("reconnect", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        start(async_operation=bool)
        ---------------------------
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

        stop(async_operation=bool)
        --------------------------
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
        AdjSID=None,
        AdministratorGroup=None,
        AdministratorGroupTo=None,
        BFlag=None,
        BandwidthPriority0=None,
        BandwidthPriority0To=None,
        BandwidthPriority1=None,
        BandwidthPriority1To=None,
        BandwidthPriority2=None,
        BandwidthPriority2To=None,
        BandwidthPriority3=None,
        BandwidthPriority3To=None,
        BandwidthPriority4=None,
        BandwidthPriority4To=None,
        BandwidthPriority5=None,
        BandwidthPriority5To=None,
        BandwidthPriority6=None,
        BandwidthPriority6To=None,
        BandwidthPriority7=None,
        BandwidthPriority7To=None,
        Dedicated1Plus1=None,
        Dedicated1To1=None,
        EnLinkProtection=None,
        Enable=None,
        EnableAdjSID=None,
        EnableSRLG=None,
        Enhanced=None,
        ExtraTraffic=None,
        LFlag=None,
        MaxBandwidth=None,
        MaxBandwidthTo=None,
        MaxReservableBandwidth=None,
        MaxReservableBandwidthTo=None,
        Metric=None,
        MetricLevel=None,
        MetricLevelTo=None,
        MetricTo=None,
        PFlag=None,
        Reserved40=None,
        Reserved80=None,
        SFlag=None,
        Shared=None,
        Unprotected=None,
        VFlag=None,
        Weight=None,
    ):
        """Base class infrastructure that gets a list of ospfPseudoInterface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AdjSID (str): optional regex of adjSID
        - AdministratorGroup (str): optional regex of administratorGroup
        - AdministratorGroupTo (str): optional regex of administratorGroupTo
        - BFlag (str): optional regex of bFlag
        - BandwidthPriority0 (str): optional regex of bandwidthPriority0
        - BandwidthPriority0To (str): optional regex of bandwidthPriority0To
        - BandwidthPriority1 (str): optional regex of bandwidthPriority1
        - BandwidthPriority1To (str): optional regex of bandwidthPriority1To
        - BandwidthPriority2 (str): optional regex of bandwidthPriority2
        - BandwidthPriority2To (str): optional regex of bandwidthPriority2To
        - BandwidthPriority3 (str): optional regex of bandwidthPriority3
        - BandwidthPriority3To (str): optional regex of bandwidthPriority3To
        - BandwidthPriority4 (str): optional regex of bandwidthPriority4
        - BandwidthPriority4To (str): optional regex of bandwidthPriority4To
        - BandwidthPriority5 (str): optional regex of bandwidthPriority5
        - BandwidthPriority5To (str): optional regex of bandwidthPriority5To
        - BandwidthPriority6 (str): optional regex of bandwidthPriority6
        - BandwidthPriority6To (str): optional regex of bandwidthPriority6To
        - BandwidthPriority7 (str): optional regex of bandwidthPriority7
        - BandwidthPriority7To (str): optional regex of bandwidthPriority7To
        - Dedicated1Plus1 (str): optional regex of dedicated1Plus1
        - Dedicated1To1 (str): optional regex of dedicated1To1
        - EnLinkProtection (str): optional regex of enLinkProtection
        - Enable (str): optional regex of enable
        - EnableAdjSID (str): optional regex of enableAdjSID
        - EnableSRLG (str): optional regex of enableSRLG
        - Enhanced (str): optional regex of enhanced
        - ExtraTraffic (str): optional regex of extraTraffic
        - LFlag (str): optional regex of lFlag
        - MaxBandwidth (str): optional regex of maxBandwidth
        - MaxBandwidthTo (str): optional regex of maxBandwidthTo
        - MaxReservableBandwidth (str): optional regex of maxReservableBandwidth
        - MaxReservableBandwidthTo (str): optional regex of maxReservableBandwidthTo
        - Metric (str): optional regex of metric
        - MetricLevel (str): optional regex of metricLevel
        - MetricLevelTo (str): optional regex of metricLevelTo
        - MetricTo (str): optional regex of metricTo
        - PFlag (str): optional regex of pFlag
        - Reserved40 (str): optional regex of reserved40
        - Reserved80 (str): optional regex of reserved80
        - SFlag (str): optional regex of sFlag
        - Shared (str): optional regex of shared
        - Unprotected (str): optional regex of unprotected
        - VFlag (str): optional regex of vFlag
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
