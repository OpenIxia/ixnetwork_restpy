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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class RsvpteLsps(Base):
    """Rsvp LSP Configuration
    The RsvpteLsps class encapsulates a list of rsvpteLsps resources that are managed by the user.
    A list of resources can be retrieved from the server using the RsvpteLsps.find() method.
    The list can be managed by using the RsvpteLsps.add() and RsvpteLsps.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "rsvpteLsps"
    _SDM_ATT_MAP = {
        "Active": "active",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableP2PEgress": "enableP2PEgress",
        "Errors": "errors",
        "ExpectedPceInitiatedLspsCount": "expectedPceInitiatedLspsCount",
        "IngressP2PLsps": "ingressP2PLsps",
        "LocalIp": "localIp",
        "Multiplier": "multiplier",
        "Name": "name",
        "P2mpEgressTunnelCount": "p2mpEgressTunnelCount",
        "P2mpIngressLspCount": "p2mpIngressLspCount",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
    }
    _SDM_ENUM_MAP = {
        "status": [
            "configured",
            "error",
            "mixed",
            "notStarted",
            "started",
            "starting",
            "stopping",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(RsvpteLsps, self).__init__(parent, list_op)

    @property
    def RsvpP2PEgressLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pegresslsps_9f054ab50236d49eeef8a9fbc0ba1127.RsvpP2PEgressLsps): An instance of the RsvpP2PEgressLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pegresslsps_9f054ab50236d49eeef8a9fbc0ba1127 import (
            RsvpP2PEgressLsps,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpP2PEgressLsps", None) is not None:
                return self._properties.get("RsvpP2PEgressLsps")
        return RsvpP2PEgressLsps(self)._select()

    @property
    def RsvpP2PIngressLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pingresslsps_b3cad06292c51571163e9346869405a0.RsvpP2PIngressLsps): An instance of the RsvpP2PIngressLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pingresslsps_b3cad06292c51571163e9346869405a0 import (
            RsvpP2PIngressLsps,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpP2PIngressLsps", None) is not None:
                return self._properties.get("RsvpP2PIngressLsps")
        return RsvpP2PIngressLsps(self)._select()

    @property
    def RsvpP2mpEgressLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpegresslsps_a7be6d237185c970a66235441605770c.RsvpP2mpEgressLsps): An instance of the RsvpP2mpEgressLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpegresslsps_a7be6d237185c970a66235441605770c import (
            RsvpP2mpEgressLsps,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpP2mpEgressLsps", None) is not None:
                return self._properties.get("RsvpP2mpEgressLsps")
        return RsvpP2mpEgressLsps(self)._select()

    @property
    def RsvpP2mpIngressLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresslsps_7b38fc09ccf52081a0ef372f9492b887.RsvpP2mpIngressLsps): An instance of the RsvpP2mpIngressLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresslsps_7b38fc09ccf52081a0ef372f9492b887 import (
            RsvpP2mpIngressLsps,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpP2mpIngressLsps", None) is not None:
                return self._properties.get("RsvpP2mpIngressLsps")
        return RsvpP2mpIngressLsps(self)._select()

    @property
    def RsvpPcepExpectedInitiatedLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvppcepexpectedinitiatedlsps_64b47067effbb8886f7ee1d4dd6e8560.RsvpPcepExpectedInitiatedLsps): An instance of the RsvpPcepExpectedInitiatedLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvppcepexpectedinitiatedlsps_64b47067effbb8886f7ee1d4dd6e8560 import (
            RsvpPcepExpectedInitiatedLsps,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpPcepExpectedInitiatedLsps", None) is not None:
                return self._properties.get("RsvpPcepExpectedInitiatedLsps")
        return RsvpPcepExpectedInitiatedLsps(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedVia"])

    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedVia"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def EnableP2PEgress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable to configure P2P Egress LSPs
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableP2PEgress"])

    @EnableP2PEgress.setter
    def EnableP2PEgress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableP2PEgress"], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def ExpectedPceInitiatedLspsCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Expected PCE Initiated RSVP-TE LSPs
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExpectedPceInitiatedLspsCount"])

    @ExpectedPceInitiatedLspsCount.setter
    def ExpectedPceInitiatedLspsCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExpectedPceInitiatedLspsCount"], value)

    @property
    def IngressP2PLsps(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of P2P Ingress LSPs configured per IPv4 Loopback
        """
        return self._get_attribute(self._SDM_ATT_MAP["IngressP2PLsps"])

    @IngressP2PLsps.setter
    def IngressP2PLsps(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IngressP2PLsps"], value)

    @property
    def LocalIp(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Local IP
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def P2mpEgressTunnelCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of P2MP Egress Tunnels configured per IPv4 Loopback
        """
        return self._get_attribute(self._SDM_ATT_MAP["P2mpEgressTunnelCount"])

    @P2mpEgressTunnelCount.setter
    def P2mpEgressTunnelCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["P2mpEgressTunnelCount"], value)

    @property
    def P2mpIngressLspCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of P2MP Ingress LSPs configured per IPv4 Loopback
        """
        return self._get_attribute(self._SDM_ATT_MAP["P2mpIngressLspCount"])

    @P2mpIngressLspCount.setter
    def P2mpIngressLspCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["P2mpIngressLspCount"], value)

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateCounts"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    def update(
        self,
        ConnectedVia=None,
        EnableP2PEgress=None,
        ExpectedPceInitiatedLspsCount=None,
        IngressP2PLsps=None,
        Multiplier=None,
        Name=None,
        P2mpEgressTunnelCount=None,
        P2mpIngressLspCount=None,
        StackedLayers=None,
    ):
        # type: (List[str], bool, int, int, int, str, int, int, List[str]) -> RsvpteLsps
        """Updates rsvpteLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableP2PEgress (bool): Enable to configure P2P Egress LSPs
        - ExpectedPceInitiatedLspsCount (number): Number of Expected PCE Initiated RSVP-TE LSPs
        - IngressP2PLsps (number): Number of P2P Ingress LSPs configured per IPv4 Loopback
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - P2mpEgressTunnelCount (number): Number of P2MP Egress Tunnels configured per IPv4 Loopback
        - P2mpIngressLspCount (number): Number of P2MP Ingress LSPs configured per IPv4 Loopback
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        EnableP2PEgress=None,
        ExpectedPceInitiatedLspsCount=None,
        IngressP2PLsps=None,
        Multiplier=None,
        Name=None,
        P2mpEgressTunnelCount=None,
        P2mpIngressLspCount=None,
        StackedLayers=None,
    ):
        # type: (List[str], bool, int, int, int, str, int, int, List[str]) -> RsvpteLsps
        """Adds a new rsvpteLsps resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableP2PEgress (bool): Enable to configure P2P Egress LSPs
        - ExpectedPceInitiatedLspsCount (number): Number of Expected PCE Initiated RSVP-TE LSPs
        - IngressP2PLsps (number): Number of P2P Ingress LSPs configured per IPv4 Loopback
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - P2mpEgressTunnelCount (number): Number of P2MP Egress Tunnels configured per IPv4 Loopback
        - P2mpIngressLspCount (number): Number of P2MP Ingress LSPs configured per IPv4 Loopback
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved rsvpteLsps resources using find and the newly added rsvpteLsps resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained rsvpteLsps resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        EnableP2PEgress=None,
        Errors=None,
        ExpectedPceInitiatedLspsCount=None,
        IngressP2PLsps=None,
        LocalIp=None,
        Multiplier=None,
        Name=None,
        P2mpEgressTunnelCount=None,
        P2mpIngressLspCount=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
    ):
        """Finds and retrieves rsvpteLsps resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve rsvpteLsps resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all rsvpteLsps resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableP2PEgress (bool): Enable to configure P2P Egress LSPs
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - ExpectedPceInitiatedLspsCount (number): Number of Expected PCE Initiated RSVP-TE LSPs
        - IngressP2PLsps (number): Number of P2P Ingress LSPs configured per IPv4 Loopback
        - LocalIp (list(str)): Local IP
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - P2mpEgressTunnelCount (number): Number of P2MP Egress Tunnels configured per IPv4 Loopback
        - P2mpIngressLspCount (number): Number of P2MP Ingress LSPs configured per IPv4 Loopback
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching rsvpteLsps resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of rsvpteLsps data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the rsvpteLsps resources from the server available through an iterator or index

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("restartDown", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

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
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None):
        """Base class infrastructure that gets a list of rsvpteLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
