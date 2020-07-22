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


class Ospfv2Router(Base):
    """Ospf Device level Configuration
    The Ospfv2Router class encapsulates a list of ospfv2Router resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ospfv2Router.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfv2Router'
    _SDM_ATT_MAP = {
        'BIERPrefix': 'BIERPrefix',
        'Active': 'active',
        'Algorithm': 'algorithm',
        'BBit': 'bBit',
        'BierAFlag': 'bierAFlag',
        'BierNFlag': 'bierNFlag',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DiscardLearnedLsa': 'discardLearnedLsa',
        'DoNotGenerateRouterLsa': 'doNotGenerateRouterLsa',
        'EBit': 'eBit',
        'EFlag': 'eFlag',
        'EnableBIER': 'enableBIER',
        'EnableMappingServer': 'enableMappingServer',
        'EnableMappingServerPreference': 'enableMappingServerPreference',
        'EnableSegmentRouting': 'enableSegmentRouting',
        'EnableSrlb': 'enableSrlb',
        'Errors': 'errors',
        'GracefulRestart': 'gracefulRestart',
        'HighPerfLearningModeForSR': 'highPerfLearningModeForSR',
        'InterFloodLsUpdateBurstGap': 'interFloodLsUpdateBurstGap',
        'LFlag': 'lFlag',
        'LocalRouterID': 'localRouterID',
        'LoopBackAddress': 'loopBackAddress',
        'LsaRefreshTime': 'lsaRefreshTime',
        'LsaRetransmitTime': 'lsaRetransmitTime',
        'MFlag': 'mFlag',
        'MappingServerPreferenceValue': 'mappingServerPreferenceValue',
        'MaxLsUpdatesPerBurst': 'maxLsUpdatesPerBurst',
        'Name': 'name',
        'NoOfAddressPrefix': 'noOfAddressPrefix',
        'NoOfBIERSubDomains': 'noOfBIERSubDomains',
        'NpFlag': 'npFlag',
        'OobResyncBreakout': 'oobResyncBreakout',
        'SRAlgorithmCount': 'sRAlgorithmCount',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'SidIndexLabel': 'sidIndexLabel',
        'SrgbRangeCount': 'srgbRangeCount',
        'SrlbRangeCount': 'srlbRangeCount',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'StrictLsaChecking': 'strictLsaChecking',
        'SupportForRfc3623': 'supportForRfc3623',
        'SupportReasonSoftReloadUpgrade': 'supportReasonSoftReloadUpgrade',
        'SupportReasonSoftRestart': 'supportReasonSoftRestart',
        'SupportReasonSwitchRedundantCntrlProcessor': 'supportReasonSwitchRedundantCntrlProcessor',
        'SupportReasonUnknown': 'supportReasonUnknown',
        'VFlag': 'vFlag',
    }

    def __init__(self, parent):
        super(Ospfv2Router, self).__init__(parent)

    @property
    def OspfBierSubDomainList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfbiersubdomainlist_a244513d4753b7b3d307266e2c9b6c70.OspfBierSubDomainList): An instance of the OspfBierSubDomainList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfbiersubdomainlist_a244513d4753b7b3d307266e2c9b6c70 import OspfBierSubDomainList
        return OspfBierSubDomainList(self)._select()

    @property
    def OspfSRAlgorithmList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsralgorithmlist_6d5b092154ba202ff142c9a80bdf1352.OspfSRAlgorithmList): An instance of the OspfSRAlgorithmList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsralgorithmlist_6d5b092154ba202ff142c9a80bdf1352 import OspfSRAlgorithmList
        return OspfSRAlgorithmList(self)

    @property
    def OspfSRGBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrgbrangesubobjectslist_3183939e699e6d81694733106246396f.OspfSRGBRangeSubObjectsList): An instance of the OspfSRGBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrgbrangesubobjectslist_3183939e699e6d81694733106246396f import OspfSRGBRangeSubObjectsList
        return OspfSRGBRangeSubObjectsList(self)

    @property
    def OspfSRLBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrlbrangesubobjectslist_3469b01175113efcd50b58a826370e91.OspfSRLBRangeSubObjectsList): An instance of the OspfSRLBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrlbrangesubobjectslist_3469b01175113efcd50b58a826370e91 import OspfSRLBRangeSubObjectsList
        return OspfSRLBRangeSubObjectsList(self)

    @property
    def BIERPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A BFR's BFR-Prefix is an IP address (either IPv4 or IPv6) of the BFR, and MUST be unique and routable within the BIER domain.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BIERPrefix']))

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
    def Algorithm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm for the Node SID/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def BBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA B-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BBit']))

    @property
    def BierAFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Attach Flag: If set an Area Border Router (ABR) will generate an Extended Prefix TLV for inter-area prefix that is locally connected or attached in other connected area
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BierAFlag']))

    @property
    def BierNFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node Flag: Set when the prefix identifies the advertising router i.e., the prefix is a host prefix advertising a globally reachable address typically associated with a loopback address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BierNFlag']))

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
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DiscardLearnedLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Discard Learned LSAs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa']))

    @property
    def DoNotGenerateRouterLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Generate Router LSA.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DoNotGenerateRouterLsa']))

    @property
    def EBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA E-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EBit']))

    @property
    def EFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit-Null Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def EnableBIER(self):
        """
        Returns
        -------
        - bool: Enable BIER
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBIER'])
    @EnableBIER.setter
    def EnableBIER(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBIER'], value)

    @property
    def EnableMappingServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Mapping Server of Segment Routing
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMappingServer']))

    @property
    def EnableMappingServerPreference(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Mapping Server Preference of Segment Routing, used if multiple Mapping Servers are configured
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMappingServerPreference']))

    @property
    def EnableSegmentRouting(self):
        """
        Returns
        -------
        - bool: Enable Segment Routing
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSegmentRouting'])
    @EnableSegmentRouting.setter
    def EnableSegmentRouting(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSegmentRouting'], value)

    @property
    def EnableSrlb(self):
        """
        Returns
        -------
        - bool: Enable SRLB
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSrlb'])
    @EnableSrlb.setter
    def EnableSrlb(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSrlb'], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def GracefulRestart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Graceful Restart,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GracefulRestart']))

    @property
    def HighPerfLearningModeForSR(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This option can be used to increase scale. When enabled then the minimum information required to generate traffic is stored instead of the entire LSA. For example, for SR traffic generation, sid, vflag, SRGB details are stored and label is calculated accordingly. Please note when this flag is enabled, we will not store any LSAs so Learned Info will not display any details. Currently this is supported for only SR opaque LSAs, other Opaque LSAs like BIER, Graceful Restart is not supported, also not supported for BGP-LS scenarios.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HighPerfLearningModeForSR']))

    @property
    def InterFloodLsUpdateBurstGap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Inter Flood LSUpdate burst gap (ms)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterFloodLsUpdateBurstGap']))

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local or Global Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def LocalRouterID(self):
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterID'])

    @property
    def LoopBackAddress(self):
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoopBackAddress'])

    @property
    def LsaRefreshTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSA Refresh time (s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LsaRefreshTime']))

    @property
    def LsaRetransmitTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): LSA Retransmit time(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LsaRetransmitTime']))

    @property
    def MFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mapping Server Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MFlag']))

    @property
    def MappingServerPreferenceValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Preference Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MappingServerPreferenceValue']))

    @property
    def MaxLsUpdatesPerBurst(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Max Flood LSUpdates Per Burst
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxLsUpdatesPerBurst']))

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
    def NoOfAddressPrefix(self):
        """
        Returns
        -------
        - number: Number Of Address Prefix Range
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfAddressPrefix'])
    @NoOfAddressPrefix.setter
    def NoOfAddressPrefix(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfAddressPrefix'], value)

    @property
    def NoOfBIERSubDomains(self):
        """
        Returns
        -------
        - number: Number of BIER Sub Domains
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfBIERSubDomains'])
    @NoOfBIERSubDomains.setter
    def NoOfBIERSubDomains(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfBIERSubDomains'], value)

    @property
    def NpFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No-PHP Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NpFlag']))

    @property
    def OobResyncBreakout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable out-of-band resynchronization breakout
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OobResyncBreakout']))

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
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[noIfaceUp | sameNbrRouterId | up]): Logs additional information about the session Information
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SidIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidIndexLabel']))

    @property
    def SrgbRangeCount(self):
        """
        Returns
        -------
        - number: SRGB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrgbRangeCount'])
    @SrgbRangeCount.setter
    def SrgbRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrgbRangeCount'], value)

    @property
    def SrlbRangeCount(self):
        """
        Returns
        -------
        - number: SRLB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrlbRangeCount'])
    @SrlbRangeCount.setter
    def SrlbRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrlbRangeCount'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def StrictLsaChecking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Terminate graceful restart when an LSA has changed
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StrictLsaChecking']))

    @property
    def SupportForRfc3623(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support RFC 3623 features,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportForRfc3623']))

    @property
    def SupportReasonSoftReloadUpgrade(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is Software Reload or Upgrade.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportReasonSoftReloadUpgrade']))

    @property
    def SupportReasonSoftRestart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is OSPFv2 software restart.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportReasonSoftRestart']))

    @property
    def SupportReasonSwitchRedundantCntrlProcessor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is unplanned switchover.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportReasonSwitchRedundantCntrlProcessor']))

    @property
    def SupportReasonUnknown(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Support graceful restart helper mode when restart reason is unknown and unplanned.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SupportReasonUnknown']))

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value or Index Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, EnableBIER=None, EnableSegmentRouting=None, EnableSrlb=None, Name=None, NoOfAddressPrefix=None, NoOfBIERSubDomains=None, SRAlgorithmCount=None, SrgbRangeCount=None, SrlbRangeCount=None):
        """Updates ospfv2Router resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableBIER (bool): Enable BIER
        - EnableSegmentRouting (bool): Enable Segment Routing
        - EnableSrlb (bool): Enable SRLB
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAddressPrefix (number): Number Of Address Prefix Range
        - NoOfBIERSubDomains (number): Number of BIER Sub Domains
        - SRAlgorithmCount (number): SR Algorithm Count
        - SrgbRangeCount (number): SRGB Range Count
        - SrlbRangeCount (number): SRLB Range Count

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, EnableBIER=None, EnableSegmentRouting=None, EnableSrlb=None, Errors=None, LocalRouterID=None, LoopBackAddress=None, Name=None, NoOfAddressPrefix=None, NoOfBIERSubDomains=None, SRAlgorithmCount=None, SessionInfo=None, SessionStatus=None, SrgbRangeCount=None, SrlbRangeCount=None, StateCounts=None, Status=None):
        """Finds and retrieves ospfv2Router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfv2Router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfv2Router resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - EnableBIER (bool): Enable BIER
        - EnableSegmentRouting (bool): Enable Segment Routing
        - EnableSrlb (bool): Enable SRLB
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalRouterID (list(str)): Router ID
        - LoopBackAddress (list(str)): Router ID
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAddressPrefix (number): Number Of Address Prefix Range
        - NoOfBIERSubDomains (number): Number of BIER Sub Domains
        - SRAlgorithmCount (number): SR Algorithm Count
        - SessionInfo (list(str[noIfaceUp | sameNbrRouterId | up])): Logs additional information about the session Information
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SrgbRangeCount (number): SRGB Range Count
        - SrlbRangeCount (number): SRLB Range Count
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ospfv2Router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfv2Router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfv2Router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BIERPrefix=None, Active=None, Algorithm=None, BBit=None, BierAFlag=None, BierNFlag=None, ConfigureSIDIndexLabel=None, DiscardLearnedLsa=None, DoNotGenerateRouterLsa=None, EBit=None, EFlag=None, EnableMappingServer=None, EnableMappingServerPreference=None, GracefulRestart=None, HighPerfLearningModeForSR=None, InterFloodLsUpdateBurstGap=None, LFlag=None, LsaRefreshTime=None, LsaRetransmitTime=None, MFlag=None, MappingServerPreferenceValue=None, MaxLsUpdatesPerBurst=None, NpFlag=None, OobResyncBreakout=None, SidIndexLabel=None, StrictLsaChecking=None, SupportForRfc3623=None, SupportReasonSoftReloadUpgrade=None, SupportReasonSoftRestart=None, SupportReasonSwitchRedundantCntrlProcessor=None, SupportReasonUnknown=None, VFlag=None):
        """Base class infrastructure that gets a list of ospfv2Router device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BIERPrefix (str): optional regex of BIERPrefix
        - Active (str): optional regex of active
        - Algorithm (str): optional regex of algorithm
        - BBit (str): optional regex of bBit
        - BierAFlag (str): optional regex of bierAFlag
        - BierNFlag (str): optional regex of bierNFlag
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - DiscardLearnedLsa (str): optional regex of discardLearnedLsa
        - DoNotGenerateRouterLsa (str): optional regex of doNotGenerateRouterLsa
        - EBit (str): optional regex of eBit
        - EFlag (str): optional regex of eFlag
        - EnableMappingServer (str): optional regex of enableMappingServer
        - EnableMappingServerPreference (str): optional regex of enableMappingServerPreference
        - GracefulRestart (str): optional regex of gracefulRestart
        - HighPerfLearningModeForSR (str): optional regex of highPerfLearningModeForSR
        - InterFloodLsUpdateBurstGap (str): optional regex of interFloodLsUpdateBurstGap
        - LFlag (str): optional regex of lFlag
        - LsaRefreshTime (str): optional regex of lsaRefreshTime
        - LsaRetransmitTime (str): optional regex of lsaRetransmitTime
        - MFlag (str): optional regex of mFlag
        - MappingServerPreferenceValue (str): optional regex of mappingServerPreferenceValue
        - MaxLsUpdatesPerBurst (str): optional regex of maxLsUpdatesPerBurst
        - NpFlag (str): optional regex of npFlag
        - OobResyncBreakout (str): optional regex of oobResyncBreakout
        - SidIndexLabel (str): optional regex of sidIndexLabel
        - StrictLsaChecking (str): optional regex of strictLsaChecking
        - SupportForRfc3623 (str): optional regex of supportForRfc3623
        - SupportReasonSoftReloadUpgrade (str): optional regex of supportReasonSoftReloadUpgrade
        - SupportReasonSoftRestart (str): optional regex of supportReasonSoftRestart
        - SupportReasonSwitchRedundantCntrlProcessor (str): optional regex of supportReasonSwitchRedundantCntrlProcessor
        - SupportReasonUnknown (str): optional regex of supportReasonUnknown
        - VFlag (str): optional regex of vFlag

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
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
        return self._execute('abort', payload=payload, response_object=None)

    def OspfStartRouter(self, *args, **kwargs):
        """Executes the ospfStartRouter operation on the server.

        Start OSPF Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ospfStartRouter(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        ospfStartRouter(SessionIndices=string)
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ospfStartRouter', payload=payload, response_object=None)

    def OspfStopRouter(self, *args, **kwargs):
        """Executes the ospfStopRouter operation on the server.

        Stop OSPF Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ospfStopRouter(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        ospfStopRouter(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ospfStopRouter', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

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
