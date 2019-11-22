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


class IsisL3PseudoInterface(Base):
    """ISIS-L3 Pseudo Interafce Configuration
    The IsisL3PseudoInterface class encapsulates a list of isisL3PseudoInterface resources that is managed by the system.
    A list of resources can be retrieved from the server using the IsisL3PseudoInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'isisL3PseudoInterface'

    def __init__(self, parent):
        super(IsisL3PseudoInterface, self).__init__(parent)

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
    def IsisDcePseudoIfaceAttPoint1Config(self):
        """An instance of the IsisDcePseudoIfaceAttPoint1Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config.IsisDcePseudoIfaceAttPoint1Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config import IsisDcePseudoIfaceAttPoint1Config
        return IsisDcePseudoIfaceAttPoint1Config(self)

    @property
    def IsisDcePseudoIfaceAttPoint2Config(self):
        """An instance of the IsisDcePseudoIfaceAttPoint2Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config.IsisDcePseudoIfaceAttPoint2Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config import IsisDcePseudoIfaceAttPoint2Config
        return IsisDcePseudoIfaceAttPoint2Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint1Config(self):
        """An instance of the IsisL3PseudoIfaceAttPoint1Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config.IsisL3PseudoIfaceAttPoint1Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config import IsisL3PseudoIfaceAttPoint1Config
        return IsisL3PseudoIfaceAttPoint1Config(self)

    @property
    def IsisL3PseudoIfaceAttPoint2Config(self):
        """An instance of the IsisL3PseudoIfaceAttPoint2Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config.IsisL3PseudoIfaceAttPoint2Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config import IsisL3PseudoIfaceAttPoint2Config
        return IsisL3PseudoIfaceAttPoint2Config(self)

    @property
    def IsisPseudoSRv6AdjSIDList(self):
        """An instance of the IsisPseudoSRv6AdjSIDList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6adjsidlist.IsisPseudoSRv6AdjSIDList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudosrv6adjsidlist import IsisPseudoSRv6AdjSIDList
        return IsisPseudoSRv6AdjSIDList(self)._select()

    @property
    def IsisSpbPseudoIfaceAttPoint1Config(self):
        """An instance of the IsisSpbPseudoIfaceAttPoint1Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config.IsisSpbPseudoIfaceAttPoint1Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config import IsisSpbPseudoIfaceAttPoint1Config
        return IsisSpbPseudoIfaceAttPoint1Config(self)

    @property
    def IsisSpbPseudoIfaceAttPoint2Config(self):
        """An instance of the IsisSpbPseudoIfaceAttPoint2Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config.IsisSpbPseudoIfaceAttPoint2Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config import IsisSpbPseudoIfaceAttPoint2Config
        return IsisSpbPseudoIfaceAttPoint2Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint1Config(self):
        """An instance of the IsisTrillPseudoIfaceAttPoint1Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config.IsisTrillPseudoIfaceAttPoint1Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config import IsisTrillPseudoIfaceAttPoint1Config
        return IsisTrillPseudoIfaceAttPoint1Config(self)

    @property
    def IsisTrillPseudoIfaceAttPoint2Config(self):
        """An instance of the IsisTrillPseudoIfaceAttPoint2Config class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config.IsisTrillPseudoIfaceAttPoint2Config)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config import IsisTrillPseudoIfaceAttPoint2Config
        return IsisTrillPseudoIfaceAttPoint2Config(self)

    @property
    def SrlgValueList(self):
        """An instance of the SrlgValueList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist.SrlgValueList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist import SrlgValueList
        return SrlgValueList(self)

    @property
    def AdjSID(self):
        """AdjSID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('adjSID')

    @property
    def AdjSidCount(self):
        """Adj SID Count

        Returns:
            number
        """
        return self._get_attribute('adjSidCount')
    @AdjSidCount.setter
    def AdjSidCount(self, value):
        self._set_attribute('adjSidCount', value)

    @property
    def AdministratorGroup(self):
        """Administrator Group

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('administratorGroup')

    @property
    def AdvertiseLinkMsd(self):
        """Advertise Link MSD

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('advertiseLinkMsd')

    @property
    def BFlag(self):
        """Backup Flag, if set, the Adj-SID is eligible for protection

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bFlag')

    @property
    def BandwidthPriority0_Bps(self):
        """Bandwidth for Priority 0 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority0_Bps')

    @property
    def BandwidthPriority1_Bps(self):
        """Bandwidth for Priority 1 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority1_Bps')

    @property
    def BandwidthPriority2_Bps(self):
        """Bandwidth for Priority 2 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority2_Bps')

    @property
    def BandwidthPriority3_Bps(self):
        """Bandwidth for Priority 3 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority3_Bps')

    @property
    def BandwidthPriority4_Bps(self):
        """Bandwidth for Priority 4 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority4_Bps')

    @property
    def BandwidthPriority5_Bps(self):
        """Bandwidth for Priority 5 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority5_Bps')

    @property
    def BandwidthPriority6_Bps(self):
        """Bandwidth for Priority 6 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority6_Bps')

    @property
    def BandwidthPriority7_Bps(self):
        """Bandwidth for Priority 7 (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bandwidthPriority7_Bps')

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DedicatedOnePlusOne(self):
        """This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dedicatedOnePlusOne')

    @property
    def DedicatedOneToOne(self):
        """This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dedicatedOneToOne')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def EnableAdjSID(self):
        """Enable Adj SID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableAdjSID')

    @property
    def EnableIPv6SID(self):
        """Enable IPv6 SID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableIPv6SID')

    @property
    def EnableLinkProtection(self):
        """This enables the link protection on the ISIS link between two mentioned interfaces.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableLinkProtection')

    @property
    def EnableMT(self):
        """Enable MT

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableMT')

    @property
    def EnableSRLG(self):
        """This enables the SRLG on the ISIS link between two mentioned interfaces.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enableSRLG')

    @property
    def Enhanced(self):
        """This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('enhanced')

    @property
    def ExtraTraffic(self):
        """This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('extraTraffic')

    @property
    def FFlag(self):
        """Address Family Flag,False value refers to an adjacency with outgoing IPv4 encapsulationTrue value refers to an adjacency with outgoing IPv6 encapsulation

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('fFlag')

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
    def IncludeMaximumEndPopMsd(self):
        """If set, then include Max-End-Pop-MSD n SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumEndPopMsd')

    @property
    def IncludeMaximumTEncapMsd(self):
        """If set, then include Maximum T.Encap MSD in SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumTEncapMsd')

    @property
    def IncludeMaximumTInsertMsd(self):
        """If set, then include Maximum T.Insert MSDin SRv6 capability

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeMaximumTInsertMsd')

    @property
    def Ipv6SidValue(self):
        """DEPRECATED IPv6 Adj SID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6SidValue')

    @property
    def LFlag(self):
        """Local Flag, if set, then the value/index carried by the Adj-SID has local significance

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lFlag')

    @property
    def LinkType(self):
        """Link Type

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('linkType')

    @property
    def MaxBandwidth_Bps(self):
        """Maximum Bandwidth (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxBandwidth_Bps')

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
    def MaxReservableBandwidth_Bps(self):
        """Maximum Reservable Bandwidth (B/sec)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxReservableBandwidth_Bps')

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
    def MaxTInsertMsd(self):
        """This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('maxTInsertMsd')

    @property
    def MetricLevel(self):
        """Metric Level

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('metricLevel')

    @property
    def MtCount(self):
        """MT Count

        Returns:
            number
        """
        return self._get_attribute('mtCount')

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
    def OverrideFFlag(self):
        """When false, then F flag value in the packet will be set TRUE/ FALSE depending on whether IPv6/ IPv4 stack is present beside ISIS respectively. When true, then F flag value will be the one as configured.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('overrideFFlag')

    @property
    def PFlag(self):
        """Persistent flag: when set, this indicates that the Adj-SID value remains persistent across router restart and/or interface flap.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('pFlag')

    @property
    def Reserved0x40(self):
        """This is a Protection Scheme with value 0x40.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('reserved0x40')

    @property
    def Reserved0x80(self):
        """This is a Protection Scheme with value 0x80.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('reserved0x80')

    @property
    def SFlag(self):
        """Set flag: when set, this indicates that the Adj-SID refers to a set of adjacencies

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sFlag')

    @property
    def Shared(self):
        """This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('shared')

    @property
    def SrlgCount(self):
        """This field value shows how many SRLG Value columns would be there in the GUI.

        Returns:
            number
        """
        return self._get_attribute('srlgCount')
    @SrlgCount.setter
    def SrlgCount(self, value):
        self._set_attribute('srlgCount', value)

    @property
    def Srv6SidFlags(self):
        """DEPRECATED This specifies the value of the SRv6 SID Flags

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('srv6SidFlags')

    @property
    def Unprotected(self):
        """This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('unprotected')

    @property
    def VFlag(self):
        """Value Flag, if set, the Adjacency SID carries a value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vFlag')

    @property
    def Weight(self):
        """Weight

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('weight')

    def update(self, AdjSidCount=None, Name=None, SrlgCount=None):
        """Updates a child instance of isisL3PseudoInterface on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            AdjSidCount (number): Adj SID Count
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, AdjSidCount=None, Count=None, DescriptiveName=None, MtCount=None, Name=None, SrlgCount=None):
        """Finds and retrieves isisL3PseudoInterface data from the server.

        All named parameters support regex and can be used to selectively retrieve isisL3PseudoInterface data from the server.
        By default the find method takes no parameters and will retrieve all isisL3PseudoInterface data from the server.

        Args:
            AdjSidCount (number): Adj SID Count
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            MtCount (number): MT Count
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.

        Returns:
            self: This instance with matching isisL3PseudoInterface data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of isisL3PseudoInterface data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the isisL3PseudoInterface data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, AdjSID=None, AdministratorGroup=None, AdvertiseLinkMsd=None, BFlag=None, BandwidthPriority0_Bps=None, BandwidthPriority1_Bps=None, BandwidthPriority2_Bps=None, BandwidthPriority3_Bps=None, BandwidthPriority4_Bps=None, BandwidthPriority5_Bps=None, BandwidthPriority6_Bps=None, BandwidthPriority7_Bps=None, DedicatedOnePlusOne=None, DedicatedOneToOne=None, EnableAdjSID=None, EnableIPv6SID=None, EnableLinkProtection=None, EnableMT=None, EnableSRLG=None, Enhanced=None, ExtraTraffic=None, FFlag=None, Funcflags=None, Function=None, IncludeMaxSlMsd=None, IncludeMaximumEndDMsd=None, IncludeMaximumEndPopMsd=None, IncludeMaximumTEncapMsd=None, IncludeMaximumTInsertMsd=None, Ipv6SidValue=None, LFlag=None, LinkType=None, MaxBandwidth_Bps=None, MaxEndDMsd=None, MaxEndPopMsd=None, MaxReservableBandwidth_Bps=None, MaxSlMsd=None, MaxTEncap=None, MaxTInsertMsd=None, MetricLevel=None, OverrideFFlag=None, PFlag=None, Reserved0x40=None, Reserved0x80=None, SFlag=None, Shared=None, Srv6SidFlags=None, Unprotected=None, VFlag=None, Weight=None):
        """Base class infrastructure that gets a list of isisL3PseudoInterface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            AdjSID (str): optional regex of adjSID
            AdministratorGroup (str): optional regex of administratorGroup
            AdvertiseLinkMsd (str): optional regex of advertiseLinkMsd
            BFlag (str): optional regex of bFlag
            BandwidthPriority0_Bps (str): optional regex of bandwidthPriority0_Bps
            BandwidthPriority1_Bps (str): optional regex of bandwidthPriority1_Bps
            BandwidthPriority2_Bps (str): optional regex of bandwidthPriority2_Bps
            BandwidthPriority3_Bps (str): optional regex of bandwidthPriority3_Bps
            BandwidthPriority4_Bps (str): optional regex of bandwidthPriority4_Bps
            BandwidthPriority5_Bps (str): optional regex of bandwidthPriority5_Bps
            BandwidthPriority6_Bps (str): optional regex of bandwidthPriority6_Bps
            BandwidthPriority7_Bps (str): optional regex of bandwidthPriority7_Bps
            DedicatedOnePlusOne (str): optional regex of dedicatedOnePlusOne
            DedicatedOneToOne (str): optional regex of dedicatedOneToOne
            EnableAdjSID (str): optional regex of enableAdjSID
            EnableIPv6SID (str): optional regex of enableIPv6SID
            EnableLinkProtection (str): optional regex of enableLinkProtection
            EnableMT (str): optional regex of enableMT
            EnableSRLG (str): optional regex of enableSRLG
            Enhanced (str): optional regex of enhanced
            ExtraTraffic (str): optional regex of extraTraffic
            FFlag (str): optional regex of fFlag
            Funcflags (str): optional regex of funcflags
            Function (str): optional regex of function
            IncludeMaxSlMsd (str): optional regex of includeMaxSlMsd
            IncludeMaximumEndDMsd (str): optional regex of includeMaximumEndDMsd
            IncludeMaximumEndPopMsd (str): optional regex of includeMaximumEndPopMsd
            IncludeMaximumTEncapMsd (str): optional regex of includeMaximumTEncapMsd
            IncludeMaximumTInsertMsd (str): optional regex of includeMaximumTInsertMsd
            Ipv6SidValue (str): optional regex of ipv6SidValue
            LFlag (str): optional regex of lFlag
            LinkType (str): optional regex of linkType
            MaxBandwidth_Bps (str): optional regex of maxBandwidth_Bps
            MaxEndDMsd (str): optional regex of maxEndDMsd
            MaxEndPopMsd (str): optional regex of maxEndPopMsd
            MaxReservableBandwidth_Bps (str): optional regex of maxReservableBandwidth_Bps
            MaxSlMsd (str): optional regex of maxSlMsd
            MaxTEncap (str): optional regex of maxTEncap
            MaxTInsertMsd (str): optional regex of maxTInsertMsd
            MetricLevel (str): optional regex of metricLevel
            OverrideFFlag (str): optional regex of overrideFFlag
            PFlag (str): optional regex of pFlag
            Reserved0x40 (str): optional regex of reserved0x40
            Reserved0x80 (str): optional regex of reserved0x80
            SFlag (str): optional regex of sFlag
            Shared (str): optional regex of shared
            Srv6SidFlags (str): optional regex of srv6SidFlags
            Unprotected (str): optional regex of unprotected
            VFlag (str): optional regex of vFlag
            Weight (str): optional regex of weight

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)
