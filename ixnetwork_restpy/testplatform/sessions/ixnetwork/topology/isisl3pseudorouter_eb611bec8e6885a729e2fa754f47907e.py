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


class IsisL3PseudoRouter(Base):
    """ISIS-L3 Pseudo Node Configuration
    The IsisL3PseudoRouter class encapsulates a list of isisL3PseudoRouter resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisL3PseudoRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'isisL3PseudoRouter'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertiseNodeMsd': 'advertiseNodeMsd',
        'AdvertiseSRLB': 'advertiseSRLB',
        'AdvertiseSidAsLocator': 'advertiseSidAsLocator',
        'Algorithm': 'algorithm',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DBit': 'dBit',
        'DBitForSRv6Cap': 'dBitForSRv6Cap',
        'DBitInsideSRv6SidTLV': 'dBitInsideSRv6SidTLV',
        'DescriptiveName': 'descriptiveName',
        'EFlag': 'eFlag',
        'EFlagOfSRv6CapTlv': 'eFlagOfSRv6CapTlv',
        'Enable': 'enable',
        'EnableIpV6TE': 'enableIpV6TE',
        'EnableMTIPv6': 'enableMTIPv6',
        'EnableSR': 'enableSR',
        'EnableWMforTEinNetworkGroup': 'enableWMforTEinNetworkGroup',
        'EnableWideMetric': 'enableWideMetric',
        'FlexAlgoCount': 'flexAlgoCount',
        'Funcflags': 'funcflags',
        'Function': 'function',
        'IncludeMaxSlMsd': 'includeMaxSlMsd',
        'IncludeMaximumEndDMsd': 'includeMaximumEndDMsd',
        'IncludeMaximumEndDSrhTLV': 'includeMaximumEndDSrhTLV',
        'IncludeMaximumEndPopMsd': 'includeMaximumEndPopMsd',
        'IncludeMaximumEndPopSrhTLV': 'includeMaximumEndPopSrhTLV',
        'IncludeMaximumSLTLV': 'includeMaximumSLTLV',
        'IncludeMaximumTEncapMsd': 'includeMaximumTEncapMsd',
        'IncludeMaximumTEncapSrhTLV': 'includeMaximumTEncapSrhTLV',
        'IncludeMaximumTInsertMsd': 'includeMaximumTInsertMsd',
        'IncludeMaximumTInsertSrhTLV': 'includeMaximumTInsertSrhTLV',
        'IpV6TERouterId': 'ipV6TERouterId',
        'Ipv4Flag': 'ipv4Flag',
        'Ipv6Flag': 'ipv6Flag',
        'Ipv6MTMetric': 'ipv6MTMetric',
        'Ipv6NodePrefix': 'ipv6NodePrefix',
        'Ipv6Srh': 'ipv6Srh',
        'LFlag': 'lFlag',
        'LocatorCount': 'locatorCount',
        'LocatorPrefixLength': 'locatorPrefixLength',
        'Mask': 'mask',
        'MaxEndD': 'maxEndD',
        'MaxEndDMsd': 'maxEndDMsd',
        'MaxEndPopMsd': 'maxEndPopMsd',
        'MaxEndPopSrh': 'maxEndPopSrh',
        'MaxSL': 'maxSL',
        'MaxSlMsd': 'maxSlMsd',
        'MaxTEncap': 'maxTEncap',
        'MaxTEncapMsd': 'maxTEncapMsd',
        'MaxTInsert': 'maxTInsert',
        'MaxTInsertMsd': 'maxTInsertMsd',
        'MtCount': 'mtCount',
        'NFlag': 'nFlag',
        'Name': 'name',
        'NodePrefix': 'nodePrefix',
        'OFlagOfSRv6Cap': 'oFlagOfSRv6Cap',
        'PFlag': 'pFlag',
        'PrefixLength': 'prefixLength',
        'RFlag': 'rFlag',
        'Redistribution': 'redistribution',
        'RedistributionForSRv6': 'redistributionForSRv6',
        'ReservedInsideFlagsOfSRv6SidTLV': 'reservedInsideFlagsOfSRv6SidTLV',
        'ReservedInsideSRv6CapFlag': 'reservedInsideSRv6CapFlag',
        'RouteMetric': 'routeMetric',
        'RouteOrigin': 'routeOrigin',
        'RtrcapId': 'rtrcapId',
        'RtrcapIdForSrv6': 'rtrcapIdForSrv6',
        'SBit': 'sBit',
        'SBitForSRv6Cap': 'sBitForSRv6Cap',
        'SIDIndexLabel': 'sIDIndexLabel',
        'SRAlgorithmCount': 'sRAlgorithmCount',
        'SRGBRangeCount': 'sRGBRangeCount',
        'SRv6NodePrefix': 'sRv6NodePrefix',
        'SRv6NodePrefixLength': 'sRv6NodePrefixLength',
        'SrlbDescriptorCount': 'srlbDescriptorCount',
        'SrlbFlags': 'srlbFlags',
        'TERouterId': 'tERouterId',
        'VFlag': 'vFlag',
    }

    def __init__(self, parent):
        super(IsisL3PseudoRouter, self).__init__(parent)

    @property
    def IPv4PseudoNodeRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4pseudonoderoutes_7cd9e3747243dcf6c295ddd7cc532731.IPv4PseudoNodeRoutes): An instance of the IPv4PseudoNodeRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4pseudonoderoutes_7cd9e3747243dcf6c295ddd7cc532731 import IPv4PseudoNodeRoutes
        return IPv4PseudoNodeRoutes(self)

    @property
    def IPv6PseudoNodeRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6pseudonoderoutes_e49889067cd5030685c5c28101e243d5.IPv6PseudoNodeRoutes): An instance of the IPv6PseudoNodeRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6pseudonoderoutes_e49889067cd5030685c5c28101e243d5 import IPv6PseudoNodeRoutes
        return IPv6PseudoNodeRoutes(self)

    @property
    def IsisPseudoMultiTopologyValuesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomultitopologyvalueslist_611d6ab2b1a502e3b27f153266aa7670.IsisPseudoMultiTopologyValuesList): An instance of the IsisPseudoMultiTopologyValuesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomultitopologyvalueslist_611d6ab2b1a502e3b27f153266aa7670 import IsisPseudoMultiTopologyValuesList
        return IsisPseudoMultiTopologyValuesList(self)

    @property
    def IsisPseudoFlexAlgorithm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudoflexalgorithm_da21ce814ae20d74de8689303f8c2e83.IsisPseudoFlexAlgorithm): An instance of the IsisPseudoFlexAlgorithm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudoflexalgorithm_da21ce814ae20d74de8689303f8c2e83 import IsisPseudoFlexAlgorithm
        return IsisPseudoFlexAlgorithm(self)._select()

    @property
    def IsisPseudoSRv6LocatorEntryList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6locatorentrylist_41e56680c4c88d313d713433ca07cac5.IsisPseudoSRv6LocatorEntryList): An instance of the IsisPseudoSRv6LocatorEntryList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6locatorentrylist_41e56680c4c88d313d713433ca07cac5 import IsisPseudoSRv6LocatorEntryList
        return IsisPseudoSRv6LocatorEntryList(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissralgorithmlist_a50f1cd4168a3642597a66e7f63343e6 import IsisSRAlgorithmList
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrgbrangesubobjectslist_6180dd47f637b6f4581c2dcaa7a1a071 import IsisSRGBRangeSubObjectsList
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrlbdescriptorlist_1eec075b53920dfd5040006478718f6a import IsisSRLBDescriptorList
        return IsisSRLBDescriptorList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvertiseNodeMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Node MSD
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseNodeMsd']))

    @property
    def AdvertiseSRLB(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables advertisement of Segment Routing Local Block (SRLB) Sub-Tlv in Router Capability Tlv
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseSRLB']))

    @property
    def AdvertiseSidAsLocator(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, then the configured IPv6 Node SID gets advertised as a reachable IPv6 prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseSidAsLocator']))

    @property
    def Algorithm(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def ConfigureSIDIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSIDIndexLabel']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DBit']))

    @property
    def DBitForSRv6Cap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DBitForSRv6Cap']))

    @property
    def DBitInsideSRv6SidTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DBitInsideSRv6SidTLV']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit NULL flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def EFlagOfSRv6CapTlv(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then router is able to apply T.Encap operation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlagOfSRv6CapTlv']))

    @property
    def Enable(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IPv4 TE
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enable']))

    @property
    def EnableIpV6TE(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If it is enabled, the ISIS Traffic Engineering Profiles will be available. If not enabled, then no TE fields will be sent out in TLV 222.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIpV6TE']))

    @property
    def EnableMTIPv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MT for IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMTIPv6']))

    @property
    def EnableSR(self):
        """
        Returns
        -------
        - bool: This enables SR MPLS on all the simulated ISIS router(s)
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSR'])
    @EnableSR.setter
    def EnableSR(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSR'], value)

    @property
    def EnableWMforTEinNetworkGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hidden field is to disable wide Metric, when user disable TE Router in Network Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableWMforTEinNetworkGroup']))

    @property
    def EnableWideMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Wide Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableWideMetric']))

    @property
    def FlexAlgoCount(self):
        """
        Returns
        -------
        - number: If the count is greater than 0, then the Flex Algo tab will appear. Default is 0. Range is 0-128.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlexAlgoCount'])
    @FlexAlgoCount.setter
    def FlexAlgoCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlexAlgoCount'], value)

    @property
    def Funcflags(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the function flags
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Funcflags']))

    @property
    def Function(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies endpoint function codes
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Function']))

    @property
    def IncludeMaxSlMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then Include Maximum Segment Left MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaxSlMsd']))

    @property
    def IncludeMaximumEndDMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum End D MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumEndDMsd']))

    @property
    def IncludeMaximumEndDSrhTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum End D SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumEndDSrhTLV']))

    @property
    def IncludeMaximumEndPopMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Max-End-Pop-MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumEndPopMsd']))

    @property
    def IncludeMaximumEndPopSrhTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Max-End-Pop-SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumEndPopSrhTLV']))

    @property
    def IncludeMaximumSLTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum SL TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumSLTLV']))

    @property
    def IncludeMaximumTEncapMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Encap MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumTEncapMsd']))

    @property
    def IncludeMaximumTEncapSrhTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Encap SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumTEncapSrhTLV']))

    @property
    def IncludeMaximumTInsertMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Insert MSD in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumTInsertMsd']))

    @property
    def IncludeMaximumTInsertSrhTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Insert SRH TLV in SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumTInsertSrhTLV']))

    @property
    def IpV6TERouterId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It is a unique ID including emulated and simulated routers. It should match IPv6 Node Prefix in SRv6 by default. It will send out the TLV 140 in ISIS.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpV6TERouterId']))

    @property
    def Ipv4Flag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MPLS IPv4 Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4Flag']))

    @property
    def Ipv6Flag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MPLS IPv6 Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Flag']))

    @property
    def Ipv6MTMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 MT Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6MTMetric']))

    @property
    def Ipv6NodePrefix(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Node Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6NodePrefix']))

    @property
    def Ipv6Srh(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router will advertise and process IPv6 SR related TLVs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Srh']))

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def LocatorCount(self):
        """
        Returns
        -------
        - number: Locator Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocatorCount'])
    @LocatorCount.setter
    def LocatorCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LocatorCount'], value)

    @property
    def LocatorPrefixLength(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Locator Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LocatorPrefixLength']))

    @property
    def Mask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mask
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mask']))

    @property
    def MaxEndD(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions if the extension header right underneath the outer IPv6 header is an SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxEndD']))

    @property
    def MaxEndDMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions. If the extension header is right underneath the outer IPv6, header is an SRH.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxEndDMsd']))

    @property
    def MaxEndPopMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in the top MSD in an MSD stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxEndPopMsd']))

    @property
    def MaxEndPopSrh(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs in the top SRH in an SRH stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxEndPopSrh']))

    @property
    def MaxSL(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum value of the Segments Left (SL) field in the SRH of a received packet before applying the function associated with a SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxSL']))

    @property
    def MaxSlMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum value of the Segments Left (SL) MSD field in the SRH of a received packet before applying the function associated with a SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxSlMsd']))

    @property
    def MaxTEncap(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTEncap']))

    @property
    def MaxTEncapMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTEncapMsd']))

    @property
    def MaxTInsert(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTInsert']))

    @property
    def MaxTInsertMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTInsertMsd']))

    @property
    def MtCount(self):
        """
        Returns
        -------
        - number: MT Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['MtCount'])
    @MtCount.setter
    def MtCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MtCount'], value)

    @property
    def NFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Nodal prefix flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NFlag']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NodePrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node Prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NodePrefix']))

    @property
    def OFlagOfSRv6Cap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, it indicates that this packet is an operations and management (OAM) packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OFlagOfSRv6Cap']))

    @property
    def PFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def PrefixLength(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixLength']))

    @property
    def RFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RFlag']))

    @property
    def Redistribution(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Redistribution']))

    @property
    def RedistributionForSRv6(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Redistribution
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RedistributionForSRv6']))

    @property
    def ReservedInsideFlagsOfSRv6SidTLV(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the reserved field (part of flags field of SRv6 SID TLV)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedInsideFlagsOfSRv6SidTLV']))

    @property
    def ReservedInsideSRv6CapFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the reserved field (as part of Flags field of SRv6 Capability TLV)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedInsideSRv6CapFlag']))

    @property
    def RouteMetric(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteMetric']))

    @property
    def RouteOrigin(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouteOrigin']))

    @property
    def RtrcapId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router Capability Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RtrcapId']))

    @property
    def RtrcapIdForSrv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router Capability Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RtrcapIdForSrv6']))

    @property
    def SBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SBit']))

    @property
    def SBitForSRv6Cap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SBitForSRv6Cap']))

    @property
    def SIDIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SIDIndexLabel']))

    @property
    def SRAlgorithmCount(self):
        """
        Returns
        -------
        - number: SR Algorithm Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SRAlgorithmCount'])
    @SRAlgorithmCount.setter
    def SRAlgorithmCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SRAlgorithmCount'], value)

    @property
    def SRGBRangeCount(self):
        """
        Returns
        -------
        - number: SRGB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SRGBRangeCount'])
    @SRGBRangeCount.setter
    def SRGBRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SRGBRangeCount'], value)

    @property
    def SRv6NodePrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is an IPv6 Node prefix for the SRv6 router
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SRv6NodePrefix']))

    @property
    def SRv6NodePrefixLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is the prefix length of the SRv6 node prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SRv6NodePrefixLength']))

    @property
    def SrlbDescriptorCount(self):
        """
        Returns
        -------
        - number: Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrlbDescriptorCount'])
    @SrlbDescriptorCount.setter
    def SrlbDescriptorCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrlbDescriptorCount'], value)

    @property
    def SrlbFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies the value of the SRLB flags field
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrlbFlags']))

    @property
    def TERouterId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TE Router ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TERouterId']))

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, EnableSR=None, FlexAlgoCount=None, LocatorCount=None, MtCount=None, Name=None, SRAlgorithmCount=None, SRGBRangeCount=None, SrlbDescriptorCount=None):
        """Updates isisL3PseudoRouter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableSR (bool): This enables SR MPLS on all the simulated ISIS router(s)
        - FlexAlgoCount (number): If the count is greater than 0, then the Flex Algo tab will appear. Default is 0. Range is 0-128.
        - LocatorCount (number): Locator Count
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SRAlgorithmCount (number): SR Algorithm Count
        - SRGBRangeCount (number): SRGB Range Count
        - SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, EnableSR=None, FlexAlgoCount=None, LocatorCount=None, MtCount=None, Name=None, SRAlgorithmCount=None, SRGBRangeCount=None, SrlbDescriptorCount=None):
        """Finds and retrieves isisL3PseudoRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisL3PseudoRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisL3PseudoRouter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - EnableSR (bool): This enables SR MPLS on all the simulated ISIS router(s)
        - FlexAlgoCount (number): If the count is greater than 0, then the Flex Algo tab will appear. Default is 0. Range is 0-128.
        - LocatorCount (number): Locator Count
        - MtCount (number): MT Count
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SRAlgorithmCount (number): SR Algorithm Count
        - SRGBRangeCount (number): SRGB Range Count
        - SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}

        Returns
        -------
        - self: This instance with matching isisL3PseudoRouter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisL3PseudoRouter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisL3PseudoRouter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseNodeMsd=None, AdvertiseSRLB=None, AdvertiseSidAsLocator=None, Algorithm=None, ConfigureSIDIndexLabel=None, DBit=None, DBitForSRv6Cap=None, DBitInsideSRv6SidTLV=None, EFlag=None, EFlagOfSRv6CapTlv=None, Enable=None, EnableIpV6TE=None, EnableMTIPv6=None, EnableWMforTEinNetworkGroup=None, EnableWideMetric=None, Funcflags=None, Function=None, IncludeMaxSlMsd=None, IncludeMaximumEndDMsd=None, IncludeMaximumEndDSrhTLV=None, IncludeMaximumEndPopMsd=None, IncludeMaximumEndPopSrhTLV=None, IncludeMaximumSLTLV=None, IncludeMaximumTEncapMsd=None, IncludeMaximumTEncapSrhTLV=None, IncludeMaximumTInsertMsd=None, IncludeMaximumTInsertSrhTLV=None, IpV6TERouterId=None, Ipv4Flag=None, Ipv6Flag=None, Ipv6MTMetric=None, Ipv6NodePrefix=None, Ipv6Srh=None, LFlag=None, LocatorPrefixLength=None, Mask=None, MaxEndD=None, MaxEndDMsd=None, MaxEndPopMsd=None, MaxEndPopSrh=None, MaxSL=None, MaxSlMsd=None, MaxTEncap=None, MaxTEncapMsd=None, MaxTInsert=None, MaxTInsertMsd=None, NFlag=None, NodePrefix=None, OFlagOfSRv6Cap=None, PFlag=None, PrefixLength=None, RFlag=None, Redistribution=None, RedistributionForSRv6=None, ReservedInsideFlagsOfSRv6SidTLV=None, ReservedInsideSRv6CapFlag=None, RouteMetric=None, RouteOrigin=None, RtrcapId=None, RtrcapIdForSrv6=None, SBit=None, SBitForSRv6Cap=None, SIDIndexLabel=None, SRv6NodePrefix=None, SRv6NodePrefixLength=None, SrlbFlags=None, TERouterId=None, VFlag=None):
        """Base class infrastructure that gets a list of isisL3PseudoRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertiseNodeMsd (str): optional regex of advertiseNodeMsd
        - AdvertiseSRLB (str): optional regex of advertiseSRLB
        - AdvertiseSidAsLocator (str): optional regex of advertiseSidAsLocator
        - Algorithm (str): optional regex of algorithm
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - DBit (str): optional regex of dBit
        - DBitForSRv6Cap (str): optional regex of dBitForSRv6Cap
        - DBitInsideSRv6SidTLV (str): optional regex of dBitInsideSRv6SidTLV
        - EFlag (str): optional regex of eFlag
        - EFlagOfSRv6CapTlv (str): optional regex of eFlagOfSRv6CapTlv
        - Enable (str): optional regex of enable
        - EnableIpV6TE (str): optional regex of enableIpV6TE
        - EnableMTIPv6 (str): optional regex of enableMTIPv6
        - EnableWMforTEinNetworkGroup (str): optional regex of enableWMforTEinNetworkGroup
        - EnableWideMetric (str): optional regex of enableWideMetric
        - Funcflags (str): optional regex of funcflags
        - Function (str): optional regex of function
        - IncludeMaxSlMsd (str): optional regex of includeMaxSlMsd
        - IncludeMaximumEndDMsd (str): optional regex of includeMaximumEndDMsd
        - IncludeMaximumEndDSrhTLV (str): optional regex of includeMaximumEndDSrhTLV
        - IncludeMaximumEndPopMsd (str): optional regex of includeMaximumEndPopMsd
        - IncludeMaximumEndPopSrhTLV (str): optional regex of includeMaximumEndPopSrhTLV
        - IncludeMaximumSLTLV (str): optional regex of includeMaximumSLTLV
        - IncludeMaximumTEncapMsd (str): optional regex of includeMaximumTEncapMsd
        - IncludeMaximumTEncapSrhTLV (str): optional regex of includeMaximumTEncapSrhTLV
        - IncludeMaximumTInsertMsd (str): optional regex of includeMaximumTInsertMsd
        - IncludeMaximumTInsertSrhTLV (str): optional regex of includeMaximumTInsertSrhTLV
        - IpV6TERouterId (str): optional regex of ipV6TERouterId
        - Ipv4Flag (str): optional regex of ipv4Flag
        - Ipv6Flag (str): optional regex of ipv6Flag
        - Ipv6MTMetric (str): optional regex of ipv6MTMetric
        - Ipv6NodePrefix (str): optional regex of ipv6NodePrefix
        - Ipv6Srh (str): optional regex of ipv6Srh
        - LFlag (str): optional regex of lFlag
        - LocatorPrefixLength (str): optional regex of locatorPrefixLength
        - Mask (str): optional regex of mask
        - MaxEndD (str): optional regex of maxEndD
        - MaxEndDMsd (str): optional regex of maxEndDMsd
        - MaxEndPopMsd (str): optional regex of maxEndPopMsd
        - MaxEndPopSrh (str): optional regex of maxEndPopSrh
        - MaxSL (str): optional regex of maxSL
        - MaxSlMsd (str): optional regex of maxSlMsd
        - MaxTEncap (str): optional regex of maxTEncap
        - MaxTEncapMsd (str): optional regex of maxTEncapMsd
        - MaxTInsert (str): optional regex of maxTInsert
        - MaxTInsertMsd (str): optional regex of maxTInsertMsd
        - NFlag (str): optional regex of nFlag
        - NodePrefix (str): optional regex of nodePrefix
        - OFlagOfSRv6Cap (str): optional regex of oFlagOfSRv6Cap
        - PFlag (str): optional regex of pFlag
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
        - TERouterId (str): optional regex of tERouterId
        - VFlag (str): optional regex of vFlag

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
