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


class IsisL3PseudoRouter(Base):
    """ISIS-L3 Pseudo Node Configuration
    The IsisL3PseudoRouter class encapsulates a list of isisL3PseudoRouter resources that is managed by the system.
    A list of resources can be retrieved from the server using the IsisL3PseudoRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'isisL3PseudoRouter'

    def __init__(self, parent):
        super(IsisL3PseudoRouter, self).__init__(parent)

    @property
    def IPv4PseudoNodeRoutes(self):
        """An instance of the IPv4PseudoNodeRoutes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4pseudonoderoutes.IPv4PseudoNodeRoutes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4pseudonoderoutes import IPv4PseudoNodeRoutes
        return IPv4PseudoNodeRoutes(self)

    @property
    def IPv6PseudoNodeRoutes(self):
        """An instance of the IPv6PseudoNodeRoutes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6pseudonoderoutes.IPv6PseudoNodeRoutes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6pseudonoderoutes import IPv6PseudoNodeRoutes
        return IPv6PseudoNodeRoutes(self)

    @property
    def IsisPseudoMultiTopologyValuesList(self):
        """An instance of the IsisPseudoMultiTopologyValuesList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomultitopologyvalueslist.IsisPseudoMultiTopologyValuesList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudomultitopologyvalueslist import IsisPseudoMultiTopologyValuesList
        return IsisPseudoMultiTopologyValuesList(self)

    @property
    def IsisPseudoSRv6LocatorEntryList(self):
        """An instance of the IsisPseudoSRv6LocatorEntryList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6locatorentrylist.IsisPseudoSRv6LocatorEntryList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6locatorentrylist import IsisPseudoSRv6LocatorEntryList
        return IsisPseudoSRv6LocatorEntryList(self)._select()

    @property
    def IsisSRAlgorithmList(self):
        """An instance of the IsisSRAlgorithmList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissralgorithmlist.IsisSRAlgorithmList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissralgorithmlist import IsisSRAlgorithmList
        return IsisSRAlgorithmList(self)

    @property
    def IsisSRGBRangeSubObjectsList(self):
        """An instance of the IsisSRGBRangeSubObjectsList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrgbrangesubobjectslist.IsisSRGBRangeSubObjectsList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrgbrangesubobjectslist import IsisSRGBRangeSubObjectsList
        return IsisSRGBRangeSubObjectsList(self)

    @property
    def IsisSRLBDescriptorList(self):
        """An instance of the IsisSRLBDescriptorList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrlbdescriptorlist.IsisSRLBDescriptorList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrlbdescriptorlist import IsisSRLBDescriptorList
        return IsisSRLBDescriptorList(self)

    @property
    def Active(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def AdvertiseNodeMsd(self):
        """Advertise Node MSD

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('advertiseNodeMsd')

    @property
    def AdvertiseSRLB(self):
        """Enables advertisement of Segment Routing Local Block (SRLB) Sub-Tlv in Router Capability Tlv

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('advertiseSRLB')

    @property
    def AdvertiseSidAsLocator(self):
        """DEPRECATED If enabled, then the configured IPv6 Node SID gets advertised as a reachable IPv6 prefix

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('advertiseSidAsLocator')

    @property
    def Algorithm(self):
        """DEPRECATED Algorithm

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('algorithm')

    @property
    def ConfigureSIDIndexLabel(self):
        """Configure SID/Index/Label

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('configureSIDIndexLabel')

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DBit(self):
        """When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dBit')

    @property
    def DBitForSRv6Cap(self):
        """When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dBitForSRv6Cap')

    @property
    def DBitInsideSRv6SidTLV(self):
        """DEPRECATED When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dBitInsideSRv6SidTLV')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def EFlag(self):
        """Explicit NULL flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eFlag')

    @property
    def EFlagOfSRv6CapTlv(self):
        """DEPRECATED If set, then router is able to apply T.Encap operation

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eFlagOfSRv6CapTlv')

    @property
    def Enable(self):
        """TE Enabled

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enable')

    @property
    def EnableMTIPv6(self):
        """Enable MT for IPv6

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableMTIPv6')

    @property
    def EnableSR(self):
        """This enables SR MPLS on all the simulated ISIS router(s)

        Returns:
            bool
        """
        return self._get_attribute('enableSR')
    @EnableSR.setter
    def EnableSR(self, value):
        self._set_attribute('enableSR', value)

    @property
    def EnableWMforTEinNetworkGroup(self):
        """Hidden field is to disable wide Metric, when user disable TE Router in Network Group

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableWMforTEinNetworkGroup')

    @property
    def EnableWideMetric(self):
        """Enable Wide Metric

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableWideMetric')

    @property
    def Funcflags(self):
        """DEPRECATED This is the function flags

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('funcflags')

    @property
    def Function(self):
        """DEPRECATED This specifies endpoint function codes

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('function')

    @property
    def IncludeMaxSlMsd(self):
        """If set, then Include Maximum Segment Left MSD in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaxSlMsd')

    @property
    def IncludeMaximumEndDMsd(self):
        """If set, then include Maximum End D MSD in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumEndDMsd')

    @property
    def IncludeMaximumEndDSrhTLV(self):
        """DEPRECATED If set, then include Maximum End D SRH TLV in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumEndDSrhTLV')

    @property
    def IncludeMaximumEndPopMsd(self):
        """If set, then include Max-End-Pop-MSD in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumEndPopMsd')

    @property
    def IncludeMaximumEndPopSrhTLV(self):
        """DEPRECATED If set, then include Max-End-Pop-SRH TLV in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumEndPopSrhTLV')

    @property
    def IncludeMaximumSLTLV(self):
        """DEPRECATED If set, then include Maximum SL TLV in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumSLTLV')

    @property
    def IncludeMaximumTEncapMsd(self):
        """If set, then include Maximum T.Encap MSD in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumTEncapMsd')

    @property
    def IncludeMaximumTEncapSrhTLV(self):
        """DEPRECATED If set, then include Maximum T.Encap SRH TLV in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumTEncapSrhTLV')

    @property
    def IncludeMaximumTInsertMsd(self):
        """If set, then include Maximum T.Insert MSD in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumTInsertMsd')

    @property
    def IncludeMaximumTInsertSrhTLV(self):
        """DEPRECATED If set, then include Maximum T.Insert SRH TLV in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumTInsertSrhTLV')

    @property
    def Ipv4Flag(self):
        """MPLS IPv4 Flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv4Flag')

    @property
    def Ipv6Flag(self):
        """MPLS IPv6 Flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6Flag')

    @property
    def Ipv6MTMetric(self):
        """IPv6 MT Metric

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6MTMetric')

    @property
    def Ipv6NodePrefix(self):
        """DEPRECATED IPv6 Node Prefix

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6NodePrefix')

    @property
    def Ipv6Srh(self):
        """Router will advertise and process IPv6 SR related TLVs

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6Srh')

    @property
    def LFlag(self):
        """Local Flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lFlag')

    @property
    def LocatorCount(self):
        """Locator Count

        Returns:
            number
        """
        return self._get_attribute('locatorCount')
    @LocatorCount.setter
    def LocatorCount(self, value):
        self._set_attribute('locatorCount', value)

    @property
    def LocatorPrefixLength(self):
        """DEPRECATED Locator Prefix Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('locatorPrefixLength')

    @property
    def Mask(self):
        """Mask

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mask')

    @property
    def MaxEndD(self):
        """DEPRECATED This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions if the extension header right underneath the outer IPv6 header is an SRH.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxEndD')

    @property
    def MaxEndDMsd(self):
        """This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions. If the extension header is right underneath the outer IPv6, header is an SRH.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxEndDMsd')

    @property
    def MaxEndPopMsd(self):
        """This field specifies the maximum number of SIDs in the top MSD in an MSD stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxEndPopMsd')

    @property
    def MaxEndPopSrh(self):
        """DEPRECATED This field specifies the maximum number of SIDs in the top SRH in an SRH stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxEndPopSrh')

    @property
    def MaxSL(self):
        """DEPRECATED This field specifies the maximum value of the Segments Left (SL) field in the SRH of a received packet before applying the function associated with a SID.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxSL')

    @property
    def MaxSlMsd(self):
        """This field specifies the maximum value of the Segments Left (SL) MSD field in the SRH of a received packet before applying the function associated with a SID.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxSlMsd')

    @property
    def MaxTEncap(self):
        """This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxTEncap')

    @property
    def MaxTInsert(self):
        """DEPRECATED This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxTInsert')

    @property
    def MaxTInsertMsd(self):
        """This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxTInsertMsd')

    @property
    def MtCount(self):
        """MT Count

        Returns:
            number
        """
        return self._get_attribute('mtCount')
    @MtCount.setter
    def MtCount(self, value):
        self._set_attribute('mtCount', value)

    @property
    def NFlag(self):
        """Nodal prefix flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('nFlag')

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NodePrefix(self):
        """Node Prefix

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('nodePrefix')

    @property
    def OFlagOfSRv6Cap(self):
        """If set, it indicates that this packet is an operations and management (OAM) packet.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('oFlagOfSRv6Cap')

    @property
    def PFlag(self):
        """No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('pFlag')

    @property
    def PrefixLength(self):
        """DEPRECATED Prefix Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('prefixLength')

    @property
    def RFlag(self):
        """Redistribution flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rFlag')

    @property
    def Redistribution(self):
        """Redistribution

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('redistribution')

    @property
    def RedistributionForSRv6(self):
        """DEPRECATED Redistribution

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('redistributionForSRv6')

    @property
    def ReservedInsideFlagsOfSRv6SidTLV(self):
        """DEPRECATED This is the reserved field (part of flags field of SRv6 SID TLV)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('reservedInsideFlagsOfSRv6SidTLV')

    @property
    def ReservedInsideSRv6CapFlag(self):
        """This is the reserved field (as part of Flags field of SRv6 Capability TLV)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('reservedInsideSRv6CapFlag')

    @property
    def RouteMetric(self):
        """DEPRECATED Route Metric

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('routeMetric')

    @property
    def RouteOrigin(self):
        """DEPRECATED Route Origin

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('routeOrigin')

    @property
    def RtrcapId(self):
        """Router Capability Id

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rtrcapId')

    @property
    def RtrcapIdForSrv6(self):
        """Router Capability Id

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rtrcapIdForSrv6')

    @property
    def SBit(self):
        """Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sBit')

    @property
    def SBitForSRv6Cap(self):
        """Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sBitForSRv6Cap')

    @property
    def SIDIndexLabel(self):
        """SID/Index/Label

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sIDIndexLabel')

    @property
    def SRAlgorithmCount(self):
        """SR Algorithm Count

        Returns:
            number
        """
        return self._get_attribute('sRAlgorithmCount')
    @SRAlgorithmCount.setter
    def SRAlgorithmCount(self, value):
        self._set_attribute('sRAlgorithmCount', value)

    @property
    def SRGBRangeCount(self):
        """SRGB Range Count

        Returns:
            number
        """
        return self._get_attribute('sRGBRangeCount')
    @SRGBRangeCount.setter
    def SRGBRangeCount(self, value):
        self._set_attribute('sRGBRangeCount', value)

    @property
    def SRv6NodePrefix(self):
        """This is an IPv6 Node prefix for the SRv6 router

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sRv6NodePrefix')

    @property
    def SRv6NodePrefixLength(self):
        """This is the prefix length of the SRv6 node prefix

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sRv6NodePrefixLength')

    @property
    def SrlbDescriptorCount(self):
        """Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}

        Returns:
            number
        """
        return self._get_attribute('srlbDescriptorCount')
    @SrlbDescriptorCount.setter
    def SrlbDescriptorCount(self, value):
        self._set_attribute('srlbDescriptorCount', value)

    @property
    def SrlbFlags(self):
        """This specifies the value of the SRLB flags field

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('srlbFlags')

    @property
    def TERouterId(self):
        """TE Router ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tERouterId')

    @property
    def VFlag(self):
        """Value Flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vFlag')

    def update(self, EnableSR=None, LocatorCount=None, MtCount=None, Name=None, SRAlgorithmCount=None, SRGBRangeCount=None, SrlbDescriptorCount=None):
        """Updates a child instance of isisL3PseudoRouter on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            EnableSR (bool): This enables SR MPLS on all the simulated ISIS router(s)
            LocatorCount (number): Locator Count
            MtCount (number): MT Count
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SRAlgorithmCount (number): SR Algorithm Count
            SRGBRangeCount (number): SRGB Range Count
            SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, Count=None, DescriptiveName=None, EnableSR=None, LocatorCount=None, MtCount=None, Name=None, SRAlgorithmCount=None, SRGBRangeCount=None, SrlbDescriptorCount=None):
        """Finds and retrieves isisL3PseudoRouter data from the server.

        All named parameters support regex and can be used to selectively retrieve isisL3PseudoRouter data from the server.
        By default the find method takes no parameters and will retrieve all isisL3PseudoRouter data from the server.

        Args:
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            EnableSR (bool): This enables SR MPLS on all the simulated ISIS router(s)
            LocatorCount (number): Locator Count
            MtCount (number): MT Count
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SRAlgorithmCount (number): SR Algorithm Count
            SRGBRangeCount (number): SRGB Range Count
            SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}

        Returns:
            self: This instance with matching isisL3PseudoRouter data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of isisL3PseudoRouter data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the isisL3PseudoRouter data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseNodeMsd=None, AdvertiseSRLB=None, AdvertiseSidAsLocator=None, Algorithm=None, ConfigureSIDIndexLabel=None, DBit=None, DBitForSRv6Cap=None, DBitInsideSRv6SidTLV=None, EFlag=None, EFlagOfSRv6CapTlv=None, Enable=None, EnableMTIPv6=None, EnableWMforTEinNetworkGroup=None, EnableWideMetric=None, Funcflags=None, Function=None, IncludeMaxSlMsd=None, IncludeMaximumEndDMsd=None, IncludeMaximumEndDSrhTLV=None, IncludeMaximumEndPopMsd=None, IncludeMaximumEndPopSrhTLV=None, IncludeMaximumSLTLV=None, IncludeMaximumTEncapMsd=None, IncludeMaximumTEncapSrhTLV=None, IncludeMaximumTInsertMsd=None, IncludeMaximumTInsertSrhTLV=None, Ipv4Flag=None, Ipv6Flag=None, Ipv6MTMetric=None, Ipv6NodePrefix=None, Ipv6Srh=None, LFlag=None, LocatorPrefixLength=None, Mask=None, MaxEndD=None, MaxEndDMsd=None, MaxEndPopMsd=None, MaxEndPopSrh=None, MaxSL=None, MaxSlMsd=None, MaxTEncap=None, MaxTInsert=None, MaxTInsertMsd=None, NFlag=None, NodePrefix=None, OFlagOfSRv6Cap=None, PFlag=None, PrefixLength=None, RFlag=None, Redistribution=None, RedistributionForSRv6=None, ReservedInsideFlagsOfSRv6SidTLV=None, ReservedInsideSRv6CapFlag=None, RouteMetric=None, RouteOrigin=None, RtrcapId=None, RtrcapIdForSrv6=None, SBit=None, SBitForSRv6Cap=None, SIDIndexLabel=None, SRv6NodePrefix=None, SRv6NodePrefixLength=None, SrlbFlags=None, TERouterId=None, VFlag=None):
        """Base class infrastructure that gets a list of isisL3PseudoRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Active (str): optional regex of active
            AdvertiseNodeMsd (str): optional regex of advertiseNodeMsd
            AdvertiseSRLB (str): optional regex of advertiseSRLB
            AdvertiseSidAsLocator (str): optional regex of advertiseSidAsLocator
            Algorithm (str): optional regex of algorithm
            ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
            DBit (str): optional regex of dBit
            DBitForSRv6Cap (str): optional regex of dBitForSRv6Cap
            DBitInsideSRv6SidTLV (str): optional regex of dBitInsideSRv6SidTLV
            EFlag (str): optional regex of eFlag
            EFlagOfSRv6CapTlv (str): optional regex of eFlagOfSRv6CapTlv
            Enable (str): optional regex of enable
            EnableMTIPv6 (str): optional regex of enableMTIPv6
            EnableWMforTEinNetworkGroup (str): optional regex of enableWMforTEinNetworkGroup
            EnableWideMetric (str): optional regex of enableWideMetric
            Funcflags (str): optional regex of funcflags
            Function (str): optional regex of function
            IncludeMaxSlMsd (str): optional regex of includeMaxSlMsd
            IncludeMaximumEndDMsd (str): optional regex of includeMaximumEndDMsd
            IncludeMaximumEndDSrhTLV (str): optional regex of includeMaximumEndDSrhTLV
            IncludeMaximumEndPopMsd (str): optional regex of includeMaximumEndPopMsd
            IncludeMaximumEndPopSrhTLV (str): optional regex of includeMaximumEndPopSrhTLV
            IncludeMaximumSLTLV (str): optional regex of includeMaximumSLTLV
            IncludeMaximumTEncapMsd (str): optional regex of includeMaximumTEncapMsd
            IncludeMaximumTEncapSrhTLV (str): optional regex of includeMaximumTEncapSrhTLV
            IncludeMaximumTInsertMsd (str): optional regex of includeMaximumTInsertMsd
            IncludeMaximumTInsertSrhTLV (str): optional regex of includeMaximumTInsertSrhTLV
            Ipv4Flag (str): optional regex of ipv4Flag
            Ipv6Flag (str): optional regex of ipv6Flag
            Ipv6MTMetric (str): optional regex of ipv6MTMetric
            Ipv6NodePrefix (str): optional regex of ipv6NodePrefix
            Ipv6Srh (str): optional regex of ipv6Srh
            LFlag (str): optional regex of lFlag
            LocatorPrefixLength (str): optional regex of locatorPrefixLength
            Mask (str): optional regex of mask
            MaxEndD (str): optional regex of maxEndD
            MaxEndDMsd (str): optional regex of maxEndDMsd
            MaxEndPopMsd (str): optional regex of maxEndPopMsd
            MaxEndPopSrh (str): optional regex of maxEndPopSrh
            MaxSL (str): optional regex of maxSL
            MaxSlMsd (str): optional regex of maxSlMsd
            MaxTEncap (str): optional regex of maxTEncap
            MaxTInsert (str): optional regex of maxTInsert
            MaxTInsertMsd (str): optional regex of maxTInsertMsd
            NFlag (str): optional regex of nFlag
            NodePrefix (str): optional regex of nodePrefix
            OFlagOfSRv6Cap (str): optional regex of oFlagOfSRv6Cap
            PFlag (str): optional regex of pFlag
            PrefixLength (str): optional regex of prefixLength
            RFlag (str): optional regex of rFlag
            Redistribution (str): optional regex of redistribution
            RedistributionForSRv6 (str): optional regex of redistributionForSRv6
            ReservedInsideFlagsOfSRv6SidTLV (str): optional regex of reservedInsideFlagsOfSRv6SidTLV
            ReservedInsideSRv6CapFlag (str): optional regex of reservedInsideSRv6CapFlag
            RouteMetric (str): optional regex of routeMetric
            RouteOrigin (str): optional regex of routeOrigin
            RtrcapId (str): optional regex of rtrcapId
            RtrcapIdForSrv6 (str): optional regex of rtrcapIdForSrv6
            SBit (str): optional regex of sBit
            SBitForSRv6Cap (str): optional regex of sBitForSRv6Cap
            SIDIndexLabel (str): optional regex of sIDIndexLabel
            SRv6NodePrefix (str): optional regex of sRv6NodePrefix
            SRv6NodePrefixLength (str): optional regex of sRv6NodePrefixLength
            SrlbFlags (str): optional regex of srlbFlags
            TERouterId (str): optional regex of tERouterId
            VFlag (str): optional regex of vFlag

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start Pseudo Node

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        start()

        start(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        start(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop Pseudo Node

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        stop()

        stop(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        stop(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
