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


class Vxlanv6(Base):
    """VXLANv6 protocol.
    The Vxlanv6 class encapsulates a list of vxlanv6 resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Vxlanv6.find() method.
    The list can be managed by the user by using the Vxlanv6.add() and Vxlanv6.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vxlanv6'

    def __init__(self, parent):
        super(Vxlanv6, self).__init__(parent)

    @property
    def Connector(self):
        """An instance of the Connector class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
        return Connector(self)

    @property
    def Ethernet(self):
        """An instance of the Ethernet class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet.Ethernet)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet import Ethernet
        return Ethernet(self)

    @property
    def Ipv4Loopback(self):
        """An instance of the Ipv4Loopback class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback.Ipv4Loopback)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback import Ipv4Loopback
        return Ipv4Loopback(self)

    @property
    def Ipv6Loopback(self):
        """An instance of the Ipv6Loopback class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback.Ipv6Loopback)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback import Ipv6Loopback
        return Ipv6Loopback(self)

    @property
    def LdpBasicRouter(self):
        """An instance of the LdpBasicRouter class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter.LdpBasicRouter)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter import LdpBasicRouter
        return LdpBasicRouter(self)

    @property
    def LdpBasicRouterV6(self):
        """An instance of the LdpBasicRouterV6 class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6.LdpBasicRouterV6)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6 import LdpBasicRouterV6
        return LdpBasicRouterV6(self)

    @property
    def LdpTargetedRouter(self):
        """An instance of the LdpTargetedRouter class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter.LdpTargetedRouter)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter import LdpTargetedRouter
        return LdpTargetedRouter(self)

    @property
    def LdpTargetedRouterV6(self):
        """An instance of the LdpTargetedRouterV6 class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6.LdpTargetedRouterV6)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6 import LdpTargetedRouterV6
        return LdpTargetedRouterV6(self)

    @property
    def LearnedInfo(self):
        """An instance of the LearnedInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
        return LearnedInfo(self)

    @property
    def VxlanIPv6StaticInfo(self):
        """An instance of the VxlanIPv6StaticInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanipv6staticinfo.VxlanIPv6StaticInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanipv6staticinfo import VxlanIPv6StaticInfo
        return VxlanIPv6StaticInfo(self)._select()

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
    def EnableStaticInfo(self):
        """If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.

        Returns:
            bool
        """
        return self._get_attribute('enableStaticInfo')
    @EnableStaticInfo.setter
    def EnableStaticInfo(self, value):
        self._set_attribute('enableStaticInfo', value)

    @property
    def Errors(self):
        """A list of errors that have occurred

        Returns:
            list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
        """
        return self._get_attribute('errors')

    @property
    def Ipv6_multicast(self):
        """IPv6 Multicast Address.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6_multicast')

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
    def StaticInfoCount(self):
        """number of unicast VTEP

        Returns:
            number
        """
        return self._get_attribute('staticInfoCount')
    @StaticInfoCount.setter
    def StaticInfoCount(self, value):
        self._set_attribute('staticInfoCount', value)

    @property
    def Status(self):
        """Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            str(configured|error|mixed|notStarted|started|starting|stopping)
        """
        return self._get_attribute('status')

    @property
    def Vni(self):
        """VXLAN Network Identifier.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vni')

    def update(self, ConnectedVia=None, EnableStaticInfo=None, Multiplier=None, Name=None, StackedLayers=None, StaticInfoCount=None):
        """Updates a child instance of vxlanv6 on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            StaticInfoCount (number): number of unicast VTEP

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ConnectedVia=None, EnableStaticInfo=None, Multiplier=None, Name=None, StackedLayers=None, StaticInfoCount=None):
        """Adds a new vxlanv6 node on the server and retrieves it in this instance.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            StaticInfoCount (number): number of unicast VTEP

        Returns:
            self: This instance with all currently retrieved vxlanv6 data using find and the newly added vxlanv6 data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vxlanv6 data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EnableStaticInfo=None, Errors=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, StaticInfoCount=None, Status=None):
        """Finds and retrieves vxlanv6 data from the server.

        All named parameters support regex and can be used to selectively retrieve vxlanv6 data from the server.
        By default the find method takes no parameters and will retrieve all vxlanv6 data from the server.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
            Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
            StaticInfoCount (number): number of unicast VTEP
            Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            self: This instance with matching vxlanv6 data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vxlanv6 data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vxlanv6 data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Ipv6_multicast=None, Vni=None):
        """Base class infrastructure that gets a list of vxlanv6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Ipv6_multicast (str): optional regex of ipv6_multicast
            Vni (str): optional regex of vni

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clear All Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        clearAllLearnedInfo()

        clearAllLearnedInfo(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        clearAllLearnedInfo(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def ClearAllLearnedInfoInClient(self, *args, **kwargs):
        """Executes the clearAllLearnedInfoInClient operation on the server.

        Clears ALL info from GUI grid for the selected VXLAN interfaces.

        clearAllLearnedInfoInClient(Arg2:list)list
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
        return self._execute('clearAllLearnedInfoInClient', payload=payload, response_object=None)

    def GetVXLANLearnedInfo(self, *args, **kwargs):
        """Executes the getVXLANLearnedInfo operation on the server.

        Get Learned Info

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        getVXLANLearnedInfo()

        getVXLANLearnedInfo(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        getVXLANLearnedInfo(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        getVXLANLearnedInfo(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

            Returns:
                list(str): ID to associate each async action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getVXLANLearnedInfo', payload=payload, response_object=None)

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
