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


class Ospfv2(Base):
    """Ospf Interface level Configuration
    The Ospfv2 class encapsulates a list of ospfv2 resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ospfv2.find() method.
    The list can be managed by using the Ospfv2.add() and Ospfv2.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfv2'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdjSID': 'adjSID',
        'AreaId': 'areaId',
        'AreaIdIp': 'areaIdIp',
        'Authentication': 'authentication',
        'AuthenticationPassword': 'authenticationPassword',
        'BFlag': 'bFlag',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DeadInterval': 'deadInterval',
        'Dedicated1Plus1': 'dedicated1Plus1',
        'Dedicated1To1': 'dedicated1To1',
        'DemandCircuit': 'demandCircuit',
        'DescriptiveName': 'descriptiveName',
        'EnLinkProtection': 'enLinkProtection',
        'EnableAdjSID': 'enableAdjSID',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableFast2wayConvergence': 'enableFast2wayConvergence',
        'EnableFastHello': 'enableFastHello',
        'EnableSRLG': 'enableSRLG',
        'Enhanced': 'enhanced',
        'Errors': 'errors',
        'ExternalAttribute': 'externalAttribute',
        'ExternalCapability': 'externalCapability',
        'ExtraTraffic': 'extraTraffic',
        'HelloInterval': 'helloInterval',
        'HelloMultiplier': 'helloMultiplier',
        'LFlag': 'lFlag',
        'LocalRouterID': 'localRouterID',
        'MaxMtu': 'maxMtu',
        'Md5Key': 'md5Key',
        'Md5KeyId': 'md5KeyId',
        'Metric': 'metric',
        'MulticastCapability': 'multicastCapability',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NeighborIp': 'neighborIp',
        'NetworkType': 'networkType',
        'NssaCapability': 'nssaCapability',
        'OpaqueLsaForwarded': 'opaqueLsaForwarded',
        'OspfIfaceState': 'ospfIfaceState',
        'OspfNeighborState': 'ospfNeighborState',
        'PFlag': 'pFlag',
        'Priority': 'priority',
        'Reserved40': 'reserved40',
        'Reserved80': 'reserved80',
        'SFlag': 'sFlag',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'Shared': 'shared',
        'SrlgCount': 'srlgCount',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'SuppressHello': 'suppressHello',
        'TypeAreaId': 'typeAreaId',
        'TypeOfServiceRouting': 'typeOfServiceRouting',
        'Unprotected': 'unprotected',
        'Unused': 'unused',
        'VFlag': 'vFlag',
        'ValidateRxMtu': 'validateRxMtu',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(Ospfv2, self).__init__(parent)

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
    def OspfSRMappingServerList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrmappingserverlist_862027d65187e27ca0fba54bb0c8b3f4.OspfSRMappingServerList): An instance of the OspfSRMappingServerList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrmappingserverlist_862027d65187e27ca0fba54bb0c8b3f4 import OspfSRMappingServerList
        return OspfSRMappingServerList(self)._select()

    @property
    def OspfTrafficEngineering(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospftrafficengineering_d69348cf2c027c25fac7ced298f72f15.OspfTrafficEngineering): An instance of the OspfTrafficEngineering class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospftrafficengineering_d69348cf2c027c25fac7ced298f72f15 import OspfTrafficEngineering
        return OspfTrafficEngineering(self)._select()

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Adjacency SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdjSID']))

    @property
    def AreaId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): OSPF Area ID for a non-connected interface, displayed in Interger format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AreaId']))

    @property
    def AreaIdIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): OSPF Area ID for a non-connected interface, displayed in IP Address format
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AreaIdIp']))

    @property
    def Authentication(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authentication']))

    @property
    def AuthenticationPassword(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Authentication Password
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AuthenticationPassword']))

    @property
    def BFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFlag']))

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
    def DeadInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Dead Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DeadInterval']))

    @property
    def Dedicated1Plus1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dedicated1Plus1']))

    @property
    def Dedicated1To1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Dedicated1To1']))

    @property
    def DemandCircuit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 7
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DemandCircuit']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnLinkProtection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the link protection on the OSPF link between two mentioned interfaces.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnLinkProtection']))

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
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable BFD Registration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration']))

    @property
    def EnableFast2wayConvergence(self):
        """
        Returns
        -------
        - bool: Enable 2-way Adj Fast Convergence
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableFast2wayConvergence'])
    @EnableFast2wayConvergence.setter
    def EnableFast2wayConvergence(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableFast2wayConvergence'], value)

    @property
    def EnableFastHello(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Fast Hello
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFastHello']))

    @property
    def EnableSRLG(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This enables the SRLG on the OSPF link between two mentioned interfaces.
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
    def ExternalAttribute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 4
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExternalAttribute']))

    @property
    def ExternalCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExternalCapability']))

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
    def HelloInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hello Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HelloInterval']))

    @property
    def HelloMultiplier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Hello Multiplier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HelloMultiplier']))

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local/Global Flag
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
    def MaxMtu(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum trasmission unit, min=68, max=14000
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxMtu']))

    @property
    def Md5Key(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MD5 Key
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Md5Key']))

    @property
    def Md5KeyId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MD5 Key ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Md5KeyId']))

    @property
    def Metric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Routing Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metric']))

    @property
    def MulticastCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 2
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastCapability']))

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
    def NeighborIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Neighbor IP when connected network is Point to Multipoint
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NeighborIp']))

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
    def NssaCapability(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NssaCapability']))

    @property
    def OpaqueLsaForwarded(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OpaqueLsaForwarded']))

    @property
    def OspfIfaceState(self):
        """
        Returns
        -------
        - list(str[backup | down | dr | drOther | pointToPoint | unrecognized | waiting]): Logs additional information about the Interface State
        """
        return self._get_attribute(self._SDM_ATT_MAP['OspfIfaceState'])

    @property
    def OspfNeighborState(self):
        """
        Returns
        -------
        - list(str[attempt | down | exchange | exStart | full | init | loading | multiNeighbor | none | twoWay]): Logs additional information about the Neighbor State
        """
        return self._get_attribute(self._SDM_ATT_MAP['OspfNeighborState'])

    @property
    def PFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Persistent Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFlag']))

    @property
    def Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Priority (when DR/BDR)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    @property
    def Reserved40(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x40.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved40']))

    @property
    def Reserved80(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a Protection Scheme with value 0x80.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved80']))

    @property
    def SFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set/Group Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SFlag']))

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[ifaceSessInfoAllNbrIn2Way | ifaceSessInfoAllNbrInattempt | ifaceSessInfoAllNbrInDown | ifaceSessInfoAllNbrInExchange | ifaceSessInfoAllNbrInExStart | ifaceSessInfoAllNbrInInit | ifaceSessInfoAllNbrInLoading | ifaceSessInfoFsmNotStarted | ifaceSessInfoSameNbrId | iPAddressNotRcvd | none]): Logs additional information about the session state
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Suppress Hello for BGP-LS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SuppressHello']))

    @property
    def TypeAreaId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Area ID Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeAreaId']))

    @property
    def TypeOfServiceRouting(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 0
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeOfServiceRouting']))

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
    def Unused(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 7
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unused']))

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value/Index Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    @property
    def ValidateRxMtu(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Validate Received MTU
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ValidateRxMtu']))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Weight']))

    def update(self, ConnectedVia=None, EnableFast2wayConvergence=None, Multiplier=None, Name=None, SrlgCount=None, StackedLayers=None):
        """Updates ospfv2 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EnableFast2wayConvergence (bool): Enable 2-way Adj Fast Convergence
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EnableFast2wayConvergence=None, Multiplier=None, Name=None, SrlgCount=None, StackedLayers=None):
        """Adds a new ospfv2 resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - EnableFast2wayConvergence (bool): Enable 2-way Adj Fast Convergence
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved ospfv2 resources using find and the newly added ospfv2 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ospfv2 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EnableFast2wayConvergence=None, Errors=None, LocalRouterID=None, Multiplier=None, Name=None, OspfIfaceState=None, OspfNeighborState=None, SessionInfo=None, SessionStatus=None, SrlgCount=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves ospfv2 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfv2 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfv2 resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - EnableFast2wayConvergence (bool): Enable 2-way Adj Fast Convergence
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalRouterID (list(str)): Router ID
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OspfIfaceState (list(str[backup | down | dr | drOther | pointToPoint | unrecognized | waiting])): Logs additional information about the Interface State
        - OspfNeighborState (list(str[attempt | down | exchange | exStart | full | init | loading | multiNeighbor | none | twoWay])): Logs additional information about the Neighbor State
        - SessionInfo (list(str[ifaceSessInfoAllNbrIn2Way | ifaceSessInfoAllNbrInattempt | ifaceSessInfoAllNbrInDown | ifaceSessInfoAllNbrInExchange | ifaceSessInfoAllNbrInExStart | ifaceSessInfoAllNbrInInit | ifaceSessInfoAllNbrInLoading | ifaceSessInfoFsmNotStarted | ifaceSessInfoSameNbrId | iPAddressNotRcvd | none])): Logs additional information about the session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ospfv2 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfv2 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfv2 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AdjSID=None, AreaId=None, AreaIdIp=None, Authentication=None, AuthenticationPassword=None, BFlag=None, DeadInterval=None, Dedicated1Plus1=None, Dedicated1To1=None, DemandCircuit=None, EnLinkProtection=None, EnableAdjSID=None, EnableBfdRegistration=None, EnableFastHello=None, EnableSRLG=None, Enhanced=None, ExternalAttribute=None, ExternalCapability=None, ExtraTraffic=None, HelloInterval=None, HelloMultiplier=None, LFlag=None, MaxMtu=None, Md5Key=None, Md5KeyId=None, Metric=None, MulticastCapability=None, NeighborIp=None, NetworkType=None, NssaCapability=None, OpaqueLsaForwarded=None, PFlag=None, Priority=None, Reserved40=None, Reserved80=None, SFlag=None, Shared=None, SuppressHello=None, TypeAreaId=None, TypeOfServiceRouting=None, Unprotected=None, Unused=None, VFlag=None, ValidateRxMtu=None, Weight=None):
        """Base class infrastructure that gets a list of ospfv2 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdjSID (str): optional regex of adjSID
        - AreaId (str): optional regex of areaId
        - AreaIdIp (str): optional regex of areaIdIp
        - Authentication (str): optional regex of authentication
        - AuthenticationPassword (str): optional regex of authenticationPassword
        - BFlag (str): optional regex of bFlag
        - DeadInterval (str): optional regex of deadInterval
        - Dedicated1Plus1 (str): optional regex of dedicated1Plus1
        - Dedicated1To1 (str): optional regex of dedicated1To1
        - DemandCircuit (str): optional regex of demandCircuit
        - EnLinkProtection (str): optional regex of enLinkProtection
        - EnableAdjSID (str): optional regex of enableAdjSID
        - EnableBfdRegistration (str): optional regex of enableBfdRegistration
        - EnableFastHello (str): optional regex of enableFastHello
        - EnableSRLG (str): optional regex of enableSRLG
        - Enhanced (str): optional regex of enhanced
        - ExternalAttribute (str): optional regex of externalAttribute
        - ExternalCapability (str): optional regex of externalCapability
        - ExtraTraffic (str): optional regex of extraTraffic
        - HelloInterval (str): optional regex of helloInterval
        - HelloMultiplier (str): optional regex of helloMultiplier
        - LFlag (str): optional regex of lFlag
        - MaxMtu (str): optional regex of maxMtu
        - Md5Key (str): optional regex of md5Key
        - Md5KeyId (str): optional regex of md5KeyId
        - Metric (str): optional regex of metric
        - MulticastCapability (str): optional regex of multicastCapability
        - NeighborIp (str): optional regex of neighborIp
        - NetworkType (str): optional regex of networkType
        - NssaCapability (str): optional regex of nssaCapability
        - OpaqueLsaForwarded (str): optional regex of opaqueLsaForwarded
        - PFlag (str): optional regex of pFlag
        - Priority (str): optional regex of priority
        - Reserved40 (str): optional regex of reserved40
        - Reserved80 (str): optional regex of reserved80
        - SFlag (str): optional regex of sFlag
        - Shared (str): optional regex of shared
        - SuppressHello (str): optional regex of suppressHello
        - TypeAreaId (str): optional regex of typeAreaId
        - TypeOfServiceRouting (str): optional regex of typeOfServiceRouting
        - Unprotected (str): optional regex of unprotected
        - Unused (str): optional regex of unused
        - VFlag (str): optional regex of vFlag
        - ValidateRxMtu (str): optional regex of validateRxMtu
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

        Clears ALL routes from GUI grid for the selected OSPF router.

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

    def GetBasicLearnedInfo(self, *args, **kwargs):
        """Executes the getBasicLearnedInfo operation on the server.

        Get Basic Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getBasicLearnedInfo(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getBasicLearnedInfo(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getBasicLearnedInfo(Arg2=list)list
        ----------------------------------
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
        return self._execute('getBasicLearnedInfo', payload=payload, response_object=None)

    def GetDetailedLearnedInfo(self, *args, **kwargs):
        """Executes the getDetailedLearnedInfo operation on the server.

        Get Detailed Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getDetailedLearnedInfo(SessionIndices=list)
        -------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        getDetailedLearnedInfo(SessionIndices=string)
        ---------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getDetailedLearnedInfo', payload=payload, response_object=None)

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

        Resume sending OSPFv2 Hellos

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

        Stop sending OSPFv2 Hellos

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
