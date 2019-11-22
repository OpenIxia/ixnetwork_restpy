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


class BondedGRE(Base):
    """
    The BondedGRE class encapsulates a list of bondedGRE resources that is be managed by the user.
    A list of resources can be retrieved from the server using the BondedGRE.find() method.
    The list can be managed by the user by using the BondedGRE.add() and BondedGRE.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bondedGRE'

    def __init__(self, parent):
        super(BondedGRE, self).__init__(parent)

    @property
    def Tag(self):
        """An instance of the Tag class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
        return Tag(self)

    @property
    def TlvProfile(self):
        """An instance of the TlvProfile class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile.TlvProfile)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile import TlvProfile
        return TlvProfile(self)

    @property
    def Active(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def BSessionInfo(self):
        """Current BondedGRE session state: Configured - The GRE session is in configured state. Unconfigured - The GRE session is in unconfigured state. Establishing - GRE Tunnel setup request message sent, waiting for Accept message from HAAP. Established - GRE Tunnel setup request has been accepted by the HAAP. Teared Down - The tunnel has been teared down by the HAAP. Denied (with error code) - GRE Tunnel setup request has been denied by the HAAP. Idle Hello - HG has entered in Idle Hello state. Active Hello - HG has entered in Active Hello state. Switching to Idle Hello - The tunnel is entering into Idle Hello state. Switching to Active Hello - The tunnel is entering into Active Hello state. Hello Paused - The tunnel has entered into Hello Paused state.

        Returns:
            list(str[activeHello|bondingTunnel|configured|denied|diagEnd|dSLFail|dSLTunnel|established|establishing|helloPaused|idleHello|lTEFail|lTETunnel|overflowedToLTETunnel|overflowingToLTETunnel|partiallyConfigured|switchedToDSLTunnel|switchingToActiveHello|switchingToDSLTunnel|switchingToIdleHello|tearedDown|unconfigured|waitForLTE])
        """
        return self._get_attribute('bSessionInfo')

    @property
    def BypassTraffic(self):
        """The Bypass Traffic Rate attribute is used to inform the HAAP of the downstream bypass bandwidth for the DSL WAN interface

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bypassTraffic')

    @property
    def ConnectedVia(self):
        """DEPRECATED List of layers this layer used to connect to the wire

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('connectedVia')
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute('connectedVia', value)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def DhcpIp(self):
        """The discovered IPv4 addresses.

        Returns:
            list(str)
        """
        return self._get_attribute('dhcpIp')

    @property
    def DslSyncRate(self):
        """DSL Synchronization Rate is used to notify the HAAP about the downstream bandwidth of the DSL link.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dslSyncRate')

    @property
    def ErrorCode(self):
        """The HAAP uses the Error Code attribute to inform the HG of the error code. It depicts why the GRE Tunnel Setup Request is denied. The list of codes is as follows: 0: No Error. 1: The HAAP was not reachable over LTE during the GRE Tunnel Setup Request. 2: The HAAP was not reachable via DSL during the GRE Tunnel Setup Request. 3: The LTE GRE tunnel to the HAAP failed. 4: The DSL GRE tunnel to the HAAP failed. 5: The given DSL User ID is not allowed to use the GRE Tunnel Bonding service. 6: The given User Alias / User ID (Globally Unique Identifier (GUID) is not allowed to use the GRE Tunnel Bonding service. 7: The LTE and DSL User IDs do not match. 8: The HAAP denied the GRE Tunnel Setup Request because a bonding session with the same User ID already exists. 9: The HAAP denied the GRE Tunnel Setup Request because the user's CIN is not permitted. 10: The HAAP terminated a GRE Tunnel Bonding session for maintenance reasons. 11: There was a communication error between the HAAP and the management system during the LTE GRE Tunnel Setup Request. 12: There was a communication error between the HAAP and the management system during the DSL GRE Tunnel Setup Request.

        Returns:
            list(number)
        """
        return self._get_attribute('errorCode')

    @property
    def Errors(self):
        """A list of errors that have occurred

        Returns:
            list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
        """
        return self._get_attribute('errors')

    @property
    def HomeGatewayInfo(self):
        """Current Home Gateway session state: Unconfigured - The HG is in unconfigured state. Configured - The HG is in configured state. Partially Configured - Only one tunnel (DSL/LTE) is configured in the HG. Diagnostic Start: Bonding Tunnel - HG has entered in diagnostic mode to test the performance of the entire bonding tunnel. Diagnostic Start: DSL Tunnel - HG has entered in diagnostic mode to test the performance of the DSL bonding tunnel. Diagnostic Start: LTE Tunnel - HG has entered in diagnostic mode to test the performance of the LTE tunnel. Diagnostic End - End of diagnostic operation. DSL Link Failure - DSL Link has failed. LTE Link Failure - LTE Link has failed. Switching to DSL Tunnel - HG uses this attribute to inform the HAAP to use the DSL GRE tunnel only. Switching to DSL Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Switching to DSL Tunnel sent by HG. Overflowing to LTE Tunnel - HG uses this attribute to inform the HAAP that the LTE GRE tunnel can be used again. Overflowing to LTE Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Overflowing to LTE Tunnel sent by HG.

        Returns:
            list(str[activeHello|bondingTunnel|configured|denied|diagEnd|dSLFail|dSLTunnel|established|establishing|helloPaused|idleHello|lTEFail|lTETunnel|overflowedToLTETunnel|overflowingToLTETunnel|partiallyConfigured|switchedToDSLTunnel|switchingToActiveHello|switchingToDSLTunnel|switchingToIdleHello|tearedDown|unconfigured|waitForLTE])
        """
        return self._get_attribute('homeGatewayInfo')

    @property
    def IdName(self):
        """This is a 40-byte string value(Allowed upto 80 bytes). It is used as the identification of the HG in the operator's network.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('idName')

    @property
    def Ipv6Prefix(self):
        """IPv6 Prefix Assigned to Host

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6Prefix')

    @property
    def Ipv6PrefixLen(self):
        """IPv6 Prefix length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6PrefixLen')

    @property
    def Multiplier(self):
        """Number of layer instances per parent instance (multiplier)

        Returns:
            number
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

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
    def SessionStatus(self):
        """Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

        Returns:
            list(str[down|notStarted|up])
        """
        return self._get_attribute('sessionStatus')

    @property
    def StackedLayers(self):
        """List of secondary (many to one) child layer protocols

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('stackedLayers')
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute('stackedLayers', value)

    @property
    def StateCounts(self):
        """A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

        Returns:
            dict(total:number,notStarted:number,down:number,up:number)
        """
        return self._get_attribute('stateCounts')

    @property
    def Status(self):
        """Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            str(configured|error|mixed|notStarted|started|starting|stopping)
        """
        return self._get_attribute('status')

    @property
    def TunnelGrp(self):
        """Displays the Mapping ID of the tunnel

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('tunnelGrp')

    @property
    def TunnelType(self):
        """Determines the Tunnel type to be used

        Returns:
            str(dsl|lte)
        """
        return self._get_attribute('tunnelType')
    @TunnelType.setter
    def TunnelType(self, value):
        self._set_attribute('tunnelType', value)

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None, TunnelType=None):
        """Updates a child instance of bondedGRE on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            TunnelType (str(dsl|lte)): Determines the Tunnel type to be used

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None, TunnelType=None):
        """Adds a new bondedGRE node on the server and retrieves it in this instance.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            TunnelType (str(dsl|lte)): Determines the Tunnel type to be used

        Returns:
            self: This instance with all currently retrieved bondedGRE data using find and the newly added bondedGRE data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the bondedGRE data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BSessionInfo=None, ConnectedVia=None, Count=None, DescriptiveName=None, DhcpIp=None, ErrorCode=None, Errors=None, HomeGatewayInfo=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, TunnelType=None):
        """Finds and retrieves bondedGRE data from the server.

        All named parameters support regex and can be used to selectively retrieve bondedGRE data from the server.
        By default the find method takes no parameters and will retrieve all bondedGRE data from the server.

        Args:
            BSessionInfo (list(str[activeHello|bondingTunnel|configured|denied|diagEnd|dSLFail|dSLTunnel|established|establishing|helloPaused|idleHello|lTEFail|lTETunnel|overflowedToLTETunnel|overflowingToLTETunnel|partiallyConfigured|switchedToDSLTunnel|switchingToActiveHello|switchingToDSLTunnel|switchingToIdleHello|tearedDown|unconfigured|waitForLTE])): Current BondedGRE session state: Configured - The GRE session is in configured state. Unconfigured - The GRE session is in unconfigured state. Establishing - GRE Tunnel setup request message sent, waiting for Accept message from HAAP. Established - GRE Tunnel setup request has been accepted by the HAAP. Teared Down - The tunnel has been teared down by the HAAP. Denied (with error code) - GRE Tunnel setup request has been denied by the HAAP. Idle Hello - HG has entered in Idle Hello state. Active Hello - HG has entered in Active Hello state. Switching to Idle Hello - The tunnel is entering into Idle Hello state. Switching to Active Hello - The tunnel is entering into Active Hello state. Hello Paused - The tunnel has entered into Hello Paused state.
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            DhcpIp (list(str)): The discovered IPv4 addresses.
            ErrorCode (list(number)): The HAAP uses the Error Code attribute to inform the HG of the error code. It depicts why the GRE Tunnel Setup Request is denied. The list of codes is as follows: 0: No Error. 1: The HAAP was not reachable over LTE during the GRE Tunnel Setup Request. 2: The HAAP was not reachable via DSL during the GRE Tunnel Setup Request. 3: The LTE GRE tunnel to the HAAP failed. 4: The DSL GRE tunnel to the HAAP failed. 5: The given DSL User ID is not allowed to use the GRE Tunnel Bonding service. 6: The given User Alias / User ID (Globally Unique Identifier (GUID) is not allowed to use the GRE Tunnel Bonding service. 7: The LTE and DSL User IDs do not match. 8: The HAAP denied the GRE Tunnel Setup Request because a bonding session with the same User ID already exists. 9: The HAAP denied the GRE Tunnel Setup Request because the user's CIN is not permitted. 10: The HAAP terminated a GRE Tunnel Bonding session for maintenance reasons. 11: There was a communication error between the HAAP and the management system during the LTE GRE Tunnel Setup Request. 12: There was a communication error between the HAAP and the management system during the DSL GRE Tunnel Setup Request.
            Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
            HomeGatewayInfo (list(str[activeHello|bondingTunnel|configured|denied|diagEnd|dSLFail|dSLTunnel|established|establishing|helloPaused|idleHello|lTEFail|lTETunnel|overflowedToLTETunnel|overflowingToLTETunnel|partiallyConfigured|switchedToDSLTunnel|switchingToActiveHello|switchingToDSLTunnel|switchingToIdleHello|tearedDown|unconfigured|waitForLTE])): Current Home Gateway session state: Unconfigured - The HG is in unconfigured state. Configured - The HG is in configured state. Partially Configured - Only one tunnel (DSL/LTE) is configured in the HG. Diagnostic Start: Bonding Tunnel - HG has entered in diagnostic mode to test the performance of the entire bonding tunnel. Diagnostic Start: DSL Tunnel - HG has entered in diagnostic mode to test the performance of the DSL bonding tunnel. Diagnostic Start: LTE Tunnel - HG has entered in diagnostic mode to test the performance of the LTE tunnel. Diagnostic End - End of diagnostic operation. DSL Link Failure - DSL Link has failed. LTE Link Failure - LTE Link has failed. Switching to DSL Tunnel - HG uses this attribute to inform the HAAP to use the DSL GRE tunnel only. Switching to DSL Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Switching to DSL Tunnel sent by HG. Overflowing to LTE Tunnel - HG uses this attribute to inform the HAAP that the LTE GRE tunnel can be used again. Overflowing to LTE Tunnel (Acknowledged) - HAAP has sent acknowledgment to the notification Overflowing to LTE Tunnel sent by HG.
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
            Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
            TunnelType (str(dsl|lte)): Determines the Tunnel type to be used

        Returns:
            self: This instance with matching bondedGRE data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of bondedGRE data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the bondedGRE data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, BypassTraffic=None, DslSyncRate=None, IdName=None, Ipv6Prefix=None, Ipv6PrefixLen=None, TunnelGrp=None):
        """Base class infrastructure that gets a list of bondedGRE device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Active (str): optional regex of active
            BypassTraffic (str): optional regex of bypassTraffic
            DslSyncRate (str): optional regex of dslSyncRate
            IdName (str): optional regex of idName
            Ipv6Prefix (str): optional regex of ipv6Prefix
            Ipv6PrefixLen (str): optional regex of ipv6PrefixLen
            TunnelGrp (str): optional regex of tunnelGrp

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def DiagBondingTunnel(self, *args, **kwargs):
        """Executes the diagBondingTunnel operation on the server.

        Sends a Bonding tunnel Diagnostic start message.

        diagBondingTunnel(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('diagBondingTunnel', payload=payload, response_object=None)

    def DiagDslTunnel(self, *args, **kwargs):
        """Executes the diagDslTunnel operation on the server.

        Sends a DSL tunnel Diagnostic start message.

        diagDslTunnel(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('diagDslTunnel', payload=payload, response_object=None)

    def DiagLteTunnel(self, *args, **kwargs):
        """Executes the diagLteTunnel operation on the server.

        Sends a LTE tunnel Diagnostic start message.

        diagLteTunnel(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('diagLteTunnel', payload=payload, response_object=None)

    def DslLinkFailure(self, *args, **kwargs):
        """Executes the dslLinkFailure operation on the server.

        Sends a Message for Emulating DSL Link Failure.

        dslLinkFailure(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dslLinkFailure', payload=payload, response_object=None)

    def EndDiag(self, *args, **kwargs):
        """Executes the endDiag operation on the server.

        Sends a End diagnostic message for the tunnel.

        endDiag(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('endDiag', payload=payload, response_object=None)

    def LteLinkFailure(self, *args, **kwargs):
        """Executes the lteLinkFailure operation on the server.

        Sends a Message for Emulating LTE Link Failure.

        lteLinkFailure(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('lteLinkFailure', payload=payload, response_object=None)

    def OverflowLte(self, *args, **kwargs):
        """Executes the overflowLte operation on the server.

        Sends a Message for Overflowing to LTE tunnel.

        overflowLte(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('overflowLte', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        restartDown()

        restartDown(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        restartDown(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Resumehello(self, *args, **kwargs):
        """Executes the resumehello operation on the server.

        Starts the protocol state machine for the given protocol session instances.

        resumehello(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each async action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumehello', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start selected protocols.

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

        Stop selected protocols.

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

    def Stophello(self, *args, **kwargs):
        """Executes the stophello operation on the server.

        Stops the protocol state machine for the given protocol session instances.

        stophello(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each async action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stophello', payload=payload, response_object=None)

    def SwitchDsl(self, *args, **kwargs):
        """Executes the switchDsl operation on the server.

        Sends a Message for switching to DSL tunnel.

        switchDsl(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('switchDsl', payload=payload, response_object=None)

    def Teardown(self, *args, **kwargs):
        """Executes the teardown operation on the server.

        Send Tear Down

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        teardown(Error_code:number)
            Args:
                args[0] is Error_code (number): This parameter requires a error_code of type kInteger

        teardown(Error_code:number, SessionIndices:list)
            Args:
                args[0] is Error_code (number): This parameter requires a error_code of type kInteger
                args[1] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        teardown(SessionIndices:string, Error_code:number)
            Args:
                args[0] is SessionIndices (str): This parameter requires a error_code of type kInteger
                args[1] is Error_code (number): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('teardown', payload=payload, response_object=None)

    def TearDown(self, *args, **kwargs):
        """Executes the tearDown operation on the server.

        Sends a Tear down message for the tunnel.

        tearDown(Arg2:list, Arg3:number)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
                args[1] is Arg3 (number): Error Code

            Returns:
                list(str): ID to associate each action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('tearDown', payload=payload, response_object=None)
