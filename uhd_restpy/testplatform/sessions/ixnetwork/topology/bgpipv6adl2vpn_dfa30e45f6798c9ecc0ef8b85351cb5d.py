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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class BgpIpv6AdL2Vpn(Base):
    """BGP AD-L2VPN Configuration
    The BgpIpv6AdL2Vpn class encapsulates a list of bgpIpv6AdL2Vpn resources that are managed by the user.
    A list of resources can be retrieved from the server using the BgpIpv6AdL2Vpn.find() method.
    The list can be managed by using the BgpIpv6AdL2Vpn.add() and BgpIpv6AdL2Vpn.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpIpv6AdL2Vpn'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AsNumberVplsId': 'asNumberVplsId',
        'AsNumberVplsRd': 'asNumberVplsRd',
        'AsNumberVplsRt': 'asNumberVplsRt',
        'AssignedNumberVplsId': 'assignedNumberVplsId',
        'AssignedNumberVplsRd': 'assignedNumberVplsRd',
        'AssignedNumberVplsRt': 'assignedNumberVplsRt',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'DutIpv6': 'dutIpv6',
        'Errors': 'errors',
        'ImportRDAsRT': 'importRDAsRT',
        'ImportVplsIdAsRd': 'importVplsIdAsRd',
        'IpAddressVplsId': 'ipAddressVplsId',
        'IpAddressVplsRd': 'ipAddressVplsRd',
        'IpAddressVplsRt': 'ipAddressVplsRt',
        'LocalIpv6': 'localIpv6',
        'LocalRouterID': 'localRouterID',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumberVsiId': 'numberVsiId',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TypeVplsId': 'typeVplsId',
        'TypeVplsRd': 'typeVplsRd',
        'TypeVplsRt': 'typeVplsRt',
        'TypeVsiId': 'typeVsiId',
    }
    _SDM_ENUM_MAP = {
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(BgpIpv6AdL2Vpn, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AsNumberVplsId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VPLS ID AS Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumberVplsId']))

    @property
    def AsNumberVplsRd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Distinguisher AS Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumberVplsRd']))

    @property
    def AsNumberVplsRt(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Target AS Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AsNumberVplsRt']))

    @property
    def AssignedNumberVplsId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VPLS ID Assigned Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumberVplsId']))

    @property
    def AssignedNumberVplsRd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Distinguisher Assigned Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumberVplsRd']))

    @property
    def AssignedNumberVplsRt(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Target Assigned Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssignedNumberVplsRt']))

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
    def DutIpv6(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): DUT IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['DutIpv6'])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def ImportRDAsRT(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use RD As RT
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ImportRDAsRT']))

    @property
    def ImportVplsIdAsRd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use VPLS ID As Route Distinguisher
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ImportVplsIdAsRd']))

    @property
    def IpAddressVplsId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VPLS ID IP Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpAddressVplsId']))

    @property
    def IpAddressVplsRd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Distinguisher IP Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpAddressVplsRd']))

    @property
    def IpAddressVplsRt(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Route Target IP Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IpAddressVplsRt']))

    @property
    def LocalIpv6(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIpv6'])

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
    def NumberVsiId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VSI ID Number
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumberVsiId']))

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

    @property
    def TypeVplsId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VPLS ID Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeVplsId']))

    @property
    def TypeVplsRd(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RD Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeVplsRd']))

    @property
    def TypeVplsRt(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RT Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeVplsRt']))

    @property
    def TypeVsiId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): VSI ID
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeVsiId']))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        # type: (List[str], int, str, List[str]) -> BgpIpv6AdL2Vpn
        """Updates bgpIpv6AdL2Vpn resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        # type: (List[str], int, str, List[str]) -> BgpIpv6AdL2Vpn
        """Adds a new bgpIpv6AdL2Vpn resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved bgpIpv6AdL2Vpn resources using find and the newly added bgpIpv6AdL2Vpn resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained bgpIpv6AdL2Vpn resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, DutIpv6=None, Errors=None, LocalIpv6=None, LocalRouterID=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves bgpIpv6AdL2Vpn resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bgpIpv6AdL2Vpn resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bgpIpv6AdL2Vpn resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DutIpv6 (list(str)): DUT IP
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LocalIpv6 (list(str)): Local IP
        - LocalRouterID (list(str)): Router ID
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching bgpIpv6AdL2Vpn resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of bgpIpv6AdL2Vpn data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bgpIpv6AdL2Vpn resources from the server available through an iterator or index

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

    def ReadvertiseADVPLSRoute(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the readvertiseADVPLSRoute operation on the server.

        Re-advertise Aged out BGP Routes in a Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        readvertiseADVPLSRoute(async_operation=bool)
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseADVPLSRoute(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        readvertiseADVPLSRoute(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------------
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
        return self._execute('readvertiseADVPLSRoute', payload=payload, response_object=None)

    def Readvertiseadvplsroute(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the readvertiseadvplsroute operation on the server.

        Readvertise only the aged-out routes contained in this route range.

        readvertiseadvplsroute(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute('readvertiseadvplsroute', payload=payload, response_object=None)

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

    def WithdrawADVPLSRoute(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the withdrawADVPLSRoute operation on the server.

        Age out percentage of BGP Routes in a Route Range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        withdrawADVPLSRoute(async_operation=bool)
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawADVPLSRoute(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawADVPLSRoute(SessionIndices=string, async_operation=bool)
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
        return self._execute('withdrawADVPLSRoute', payload=payload, response_object=None)

    def Withdrawadvplsroute(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the withdrawadvplsroute operation on the server.

        Completely/Partially age out routes contained in this route range.

        withdrawadvplsroute(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
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
        return self._execute('withdrawadvplsroute', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, AsNumberVplsId=None, AsNumberVplsRd=None, AsNumberVplsRt=None, AssignedNumberVplsId=None, AssignedNumberVplsRd=None, AssignedNumberVplsRt=None, ImportRDAsRT=None, ImportVplsIdAsRd=None, IpAddressVplsId=None, IpAddressVplsRd=None, IpAddressVplsRt=None, NumberVsiId=None, TypeVplsId=None, TypeVplsRd=None, TypeVplsRt=None, TypeVsiId=None):
        """Base class infrastructure that gets a list of bgpIpv6AdL2Vpn device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AsNumberVplsId (str): optional regex of asNumberVplsId
        - AsNumberVplsRd (str): optional regex of asNumberVplsRd
        - AsNumberVplsRt (str): optional regex of asNumberVplsRt
        - AssignedNumberVplsId (str): optional regex of assignedNumberVplsId
        - AssignedNumberVplsRd (str): optional regex of assignedNumberVplsRd
        - AssignedNumberVplsRt (str): optional regex of assignedNumberVplsRt
        - ImportRDAsRT (str): optional regex of importRDAsRT
        - ImportVplsIdAsRd (str): optional regex of importVplsIdAsRd
        - IpAddressVplsId (str): optional regex of ipAddressVplsId
        - IpAddressVplsRd (str): optional regex of ipAddressVplsRd
        - IpAddressVplsRt (str): optional regex of ipAddressVplsRt
        - NumberVsiId (str): optional regex of numberVsiId
        - TypeVplsId (str): optional regex of typeVplsId
        - TypeVplsRd (str): optional regex of typeVplsRd
        - TypeVplsRt (str): optional regex of typeVplsRt
        - TypeVsiId (str): optional regex of typeVsiId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
