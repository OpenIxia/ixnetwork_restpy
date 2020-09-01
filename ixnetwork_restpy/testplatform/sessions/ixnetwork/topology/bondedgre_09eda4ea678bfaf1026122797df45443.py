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


class BondedGRE(Base):
    """
    The BondedGRE class encapsulates a list of bondedGRE resources that are managed by the user.
    A list of resources can be retrieved from the server using the BondedGRE.find() method.
    The list can be managed by using the BondedGRE.add() and BondedGRE.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bondedGRE'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'BSessionInfo': 'bSessionInfo',
        'BypassTraffic': 'bypassTraffic',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DhcpIp': 'dhcpIp',
        'DslSyncRate': 'dslSyncRate',
        'ErrorCode': 'errorCode',
        'Errors': 'errors',
        'HomeGatewayInfo': 'homeGatewayInfo',
        'IdName': 'idName',
        'Ipv6Prefix': 'ipv6Prefix',
        'Ipv6PrefixLen': 'ipv6PrefixLen',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TunnelGrp': 'tunnelGrp',
        'TunnelType': 'tunnelType',
    }

    def __init__(self, parent):
        super(BondedGRE, self).__init__(parent)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def TlvProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c.TlvProfile): An instance of the TlvProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile_69db000d3ef3b060f5edc387b878736c import TlvProfile
        return TlvProfile(self)

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
    def BSessionInfo(self):
        """
        Returns
        -------
        - list(str[activeHello | bondingTunnel | configured | denied | diagEnd | dSLFail | dSLTunnel | established | establishing | helloPaused | idleHello | lTEFail | lTETunnel | overflowedToLTETunnel | overflowingToLTETunnel | partiallyConfigured | switchedToDSLTunnel | switchingToActiveHello | switchingToDSLTunnel | switchingToIdleHello | tearedDown | unconfigured | waitForLTE]): Current BondedGRE session state: Configured - The GRE session is in configured state. Unconfigured - The GRE session is in unconfigured state. Establishing - GRE Tunnel setup request message sent, waiting for Accept message from HAAP. Established - GRE Tunnel setup request has been accepted by the HAAP. Teared Down - The tunnel has been teared down by the HAAP. Denied (with error code) - GRE Tunnel setup request has been denied by the HAAP. Idle Hello - HG has entered in Idle Hello state. Active Hello - HG has entered in Active Hello state. Switching to Idle Hello - The tunnel is entering into Idle Hello state. Switching to Active Hello - The tunnel is entering into Active Hello state. Hello Paused - The tunnel has entered into Hello Paused state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BSessionInfo'])

    @property
    def BypassTraffic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Bypass Traffic Rate attribute is used to inform the HAAP of the downstream bypass bandwidth for the DSL WAN interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BypassTraffic']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
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
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DhcpIp(self):
        """
        Returns
        -------
        - list(str): The discovered IPv4 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DhcpIp'])

    @property
    def DslSyncRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): DSL Synchronization Rate is used to notify the HAAP about the downstream bandwidth of the DSL link.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DslSyncRate']))

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - list(number): The HAAP uses the Error Code attribute to inform the HG of the error code. It depicts why the GRE Tunnel Setup Request is denied. The list of codes is as follows: 0: No Error. 1: The HAAP was not reachable over LTE during the GRE Tunnel Setup Request. 2: The HAAP was not reachable via DSL during the GRE Tunnel Setup Request. 3: The LTE GRE tunnel to the HAAP failed. 4: The DSL GRE tunnel to the HAAP failed. 5: The given DSL User ID is not allowed to use the GRE Tunnel Bonding service. 6: The given User Alias / User ID (Globally Unique Identifier (GUID) is not allowed to use the GRE Tunnel Bonding service. 7: The LTE and DSL User IDs do not match. 8: The HAAP denied the GRE Tunnel Setup Request because a bonding session with the same User ID already exists. 9: The HAAP denied the GRE Tunnel Setup Request because the user's CIN is not permitted. 10: The HAAP terminated a GRE Tunnel Bonding session for maintenance reasons. 11: There was a communication error between the HAAP and the management system during the LTE GRE Tunnel Setup Request. 12: There was a communication error between the HAAP and the management system during the DSL GRE Tunnel Setup Request.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorCode'])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def HomeGatewayInfo(self):
        """
        Returns
        -------
        - list(str[activeHello | bondingTunnel | configured | denied | diagEnd | dSLFail | dSLTunnel | established | establishing | helloPaused | idleHello | lTEFail | lTETunnel | overflowedToLTETunnel | overflowingToLTETunnel | partiallyConfigured | switchedToDSLTunnel | switchingToActiveHello | switchingToDSLTunnel | switchingToIdleHello | tearedDown | unconfigured | waitForLTE]): Current Home Gateway session state: Unconfigured - The HG is in unconfigured state. Configured - The HG is in configured state. Partially Configured - Only one tunnel (DSL/LTE) is configured in the HG. Diagnostic Start: Bonding Tunnel - HG has entered in diagnostic mode to test the performance of the entire bonding tunnel. Diagnostic Start: DSL Tunnel - HG has entered in diagnostic mode to test the performance of the DSL bonding tunnel. Diagnostic Start: LTE Tunnel - HG has entered in diagnostic mode to test the performance of the LTE tunnel. Diagnostic End - End of diagnostic operation. DSL Link Failure - DSL Link has failed. LTE Link Failure - LTE Link has failed. Switching to DSL Tunnel - HG uses this attribute to inform the HAAP to use the DSL GRE tunnel only. Switching to DSL Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Switching to DSL Tunnel sent by HG. Overflowing to LTE Tunnel - HG uses this attribute to inform the HAAP that the LTE GRE tunnel can be used again. Overflowing to LTE Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Overflowing to LTE Tunnel sent by HG.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HomeGatewayInfo'])

    @property
    def IdName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a 40-byte string value(Allowed upto 80 bytes). It is used as the identification of the HG in the operator's network.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IdName']))

    @property
    def Ipv6Prefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Prefix Assigned to Host
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6Prefix']))

    @property
    def Ipv6PrefixLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Prefix length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6PrefixLen']))

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
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

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
    def TunnelGrp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Displays the Mapping ID of the tunnel
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TunnelGrp']))

    @property
    def TunnelType(self):
        """
        Returns
        -------
        - str(dsl | lte): Determines the Tunnel type to be used
        """
        return self._get_attribute(self._SDM_ATT_MAP['TunnelType'])
    @TunnelType.setter
    def TunnelType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TunnelType'], value)

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None, TunnelType=None):
        """Updates bondedGRE resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TunnelType (str(dsl | lte)): Determines the Tunnel type to be used

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None, TunnelType=None):
        """Adds a new bondedGRE resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - TunnelType (str(dsl | lte)): Determines the Tunnel type to be used

        Returns
        -------
        - self: This instance with all currently retrieved bondedGRE resources using find and the newly added bondedGRE resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bondedGRE resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BSessionInfo=None, ConnectedVia=None, Count=None, DescriptiveName=None, DhcpIp=None, ErrorCode=None, Errors=None, HomeGatewayInfo=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, TunnelType=None):
        """Finds and retrieves bondedGRE resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bondedGRE resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bondedGRE resources from the server.

        Args
        ----
        - BSessionInfo (list(str[activeHello | bondingTunnel | configured | denied | diagEnd | dSLFail | dSLTunnel | established | establishing | helloPaused | idleHello | lTEFail | lTETunnel | overflowedToLTETunnel | overflowingToLTETunnel | partiallyConfigured | switchedToDSLTunnel | switchingToActiveHello | switchingToDSLTunnel | switchingToIdleHello | tearedDown | unconfigured | waitForLTE])): Current BondedGRE session state: Configured - The GRE session is in configured state. Unconfigured - The GRE session is in unconfigured state. Establishing - GRE Tunnel setup request message sent, waiting for Accept message from HAAP. Established - GRE Tunnel setup request has been accepted by the HAAP. Teared Down - The tunnel has been teared down by the HAAP. Denied (with error code) - GRE Tunnel setup request has been denied by the HAAP. Idle Hello - HG has entered in Idle Hello state. Active Hello - HG has entered in Active Hello state. Switching to Idle Hello - The tunnel is entering into Idle Hello state. Switching to Active Hello - The tunnel is entering into Active Hello state. Hello Paused - The tunnel has entered into Hello Paused state.
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DhcpIp (list(str)): The discovered IPv4 addresses.
        - ErrorCode (list(number)): The HAAP uses the Error Code attribute to inform the HG of the error code. It depicts why the GRE Tunnel Setup Request is denied. The list of codes is as follows: 0: No Error. 1: The HAAP was not reachable over LTE during the GRE Tunnel Setup Request. 2: The HAAP was not reachable via DSL during the GRE Tunnel Setup Request. 3: The LTE GRE tunnel to the HAAP failed. 4: The DSL GRE tunnel to the HAAP failed. 5: The given DSL User ID is not allowed to use the GRE Tunnel Bonding service. 6: The given User Alias / User ID (Globally Unique Identifier (GUID) is not allowed to use the GRE Tunnel Bonding service. 7: The LTE and DSL User IDs do not match. 8: The HAAP denied the GRE Tunnel Setup Request because a bonding session with the same User ID already exists. 9: The HAAP denied the GRE Tunnel Setup Request because the user's CIN is not permitted. 10: The HAAP terminated a GRE Tunnel Bonding session for maintenance reasons. 11: There was a communication error between the HAAP and the management system during the LTE GRE Tunnel Setup Request. 12: There was a communication error between the HAAP and the management system during the DSL GRE Tunnel Setup Request.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - HomeGatewayInfo (list(str[activeHello | bondingTunnel | configured | denied | diagEnd | dSLFail | dSLTunnel | established | establishing | helloPaused | idleHello | lTEFail | lTETunnel | overflowedToLTETunnel | overflowingToLTETunnel | partiallyConfigured | switchedToDSLTunnel | switchingToActiveHello | switchingToDSLTunnel | switchingToIdleHello | tearedDown | unconfigured | waitForLTE])): Current Home Gateway session state: Unconfigured - The HG is in unconfigured state. Configured - The HG is in configured state. Partially Configured - Only one tunnel (DSL/LTE) is configured in the HG. Diagnostic Start: Bonding Tunnel - HG has entered in diagnostic mode to test the performance of the entire bonding tunnel. Diagnostic Start: DSL Tunnel - HG has entered in diagnostic mode to test the performance of the DSL bonding tunnel. Diagnostic Start: LTE Tunnel - HG has entered in diagnostic mode to test the performance of the LTE tunnel. Diagnostic End - End of diagnostic operation. DSL Link Failure - DSL Link has failed. LTE Link Failure - LTE Link has failed. Switching to DSL Tunnel - HG uses this attribute to inform the HAAP to use the DSL GRE tunnel only. Switching to DSL Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Switching to DSL Tunnel sent by HG. Overflowing to LTE Tunnel - HG uses this attribute to inform the HAAP that the LTE GRE tunnel can be used again. Overflowing to LTE Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Overflowing to LTE Tunnel sent by HG.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TunnelType (str(dsl | lte)): Determines the Tunnel type to be used

        Returns
        -------
        - self: This instance with matching bondedGRE resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bondedGRE data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bondedGRE resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, BypassTraffic=None, DslSyncRate=None, IdName=None, Ipv6Prefix=None, Ipv6PrefixLen=None, TunnelGrp=None):
        """Base class infrastructure that gets a list of bondedGRE device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BypassTraffic (str): optional regex of bypassTraffic
        - DslSyncRate (str): optional regex of dslSyncRate
        - IdName (str): optional regex of idName
        - Ipv6Prefix (str): optional regex of ipv6Prefix
        - Ipv6PrefixLen (str): optional regex of ipv6PrefixLen
        - TunnelGrp (str): optional regex of tunnelGrp

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

    def DiagBondingTunnel(self, *args, **kwargs):
        """Executes the diagBondingTunnel operation on the server.

        Sends a Bonding tunnel Diagnostic start message.

        diagBondingTunnel(Arg2=list)list
        --------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('diagBondingTunnel', payload=payload, response_object=None)

    def DiagDslTunnel(self, *args, **kwargs):
        """Executes the diagDslTunnel operation on the server.

        Sends a DSL tunnel Diagnostic start message.

        diagDslTunnel(Arg2=list)list
        ----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('diagDslTunnel', payload=payload, response_object=None)

    def DiagLteTunnel(self, *args, **kwargs):
        """Executes the diagLteTunnel operation on the server.

        Sends a LTE tunnel Diagnostic start message.

        diagLteTunnel(Arg2=list)list
        ----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('diagLteTunnel', payload=payload, response_object=None)

    def DslLinkFailure(self, *args, **kwargs):
        """Executes the dslLinkFailure operation on the server.

        Sends a Message for Emulating DSL Link Failure.

        dslLinkFailure(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dslLinkFailure', payload=payload, response_object=None)

    def EndDiag(self, *args, **kwargs):
        """Executes the endDiag operation on the server.

        Sends a End diagnostic message for the tunnel.

        endDiag(Arg2=list)list
        ----------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('endDiag', payload=payload, response_object=None)

    def LteLinkFailure(self, *args, **kwargs):
        """Executes the lteLinkFailure operation on the server.

        Sends a Message for Emulating LTE Link Failure.

        lteLinkFailure(Arg2=list)list
        -----------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('lteLinkFailure', payload=payload, response_object=None)

    def OverflowLte(self, *args, **kwargs):
        """Executes the overflowLte operation on the server.

        Sends a Message for Overflowing to LTE tunnel.

        overflowLte(Arg2=list)list
        --------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('overflowLte', payload=payload, response_object=None)

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

    def SwitchDsl(self, *args, **kwargs):
        """Executes the switchDsl operation on the server.

        Sends a Message for switching to DSL tunnel.

        switchDsl(Arg2=list)list
        ------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('switchDsl', payload=payload, response_object=None)

    def Teardown(self, *args, **kwargs):
        """Executes the teardown operation on the server.

        Send Tear Down

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        teardown(Error_code=number)
        ---------------------------
        - Error_code (number): This parameter requires a error_code of type kInteger

        teardown(Error_code=number, SessionIndices=list)
        ------------------------------------------------
        - Error_code (number): This parameter requires a error_code of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        teardown(SessionIndices=string, Error_code=number)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a error_code of type kInteger
        - Error_code (number): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('teardown', payload=payload, response_object=None)

    def TearDown(self, *args, **kwargs):
        """Executes the tearDown operation on the server.

        Sends a Tear down message for the tunnel.

        tearDown(Arg2=list, Arg3=number)list
        ------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (number): Error Code
        - Returns list(str): ID to associate each action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('tearDown', payload=payload, response_object=None)
