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
from typing import List, Any, Union


class LdpTargetedRouterV6(Base):
    """LDPv6 Targeted Router Configuration
    The LdpTargetedRouterV6 class encapsulates a list of ldpTargetedRouterV6 resources that are managed by the user.
    A list of resources can be retrieved from the server using the LdpTargetedRouterV6.find() method.
    The list can be managed by using the LdpTargetedRouterV6.add() and LdpTargetedRouterV6.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ldpTargetedRouterV6'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BfdOpeMode': 'bfdOpeMode',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableBfdMplsLearnedLsp': 'enableBfdMplsLearnedLsp',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableFec128Advertisement': 'enableFec128Advertisement',
        'EnableFec129Advertisement': 'enableFec129Advertisement',
        'EnableGracefulRestart': 'enableGracefulRestart',
        'EnableIpv4Advertisement': 'enableIpv4Advertisement',
        'EnableIpv6Advertisement': 'enableIpv6Advertisement',
        'EnableLspPingLearnedLsp': 'enableLspPingLearnedLsp',
        'EnableP2MPCapability': 'enableP2MPCapability',
        'Errors': 'errors',
        'IgnoreStateAdvertisementControlCapability': 'ignoreStateAdvertisementControlCapability',
        'IncludeSac': 'includeSac',
        'Ipv6peerCount': 'ipv6peerCount',
        'KeepAliveHoldTime': 'keepAliveHoldTime',
        'KeepAliveInterval': 'keepAliveInterval',
        'LabelSpaceID': 'labelSpaceID',
        'LdpVersion': 'ldpVersion',
        'LeafRangesCountV6': 'leafRangesCountV6',
        'LocalRouterID': 'localRouterID',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'OperationMode': 'operationMode',
        'PeerCount': 'peerCount',
        'ReconnectTime': 'reconnectTime',
        'RecoveryTime': 'recoveryTime',
        'RootRangesCountV6': 'rootRangesCountV6',
        'SessionInfo': 'sessionInfo',
        'SessionPreference': 'sessionPreference',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
    }
    _SDM_ENUM_MAP = {
        'ldpVersion': ['version1', 'version2'],
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(LdpTargetedRouterV6, self).__init__(parent, list_op)

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
        if self._properties.get('Connector', None) is not None:
            return self._properties.get('Connector')
        else:
            return Connector(self)

    @property
    def LdpLeafRangeV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpleafrangev6_3dad6635b6afcf8ce78906311e26bfe0.LdpLeafRangeV6): An instance of the LdpLeafRangeV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpleafrangev6_3dad6635b6afcf8ce78906311e26bfe0 import LdpLeafRangeV6
        if self._properties.get('LdpLeafRangeV6', None) is not None:
            return self._properties.get('LdpLeafRangeV6')
        else:
            return LdpLeafRangeV6(self)._select()

    @property
    def LdpRootRangeV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldprootrangev6_45885b6f21e934c88aa56da8381f4ec3.LdpRootRangeV6): An instance of the LdpRootRangeV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldprootrangev6_45885b6f21e934c88aa56da8381f4ec3 import LdpRootRangeV6
        if self._properties.get('LdpRootRangeV6', None) is not None:
            return self._properties.get('LdpRootRangeV6')
        else:
            return LdpRootRangeV6(self)._select()

    @property
    def LdpTargetedIpv6Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedipv6peer_cf8c841244e1f69d674a5c2fa9c4b473.LdpTargetedIpv6Peer): An instance of the LdpTargetedIpv6Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedipv6peer_cf8c841244e1f69d674a5c2fa9c4b473 import LdpTargetedIpv6Peer
        if self._properties.get('LdpTargetedIpv6Peer', None) is not None:
            return self._properties.get('LdpTargetedIpv6Peer')
        else:
            return LdpTargetedIpv6Peer(self)._select()

    @property
    def LdpTargetedPeer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedpeer_3f5aecf84abee4c45cfdedcf70163bfc.LdpTargetedPeer): An instance of the LdpTargetedPeer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedpeer_3f5aecf84abee4c45cfdedcf70163bfc import LdpTargetedPeer
        if self._properties.get('LdpTargetedPeer', None) is not None:
            return self._properties.get('LdpTargetedPeer')
        else:
            return LdpTargetedPeer(self)._select()

    @property
    def Ldpotherpws(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpotherpws_c7a119da3cff2b6dc1e78257b76d70b9.Ldpotherpws): An instance of the Ldpotherpws class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpotherpws_c7a119da3cff2b6dc1e78257b76d70b9 import Ldpotherpws
        if self._properties.get('Ldpotherpws', None) is not None:
            return self._properties.get('Ldpotherpws')
        else:
            return Ldpotherpws(self)

    @property
    def Ldppwvpls(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppwvpls_e691d6b250f877cef17952ec6e6b30b9.Ldppwvpls): An instance of the Ldppwvpls class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppwvpls_e691d6b250f877cef17952ec6e6b30b9 import Ldppwvpls
        if self._properties.get('Ldppwvpls', None) is not None:
            return self._properties.get('Ldppwvpls')
        else:
            return Ldppwvpls(self)

    @property
    def Ldpvplsbgpad(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpvplsbgpad_0f32fa32863dd9e13cd7e772a3fb8771.Ldpvplsbgpad): An instance of the Ldpvplsbgpad class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpvplsbgpad_0f32fa32863dd9e13cd7e772a3fb8771 import Ldpvplsbgpad
        if self._properties.get('Ldpvplsbgpad', None) is not None:
            return self._properties.get('Ldpvplsbgpad')
        else:
            return Ldpvplsbgpad(self)

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
        if self._properties.get('LearnedInfo', None) is not None:
            return self._properties.get('LearnedInfo')
        else:
            return LearnedInfo(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def BfdOpeMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BFD Operation Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BfdOpeMode']))

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableBfdMplsLearnedLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, BFD MPLS is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBfdMplsLearnedLsp']))

    @property
    def EnableBfdRegistration(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable BFD Registration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration']))

    @property
    def EnableFec128Advertisement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, FEC128 P2P-PW app type is enabled in SAC TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFec128Advertisement']))

    @property
    def EnableFec129Advertisement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, FEC129 P2P-PW app type is enabled in SAC TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFec129Advertisement']))

    @property
    def EnableGracefulRestart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestart']))

    @property
    def EnableIpv4Advertisement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIpv4Advertisement']))

    @property
    def EnableIpv6Advertisement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableIpv6Advertisement']))

    @property
    def EnableLspPingLearnedLsp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LSP Ping is enabled for learned LSPs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableLspPingLearnedLsp']))

    @property
    def EnableP2MPCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LDP Router is P2MP capable.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableP2MPCapability']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def IgnoreStateAdvertisementControlCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, LDP Router ignores SAC TLV it receives.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IgnoreStateAdvertisementControlCapability']))

    @property
    def IncludeSac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IncludeSac']))

    @property
    def Ipv6peerCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of ipv6 Target Peers configured for this LDP router
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6peerCount'])
    @Ipv6peerCount.setter
    def Ipv6peerCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Ipv6peerCount'], value)

    @property
    def KeepAliveHoldTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['KeepAliveHoldTime']))

    @property
    def KeepAliveInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['KeepAliveInterval']))

    @property
    def LabelSpaceID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identifies the set of labels that will be used. Part of the LDP Identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LabelSpaceID']))

    @property
    def LdpVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str(version1 | version2): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
        """
        return self._get_attribute(self._SDM_ATT_MAP['LdpVersion'])
    @LdpVersion.setter
    def LdpVersion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LdpVersion'], value)

    @property
    def LeafRangesCountV6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Leaf Ranges configured for this LDP router
        """
        return self._get_attribute(self._SDM_ATT_MAP['LeafRangesCountV6'])
    @LeafRangesCountV6.setter
    def LeafRangesCountV6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['LeafRangesCountV6'], value)

    @property
    def LocalRouterID(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterID'])

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def OperationMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of LDP Label Advertisement
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OperationMode']))

    @property
    def PeerCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Target Peers configured for this LDP router
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerCount'])
    @PeerCount.setter
    def PeerCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PeerCount'], value)

    @property
    def ReconnectTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reconnect Time ms
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReconnectTime']))

    @property
    def RecoveryTime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RecoveryTime']))

    @property
    def RootRangesCountV6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Root Ranges configured for this LDP router
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootRangesCountV6'])
    @RootRangesCountV6.setter
    def RootRangesCountV6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['RootRangesCountV6'], value)

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[lDP_STATE_INITIALIZED | lDP_STATE_MULTIPLE_PEERS | lDP_STATE_NON_EXISTENT | lDP_STATE_OPENREC | lDP_STATE_OPENSENT | lDP_STATE_OPERATIONAL | none]): Logs additional information about the LDP session state
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionPreference(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SessionPreference']))

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
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
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    def update(self, ConnectedVia=None, Ipv6peerCount=None, LdpVersion=None, LeafRangesCountV6=None, Multiplier=None, Name=None, PeerCount=None, RootRangesCountV6=None, StackedLayers=None):
        # type: (List[str], int, str, int, int, str, int, int, List[str]) -> LdpTargetedRouterV6
        """Updates ldpTargetedRouterV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
        - LdpVersion (str(version1 | version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
        - LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerCount (number): The number of Target Peers configured for this LDP router
        - RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Ipv6peerCount=None, LdpVersion=None, LeafRangesCountV6=None, Multiplier=None, Name=None, PeerCount=None, RootRangesCountV6=None, StackedLayers=None):
        # type: (List[str], int, str, int, int, str, int, int, List[str]) -> LdpTargetedRouterV6
        """Adds a new ldpTargetedRouterV6 resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
        - LdpVersion (str(version1 | version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
        - LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerCount (number): The number of Target Peers configured for this LDP router
        - RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved ldpTargetedRouterV6 resources using find and the newly added ldpTargetedRouterV6 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ldpTargetedRouterV6 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Ipv6peerCount=None, LdpVersion=None, LeafRangesCountV6=None, LocalRouterID=None, Multiplier=None, Name=None, PeerCount=None, RootRangesCountV6=None, SessionInfo=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves ldpTargetedRouterV6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ldpTargetedRouterV6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ldpTargetedRouterV6 resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
        - LdpVersion (str(version1 | version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
        - LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
        - LocalRouterID (list(str)): Router ID
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PeerCount (number): The number of Target Peers configured for this LDP router
        - RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
        - SessionInfo (list(str[lDP_STATE_INITIALIZED | lDP_STATE_MULTIPLE_PEERS | lDP_STATE_NON_EXISTENT | lDP_STATE_OPENREC | lDP_STATE_OPENSENT | lDP_STATE_OPERATIONAL | none])): Logs additional information about the LDP session state
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ldpTargetedRouterV6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ldpTargetedRouterV6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ldpTargetedRouterV6 resources from the server available through an iterator or index

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def ClearAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedInfo(async_operation=bool)
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedInfo(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedInfo(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearAllLearnedInfoInClient operation on the server.

        Clears ALL routes from GUI grid for the selected LDP Router.

        clearAllLearnedInfoInClient(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
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

    def GetAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getAllLearnedInfo operation on the server.

        Get All Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getAllLearnedInfo(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAllLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAllLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAllLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getAllLearnedInfo', payload=payload, response_object=None)

    def GetFEC128LearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getFEC128LearnedInfo operation on the server.

        Get FEC 128 Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getFEC128LearnedInfo(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getFEC128LearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getFEC128LearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getFEC128LearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getFEC128LearnedInfo', payload=payload, response_object=None)

    def GetFEC129LearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getFEC129LearnedInfo operation on the server.

        Get FEC 129 Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getFEC129LearnedInfo(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getFEC129LearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getFEC129LearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getFEC129LearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getFEC129LearnedInfo', payload=payload, response_object=None)

    def GetIPv4FECLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv4FECLearnedInfo operation on the server.

        Get IPv4 FEC Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv4FECLearnedInfo(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4FECLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4FECLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv4FECLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getIPv4FECLearnedInfo', payload=payload, response_object=None)

    def GetIPv6FECLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getIPv6FECLearnedInfo operation on the server.

        Get IPv6 FEC Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getIPv6FECLearnedInfo(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6FECLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6FECLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getIPv6FECLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getIPv6FECLearnedInfo', payload=payload, response_object=None)

    def GetP2MPFECLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getP2MPFECLearnedInfo operation on the server.

        Get P2MP FEC Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getP2MPFECLearnedInfo(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getP2MPFECLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getP2MPFECLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getP2MPFECLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getP2MPFECLearnedInfo', payload=payload, response_object=None)

    def GracefullyRestart(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the gracefullyRestart operation on the server.

        Gracefully Restart

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        gracefullyRestart(Delay=number, async_operation=bool)
        -----------------------------------------------------
        - Delay (number): This parameter requires a delay of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        gracefullyRestart(Delay=number, SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------
        - Delay (number): This parameter requires a delay of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        gracefullyRestart(SessionIndices=string, Delay=number, async_operation=bool)
        ----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a delay of type kInteger
        - Delay (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        gracefullyRestart(Arg2=list, Arg3=number, async_operation=bool)list
        -------------------------------------------------------------------
        - Arg2 (list(number)): Action indices for gracefully restart
        - Arg3 (number): Restart After Time (in secs)
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('gracefullyRestart', payload=payload, response_object=None)

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def ResumeKeepAlive(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the resumeKeepAlive operation on the server.

        Resume sending KeepAlive

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeKeepAlive(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeKeepAlive(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeKeepAlive(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumeKeepAlive', payload=payload, response_object=None)

    def Resumekeepalive(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumekeepalive operation on the server.

        Start Sending Keep Alive Messages.

        resumekeepalive(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumekeepalive', payload=payload, response_object=None)

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def StopKeepAlive(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopKeepAlive operation on the server.

        Stop sending KeepAlive

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopKeepAlive(async_operation=bool)
        -----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopKeepAlive(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopKeepAlive(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopKeepAlive', payload=payload, response_object=None)

    def Stopkeepalive(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopkeepalive operation on the server.

        Stop Sending Keep Alive Messages.

        stopkeepalive(Arg2=list, async_operation=bool)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopkeepalive', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, BfdOpeMode=None, EnableBfdMplsLearnedLsp=None, EnableBfdRegistration=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LabelSpaceID=None, OperationMode=None, ReconnectTime=None, RecoveryTime=None, SessionPreference=None):
        """Base class infrastructure that gets a list of ldpTargetedRouterV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BfdOpeMode (str): optional regex of bfdOpeMode
        - EnableBfdMplsLearnedLsp (str): optional regex of enableBfdMplsLearnedLsp
        - EnableBfdRegistration (str): optional regex of enableBfdRegistration
        - EnableFec128Advertisement (str): optional regex of enableFec128Advertisement
        - EnableFec129Advertisement (str): optional regex of enableFec129Advertisement
        - EnableGracefulRestart (str): optional regex of enableGracefulRestart
        - EnableIpv4Advertisement (str): optional regex of enableIpv4Advertisement
        - EnableIpv6Advertisement (str): optional regex of enableIpv6Advertisement
        - EnableLspPingLearnedLsp (str): optional regex of enableLspPingLearnedLsp
        - EnableP2MPCapability (str): optional regex of enableP2MPCapability
        - IgnoreStateAdvertisementControlCapability (str): optional regex of ignoreStateAdvertisementControlCapability
        - IncludeSac (str): optional regex of includeSac
        - KeepAliveHoldTime (str): optional regex of keepAliveHoldTime
        - KeepAliveInterval (str): optional regex of keepAliveInterval
        - LabelSpaceID (str): optional regex of labelSpaceID
        - OperationMode (str): optional regex of operationMode
        - ReconnectTime (str): optional regex of reconnectTime
        - RecoveryTime (str): optional regex of recoveryTime
        - SessionPreference (str): optional regex of sessionPreference

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
