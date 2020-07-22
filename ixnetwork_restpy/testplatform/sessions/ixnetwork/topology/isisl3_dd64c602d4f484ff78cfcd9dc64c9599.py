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


class IsisL3(Base):
    """ISIS Interface level Configuration
    The IsisL3 class encapsulates a list of isisL3 resources that are managed by the user.
    A list of resources can be retrieved from the server using the IsisL3.find() method.
    The list can be managed by using the IsisL3.add() and IsisL3.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'isisL3'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdjSID': 'adjSID',
        'AdjSidCount': 'adjSidCount',
        'AdvertiseLinkMsd': 'advertiseLinkMsd',
        'AuthType': 'authType',
        'AutoAdjustArea': 'autoAdjustArea',
        'AutoAdjustMTU': 'autoAdjustMTU',
        'AutoAdjustSupportedProtocols': 'autoAdjustSupportedProtocols',
        'BFlag': 'bFlag',
        'CircuitTranmitPasswordOrMD5Key': 'circuitTranmitPasswordOrMD5Key',
        'ConfiguredHoldTime': 'configuredHoldTime',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DedicatedOnePlusOne': 'dedicatedOnePlusOne',
        'DedicatedOneToOne': 'dedicatedOneToOne',
        'DescriptiveName': 'descriptiveName',
        'Enable3WayHandshake': 'enable3WayHandshake',
        'EnableAdjSID': 'enableAdjSID',
        'EnableAppSpecSrlg': 'enableAppSpecSrlg',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableConfiguredHoldTime': 'enableConfiguredHoldTime',
        'EnableIPv6SID': 'enableIPv6SID',
        'EnableLinkProtection': 'enableLinkProtection',
        'EnableMT': 'enableMT',
        'EnableSRLG': 'enableSRLG',
        'Enhanced': 'enhanced',
        'Errors': 'errors',
        'ExtendedLocalCircuitId': 'extendedLocalCircuitId',
        'ExtraTraffic': 'extraTraffic',
        'FFlag': 'fFlag',
        'Funcflags': 'funcflags',
        'Function': 'function',
        'IncludeMaxSlMsd': 'includeMaxSlMsd',
        'IncludeMaximumEndDMsd': 'includeMaximumEndDMsd',
        'IncludeMaximumEndPopMsd': 'includeMaximumEndPopMsd',
        'IncludeMaximumTEncapMsd': 'includeMaximumTEncapMsd',
        'IncludeMaximumTInsertMsd': 'includeMaximumTInsertMsd',
        'InterfaceMetric': 'interfaceMetric',
        'Ipv6MTMetric': 'ipv6MTMetric',
        'Ipv6SidValue': 'ipv6SidValue',
        'LFlag': 'lFlag',
        'Level1DeadInterval': 'level1DeadInterval',
        'Level1HelloInterval': 'level1HelloInterval',
        'Level1Priority': 'level1Priority',
        'Level2DeadInterval': 'level2DeadInterval',
        'Level2HelloInterval': 'level2HelloInterval',
        'Level2Priority': 'level2Priority',
        'LevelType': 'levelType',
        'LocalSystemID': 'localSystemID',
        'MaxEndDMsd': 'maxEndDMsd',
        'MaxEndPopMsd': 'maxEndPopMsd',
        'MaxSlMsd': 'maxSlMsd',
        'MaxTEncap': 'maxTEncap',
        'MaxTInsertMsd': 'maxTInsertMsd',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NetworkType': 'networkType',
        'NoOfAppSpecSrlg': 'noOfAppSpecSrlg',
        'NoOfTeProfile': 'noOfTeProfile',
        'OverrideFFlag': 'overrideFFlag',
        'PFlag': 'pFlag',
        'Reserved0x40': 'reserved0x40',
        'Reserved0x80': 'reserved0x80',
        'SFlag': 'sFlag',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'Shared': 'shared',
        'SrlgCount': 'srlgCount',
        'Srv6SidFlags': 'srv6SidFlags',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SuppressHello': 'suppressHello',
        'Unprotected': 'unprotected',
        'VFlag': 'vFlag',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(IsisL3, self).__init__(parent)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

    @property
    def IsisAppSpecSrlgList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisappspecsrlglist_c86dcbcff988ad5c54aecdd16dd33b6f.IsisAppSpecSrlgList): An instance of the IsisAppSpecSrlgList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisappspecsrlglist_c86dcbcff988ad5c54aecdd16dd33b6f import IsisAppSpecSrlgList
        return IsisAppSpecSrlgList(self)._select()

    @property
    def IsisSRv6AdjSIDList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrv6adjsidlist_16299dd6f98290fd7ee533e18848a8f5.IsisSRv6AdjSIDList): An instance of the IsisSRv6AdjSIDList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isissrv6adjsidlist_16299dd6f98290fd7ee533e18848a8f5 import IsisSRv6AdjSIDList
        return IsisSRv6AdjSIDList(self)._select()

    @property
    def IsisTrafficEngineering(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrafficengineering_6032af9b157866ba1321273f0c47a612.IsisTrafficEngineering): An instance of the IsisTrafficEngineering class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrafficengineering_6032af9b157866ba1321273f0c47a612 import IsisTrafficEngineering
        return IsisTrafficEngineering(self)._select()

    @property
    def IsisTrafficEngineeringProfileList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrafficengineeringprofilelist_c47e6899658130ebf14e5ea5147ac23a.IsisTrafficEngineeringProfileList): An instance of the IsisTrafficEngineeringProfileList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrafficengineeringprofilelist_c47e6899658130ebf14e5ea5147ac23a import IsisTrafficEngineeringProfileList
        return IsisTrafficEngineeringProfileList(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        return LearnedInfo(self)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist_355b617a5f46ce90d800290d21158418 import SrlgValueList
        return SrlgValueList(self)

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
    def AdjSID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AdjSID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdjSID']))

    @property
    def AdjSidCount(self):
        """
        Returns
        -------
        - number: Adj SID Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdjSidCount'])
    @AdjSidCount.setter
    def AdjSidCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AdjSidCount'], value)

    @property
    def AdvertiseLinkMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise Link MSD
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseLinkMsd']))

    @property
    def AuthType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthType']))

    @property
    def AutoAdjustArea(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Adjust Area
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoAdjustArea']))

    @property
    def AutoAdjustMTU(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Adjust MTU
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoAdjustMTU']))

    @property
    def AutoAdjustSupportedProtocols(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Adjust Supported Protocols
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AutoAdjustSupportedProtocols']))

    @property
    def BFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup Flag, if set, the Adj-SID is eligible for protection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlag']))

    @property
    def CircuitTranmitPasswordOrMD5Key(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Circuit Transmit Password / MD5-Key
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CircuitTranmitPasswordOrMD5Key']))

    @property
    def ConfiguredHoldTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configured Hold Time
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfiguredHoldTime']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DedicatedOnePlusOne(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DedicatedOnePlusOne']))

    @property
    def DedicatedOneToOne(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DedicatedOneToOne']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Enable3WayHandshake(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable 3-way Handshake
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enable3WayHandshake']))

    @property
    def EnableAdjSID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Adj SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAdjSID']))

    @property
    def EnableAppSpecSrlg(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables Application Specific SRLG on the ISIS link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableAppSpecSrlg']))

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable BFD Registration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration']))

    @property
    def EnableConfiguredHoldTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Configured Hold Time
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableConfiguredHoldTime']))

    @property
    def EnableIPv6SID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable IPv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIPv6SID']))

    @property
    def EnableLinkProtection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the link protection on the ISIS link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLinkProtection']))

    @property
    def EnableMT(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable MT
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableMT']))

    @property
    def EnableSRLG(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the SRLG on the ISIS link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableSRLG']))

    @property
    def Enhanced(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enhanced']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def ExtendedLocalCircuitId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Extended Local Circuit Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtendedLocalCircuitId']))

    @property
    def ExtraTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtraTraffic']))

    @property
    def FFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Address Family Flag,False value refers to an adjacency with outgoing IPv4 encapsulationTrue value refers to an adjacency with outgoing IPv6 encapsulation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FFlag']))

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
    def IncludeMaximumEndPopMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Max-End-Pop-MSD n SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumEndPopMsd']))

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
    def IncludeMaximumTInsertMsd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If set, then include Maximum T.Insert MSDin SRv6 capability
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeMaximumTInsertMsd']))

    @property
    def InterfaceMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InterfaceMetric']))

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
    def Ipv6SidValue(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Adj SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6SidValue']))

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Flag, if set, then the value/index carried by the Adj-SID has local significance
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def Level1DeadInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Level 1 Dead Interval (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level1DeadInterval']))

    @property
    def Level1HelloInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Level 1 Hello Interval (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level1HelloInterval']))

    @property
    def Level1Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Level 1 Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level1Priority']))

    @property
    def Level2DeadInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Level 2 Dead Interval (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level2DeadInterval']))

    @property
    def Level2HelloInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Level 2 Hello Interval (sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level2HelloInterval']))

    @property
    def Level2Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Level 2 Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level2Priority']))

    @property
    def LevelType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Level Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LevelType']))

    @property
    def LocalSystemID(self):
        """
        Returns
        -------
        - list(str): System ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalSystemID'])

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
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH, it is the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxTEncap']))

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
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

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
    def NetworkType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Network Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkType']))

    @property
    def NoOfAppSpecSrlg(self):
        """
        Returns
        -------
        - number: This field value shows how many SRLG Value columns would be there in the GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfAppSpecSrlg'])
    @NoOfAppSpecSrlg.setter
    def NoOfAppSpecSrlg(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfAppSpecSrlg'], value)

    @property
    def NoOfTeProfile(self):
        """
        Returns
        -------
        - number: Number of TE Profile
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfTeProfile'])
    @NoOfTeProfile.setter
    def NoOfTeProfile(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfTeProfile'], value)

    @property
    def OverrideFFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When false, then F flag value in the packet will be set TRUE/ FALSE depending on whether IPv6/ IPv4 stack is present beside ISIS respectively. When true, then F flag value will be the one as configured.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OverrideFFlag']))

    @property
    def PFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Persistent flag: when set, this indicates that the Adj-SID value remains persistent across router restart and/or interface flap.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def Reserved0x40(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x40.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved0x40']))

    @property
    def Reserved0x80(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x80.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved0x80']))

    @property
    def SFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set flag: when set, this indicates that the Adj-SID refers to a set of adjacencies
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlag']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[ifaceSessInfoFsmNotStarted | ifaceSessInfoNotAllNbrInFull | iPAddressNotRcvd | none]): Logs additional information about the session state
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
    def Shared(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Shared']))

    @property
    def SrlgCount(self):
        """
        Returns
        -------
        - number: This field value shows how many SRLG Value columns would be there in the GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrlgCount'])
    @SrlgCount.setter
    def SrlgCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrlgCount'], value)

    @property
    def Srv6SidFlags(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies the value of the SRv6 SID Flags
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6SidFlags']))

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

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
    def SuppressHello(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hello suppression
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SuppressHello']))

    @property
    def Unprotected(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unprotected']))

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value Flag, if set, the Adjacency SID carries a value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, AdjSidCount=None, ConnectedVia=None, Multiplier=None, Name=None, NoOfAppSpecSrlg=None, NoOfTeProfile=None, SrlgCount=None, StackedLayers=None):
        """Updates isisL3 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - AdjSidCount (number): Adj SID Count
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAppSpecSrlg (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdjSidCount=None, ConnectedVia=None, Multiplier=None, Name=None, NoOfAppSpecSrlg=None, NoOfTeProfile=None, SrlgCount=None, StackedLayers=None):
        """Adds a new isisL3 resource on the server and adds it to the container.

        Args
        ----
        - AdjSidCount (number): Adj SID Count
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAppSpecSrlg (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - NoOfTeProfile (number): Number of TE Profile
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved isisL3 resources using find and the newly added isisL3 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained isisL3 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdjSidCount=None, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, LocalSystemID=None, Multiplier=None, Name=None, NoOfAppSpecSrlg=None, NoOfTeProfile=None, SessionInfo=None, SessionStatus=None, SrlgCount=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves isisL3 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisL3 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisL3 resources from the server.

        Args
        ----
        - AdjSidCount (number): Adj SID Count
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalSystemID (list(str)): System ID
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAppSpecSrlg (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - NoOfTeProfile (number): Number of TE Profile
        - SessionInfo (list(str[ifaceSessInfoFsmNotStarted | ifaceSessInfoNotAllNbrInFull | iPAddressNotRcvd | none])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching isisL3 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisL3 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisL3 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AdjSID=None, AdvertiseLinkMsd=None, AuthType=None, AutoAdjustArea=None, AutoAdjustMTU=None, AutoAdjustSupportedProtocols=None, BFlag=None, CircuitTranmitPasswordOrMD5Key=None, ConfiguredHoldTime=None, DedicatedOnePlusOne=None, DedicatedOneToOne=None, Enable3WayHandshake=None, EnableAdjSID=None, EnableAppSpecSrlg=None, EnableBfdRegistration=None, EnableConfiguredHoldTime=None, EnableIPv6SID=None, EnableLinkProtection=None, EnableMT=None, EnableSRLG=None, Enhanced=None, ExtendedLocalCircuitId=None, ExtraTraffic=None, FFlag=None, Funcflags=None, Function=None, IncludeMaxSlMsd=None, IncludeMaximumEndDMsd=None, IncludeMaximumEndPopMsd=None, IncludeMaximumTEncapMsd=None, IncludeMaximumTInsertMsd=None, InterfaceMetric=None, Ipv6MTMetric=None, Ipv6SidValue=None, LFlag=None, Level1DeadInterval=None, Level1HelloInterval=None, Level1Priority=None, Level2DeadInterval=None, Level2HelloInterval=None, Level2Priority=None, LevelType=None, MaxEndDMsd=None, MaxEndPopMsd=None, MaxSlMsd=None, MaxTEncap=None, MaxTInsertMsd=None, NetworkType=None, OverrideFFlag=None, PFlag=None, Reserved0x40=None, Reserved0x80=None, SFlag=None, Shared=None, Srv6SidFlags=None, SuppressHello=None, Unprotected=None, VFlag=None, Weight=None):
        """Base class infrastructure that gets a list of isisL3 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdjSID (str): optional regex of adjSID
        - AdvertiseLinkMsd (str): optional regex of advertiseLinkMsd
        - AuthType (str): optional regex of authType
        - AutoAdjustArea (str): optional regex of autoAdjustArea
        - AutoAdjustMTU (str): optional regex of autoAdjustMTU
        - AutoAdjustSupportedProtocols (str): optional regex of autoAdjustSupportedProtocols
        - BFlag (str): optional regex of bFlag
        - CircuitTranmitPasswordOrMD5Key (str): optional regex of circuitTranmitPasswordOrMD5Key
        - ConfiguredHoldTime (str): optional regex of configuredHoldTime
        - DedicatedOnePlusOne (str): optional regex of dedicatedOnePlusOne
        - DedicatedOneToOne (str): optional regex of dedicatedOneToOne
        - Enable3WayHandshake (str): optional regex of enable3WayHandshake
        - EnableAdjSID (str): optional regex of enableAdjSID
        - EnableAppSpecSrlg (str): optional regex of enableAppSpecSrlg
        - EnableBfdRegistration (str): optional regex of enableBfdRegistration
        - EnableConfiguredHoldTime (str): optional regex of enableConfiguredHoldTime
        - EnableIPv6SID (str): optional regex of enableIPv6SID
        - EnableLinkProtection (str): optional regex of enableLinkProtection
        - EnableMT (str): optional regex of enableMT
        - EnableSRLG (str): optional regex of enableSRLG
        - Enhanced (str): optional regex of enhanced
        - ExtendedLocalCircuitId (str): optional regex of extendedLocalCircuitId
        - ExtraTraffic (str): optional regex of extraTraffic
        - FFlag (str): optional regex of fFlag
        - Funcflags (str): optional regex of funcflags
        - Function (str): optional regex of function
        - IncludeMaxSlMsd (str): optional regex of includeMaxSlMsd
        - IncludeMaximumEndDMsd (str): optional regex of includeMaximumEndDMsd
        - IncludeMaximumEndPopMsd (str): optional regex of includeMaximumEndPopMsd
        - IncludeMaximumTEncapMsd (str): optional regex of includeMaximumTEncapMsd
        - IncludeMaximumTInsertMsd (str): optional regex of includeMaximumTInsertMsd
        - InterfaceMetric (str): optional regex of interfaceMetric
        - Ipv6MTMetric (str): optional regex of ipv6MTMetric
        - Ipv6SidValue (str): optional regex of ipv6SidValue
        - LFlag (str): optional regex of lFlag
        - Level1DeadInterval (str): optional regex of level1DeadInterval
        - Level1HelloInterval (str): optional regex of level1HelloInterval
        - Level1Priority (str): optional regex of level1Priority
        - Level2DeadInterval (str): optional regex of level2DeadInterval
        - Level2HelloInterval (str): optional regex of level2HelloInterval
        - Level2Priority (str): optional regex of level2Priority
        - LevelType (str): optional regex of levelType
        - MaxEndDMsd (str): optional regex of maxEndDMsd
        - MaxEndPopMsd (str): optional regex of maxEndPopMsd
        - MaxSlMsd (str): optional regex of maxSlMsd
        - MaxTEncap (str): optional regex of maxTEncap
        - MaxTInsertMsd (str): optional regex of maxTInsertMsd
        - NetworkType (str): optional regex of networkType
        - OverrideFFlag (str): optional regex of overrideFFlag
        - PFlag (str): optional regex of pFlag
        - Reserved0x40 (str): optional regex of reserved0x40
        - Reserved0x80 (str): optional regex of reserved0x80
        - SFlag (str): optional regex of sFlag
        - Shared (str): optional regex of shared
        - Srv6SidFlags (str): optional regex of srv6SidFlags
        - SuppressHello (str): optional regex of suppressHello
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

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedInfo(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        clearAllLearnedInfo(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def ClearAllLearnedInfoInClient(self, *args, **kwargs):
        """Executes the clearAllLearnedInfoInClient operation on the server.

        Clear ALL the LSPs and Topologies learnt by this ISIS Router.

        clearAllLearnedInfoInClient(Arg2=list)list
        ------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfoInClient', payload=payload, response_object=None)

    def GetLearnedInfo(self, *args, **kwargs):
        """Executes the getLearnedInfo operation on the server.

        Get Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLearnedInfo(SessionIndices=list)
        -----------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getLearnedInfo(SessionIndices=string)
        -------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getLearnedInfo(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getLearnedInfo', payload=payload, response_object=None)

    def IsisStartInterface(self, *args, **kwargs):
        """Executes the isisStartInterface operation on the server.

        Start ISIS Interface

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        isisStartInterface(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        isisStartInterface(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('isisStartInterface', payload=payload, response_object=None)

    def IsisStopInterface(self, *args, **kwargs):
        """Executes the isisStopInterface operation on the server.

        Stop ISIS Interface

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        isisStopInterface(SessionIndices=list)
        --------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        isisStopInterface(SessionIndices=string)
        ----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('isisStopInterface', payload=payload, response_object=None)

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

    def ResumeHello(self, *args, **kwargs):
        """Executes the resumeHello operation on the server.

        Resume sending ISIS Hellos

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeHello(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        resumeHello(SessionIndices=string)
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
        return self._execute('resumeHello', payload=payload, response_object=None)

    def Resumehello(self, *args, **kwargs):
        """Executes the resumehello operation on the server.

        Starts the protocol state machine for the given protocol session instances.

        resumehello(Arg2=list)list
        --------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumehello', payload=payload, response_object=None)

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

    def StopHello(self, *args, **kwargs):
        """Executes the stopHello operation on the server.

        Stop sending ISIS Hellos

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopHello(SessionIndices=list)
        ------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopHello(SessionIndices=string)
        --------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopHello', payload=payload, response_object=None)

    def Stophello(self, *args, **kwargs):
        """Executes the stophello operation on the server.

        Stops the protocol state machine for the given protocol session instances.

        stophello(Arg2=list)list
        ------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stophello', payload=payload, response_object=None)
