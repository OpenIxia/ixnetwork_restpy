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


class IsisL3PseudoInterface(Base):
    """ISIS-L3 Pseudo Interafce Configuration
    The IsisL3PseudoInterface class encapsulates a list of isisL3PseudoInterface resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisL3PseudoInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "isisL3PseudoInterface"
    _SDM_ATT_MAP = {
        "AdjSID": "adjSID",
        "AdjSidCount": "adjSidCount",
        "AdministratorGroup": "administratorGroup",
        "AdvertiseLinkMsd": "advertiseLinkMsd",
        "BFlag": "bFlag",
        "BandwidthPriority0_Bps": "bandwidthPriority0_Bps",
        "BandwidthPriority1_Bps": "bandwidthPriority1_Bps",
        "BandwidthPriority2_Bps": "bandwidthPriority2_Bps",
        "BandwidthPriority3_Bps": "bandwidthPriority3_Bps",
        "BandwidthPriority4_Bps": "bandwidthPriority4_Bps",
        "BandwidthPriority5_Bps": "bandwidthPriority5_Bps",
        "BandwidthPriority6_Bps": "bandwidthPriority6_Bps",
        "BandwidthPriority7_Bps": "bandwidthPriority7_Bps",
        "Count": "count",
        "DedicatedOnePlusOne": "dedicatedOnePlusOne",
        "DedicatedOneToOne": "dedicatedOneToOne",
        "DescriptiveName": "descriptiveName",
        "Enable": "enable",
        "EnableAdjSID": "enableAdjSID",
        "EnableAppSpecSrlg": "enableAppSpecSrlg",
        "EnableBit4": "enableBit4",
        "EnableBit5": "enableBit5",
        "EnableBit6": "enableBit6",
        "EnableBit7": "enableBit7",
        "EnableBit8": "enableBit8",
        "EnableIPv6SID": "enableIPv6SID",
        "EnableLinkProtection": "enableLinkProtection",
        "EnableMT": "enableMT",
        "EnableMt": "enableMt",
        "EnableNFlag": "enableNFlag",
        "EnableRFlag": "enableRFlag",
        "EnableSRLG": "enableSRLG",
        "EnableXFlag": "enableXFlag",
        "Enhanced": "enhanced",
        "ExtraTraffic": "extraTraffic",
        "FFlag": "fFlag",
        "Funcflags": "funcflags",
        "Function": "function",
        "IncludeMaxSlMsd": "includeMaxSlMsd",
        "IncludeMaximumEndDMsd": "includeMaximumEndDMsd",
        "IncludeMaximumEndPopMsd": "includeMaximumEndPopMsd",
        "IncludeMaximumHEncapMsd": "includeMaximumHEncapMsd",
        "IncludeMaximumTEncapMsd": "includeMaximumTEncapMsd",
        "IncludeMaximumTInsertMsd": "includeMaximumTInsertMsd",
        "Ipv6SidValue": "ipv6SidValue",
        "LFlag": "lFlag",
        "LinkType": "linkType",
        "MaxBandwidth_Bps": "maxBandwidth_Bps",
        "MaxEndDMsd": "maxEndDMsd",
        "MaxEndPopMsd": "maxEndPopMsd",
        "MaxHEncap": "maxHEncap",
        "MaxReservableBandwidth_Bps": "maxReservableBandwidth_Bps",
        "MaxSlMsd": "maxSlMsd",
        "MaxTEncap": "maxTEncap",
        "MaxTInsertMsd": "maxTInsertMsd",
        "MetricLevel": "metricLevel",
        "MtCount": "mtCount",
        "Name": "name",
        "NoOfAppSpecSrlg": "noOfAppSpecSrlg",
        "NoOfMtIds": "noOfMtIds",
        "NoOfTeProfile": "noOfTeProfile",
        "OverrideFFlag": "overrideFFlag",
        "PFlag": "pFlag",
        "Reserved0x40": "reserved0x40",
        "Reserved0x80": "reserved0x80",
        "SFlag": "sFlag",
        "Shared": "shared",
        "SrlgCount": "srlgCount",
        "Srv6SidFlags": "srv6SidFlags",
        "Unprotected": "unprotected",
        "VFlag": "vFlag",
        "Weight": "weight",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IsisL3PseudoInterface, self).__init__(parent, list_op)

    @property
    def IsisPseudoMultiTopologyValuesList(self):
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomultitopologyvalueslist_611d6ab2b1a502e3b27f153266aa7670.IsisPseudoMultiTopologyValuesList): An instance of the IsisPseudoMultiTopologyValuesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomultitopologyvalueslist_611d6ab2b1a502e3b27f153266aa7670 import (
            IsisPseudoMultiTopologyValuesList,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisPseudoMultiTopologyValuesList", None)
                is not None
            ):
                return self._properties.get("IsisPseudoMultiTopologyValuesList")
        return IsisPseudoMultiTopologyValuesList(self)

    @property
    def IsisDcePseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config_1c86fa3992ce0fd24a3980c360d8868a.IsisDcePseudoIfaceAttPoint1Config): An instance of the IsisDcePseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config_1c86fa3992ce0fd24a3980c360d8868a import (
            IsisDcePseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisDcePseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisDcePseudoIfaceAttPoint1Config")
        return IsisDcePseudoIfaceAttPoint1Config(self)

    @property
    def IsisDcePseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config_ccee80f0e3b46537138b8f528ef26472.IsisDcePseudoIfaceAttPoint2Config): An instance of the IsisDcePseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config_ccee80f0e3b46537138b8f528ef26472 import (
            IsisDcePseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisDcePseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisDcePseudoIfaceAttPoint2Config")
        return IsisDcePseudoIfaceAttPoint2Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config_fba88625727b27e259a6fefcf3fe66b2.IsisL3PseudoIfaceAttPoint1Config): An instance of the IsisL3PseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config_fba88625727b27e259a6fefcf3fe66b2 import (
            IsisL3PseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisL3PseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisL3PseudoIfaceAttPoint1Config")
        return IsisL3PseudoIfaceAttPoint1Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config_0204b3dc43c585ae158544fee37480a0.IsisL3PseudoIfaceAttPoint2Config): An instance of the IsisL3PseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config_0204b3dc43c585ae158544fee37480a0 import (
            IsisL3PseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisL3PseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisL3PseudoIfaceAttPoint2Config")
        return IsisL3PseudoIfaceAttPoint2Config(self)

    @property
    def IsisPseudoAppSpecSrlgList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudoappspecsrlglist_16c6e7265cceee1929bab1415b66b941.IsisPseudoAppSpecSrlgList): An instance of the IsisPseudoAppSpecSrlgList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudoappspecsrlglist_16c6e7265cceee1929bab1415b66b941 import (
            IsisPseudoAppSpecSrlgList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisPseudoAppSpecSrlgList", None) is not None:
                return self._properties.get("IsisPseudoAppSpecSrlgList")
        return IsisPseudoAppSpecSrlgList(self)._select()

    @property
    def IsisPseudoMTIDList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomtidlist_953f6f5d73f9f8b772ed5ed34413424e.IsisPseudoMTIDList): An instance of the IsisPseudoMTIDList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomtidlist_953f6f5d73f9f8b772ed5ed34413424e import (
            IsisPseudoMTIDList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisPseudoMTIDList", None) is not None:
                return self._properties.get("IsisPseudoMTIDList")
        return IsisPseudoMTIDList(self)._select()

    @property
    def IsisPseudoSRv6AdjSIDList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6adjsidlist_4bf1c7cd2b913a5dfd4e1e7ab2e4a493.IsisPseudoSRv6AdjSIDList): An instance of the IsisPseudoSRv6AdjSIDList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6adjsidlist_4bf1c7cd2b913a5dfd4e1e7ab2e4a493 import (
            IsisPseudoSRv6AdjSIDList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisPseudoSRv6AdjSIDList", None) is not None:
                return self._properties.get("IsisPseudoSRv6AdjSIDList")
        return IsisPseudoSRv6AdjSIDList(self)._select()

    @property
    def IsisPseudoTraffEngProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudotraffengprofile_4b26eb844b57581d51b1f16b6e17c94a.IsisPseudoTraffEngProfile): An instance of the IsisPseudoTraffEngProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudotraffengprofile_4b26eb844b57581d51b1f16b6e17c94a import (
            IsisPseudoTraffEngProfile,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisPseudoTraffEngProfile", None) is not None:
                return self._properties.get("IsisPseudoTraffEngProfile")
        return IsisPseudoTraffEngProfile(self)._select()

    @property
    def IsisSpbPseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config_092b727de5b08e6f5f9e63b9a006b7e1.IsisSpbPseudoIfaceAttPoint1Config): An instance of the IsisSpbPseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config_092b727de5b08e6f5f9e63b9a006b7e1 import (
            IsisSpbPseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisSpbPseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisSpbPseudoIfaceAttPoint1Config")
        return IsisSpbPseudoIfaceAttPoint1Config(self)

    @property
    def IsisSpbPseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config_39508f250dc5c6ad5bffd3fc89ed10ac.IsisSpbPseudoIfaceAttPoint2Config): An instance of the IsisSpbPseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config_39508f250dc5c6ad5bffd3fc89ed10ac import (
            IsisSpbPseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisSpbPseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisSpbPseudoIfaceAttPoint2Config")
        return IsisSpbPseudoIfaceAttPoint2Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint1Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config_6812126cb30044d635b18984fe3b5ccf.IsisTrillPseudoIfaceAttPoint1Config): An instance of the IsisTrillPseudoIfaceAttPoint1Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config_6812126cb30044d635b18984fe3b5ccf import (
            IsisTrillPseudoIfaceAttPoint1Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisTrillPseudoIfaceAttPoint1Config", None)
                is not None
            ):
                return self._properties.get("IsisTrillPseudoIfaceAttPoint1Config")
        return IsisTrillPseudoIfaceAttPoint1Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint2Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config_391dc09e39440c04d9fb0809e7dafb50.IsisTrillPseudoIfaceAttPoint2Config): An instance of the IsisTrillPseudoIfaceAttPoint2Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config_391dc09e39440c04d9fb0809e7dafb50 import (
            IsisTrillPseudoIfaceAttPoint2Config,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IsisTrillPseudoIfaceAttPoint2Config", None)
                is not None
            ):
                return self._properties.get("IsisTrillPseudoIfaceAttPoint2Config")
        return IsisTrillPseudoIfaceAttPoint2Config(self)

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): AdjSID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdjSID"]))

    @property
    def AdjSidCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Adj SID Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdjSidCount"])

    @AdjSidCount.setter
    def AdjSidCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdjSidCount"], value)

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
    def AdvertiseLinkMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Link MSD
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseLinkMsd"])
        )

    @property
    def BFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup Flag, if set, the Adj-SID is eligible for protection
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BFlag"]))

    @property
    def BandwidthPriority0_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 0 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority0_Bps"])
        )

    @property
    def BandwidthPriority1_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 1 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority1_Bps"])
        )

    @property
    def BandwidthPriority2_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 2 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority2_Bps"])
        )

    @property
    def BandwidthPriority3_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 3 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority3_Bps"])
        )

    @property
    def BandwidthPriority4_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 4 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority4_Bps"])
        )

    @property
    def BandwidthPriority5_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 5 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority5_Bps"])
        )

    @property
    def BandwidthPriority6_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 6 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority6_Bps"])
        )

    @property
    def BandwidthPriority7_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth for Priority 7 (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BandwidthPriority7_Bps"])
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
    def DedicatedOnePlusOne(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DedicatedOnePlusOne"])
        )

    @property
    def DedicatedOneToOne(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DedicatedOneToOne"])
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
    def Enable(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This,if enabled, sends the prefix attributes flags.
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
    def EnableAppSpecSrlg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables Application Specific SRLG on the ISIS link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableAppSpecSrlg"])
        )

    @property
    def EnableBit4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 4th bit of the byte representing flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit4"]))

    @property
    def EnableBit5(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 5th bit of the byte representing flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit5"]))

    @property
    def EnableBit6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 6th bit of the byte representing flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit6"]))

    @property
    def EnableBit7(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 7th bit of the byte representing flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit7"]))

    @property
    def EnableBit8(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 8th bit of the byte representing flags.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit8"]))

    @property
    def EnableIPv6SID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IPv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableIPv6SID"]))

    @property
    def EnableLinkProtection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the link protection on the ISIS link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableLinkProtection"])
        )

    @property
    def EnableMT(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MT
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableMT"]))

    @property
    def EnableMt(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable MT
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableMt"])

    @EnableMt.setter
    def EnableMt(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableMt"], value)

    @property
    def EnableNFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables Node flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableNFlag"]))

    @property
    def EnableRFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables redistribution flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableRFlag"]))

    @property
    def EnableSRLG(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the SRLG on the ISIS link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableSRLG"]))

    @property
    def EnableXFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables external flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableXFlag"]))

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
    def FFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Address Family Flag,False value refers to an adjacency with outgoing IPv4 encapsulationTrue value refers to an adjacency with outgoing IPv6 encapsulation
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FFlag"]))

    @property
    def Funcflags(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the function flags
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Funcflags"]))

    @property
    def Function(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies endpoint function codes
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Function"]))

    @property
    def IncludeMaxSlMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then Include Maximum Segment Left MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaxSlMsd"])
        )

    @property
    def IncludeMaximumEndDMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum End D MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumEndDMsd"])
        )

    @property
    def IncludeMaximumEndPopMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Max-End-Pop-MSD n SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumEndPopMsd"])
        )

    @property
    def IncludeMaximumHEncapMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum H.Encap MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumHEncapMsd"])
        )

    @property
    def IncludeMaximumTEncapMsd(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Encap MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumTEncapMsd"])
        )

    @property
    def IncludeMaximumTInsertMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Insert MSDin SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumTInsertMsd"])
        )

    @property
    def Ipv6SidValue(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Adj SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6SidValue"]))

    @property
    def LFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Flag, if set, then the value/index carried by the Adj-SID has local significance
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LFlag"]))

    @property
    def LinkType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LinkType"]))

    @property
    def MaxBandwidth_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxBandwidth_Bps"])
        )

    @property
    def MaxEndDMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions. If the extension header is right underneath the outer IPv6, header is an SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxEndDMsd"]))

    @property
    def MaxEndPopMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in the top MSD in an MSD stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxEndPopMsd"]))

    @property
    def MaxHEncap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the H.Encap behavior. If this field is zero and the E flag is set, then the router can apply H.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxHEncap"]))

    @property
    def MaxReservableBandwidth_Bps(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Reservable Bandwidth (B/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxReservableBandwidth_Bps"])
        )

    @property
    def MaxSlMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum value of the Segments Left (SL) MSD field in the SRH of a received packet before applying the function associated with a SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxSlMsd"]))

    @property
    def MaxTEncap(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxTEncap"]))

    @property
    def MaxTInsertMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxTInsertMsd"]))

    @property
    def MetricLevel(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Metric Level
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MetricLevel"]))

    @property
    def MtCount(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: MT Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["MtCount"])

    @MtCount.setter
    def MtCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MtCount"], value)

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
    def NoOfAppSpecSrlg(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This field value shows how many SRLG Value columns would be there in the GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfAppSpecSrlg"])

    @NoOfAppSpecSrlg.setter
    def NoOfAppSpecSrlg(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfAppSpecSrlg"], value)

    @property
    def NoOfMtIds(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Multi Topologies
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfMtIds"])

    @NoOfMtIds.setter
    def NoOfMtIds(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfMtIds"], value)

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
    def OverrideFFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When false, then F flag value in the packet will be set TRUE/ FALSE depending on whether IPv6/ IPv4 stack is present beside ISIS respectively. When true, then F flag value will be the one as configured.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OverrideFFlag"]))

    @property
    def PFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Persistent flag: when set, this indicates that the Adj-SID value remains persistent across router restart and/or interface flap.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PFlag"]))

    @property
    def Reserved0x40(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x40.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved0x40"]))

    @property
    def Reserved0x80(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x80.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Reserved0x80"]))

    @property
    def SFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set flag: when set, this indicates that the Adj-SID refers to a set of adjacencies
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
    def Srv6SidFlags(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies the value of the SRv6 SID Flags
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Srv6SidFlags"]))

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value Flag, if set, the Adjacency SID carries a value
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

    def update(
        self,
        AdjSidCount=None,
        EnableMt=None,
        MtCount=None,
        Name=None,
        NoOfAppSpecSrlg=None,
        NoOfMtIds=None,
        NoOfTeProfile=None,
        SrlgCount=None,
    ):
        # type: (int, bool, int, str, int, int, int, int) -> IsisL3PseudoInterface
        """Updates isisL3PseudoInterface resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AdjSidCount (number): Adj SID Count
        - EnableMt (bool): Enable MT
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAppSpecSrlg (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - NoOfMtIds (number): Number of Multi Topologies
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AdjSidCount=None,
        EnableMt=None,
        MtCount=None,
        Name=None,
        NoOfAppSpecSrlg=None,
        NoOfMtIds=None,
        NoOfTeProfile=None,
        SrlgCount=None,
    ):
        # type: (int, bool, int, str, int, int, int, int) -> IsisL3PseudoInterface
        """Adds a new isisL3PseudoInterface resource on the json, only valid with batch add utility

        Args
        ----
        - AdjSidCount (number): Adj SID Count
        - EnableMt (bool): Enable MT
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAppSpecSrlg (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - NoOfMtIds (number): Number of Multi Topologies
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Returns
        -------
        - self: This instance with all currently retrieved isisL3PseudoInterface resources using find and the newly added isisL3PseudoInterface resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AdjSidCount=None,
        Count=None,
        DescriptiveName=None,
        EnableMt=None,
        MtCount=None,
        Name=None,
        NoOfAppSpecSrlg=None,
        NoOfMtIds=None,
        NoOfTeProfile=None,
        SrlgCount=None,
    ):
        # type: (int, int, str, bool, int, str, int, int, int, int) -> IsisL3PseudoInterface
        """Finds and retrieves isisL3PseudoInterface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisL3PseudoInterface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisL3PseudoInterface resources from the server.

        Args
        ----
        - AdjSidCount (number): Adj SID Count
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableMt (bool): Enable MT
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAppSpecSrlg (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - NoOfMtIds (number): Number of Multi Topologies
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Returns
        -------
        - self: This instance with matching isisL3PseudoInterface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisL3PseudoInterface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisL3PseudoInterface resources from the server available through an iterator or index

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
        AdvertiseLinkMsd=None,
        BFlag=None,
        BandwidthPriority0_Bps=None,
        BandwidthPriority1_Bps=None,
        BandwidthPriority2_Bps=None,
        BandwidthPriority3_Bps=None,
        BandwidthPriority4_Bps=None,
        BandwidthPriority5_Bps=None,
        BandwidthPriority6_Bps=None,
        BandwidthPriority7_Bps=None,
        DedicatedOnePlusOne=None,
        DedicatedOneToOne=None,
        Enable=None,
        EnableAdjSID=None,
        EnableAppSpecSrlg=None,
        EnableBit4=None,
        EnableBit5=None,
        EnableBit6=None,
        EnableBit7=None,
        EnableBit8=None,
        EnableIPv6SID=None,
        EnableLinkProtection=None,
        EnableMT=None,
        EnableNFlag=None,
        EnableRFlag=None,
        EnableSRLG=None,
        EnableXFlag=None,
        Enhanced=None,
        ExtraTraffic=None,
        FFlag=None,
        Funcflags=None,
        Function=None,
        IncludeMaxSlMsd=None,
        IncludeMaximumEndDMsd=None,
        IncludeMaximumEndPopMsd=None,
        IncludeMaximumHEncapMsd=None,
        IncludeMaximumTEncapMsd=None,
        IncludeMaximumTInsertMsd=None,
        Ipv6SidValue=None,
        LFlag=None,
        LinkType=None,
        MaxBandwidth_Bps=None,
        MaxEndDMsd=None,
        MaxEndPopMsd=None,
        MaxHEncap=None,
        MaxReservableBandwidth_Bps=None,
        MaxSlMsd=None,
        MaxTEncap=None,
        MaxTInsertMsd=None,
        MetricLevel=None,
        OverrideFFlag=None,
        PFlag=None,
        Reserved0x40=None,
        Reserved0x80=None,
        SFlag=None,
        Shared=None,
        Srv6SidFlags=None,
        Unprotected=None,
        VFlag=None,
        Weight=None,
    ):
        """Base class infrastructure that gets a list of isisL3PseudoInterface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AdjSID (str): optional regex of adjSID
        - AdministratorGroup (str): optional regex of administratorGroup
        - AdvertiseLinkMsd (str): optional regex of advertiseLinkMsd
        - BFlag (str): optional regex of bFlag
        - BandwidthPriority0_Bps (str): optional regex of bandwidthPriority0_Bps
        - BandwidthPriority1_Bps (str): optional regex of bandwidthPriority1_Bps
        - BandwidthPriority2_Bps (str): optional regex of bandwidthPriority2_Bps
        - BandwidthPriority3_Bps (str): optional regex of bandwidthPriority3_Bps
        - BandwidthPriority4_Bps (str): optional regex of bandwidthPriority4_Bps
        - BandwidthPriority5_Bps (str): optional regex of bandwidthPriority5_Bps
        - BandwidthPriority6_Bps (str): optional regex of bandwidthPriority6_Bps
        - BandwidthPriority7_Bps (str): optional regex of bandwidthPriority7_Bps
        - DedicatedOnePlusOne (str): optional regex of dedicatedOnePlusOne
        - DedicatedOneToOne (str): optional regex of dedicatedOneToOne
        - Enable (str): optional regex of enable
        - EnableAdjSID (str): optional regex of enableAdjSID
        - EnableAppSpecSrlg (str): optional regex of enableAppSpecSrlg
        - EnableBit4 (str): optional regex of enableBit4
        - EnableBit5 (str): optional regex of enableBit5
        - EnableBit6 (str): optional regex of enableBit6
        - EnableBit7 (str): optional regex of enableBit7
        - EnableBit8 (str): optional regex of enableBit8
        - EnableIPv6SID (str): optional regex of enableIPv6SID
        - EnableLinkProtection (str): optional regex of enableLinkProtection
        - EnableMT (str): optional regex of enableMT
        - EnableNFlag (str): optional regex of enableNFlag
        - EnableRFlag (str): optional regex of enableRFlag
        - EnableSRLG (str): optional regex of enableSRLG
        - EnableXFlag (str): optional regex of enableXFlag
        - Enhanced (str): optional regex of enhanced
        - ExtraTraffic (str): optional regex of extraTraffic
        - FFlag (str): optional regex of fFlag
        - Funcflags (str): optional regex of funcflags
        - Function (str): optional regex of function
        - IncludeMaxSlMsd (str): optional regex of includeMaxSlMsd
        - IncludeMaximumEndDMsd (str): optional regex of includeMaximumEndDMsd
        - IncludeMaximumEndPopMsd (str): optional regex of includeMaximumEndPopMsd
        - IncludeMaximumHEncapMsd (str): optional regex of includeMaximumHEncapMsd
        - IncludeMaximumTEncapMsd (str): optional regex of includeMaximumTEncapMsd
        - IncludeMaximumTInsertMsd (str): optional regex of includeMaximumTInsertMsd
        - Ipv6SidValue (str): optional regex of ipv6SidValue
        - LFlag (str): optional regex of lFlag
        - LinkType (str): optional regex of linkType
        - MaxBandwidth_Bps (str): optional regex of maxBandwidth_Bps
        - MaxEndDMsd (str): optional regex of maxEndDMsd
        - MaxEndPopMsd (str): optional regex of maxEndPopMsd
        - MaxHEncap (str): optional regex of maxHEncap
        - MaxReservableBandwidth_Bps (str): optional regex of maxReservableBandwidth_Bps
        - MaxSlMsd (str): optional regex of maxSlMsd
        - MaxTEncap (str): optional regex of maxTEncap
        - MaxTInsertMsd (str): optional regex of maxTInsertMsd
        - MetricLevel (str): optional regex of metricLevel
        - OverrideFFlag (str): optional regex of overrideFFlag
        - PFlag (str): optional regex of pFlag
        - Reserved0x40 (str): optional regex of reserved0x40
        - Reserved0x80 (str): optional regex of reserved0x80
        - SFlag (str): optional regex of sFlag
        - Shared (str): optional regex of shared
        - Srv6SidFlags (str): optional regex of srv6SidFlags
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
