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


class IsisL3Router(Base):
    """ISIS-L3 Router configuration
    The IsisL3Router class encapsulates a list of isisL3Router resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisL3Router.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "isisL3Router"
    _SDM_ATT_MAP = {
        "BIERNodePrefix": "BIERNodePrefix",
        "Active": "active",
        "AdvertiseNodeMsd": "advertiseNodeMsd",
        "AdvertiseSRLB": "advertiseSRLB",
        "AdvertiseSRMSPreference": "advertiseSRMSPreference",
        "AdvertiseSidAsLocator": "advertiseSidAsLocator",
        "Algorithm": "algorithm",
        "Algorithmsrmpls": "algorithmsrmpls",
        "AreaAddresses": "areaAddresses",
        "AreaAuthenticationType": "areaAuthenticationType",
        "AreaTransmitPasswordOrMD5Key": "areaTransmitPasswordOrMD5Key",
        "Attached": "attached",
        "BIERIPv6NodePrefix": "bIERIPv6NodePrefix",
        "BierNFlag": "bierNFlag",
        "BierRFlag": "bierRFlag",
        "CFlagOfSRv6Cap": "cFlagOfSRv6Cap",
        "CSNPInterval": "cSNPInterval",
        "ConfigureAlgorithm": "configureAlgorithm",
        "ConfigureSIDIndexLabel": "configureSIDIndexLabel",
        "Count": "count",
        "CurrentAreaKey": "currentAreaKey",
        "CurrentDomainKey": "currentDomainKey",
        "DBit": "dBit",
        "DBitForSRv6Cap": "dBitForSRv6Cap",
        "DBitInsideSRv6SidTLV": "dBitInsideSRv6SidTLV",
        "DescriptiveName": "descriptiveName",
        "DiscardLSPs": "discardLSPs",
        "Distribution": "distribution",
        "DomainAuthenticationType": "domainAuthenticationType",
        "DomainTransmitPasswordOrMD5Key": "domainTransmitPasswordOrMD5Key",
        "EFlag": "eFlag",
        "EFlagOfSRv6CapTlv": "eFlagOfSRv6CapTlv",
        "Enable": "enable",
        "EnableBIER": "enableBIER",
        "EnableBit4": "enableBit4",
        "EnableBit5": "enableBit5",
        "EnableBit6": "enableBit6",
        "EnableBit7": "enableBit7",
        "EnableBit8": "enableBit8",
        "EnableHelloPadding": "enableHelloPadding",
        "EnableHitlessRestart": "enableHitlessRestart",
        "EnableHostName": "enableHostName",
        "EnableITID": "enableITID",
        "EnableIpV6TE": "enableIpV6TE",
        "EnableKeyRotation": "enableKeyRotation",
        "EnableMI": "enableMI",
        "EnableMTIPv6": "enableMTIPv6",
        "EnableMappingServer": "enableMappingServer",
        "EnableNFlag": "enableNFlag",
        "EnableRFlag": "enableRFlag",
        "EnableSR": "enableSR",
        "EnableTE": "enableTE",
        "EnableWMforTE": "enableWMforTE",
        "EnableWideMetric": "enableWideMetric",
        "EnableXFlag": "enableXFlag",
        "Errors": "errors",
        "FlexAlgoCount": "flexAlgoCount",
        "Funcflags": "funcflags",
        "Function": "function",
        "HitlessRestartMode": "hitlessRestartMode",
        "HitlessRestartTime": "hitlessRestartTime",
        "HitlessRestartVersion": "hitlessRestartVersion",
        "HostName": "hostName",
        "IgnoreReceiveMD5": "ignoreReceiveMD5",
        "Iid": "iid",
        "IncludeMaxSlMsd": "includeMaxSlMsd",
        "IncludeMaximumEndDMsd": "includeMaximumEndDMsd",
        "IncludeMaximumEndDSrhTLV": "includeMaximumEndDSrhTLV",
        "IncludeMaximumEndPopMsd": "includeMaximumEndPopMsd",
        "IncludeMaximumEndPopSrhTLV": "includeMaximumEndPopSrhTLV",
        "IncludeMaximumHEncapMsd": "includeMaximumHEncapMsd",
        "IncludeMaximumSLTLV": "includeMaximumSLTLV",
        "IncludeMaximumTEncapMsd": "includeMaximumTEncapMsd",
        "IncludeMaximumTEncapSrhTLV": "includeMaximumTEncapSrhTLV",
        "IncludeMaximumTInsertMsd": "includeMaximumTInsertMsd",
        "IncludeMaximumTInsertSrhTLV": "includeMaximumTInsertSrhTLV",
        "IncludePrefixAttrFlags": "includePrefixAttrFlags",
        "InterLSPsOrMGroupPDUBurstGap": "interLSPsOrMGroupPDUBurstGap",
        "IpV6TERouterId": "ipV6TERouterId",
        "Ipv4Flag": "ipv4Flag",
        "Ipv6Flag": "ipv6Flag",
        "Ipv6NodePrefix": "ipv6NodePrefix",
        "Ipv6Srh": "ipv6Srh",
        "Itid": "itid",
        "LFlag": "lFlag",
        "LSPLifetime": "lSPLifetime",
        "LSPRefreshRate": "lSPRefreshRate",
        "LSPorMGroupPDUMinTransmissionInterval": "lSPorMGroupPDUMinTransmissionInterval",
        "LocalSystemID": "localSystemID",
        "LocatorCount": "locatorCount",
        "LocatorPrefixLength": "locatorPrefixLength",
        "Mask": "mask",
        "MaxAreaAddresses": "maxAreaAddresses",
        "MaxEndD": "maxEndD",
        "MaxEndDMsd": "maxEndDMsd",
        "MaxEndPopMsd": "maxEndPopMsd",
        "MaxEndPopSrh": "maxEndPopSrh",
        "MaxHEncapMsd": "maxHEncapMsd",
        "MaxLSPSize": "maxLSPSize",
        "MaxLSPsOrMGroupPDUsPerBurst": "maxLSPsOrMGroupPDUsPerBurst",
        "MaxSL": "maxSL",
        "MaxSlMsd": "maxSlMsd",
        "MaxTEncap": "maxTEncap",
        "MaxTEncapMsd": "maxTEncapMsd",
        "MaxTInsert": "maxTInsert",
        "MaxTInsertMsd": "maxTInsertMsd",
        "MtCount": "mtCount",
        "MvDontAdvNodePrefix": "mvDontAdvNodePrefix",
        "NFlag": "nFlag",
        "Name": "name",
        "NoOfBIERSubDomains": "noOfBIERSubDomains",
        "NoOfSRTunnels": "noOfSRTunnels",
        "NodePrefix": "nodePrefix",
        "NumberOfKeys": "numberOfKeys",
        "NumberOfMappingIPV4Ranges": "numberOfMappingIPV4Ranges",
        "NumberOfMappingIPV6Ranges": "numberOfMappingIPV6Ranges",
        "OFlagOfSRv6Cap": "oFlagOfSRv6Cap",
        "OFlagOfSRv6CapTlv": "oFlagOfSRv6CapTlv",
        "Overloaded": "overloaded",
        "PFlag": "pFlag",
        "PSNPInterval": "pSNPInterval",
        "PartitionRepair": "partitionRepair",
        "PrefixAdvertisementType": "prefixAdvertisementType",
        "PrefixLength": "prefixLength",
        "RFlag": "rFlag",
        "Redistribution": "redistribution",
        "RedistributionForSRv6": "redistributionForSRv6",
        "ReservedInsideFlagsOfSRv6SidTLV": "reservedInsideFlagsOfSRv6SidTLV",
        "ReservedInsideSRv6CapFlag": "reservedInsideSRv6CapFlag",
        "RouteMetric": "routeMetric",
        "RouteOrigin": "routeOrigin",
        "RtrcapId": "rtrcapId",
        "RtrcapIdForSrv6": "rtrcapIdForSrv6",
        "SBit": "sBit",
        "SBitForSRv6Cap": "sBitForSRv6Cap",
        "SIDIndexLabel": "sIDIndexLabel",
        "SRAlgorithmCount": "sRAlgorithmCount",
        "SRGBRangeCount": "sRGBRangeCount",
        "SRv6NodePrefix": "sRv6NodePrefix",
        "SRv6NodePrefixLength": "sRv6NodePrefixLength",
        "SessionInfo": "sessionInfo",
        "SessionStatus": "sessionStatus",
        "SetIpv6TERouterId": "setIpv6TERouterId",
        "SetTERouterId": "setTERouterId",
        "SrlbDescriptorCount": "srlbDescriptorCount",
        "SrlbFlags": "srlbFlags",
        "SrmsPreference": "srmsPreference",
        "Srv6OAMService": "srv6OAMService",
        "StateCounts": "stateCounts",
        "Status": "status",
        "TERouterId": "tERouterId",
        "TilfaCardNo": "tilfaCardNo",
        "TilfaMac": "tilfaMac",
        "TilfaPortIp": "tilfaPortIp",
        "TilfaPortNo": "tilfaPortNo",
        "VFlag": "vFlag",
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
        super(IsisL3Router, self).__init__(parent, list_op)

    @property
    def IsisBierSubDomainList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisbiersubdomainlist_e392fab58663b756ea9ae50d89caf0aa.IsisBierSubDomainList): An instance of the IsisBierSubDomainList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisbiersubdomainlist_e392fab58663b756ea9ae50d89caf0aa import (
            IsisBierSubDomainList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisBierSubDomainList", None) is not None:
                return self._properties.get("IsisBierSubDomainList")
        return IsisBierSubDomainList(self)._select()

    @property
    def IsisFlexAlgorithmList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisflexalgorithmlist_d9008e99957f9f9e1c7f80b24180ceb1.IsisFlexAlgorithmList): An instance of the IsisFlexAlgorithmList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisflexalgorithmlist_d9008e99957f9f9e1c7f80b24180ceb1 import (
            IsisFlexAlgorithmList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisFlexAlgorithmList", None) is not None:
                return self._properties.get("IsisFlexAlgorithmList")
        return IsisFlexAlgorithmList(self)._select()

    @property
    def IsisMappingServerIPV4List(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isismappingserveripv4list_c7d4f6854a653f4b6b5515d4e80967be.IsisMappingServerIPV4List): An instance of the IsisMappingServerIPV4List class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isismappingserveripv4list_c7d4f6854a653f4b6b5515d4e80967be import (
            IsisMappingServerIPV4List,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisMappingServerIPV4List", None) is not None:
                return self._properties.get("IsisMappingServerIPV4List")
        return IsisMappingServerIPV4List(self)._select()

    @property
    def IsisMappingServerIPV6List(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isismappingserveripv6list_1942b0df99563e99e9978de27ba52354.IsisMappingServerIPV6List): An instance of the IsisMappingServerIPV6List class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isismappingserveripv6list_1942b0df99563e99e9978de27ba52354 import (
            IsisMappingServerIPV6List,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisMappingServerIPV6List", None) is not None:
                return self._properties.get("IsisMappingServerIPV6List")
        return IsisMappingServerIPV6List(self)._select()

    @property
    def IsisMultiTopologyValuesList(self):
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isismultitopologyvalueslist_aade22a247f2e2b1f2285c77e9114dda.IsisMultiTopologyValuesList): An instance of the IsisMultiTopologyValuesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isismultitopologyvalueslist_aade22a247f2e2b1f2285c77e9114dda import (
            IsisMultiTopologyValuesList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisMultiTopologyValuesList", None) is not None:
                return self._properties.get("IsisMultiTopologyValuesList")
        return IsisMultiTopologyValuesList(self)

    @property
    def IsisRouterKeyList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisrouterkeylist_1ca3576036ca25f0a27ee9750620e641.IsisRouterKeyList): An instance of the IsisRouterKeyList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisrouterkeylist_1ca3576036ca25f0a27ee9750620e641 import (
            IsisRouterKeyList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisRouterKeyList", None) is not None:
                return self._properties.get("IsisRouterKeyList")
        return IsisRouterKeyList(self)._select()

    @property
    def IsisSRAlgorithmList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissralgorithmlist_a50f1cd4168a3642597a66e7f63343e6.IsisSRAlgorithmList): An instance of the IsisSRAlgorithmList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissralgorithmlist_a50f1cd4168a3642597a66e7f63343e6 import (
            IsisSRAlgorithmList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSRAlgorithmList", None) is not None:
                return self._properties.get("IsisSRAlgorithmList")
        return IsisSRAlgorithmList(self)

    @property
    def IsisSRGBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrgbrangesubobjectslist_6180dd47f637b6f4581c2dcaa7a1a071.IsisSRGBRangeSubObjectsList): An instance of the IsisSRGBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrgbrangesubobjectslist_6180dd47f637b6f4581c2dcaa7a1a071 import (
            IsisSRGBRangeSubObjectsList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSRGBRangeSubObjectsList", None) is not None:
                return self._properties.get("IsisSRGBRangeSubObjectsList")
        return IsisSRGBRangeSubObjectsList(self)

    @property
    def IsisSRLBDescriptorList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrlbdescriptorlist_1eec075b53920dfd5040006478718f6a.IsisSRLBDescriptorList): An instance of the IsisSRLBDescriptorList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrlbdescriptorlist_1eec075b53920dfd5040006478718f6a import (
            IsisSRLBDescriptorList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSRLBDescriptorList", None) is not None:
                return self._properties.get("IsisSRLBDescriptorList")
        return IsisSRLBDescriptorList(self)

    @property
    def IsisSRTunnelList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrtunnellist_4c3217e504788bc35135af392bfa9c40.IsisSRTunnelList): An instance of the IsisSRTunnelList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrtunnellist_4c3217e504788bc35135af392bfa9c40 import (
            IsisSRTunnelList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSRTunnelList", None) is not None:
                return self._properties.get("IsisSRTunnelList")
        return IsisSRTunnelList(self)._select()

    @property
    def IsisSRv6LocatorEntryList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrv6locatorentrylist_965cfb223e730eee317d21e8ffbbfe07.IsisSRv6LocatorEntryList): An instance of the IsisSRv6LocatorEntryList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrv6locatorentrylist_965cfb223e730eee317d21e8ffbbfe07 import (
            IsisSRv6LocatorEntryList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisSRv6LocatorEntryList", None) is not None:
                return self._properties.get("IsisSRv6LocatorEntryList")
        return IsisSRv6LocatorEntryList(self)._select()

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
    def BIERNodePrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BIERNodePrefix"])
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
    def AdvertiseNodeMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Node MSD
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseNodeMsd"])
        )

    @property
    def AdvertiseSRLB(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables advertisement of Segment Routing Local Block (SRLB) Sub-Tlv in Router Capability Tlv
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseSRLB"]))

    @property
    def AdvertiseSRMSPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRMS Preference sub-TLV in Router capability TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseSRMSPreference"])
        )

    @property
    def AdvertiseSidAsLocator(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, then the configured IPv6 Node SID gets advertised as a reachable IPv6 prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AdvertiseSidAsLocator"])
        )

    @property
    def Algorithm(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Algorithm"]))

    @property
    def Algorithmsrmpls(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm in SR-MPLS
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Algorithmsrmpls"])
        )

    @property
    def AreaAddresses(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AreaAddresses"]))

    @property
    def AreaAuthenticationType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Authentication Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AreaAuthenticationType"])
        )

    @property
    def AreaTransmitPasswordOrMD5Key(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area Transmit Password / MD5-Key
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AreaTransmitPasswordOrMD5Key"])
        )

    @property
    def Attached(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Attached
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Attached"]))

    @property
    def BIERIPv6NodePrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Node Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BIERIPv6NodePrefix"])
        )

    @property
    def BierNFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nodal prefix flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BierNFlag"]))

    @property
    def BierRFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BierRFlag"]))

    @property
    def CFlagOfSRv6Cap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, it indicates that this node support compression.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CFlagOfSRv6Cap"])
        )

    @property
    def CSNPInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CSNP Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CSNPInterval"]))

    @property
    def ConfigureAlgorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, algorithm value will be used from here. Else algorithm is taken as the lowest algorithm from the SR-Capability-List.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureAlgorithm"])
        )

    @property
    def ConfigureSIDIndexLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureSIDIndexLabel"])
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
    def CurrentAreaKey(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Logs the current Area key being used for authentication.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentAreaKey"])

    @property
    def CurrentDomainKey(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Logs the current Domain key being used for authentication.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentDomainKey"])

    @property
    def DBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DBit"]))

    @property
    def DBitForSRv6Cap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DBitForSRv6Cap"])
        )

    @property
    def DBitInsideSRv6SidTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DBitInsideSRv6SidTLV"])
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
    def DiscardLSPs(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discard LSPs
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DiscardLSPs"]))

    @property
    def Distribution(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Distribution
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Distribution"]))

    @property
    def DomainAuthenticationType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Authentication Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DomainAuthenticationType"])
        )

    @property
    def DomainTransmitPasswordOrMD5Key(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Domain Transmit Password / MD5-Key
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DomainTransmitPasswordOrMD5Key"]),
        )

    @property
    def EFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit NULL flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EFlag"]))

    @property
    def EFlagOfSRv6CapTlv(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then router is able to apply T.Encap operation
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EFlagOfSRv6CapTlv"])
        )

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
    def EnableBIER(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable BIER
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBIER"])

    @EnableBIER.setter
    def EnableBIER(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBIER"], value)

    @property
    def EnableBit4(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 4th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit4"]))

    @property
    def EnableBit5(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 5th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit5"]))

    @property
    def EnableBit6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 6th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit6"]))

    @property
    def EnableBit7(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 7th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit7"]))

    @property
    def EnableBit8(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables 8th bit of the byte representing the flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableBit8"]))

    @property
    def EnableHelloPadding(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Hello Padding
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableHelloPadding"])
        )

    @property
    def EnableHitlessRestart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Hitless Restart
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableHitlessRestart"])
        )

    @property
    def EnableHostName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableHostName"])
        )

    @property
    def EnableITID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this checkbox to enable Instance-specific topology identifier. Once it is enabled, it allows to configure ITID value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableITID"]))

    @property
    def EnableIpV6TE(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If it is enabled, the ISIS Traffic Engineering Profiles will be available. If not enabled, then no TE fields will be sent out in TLV 222.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableIpV6TE"]))

    @property
    def EnableKeyRotation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable Key rotation feature.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableKeyRotation"])

    @EnableKeyRotation.setter
    def EnableKeyRotation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableKeyRotation"], value)

    @property
    def EnableMI(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select this checkbox to configure the Router as Multi Instance. Once it is enabled, it allows to configure IID and ITID details.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableMI"]))

    @property
    def EnableMTIPv6(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MT for IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableMTIPv6"]))

    @property
    def EnableMappingServer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This ensures whether the ISIS router will behave as a Segment Routing Mapping Server (SRMS) or not.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableMappingServer"])
        )

    @property
    def EnableNFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables node flag.
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
    def EnableSR(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This enables SR MPLS on all the emulated ISIS router(s)
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSR"])

    @EnableSR.setter
    def EnableSR(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSR"], value)

    @property
    def EnableTE(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IPv4 TE
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableTE"]))

    @property
    def EnableWMforTE(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hidden field is to disable wide Metric, when user disable TE Router conditionally
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableWMforTE"]))

    @property
    def EnableWideMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Wide Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableWideMetric"])
        )

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
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def FlexAlgoCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If the count is greater than 0, then the Flex Algo tab will appear after ISIS-L3 RTR tab. Default is 0. Range is 0-128.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlexAlgoCount"])

    @FlexAlgoCount.setter
    def FlexAlgoCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlexAlgoCount"], value)

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
    def HitlessRestartMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HitlessRestartMode"])
        )

    @property
    def HitlessRestartTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Time
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HitlessRestartTime"])
        )

    @property
    def HitlessRestartVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Restart Version
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HitlessRestartVersion"])
        )

    @property
    def HostName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostName"]))

    @property
    def IgnoreReceiveMD5(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ignore Receive MD5
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IgnoreReceiveMD5"])
        )

    @property
    def Iid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Instance Identifier. Configure any number within the range of 0-65535.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Iid"]))

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
    def IncludeMaximumEndDSrhTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum End D SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumEndDSrhTLV"])
        )

    @property
    def IncludeMaximumEndPopMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Max-End-Pop-MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumEndPopMsd"])
        )

    @property
    def IncludeMaximumEndPopSrhTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Max-End-Pop-SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumEndPopSrhTLV"])
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
    def IncludeMaximumSLTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum SL TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumSLTLV"])
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
    def IncludeMaximumTEncapSrhTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Encap SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumTEncapSrhTLV"])
        )

    @property
    def IncludeMaximumTInsertMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Insert MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumTInsertMsd"])
        )

    @property
    def IncludeMaximumTInsertSrhTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Insert SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludeMaximumTInsertSrhTLV"])
        )

    @property
    def IncludePrefixAttrFlags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Prefix Attributes Flags
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IncludePrefixAttrFlags"])
        )

    @property
    def InterLSPsOrMGroupPDUBurstGap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Inter LSPs/MGROUP-PDUs Burst Gap (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterLSPsOrMGroupPDUBurstGap"])
        )

    @property
    def IpV6TERouterId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It is a unique ID including emulated and simulated routers. It should match IPv6 Node Prefix in SRv6 by default. It will send out the TLV 140 in ISIS.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IpV6TERouterId"])
        )

    @property
    def Ipv4Flag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then the router is capable of processing SR MPLS encapsulated IPv4 packets on all interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv4Flag"]))

    @property
    def Ipv6Flag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then the router is capable of processing SR MPLS encapsulated IPv6 packets on all interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6Flag"]))

    @property
    def Ipv6NodePrefix(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Node SID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ipv6NodePrefix"])
        )

    @property
    def Ipv6Srh(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the SR-IPv6 flag. If set to true, then this enables the SRv6 capability on the router If set to false, then this enables the MPLS SR capability on the router
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ipv6Srh"]))

    @property
    def Itid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Instance-specific topology identifier. Configure any number within the range of 0-65535.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Itid"]))

    @property
    def LFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LFlag"]))

    @property
    def LSPLifetime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Rifetime (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LSPLifetime"]))

    @property
    def LSPRefreshRate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP Refresh Rate (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LSPRefreshRate"])
        )

    @property
    def LSPorMGroupPDUMinTransmissionInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSP/MGROUP-PDU Min Transmission Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["LSPorMGroupPDUMinTransmissionInterval"]
            ),
        )

    @property
    def LocalSystemID(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): System ID
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalSystemID"])

    @property
    def LocatorCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Locator Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocatorCount"])

    @LocatorCount.setter
    def LocatorCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LocatorCount"], value)

    @property
    def LocatorPrefixLength(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LocatorPrefixLength"])
        )

    @property
    def Mask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mask
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mask"]))

    @property
    def MaxAreaAddresses(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Area Addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxAreaAddresses"])
        )

    @property
    def MaxEndD(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions if the extension header right underneath the outer IPv6 header is an SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxEndD"]))

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
    def MaxEndPopSrh(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in the top SRH in an SRH stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxEndPopSrh"]))

    @property
    def MaxHEncapMsd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the H.Encap behavior. If this field is zero and the E flag is set, then the router can apply H.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxHEncapMsd"]))

    @property
    def MaxLSPSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max PDU Size
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxLSPSize"]))

    @property
    def MaxLSPsOrMGroupPDUsPerBurst(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max LSPs/MGROUP-PDUs Per Burst
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxLSPsOrMGroupPDUsPerBurst"])
        )

    @property
    def MaxSL(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum value of the Segments Left (SL) field in the SRH of a received packet before applying the function associated with a SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxSL"]))

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxTEncap"]))

    @property
    def MaxTEncapMsd(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxTEncapMsd"]))

    @property
    def MaxTInsert(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxTInsert"]))

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
    def MvDontAdvNodePrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If disabled, the node prefix/node SID in ISIS RTR SR tab is not advertised (in TLV 135, 235 or 237). This may be used when user wants router to send one node prefix with multiple flexible algorithms in single TLV. User can disable advertising the node prefix in router configuration, then configure same node prefix with multiple algorithms and SIDs in Network Group.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MvDontAdvNodePrefix"])
        )

    @property
    def NFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nodal prefix flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NFlag"]))

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
    def NoOfBIERSubDomains(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of BIER Sub Domains
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfBIERSubDomains"])

    @NoOfBIERSubDomains.setter
    def NoOfBIERSubDomains(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfBIERSubDomains"], value)

    @property
    def NoOfSRTunnels(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of MPLS SR Tunnels
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfSRTunnels"])

    @NoOfSRTunnels.setter
    def NoOfSRTunnels(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfSRTunnels"], value)

    @property
    def NodePrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["NodePrefix"]))

    @property
    def NumberOfKeys(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Keys to be used for authetication
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfKeys"])

    @NumberOfKeys.setter
    def NumberOfKeys(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfKeys"], value)

    @property
    def NumberOfMappingIPV4Ranges(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of IPv4 mappings or range TLVs that each router in a DG can advertise.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfMappingIPV4Ranges"])

    @NumberOfMappingIPV4Ranges.setter
    def NumberOfMappingIPV4Ranges(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfMappingIPV4Ranges"], value)

    @property
    def NumberOfMappingIPV6Ranges(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of IPv6 mappings or range TLVs that each router in a DG can advertise.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfMappingIPV6Ranges"])

    @NumberOfMappingIPV6Ranges.setter
    def NumberOfMappingIPV6Ranges(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfMappingIPV6Ranges"], value)

    @property
    def OFlagOfSRv6Cap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, it indicates that this packet is an operations and management (OAM) packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OFlagOfSRv6Cap"])
        )

    @property
    def OFlagOfSRv6CapTlv(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, it indicates that this packet is an operations and management (OAM) packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OFlagOfSRv6CapTlv"])
        )

    @property
    def Overloaded(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Overloaded
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Overloaded"]))

    @property
    def PFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PFlag"]))

    @property
    def PSNPInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PSNP Interval (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PSNPInterval"]))

    @property
    def PartitionRepair(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Partition Repair
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PartitionRepair"])
        )

    @property
    def PrefixAdvertisementType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix Advertisement Type
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrefixAdvertisementType"])
        )

    @property
    def PrefixLength(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PrefixLength"]))

    @property
    def RFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RFlag"]))

    @property
    def Redistribution(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Redistribution"])
        )

    @property
    def RedistributionForSRv6(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RedistributionForSRv6"])
        )

    @property
    def ReservedInsideFlagsOfSRv6SidTLV(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the reserved field (part of flags field of SRv6 SID TLV)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["ReservedInsideFlagsOfSRv6SidTLV"]),
        )

    @property
    def ReservedInsideSRv6CapFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the reserved field (as part of Flags field of SRv6 Capability TLV)
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReservedInsideSRv6CapFlag"])
        )

    @property
    def RouteMetric(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RouteMetric"]))

    @property
    def RouteOrigin(self):
        # type: () -> 'Multivalue'
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RouteOrigin"]))

    @property
    def RtrcapId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router Capability Id
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RtrcapId"]))

    @property
    def RtrcapIdForSrv6(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router Capability Id
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtrcapIdForSrv6"])
        )

    @property
    def SBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SBit"]))

    @property
    def SBitForSRv6Cap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SBitForSRv6Cap"])
        )

    @property
    def SIDIndexLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SIDIndexLabel"]))

    @property
    def SRAlgorithmCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SR Algorithm Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SRAlgorithmCount"])

    @SRAlgorithmCount.setter
    def SRAlgorithmCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SRAlgorithmCount"], value)

    @property
    def SRGBRangeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SRGB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP["SRGBRangeCount"])

    @SRGBRangeCount.setter
    def SRGBRangeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SRGBRangeCount"], value)

    @property
    def SRv6NodePrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is an IPv6 Node prefix for the SRv6 router
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SRv6NodePrefix"])
        )

    @property
    def SRv6NodePrefixLength(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the prefix length of the SRv6 node prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SRv6NodePrefixLength"])
        )

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[noIfaceUp | up]): Logs additional information about the session Information
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
    def SetIpv6TERouterId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the IPv6 TE Router ID IPv6 address in the Simulated Bridge tab is set to the same value as IPv6 Node Prefix. If IPv6 Node Prefix is changed, the IPv6 TE Router ID value also changes automatically. This avoids duplicate configuration in the IPv6 TE router ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetIpv6TERouterId"])

    @SetIpv6TERouterId.setter
    def SetIpv6TERouterId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetIpv6TERouterId"], value)

    @property
    def SetTERouterId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the TE Router ID IP address in the Basic tab is set to the same value as Node Prefix. If Node Prefix is changed, the TE Router ID value also changes automatically. This avoids duplicate configuration in the TE router ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetTERouterId"])

    @SetTERouterId.setter
    def SetTERouterId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetTERouterId"], value)

    @property
    def SrlbDescriptorCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrlbDescriptorCount"])

    @SrlbDescriptorCount.setter
    def SrlbDescriptorCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SrlbDescriptorCount"], value)

    @property
    def SrlbFlags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies the value of the SRLB flags field
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SrlbFlags"]))

    @property
    def SrmsPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is used to associate a preference with SRMS advertisements and is being advertised as a sub-TLV in Router Capability TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SrmsPreference"])
        )

    @property
    def Srv6OAMService(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This option will enable OAM services for ISIS SRv6.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Srv6OAMService"])
        )

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
    def TERouterId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE Router ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TERouterId"]))

    @property
    def TilfaCardNo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Target card number to create backup path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TilfaCardNo"]))

    @property
    def TilfaMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination mac address to create backup path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TilfaMac"]))

    @property
    def TilfaPortIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Target port IP address to create backup path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TilfaPortIp"]))

    @property
    def TilfaPortNo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Target port number to create backup path
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TilfaPortNo"]))

    @property
    def VFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VFlag"]))

    def update(
        self,
        EnableBIER=None,
        EnableKeyRotation=None,
        EnableSR=None,
        FlexAlgoCount=None,
        LocatorCount=None,
        MtCount=None,
        Name=None,
        NoOfBIERSubDomains=None,
        NoOfSRTunnels=None,
        NumberOfKeys=None,
        NumberOfMappingIPV4Ranges=None,
        NumberOfMappingIPV6Ranges=None,
        SRAlgorithmCount=None,
        SRGBRangeCount=None,
        SetIpv6TERouterId=None,
        SetTERouterId=None,
        SrlbDescriptorCount=None,
    ):
        # type: (bool, bool, bool, int, int, int, str, int, int, int, int, int, int, int, bool, bool, int) -> IsisL3Router
        """Updates isisL3Router resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableBIER (bool): Enable BIER
        - EnableKeyRotation (bool): Enable Key rotation feature.
        - EnableSR (bool): This enables SR MPLS on all the emulated ISIS router(s)
        - FlexAlgoCount (number): If the count is greater than 0, then the Flex Algo tab will appear after ISIS-L3 RTR tab. Default is 0. Range is 0-128.
        - LocatorCount (number): Locator Count
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfBIERSubDomains (number): Number of BIER Sub Domains
        - NoOfSRTunnels (number): Number of MPLS SR Tunnels
        - NumberOfKeys (number): Number of Keys to be used for authetication
        - NumberOfMappingIPV4Ranges (number): Specifies the number of IPv4 mappings or range TLVs that each router in a DG can advertise.
        - NumberOfMappingIPV6Ranges (number): Specifies the number of IPv6 mappings or range TLVs that each router in a DG can advertise.
        - SRAlgorithmCount (number): SR Algorithm Count
        - SRGBRangeCount (number): SRGB Range Count
        - SetIpv6TERouterId (bool): If enabled, the IPv6 TE Router ID IPv6 address in the Simulated Bridge tab is set to the same value as IPv6 Node Prefix. If IPv6 Node Prefix is changed, the IPv6 TE Router ID value also changes automatically. This avoids duplicate configuration in the IPv6 TE router ID field.
        - SetTERouterId (bool): If enabled, the TE Router ID IP address in the Basic tab is set to the same value as Node Prefix. If Node Prefix is changed, the TE Router ID value also changes automatically. This avoids duplicate configuration in the TE router ID field.
        - SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        EnableBIER=None,
        EnableKeyRotation=None,
        EnableSR=None,
        FlexAlgoCount=None,
        LocatorCount=None,
        MtCount=None,
        Name=None,
        NoOfBIERSubDomains=None,
        NoOfSRTunnels=None,
        NumberOfKeys=None,
        NumberOfMappingIPV4Ranges=None,
        NumberOfMappingIPV6Ranges=None,
        SRAlgorithmCount=None,
        SRGBRangeCount=None,
        SetIpv6TERouterId=None,
        SetTERouterId=None,
        SrlbDescriptorCount=None,
    ):
        # type: (bool, bool, bool, int, int, int, str, int, int, int, int, int, int, int, bool, bool, int) -> IsisL3Router
        """Adds a new isisL3Router resource on the json, only valid with batch add utility

        Args
        ----
        - EnableBIER (bool): Enable BIER
        - EnableKeyRotation (bool): Enable Key rotation feature.
        - EnableSR (bool): This enables SR MPLS on all the emulated ISIS router(s)
        - FlexAlgoCount (number): If the count is greater than 0, then the Flex Algo tab will appear after ISIS-L3 RTR tab. Default is 0. Range is 0-128.
        - LocatorCount (number): Locator Count
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfBIERSubDomains (number): Number of BIER Sub Domains
        - NoOfSRTunnels (number): Number of MPLS SR Tunnels
        - NumberOfKeys (number): Number of Keys to be used for authetication
        - NumberOfMappingIPV4Ranges (number): Specifies the number of IPv4 mappings or range TLVs that each router in a DG can advertise.
        - NumberOfMappingIPV6Ranges (number): Specifies the number of IPv6 mappings or range TLVs that each router in a DG can advertise.
        - SRAlgorithmCount (number): SR Algorithm Count
        - SRGBRangeCount (number): SRGB Range Count
        - SetIpv6TERouterId (bool): If enabled, the IPv6 TE Router ID IPv6 address in the Simulated Bridge tab is set to the same value as IPv6 Node Prefix. If IPv6 Node Prefix is changed, the IPv6 TE Router ID value also changes automatically. This avoids duplicate configuration in the IPv6 TE router ID field.
        - SetTERouterId (bool): If enabled, the TE Router ID IP address in the Basic tab is set to the same value as Node Prefix. If Node Prefix is changed, the TE Router ID value also changes automatically. This avoids duplicate configuration in the TE router ID field.
        - SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}

        Returns
        -------
        - self: This instance with all currently retrieved isisL3Router resources using find and the newly added isisL3Router resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        CurrentAreaKey=None,
        CurrentDomainKey=None,
        DescriptiveName=None,
        EnableBIER=None,
        EnableKeyRotation=None,
        EnableSR=None,
        Errors=None,
        FlexAlgoCount=None,
        LocalSystemID=None,
        LocatorCount=None,
        MtCount=None,
        Name=None,
        NoOfBIERSubDomains=None,
        NoOfSRTunnels=None,
        NumberOfKeys=None,
        NumberOfMappingIPV4Ranges=None,
        NumberOfMappingIPV6Ranges=None,
        SRAlgorithmCount=None,
        SRGBRangeCount=None,
        SessionInfo=None,
        SessionStatus=None,
        SetIpv6TERouterId=None,
        SetTERouterId=None,
        SrlbDescriptorCount=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves isisL3Router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisL3Router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisL3Router resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - CurrentAreaKey (list(number)): Logs the current Area key being used for authentication.
        - CurrentDomainKey (list(number)): Logs the current Domain key being used for authentication.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableBIER (bool): Enable BIER
        - EnableKeyRotation (bool): Enable Key rotation feature.
        - EnableSR (bool): This enables SR MPLS on all the emulated ISIS router(s)
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - FlexAlgoCount (number): If the count is greater than 0, then the Flex Algo tab will appear after ISIS-L3 RTR tab. Default is 0. Range is 0-128.
        - LocalSystemID (list(str)): System ID
        - LocatorCount (number): Locator Count
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfBIERSubDomains (number): Number of BIER Sub Domains
        - NoOfSRTunnels (number): Number of MPLS SR Tunnels
        - NumberOfKeys (number): Number of Keys to be used for authetication
        - NumberOfMappingIPV4Ranges (number): Specifies the number of IPv4 mappings or range TLVs that each router in a DG can advertise.
        - NumberOfMappingIPV6Ranges (number): Specifies the number of IPv6 mappings or range TLVs that each router in a DG can advertise.
        - SRAlgorithmCount (number): SR Algorithm Count
        - SRGBRangeCount (number): SRGB Range Count
        - SessionInfo (list(str[noIfaceUp | up])): Logs additional information about the session Information
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SetIpv6TERouterId (bool): If enabled, the IPv6 TE Router ID IPv6 address in the Simulated Bridge tab is set to the same value as IPv6 Node Prefix. If IPv6 Node Prefix is changed, the IPv6 TE Router ID value also changes automatically. This avoids duplicate configuration in the IPv6 TE router ID field.
        - SetTERouterId (bool): If enabled, the TE Router ID IP address in the Basic tab is set to the same value as Node Prefix. If Node Prefix is changed, the TE Router ID value also changes automatically. This avoids duplicate configuration in the TE router ID field.
        - SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching isisL3Router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisL3Router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisL3Router resources from the server available through an iterator or index

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

    def IsisStartRouter(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the isisStartRouter operation on the server.

        Start ISIS Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        isisStartRouter(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        isisStartRouter(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        isisStartRouter(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------
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
        return self._execute("isisStartRouter", payload=payload, response_object=None)

    def IsisStopRouter(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the isisStopRouter operation on the server.

        Stop ISIS Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        isisStopRouter(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        isisStopRouter(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        isisStopRouter(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------
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
        return self._execute("isisStopRouter", payload=payload, response_object=None)

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
        BIERNodePrefix=None,
        Active=None,
        AdvertiseNodeMsd=None,
        AdvertiseSRLB=None,
        AdvertiseSRMSPreference=None,
        AdvertiseSidAsLocator=None,
        Algorithm=None,
        Algorithmsrmpls=None,
        AreaAddresses=None,
        AreaAuthenticationType=None,
        AreaTransmitPasswordOrMD5Key=None,
        Attached=None,
        BIERIPv6NodePrefix=None,
        BierNFlag=None,
        BierRFlag=None,
        CFlagOfSRv6Cap=None,
        CSNPInterval=None,
        ConfigureAlgorithm=None,
        ConfigureSIDIndexLabel=None,
        DBit=None,
        DBitForSRv6Cap=None,
        DBitInsideSRv6SidTLV=None,
        DiscardLSPs=None,
        Distribution=None,
        DomainAuthenticationType=None,
        DomainTransmitPasswordOrMD5Key=None,
        EFlag=None,
        EFlagOfSRv6CapTlv=None,
        Enable=None,
        EnableBit4=None,
        EnableBit5=None,
        EnableBit6=None,
        EnableBit7=None,
        EnableBit8=None,
        EnableHelloPadding=None,
        EnableHitlessRestart=None,
        EnableHostName=None,
        EnableITID=None,
        EnableIpV6TE=None,
        EnableMI=None,
        EnableMTIPv6=None,
        EnableMappingServer=None,
        EnableNFlag=None,
        EnableRFlag=None,
        EnableTE=None,
        EnableWMforTE=None,
        EnableWideMetric=None,
        EnableXFlag=None,
        Funcflags=None,
        Function=None,
        HitlessRestartMode=None,
        HitlessRestartTime=None,
        HitlessRestartVersion=None,
        HostName=None,
        IgnoreReceiveMD5=None,
        Iid=None,
        IncludeMaxSlMsd=None,
        IncludeMaximumEndDMsd=None,
        IncludeMaximumEndDSrhTLV=None,
        IncludeMaximumEndPopMsd=None,
        IncludeMaximumEndPopSrhTLV=None,
        IncludeMaximumHEncapMsd=None,
        IncludeMaximumSLTLV=None,
        IncludeMaximumTEncapMsd=None,
        IncludeMaximumTEncapSrhTLV=None,
        IncludeMaximumTInsertMsd=None,
        IncludeMaximumTInsertSrhTLV=None,
        IncludePrefixAttrFlags=None,
        InterLSPsOrMGroupPDUBurstGap=None,
        IpV6TERouterId=None,
        Ipv4Flag=None,
        Ipv6Flag=None,
        Ipv6NodePrefix=None,
        Ipv6Srh=None,
        Itid=None,
        LFlag=None,
        LSPLifetime=None,
        LSPRefreshRate=None,
        LSPorMGroupPDUMinTransmissionInterval=None,
        LocatorPrefixLength=None,
        Mask=None,
        MaxAreaAddresses=None,
        MaxEndD=None,
        MaxEndDMsd=None,
        MaxEndPopMsd=None,
        MaxEndPopSrh=None,
        MaxHEncapMsd=None,
        MaxLSPSize=None,
        MaxLSPsOrMGroupPDUsPerBurst=None,
        MaxSL=None,
        MaxSlMsd=None,
        MaxTEncap=None,
        MaxTEncapMsd=None,
        MaxTInsert=None,
        MaxTInsertMsd=None,
        MvDontAdvNodePrefix=None,
        NFlag=None,
        NodePrefix=None,
        OFlagOfSRv6Cap=None,
        OFlagOfSRv6CapTlv=None,
        Overloaded=None,
        PFlag=None,
        PSNPInterval=None,
        PartitionRepair=None,
        PrefixAdvertisementType=None,
        PrefixLength=None,
        RFlag=None,
        Redistribution=None,
        RedistributionForSRv6=None,
        ReservedInsideFlagsOfSRv6SidTLV=None,
        ReservedInsideSRv6CapFlag=None,
        RouteMetric=None,
        RouteOrigin=None,
        RtrcapId=None,
        RtrcapIdForSrv6=None,
        SBit=None,
        SBitForSRv6Cap=None,
        SIDIndexLabel=None,
        SRv6NodePrefix=None,
        SRv6NodePrefixLength=None,
        SrlbFlags=None,
        SrmsPreference=None,
        Srv6OAMService=None,
        TERouterId=None,
        TilfaCardNo=None,
        TilfaMac=None,
        TilfaPortIp=None,
        TilfaPortNo=None,
        VFlag=None,
    ):
        """Base class infrastructure that gets a list of isisL3Router device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BIERNodePrefix (str): optional regex of BIERNodePrefix
        - Active (str): optional regex of active
        - AdvertiseNodeMsd (str): optional regex of advertiseNodeMsd
        - AdvertiseSRLB (str): optional regex of advertiseSRLB
        - AdvertiseSRMSPreference (str): optional regex of advertiseSRMSPreference
        - AdvertiseSidAsLocator (str): optional regex of advertiseSidAsLocator
        - Algorithm (str): optional regex of algorithm
        - Algorithmsrmpls (str): optional regex of algorithmsrmpls
        - AreaAddresses (str): optional regex of areaAddresses
        - AreaAuthenticationType (str): optional regex of areaAuthenticationType
        - AreaTransmitPasswordOrMD5Key (str): optional regex of areaTransmitPasswordOrMD5Key
        - Attached (str): optional regex of attached
        - BIERIPv6NodePrefix (str): optional regex of bIERIPv6NodePrefix
        - BierNFlag (str): optional regex of bierNFlag
        - BierRFlag (str): optional regex of bierRFlag
        - CFlagOfSRv6Cap (str): optional regex of cFlagOfSRv6Cap
        - CSNPInterval (str): optional regex of cSNPInterval
        - ConfigureAlgorithm (str): optional regex of configureAlgorithm
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - DBit (str): optional regex of dBit
        - DBitForSRv6Cap (str): optional regex of dBitForSRv6Cap
        - DBitInsideSRv6SidTLV (str): optional regex of dBitInsideSRv6SidTLV
        - DiscardLSPs (str): optional regex of discardLSPs
        - Distribution (str): optional regex of distribution
        - DomainAuthenticationType (str): optional regex of domainAuthenticationType
        - DomainTransmitPasswordOrMD5Key (str): optional regex of domainTransmitPasswordOrMD5Key
        - EFlag (str): optional regex of eFlag
        - EFlagOfSRv6CapTlv (str): optional regex of eFlagOfSRv6CapTlv
        - Enable (str): optional regex of enable
        - EnableBit4 (str): optional regex of enableBit4
        - EnableBit5 (str): optional regex of enableBit5
        - EnableBit6 (str): optional regex of enableBit6
        - EnableBit7 (str): optional regex of enableBit7
        - EnableBit8 (str): optional regex of enableBit8
        - EnableHelloPadding (str): optional regex of enableHelloPadding
        - EnableHitlessRestart (str): optional regex of enableHitlessRestart
        - EnableHostName (str): optional regex of enableHostName
        - EnableITID (str): optional regex of enableITID
        - EnableIpV6TE (str): optional regex of enableIpV6TE
        - EnableMI (str): optional regex of enableMI
        - EnableMTIPv6 (str): optional regex of enableMTIPv6
        - EnableMappingServer (str): optional regex of enableMappingServer
        - EnableNFlag (str): optional regex of enableNFlag
        - EnableRFlag (str): optional regex of enableRFlag
        - EnableTE (str): optional regex of enableTE
        - EnableWMforTE (str): optional regex of enableWMforTE
        - EnableWideMetric (str): optional regex of enableWideMetric
        - EnableXFlag (str): optional regex of enableXFlag
        - Funcflags (str): optional regex of funcflags
        - Function (str): optional regex of function
        - HitlessRestartMode (str): optional regex of hitlessRestartMode
        - HitlessRestartTime (str): optional regex of hitlessRestartTime
        - HitlessRestartVersion (str): optional regex of hitlessRestartVersion
        - HostName (str): optional regex of hostName
        - IgnoreReceiveMD5 (str): optional regex of ignoreReceiveMD5
        - Iid (str): optional regex of iid
        - IncludeMaxSlMsd (str): optional regex of includeMaxSlMsd
        - IncludeMaximumEndDMsd (str): optional regex of includeMaximumEndDMsd
        - IncludeMaximumEndDSrhTLV (str): optional regex of includeMaximumEndDSrhTLV
        - IncludeMaximumEndPopMsd (str): optional regex of includeMaximumEndPopMsd
        - IncludeMaximumEndPopSrhTLV (str): optional regex of includeMaximumEndPopSrhTLV
        - IncludeMaximumHEncapMsd (str): optional regex of includeMaximumHEncapMsd
        - IncludeMaximumSLTLV (str): optional regex of includeMaximumSLTLV
        - IncludeMaximumTEncapMsd (str): optional regex of includeMaximumTEncapMsd
        - IncludeMaximumTEncapSrhTLV (str): optional regex of includeMaximumTEncapSrhTLV
        - IncludeMaximumTInsertMsd (str): optional regex of includeMaximumTInsertMsd
        - IncludeMaximumTInsertSrhTLV (str): optional regex of includeMaximumTInsertSrhTLV
        - IncludePrefixAttrFlags (str): optional regex of includePrefixAttrFlags
        - InterLSPsOrMGroupPDUBurstGap (str): optional regex of interLSPsOrMGroupPDUBurstGap
        - IpV6TERouterId (str): optional regex of ipV6TERouterId
        - Ipv4Flag (str): optional regex of ipv4Flag
        - Ipv6Flag (str): optional regex of ipv6Flag
        - Ipv6NodePrefix (str): optional regex of ipv6NodePrefix
        - Ipv6Srh (str): optional regex of ipv6Srh
        - Itid (str): optional regex of itid
        - LFlag (str): optional regex of lFlag
        - LSPLifetime (str): optional regex of lSPLifetime
        - LSPRefreshRate (str): optional regex of lSPRefreshRate
        - LSPorMGroupPDUMinTransmissionInterval (str): optional regex of lSPorMGroupPDUMinTransmissionInterval
        - LocatorPrefixLength (str): optional regex of locatorPrefixLength
        - Mask (str): optional regex of mask
        - MaxAreaAddresses (str): optional regex of maxAreaAddresses
        - MaxEndD (str): optional regex of maxEndD
        - MaxEndDMsd (str): optional regex of maxEndDMsd
        - MaxEndPopMsd (str): optional regex of maxEndPopMsd
        - MaxEndPopSrh (str): optional regex of maxEndPopSrh
        - MaxHEncapMsd (str): optional regex of maxHEncapMsd
        - MaxLSPSize (str): optional regex of maxLSPSize
        - MaxLSPsOrMGroupPDUsPerBurst (str): optional regex of maxLSPsOrMGroupPDUsPerBurst
        - MaxSL (str): optional regex of maxSL
        - MaxSlMsd (str): optional regex of maxSlMsd
        - MaxTEncap (str): optional regex of maxTEncap
        - MaxTEncapMsd (str): optional regex of maxTEncapMsd
        - MaxTInsert (str): optional regex of maxTInsert
        - MaxTInsertMsd (str): optional regex of maxTInsertMsd
        - MvDontAdvNodePrefix (str): optional regex of mvDontAdvNodePrefix
        - NFlag (str): optional regex of nFlag
        - NodePrefix (str): optional regex of nodePrefix
        - OFlagOfSRv6Cap (str): optional regex of oFlagOfSRv6Cap
        - OFlagOfSRv6CapTlv (str): optional regex of oFlagOfSRv6CapTlv
        - Overloaded (str): optional regex of overloaded
        - PFlag (str): optional regex of pFlag
        - PSNPInterval (str): optional regex of pSNPInterval
        - PartitionRepair (str): optional regex of partitionRepair
        - PrefixAdvertisementType (str): optional regex of prefixAdvertisementType
        - PrefixLength (str): optional regex of prefixLength
        - RFlag (str): optional regex of rFlag
        - Redistribution (str): optional regex of redistribution
        - RedistributionForSRv6 (str): optional regex of redistributionForSRv6
        - ReservedInsideFlagsOfSRv6SidTLV (str): optional regex of reservedInsideFlagsOfSRv6SidTLV
        - ReservedInsideSRv6CapFlag (str): optional regex of reservedInsideSRv6CapFlag
        - RouteMetric (str): optional regex of routeMetric
        - RouteOrigin (str): optional regex of routeOrigin
        - RtrcapId (str): optional regex of rtrcapId
        - RtrcapIdForSrv6 (str): optional regex of rtrcapIdForSrv6
        - SBit (str): optional regex of sBit
        - SBitForSRv6Cap (str): optional regex of sBitForSRv6Cap
        - SIDIndexLabel (str): optional regex of sIDIndexLabel
        - SRv6NodePrefix (str): optional regex of sRv6NodePrefix
        - SRv6NodePrefixLength (str): optional regex of sRv6NodePrefixLength
        - SrlbFlags (str): optional regex of srlbFlags
        - SrmsPreference (str): optional regex of srmsPreference
        - Srv6OAMService (str): optional regex of srv6OAMService
        - TERouterId (str): optional regex of tERouterId
        - TilfaCardNo (str): optional regex of tilfaCardNo
        - TilfaMac (str): optional regex of tilfaMac
        - TilfaPortIp (str): optional regex of tilfaPortIp
        - TilfaPortNo (str): optional regex of tilfaPortNo
        - VFlag (str): optional regex of vFlag

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
