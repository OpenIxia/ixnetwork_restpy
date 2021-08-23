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


class Vxlan(Base):
    """VXLAN protocol.
    The Vxlan class encapsulates a list of vxlan resources that are managed by the user.
    A list of resources can be retrieved from the server using the Vxlan.find() method.
    The list can be managed by using the Vxlan.add() and Vxlan.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vxlan'
    _SDM_ATT_MAP = {
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableStaticInfo': 'enableStaticInfo',
        'Errors': 'errors',
        'ExternalLearning': 'externalLearning',
        'Ipv4_multicast': 'ipv4_multicast',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'OvsdbConnectorMultiplier': 'ovsdbConnectorMultiplier',
        'RunningMode': 'runningMode',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'StaticInfoCount': 'staticInfoCount',
        'Status': 'status',
        'Vni': 'vni',
    }
    _SDM_ENUM_MAP = {
        'runningMode': ['none', 'ovsdbStack', 'ovsdbControllerBfdStack'],
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(Vxlan, self).__init__(parent, list_op)

    @property
    def Bfdv4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e.Bfdv4Interface): An instance of the Bfdv4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e import Bfdv4Interface
        if self._properties.get('Bfdv4Interface', None) is not None:
            return self._properties.get('Bfdv4Interface')
        else:
            return Bfdv4Interface(self)

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
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635 import Ethernet
        if self._properties.get('Ethernet', None) is not None:
            return self._properties.get('Ethernet')
        else:
            return Ethernet(self)

    @property
    def Ipv4Loopback(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback_f84286c6e2c90f5267670278dde3f258.Ipv4Loopback): An instance of the Ipv4Loopback class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback_f84286c6e2c90f5267670278dde3f258 import Ipv4Loopback
        if self._properties.get('Ipv4Loopback', None) is not None:
            return self._properties.get('Ipv4Loopback')
        else:
            return Ipv4Loopback(self)

    @property
    def Ipv6Loopback(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback_c5557054afff2b9cc84b7676de50b805.Ipv6Loopback): An instance of the Ipv6Loopback class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback_c5557054afff2b9cc84b7676de50b805 import Ipv6Loopback
        if self._properties.get('Ipv6Loopback', None) is not None:
            return self._properties.get('Ipv6Loopback')
        else:
            return Ipv6Loopback(self)

    @property
    def LdpBasicRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6.LdpBasicRouter): An instance of the LdpBasicRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6 import LdpBasicRouter
        if self._properties.get('LdpBasicRouter', None) is not None:
            return self._properties.get('LdpBasicRouter')
        else:
            return LdpBasicRouter(self)

    @property
    def LdpBasicRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c.LdpBasicRouterV6): An instance of the LdpBasicRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c import LdpBasicRouterV6
        if self._properties.get('LdpBasicRouterV6', None) is not None:
            return self._properties.get('LdpBasicRouterV6')
        else:
            return LdpBasicRouterV6(self)

    @property
    def LdpTargetedRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692.LdpTargetedRouter): An instance of the LdpTargetedRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692 import LdpTargetedRouter
        if self._properties.get('LdpTargetedRouter', None) is not None:
            return self._properties.get('LdpTargetedRouter')
        else:
            return LdpTargetedRouter(self)

    @property
    def LdpTargetedRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf.LdpTargetedRouterV6): An instance of the LdpTargetedRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf import LdpTargetedRouterV6
        if self._properties.get('LdpTargetedRouterV6', None) is not None:
            return self._properties.get('LdpTargetedRouterV6')
        else:
            return LdpTargetedRouterV6(self)

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
    def VxlanStaticInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanstaticinfo_6879422db4d58cf50c6662a6238ea2d4.VxlanStaticInfo): An instance of the VxlanStaticInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanstaticinfo_6879422db4d58cf50c6662a6238ea2d4 import VxlanStaticInfo
        if self._properties.get('VxlanStaticInfo', None) is not None:
            return self._properties.get('VxlanStaticInfo')
        else:
            return VxlanStaticInfo(self)._select()

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
    def EnableStaticInfo(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStaticInfo'])
    @EnableStaticInfo.setter
    def EnableStaticInfo(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableStaticInfo'], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def ExternalLearning(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, VXLAN will use information received from another protocol which will handle the learning mechanism.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExternalLearning'])
    @ExternalLearning.setter
    def ExternalLearning(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ExternalLearning'], value)

    @property
    def Ipv4_multicast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Multicast Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4_multicast']))

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
    def OvsdbConnectorMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Ovsdb to Vxlan multiplier, when part of OVSDB Server stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OvsdbConnectorMultiplier'])
    @OvsdbConnectorMultiplier.setter
    def OvsdbConnectorMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['OvsdbConnectorMultiplier'], value)

    @property
    def RunningMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | ovsdbStack | ovsdbControllerBfdStack): There will be different behaviours based on role (normal=0, ovsdb controller stack=1, bfd stack=2.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningMode'])
    @RunningMode.setter
    def RunningMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RunningMode'], value)

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
    def StaticInfoCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: number of unicast VTEP
        """
        return self._get_attribute(self._SDM_ATT_MAP['StaticInfoCount'])
    @StaticInfoCount.setter
    def StaticInfoCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['StaticInfoCount'], value)

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def Vni(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VXLAN Network Identifier.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vni']))

    def update(self, ConnectedVia=None, EnableStaticInfo=None, ExternalLearning=None, Multiplier=None, Name=None, OvsdbConnectorMultiplier=None, RunningMode=None, StackedLayers=None, StaticInfoCount=None):
        # type: (List[str], bool, bool, int, str, int, str, List[str], int) -> Vxlan
        """Updates vxlan resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
        - ExternalLearning (bool): If true, VXLAN will use information received from another protocol which will handle the learning mechanism.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OvsdbConnectorMultiplier (number): Ovsdb to Vxlan multiplier, when part of OVSDB Server stack.
        - RunningMode (str(none | ovsdbStack | ovsdbControllerBfdStack)): There will be different behaviours based on role (normal=0, ovsdb controller stack=1, bfd stack=2.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StaticInfoCount (number): number of unicast VTEP

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, EnableStaticInfo=None, ExternalLearning=None, Multiplier=None, Name=None, OvsdbConnectorMultiplier=None, RunningMode=None, StackedLayers=None, StaticInfoCount=None):
        # type: (List[str], bool, bool, int, str, int, str, List[str], int) -> Vxlan
        """Adds a new vxlan resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
        - ExternalLearning (bool): If true, VXLAN will use information received from another protocol which will handle the learning mechanism.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OvsdbConnectorMultiplier (number): Ovsdb to Vxlan multiplier, when part of OVSDB Server stack.
        - RunningMode (str(none | ovsdbStack | ovsdbControllerBfdStack)): There will be different behaviours based on role (normal=0, ovsdb controller stack=1, bfd stack=2.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StaticInfoCount (number): number of unicast VTEP

        Returns
        -------
        - self: This instance with all currently retrieved vxlan resources using find and the newly added vxlan resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vxlan resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EnableStaticInfo=None, Errors=None, ExternalLearning=None, Multiplier=None, Name=None, OvsdbConnectorMultiplier=None, RunningMode=None, SessionStatus=None, StackedLayers=None, StateCounts=None, StaticInfoCount=None, Status=None):
        """Finds and retrieves vxlan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vxlan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vxlan resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - ExternalLearning (bool): If true, VXLAN will use information received from another protocol which will handle the learning mechanism.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - OvsdbConnectorMultiplier (number): Ovsdb to Vxlan multiplier, when part of OVSDB Server stack.
        - RunningMode (str(none | ovsdbStack | ovsdbControllerBfdStack)): There will be different behaviours based on role (normal=0, ovsdb controller stack=1, bfd stack=2.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - StaticInfoCount (number): number of unicast VTEP
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching vxlan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vxlan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vxlan resources from the server available through an iterator or index

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

        Clears ALL info from GUI grid for the selected VXLAN interfaces.

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

    def GetVXLANLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getVXLANLearnedInfo operation on the server.

        Get Learned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getVXLANLearnedInfo(async_operation=bool)
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getVXLANLearnedInfo(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getVXLANLearnedInfo(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getVXLANLearnedInfo(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
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
        return self._execute('getVXLANLearnedInfo', payload=payload, response_object=None)

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

    def get_device_ids(self, PortNames=None, Ipv4_multicast=None, Vni=None):
        """Base class infrastructure that gets a list of vxlan device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Ipv4_multicast (str): optional regex of ipv4_multicast
        - Vni (str): optional regex of vni

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
