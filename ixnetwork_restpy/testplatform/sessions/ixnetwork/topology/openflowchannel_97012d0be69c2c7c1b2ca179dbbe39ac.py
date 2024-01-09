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


class OpenFlowChannel(Base):
    """Openflow Controller Channel level Configuration
    The OpenFlowChannel class encapsulates a list of openFlowChannel resources that are managed by the user.
    A list of resources can be retrieved from the server using the OpenFlowChannel.find() method.
    The list can be managed by using the OpenFlowChannel.add() and OpenFlowChannel.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "openFlowChannel"
    _SDM_ATT_MAP = {
        "Active": "active",
        "CalcFlowRate": "calcFlowRate",
        "CalcFlowRateWithBarrier": "calcFlowRateWithBarrier",
        "ConnectedVia": "connectedVia",
        "ControllerIndex": "controllerIndex",
        "ControllerName": "controllerName",
        "Count": "count",
        "DatapathId": "datapathId",
        "DatapathIdHex": "datapathIdHex",
        "DescriptiveName": "descriptiveName",
        "EnableHelloElement": "enableHelloElement",
        "Errors": "errors",
        "FlowTxBurstSize": "flowTxBurstSize",
        "GroupsPerChannel": "groupsPerChannel",
        "InterFlowBurstGap": "interFlowBurstGap",
        "LocalIp": "localIp",
        "MaxFlowsAtATime": "maxFlowsAtATime",
        "MetersPerChannel": "metersPerChannel",
        "Multiplier": "multiplier",
        "Name": "name",
        "RemoteIp": "remoteIp",
        "SendRoleRequest": "sendRoleRequest",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StartupGenerationId": "startupGenerationId",
        "StartupRoleRequest": "startupRoleRequest",
        "StateCounts": "stateCounts",
        "Status": "status",
        "TablesPerChannel": "tablesPerChannel",
        "UseDatapathID": "useDatapathID",
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
        super(OpenFlowChannel, self).__init__(parent, list_op)

    @property
    def Groups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.groups_b0203364879843ea921d92b31d3b37a9.Groups): An instance of the Groups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.groups_b0203364879843ea921d92b31d3b37a9 import (
            Groups,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Groups", None) is not None:
                return self._properties.get("Groups")
        return Groups(self)

    @property
    def Meters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.meters_8b28210732dd4e9a4bab19a7e6241a11.Meters): An instance of the Meters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.meters_8b28210732dd4e9a4bab19a7e6241a11 import (
            Meters,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Meters", None) is not None:
                return self._properties.get("Meters")
        return Meters(self)

    @property
    def Tables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tables_3d687bbed07969785585da03f7a19e75.Tables): An instance of the Tables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tables_3d687bbed07969785585da03f7a19e75 import (
            Tables,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Tables", None) is not None:
                return self._properties.get("Tables")
        return Tables(self)

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
    def CalcFlowRate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the statistics on the rate of transmission of flows per second by the controller is published.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["CalcFlowRate"]))

    @property
    def CalcFlowRateWithBarrier(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, statistics on the rate of transmission of flows per second by the controller, along with Barrier Request messages is published.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CalcFlowRateWithBarrier"])
        )

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
    def ControllerIndex(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Parent Controller Index
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControllerIndex"])

    @property
    def ControllerName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Parent Controller Name
        """
        return self._get_attribute(self._SDM_ATT_MAP["ControllerName"])

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
    def DatapathId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Datapath ID of the OF Channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DatapathId"]))

    @property
    def DatapathIdHex(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Datapath ID in hexadecimal format.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DatapathIdHex"]))

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
    def EnableHelloElement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Controller sends a hello message consisting of an OpenFlow header and a set of variable size hello elements to inform the initial handshake of the connection.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableHelloElement"])
        )

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def FlowTxBurstSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the number of Flow transmitting packets that can be sent in a single burst within the time frame specified by the Inter Flow Burst Gap value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlowTxBurstSize"])
        )

    @property
    def GroupsPerChannel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Groups per Channel
        """
        return self._get_attribute(self._SDM_ATT_MAP["GroupsPerChannel"])

    @GroupsPerChannel.setter
    def GroupsPerChannel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GroupsPerChannel"], value)

    @property
    def InterFlowBurstGap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the duration (in milliseconds) for which the controller waits between successive flow advertisements.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["InterFlowBurstGap"])
        )

    @property
    def LocalIp(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The local IP address of the interface. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalIp"])

    @property
    def MaxFlowsAtATime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Max Number of Flows Processed at a Time is the size of an internal buffer maintained by the Ixiacontroller, which prevents it from sending more flows than the Openflow switch can consume at a time.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxFlowsAtATime"])
        )

    @property
    def MetersPerChannel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Meters per Channel
        """
        return self._get_attribute(self._SDM_ATT_MAP["MetersPerChannel"])

    @MetersPerChannel.setter
    def MetersPerChannel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MetersPerChannel"], value)

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
    def RemoteIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the DUT at the other end of the OF Channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RemoteIp"]))

    @property
    def SendRoleRequest(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the controller sends a Role Request message after the connection is established; to change its role according to the Role Request option selected.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendRoleRequest"])
        )

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
    def StartupGenerationId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 64-bit sequence number field that identifies a given mastership view.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartupGenerationId"])
        )

    @property
    def StartupRoleRequest(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This defines role of the controller.Options include: 1) No Change 2) Equal 3) Master 4) Slave
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StartupRoleRequest"])
        )

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

    @property
    def TablesPerChannel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Tables per Channel
        """
        return self._get_attribute(self._SDM_ATT_MAP["TablesPerChannel"])

    @TablesPerChannel.setter
    def TablesPerChannel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TablesPerChannel"], value)

    @property
    def UseDatapathID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Datapath ID and IP address are used as the OF Channel identifier.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UseDatapathID"]))

    def update(
        self,
        ConnectedVia=None,
        GroupsPerChannel=None,
        MetersPerChannel=None,
        Multiplier=None,
        Name=None,
        StackedLayers=None,
        TablesPerChannel=None,
    ):
        # type: (List[str], int, int, int, str, List[str], int) -> OpenFlowChannel
        """Updates openFlowChannel resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - GroupsPerChannel (number): Number of Groups per Channel
        - MetersPerChannel (number): Number of Meters per Channel
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - TablesPerChannel (number): Number of Tables per Channel

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        GroupsPerChannel=None,
        MetersPerChannel=None,
        Multiplier=None,
        Name=None,
        StackedLayers=None,
        TablesPerChannel=None,
    ):
        # type: (List[str], int, int, int, str, List[str], int) -> OpenFlowChannel
        """Adds a new openFlowChannel resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - GroupsPerChannel (number): Number of Groups per Channel
        - MetersPerChannel (number): Number of Meters per Channel
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - TablesPerChannel (number): Number of Tables per Channel

        Returns
        -------
        - self: This instance with all currently retrieved openFlowChannel resources using find and the newly added openFlowChannel resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained openFlowChannel resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ConnectedVia=None,
        ControllerIndex=None,
        ControllerName=None,
        Count=None,
        DescriptiveName=None,
        Errors=None,
        GroupsPerChannel=None,
        LocalIp=None,
        MetersPerChannel=None,
        Multiplier=None,
        Name=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        TablesPerChannel=None,
    ):
        """Finds and retrieves openFlowChannel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openFlowChannel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openFlowChannel resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - ControllerIndex (list(str)): Parent Controller Index
        - ControllerName (str): Parent Controller Name
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - GroupsPerChannel (number): Number of Groups per Channel
        - LocalIp (list(str)): The local IP address of the interface. This field is auto-populated and cannot be changed.
        - MetersPerChannel (number): Number of Meters per Channel
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TablesPerChannel (number): Number of Tables per Channel

        Returns
        -------
        - self: This instance with matching openFlowChannel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of openFlowChannel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openFlowChannel resources from the server available through an iterator or index

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

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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

    def GetAsynchronousConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getAsynchronousConfiguration operation on the server.

        Get Asynchronous Configurationr

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getAsynchronousConfiguration(async_operation=bool)
        --------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAsynchronousConfiguration(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAsynchronousConfiguration(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getAsynchronousConfiguration(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "getAsynchronousConfiguration", payload=payload, response_object=None
        )

    def InvokeSendRoleRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the invokeSendRoleRequest operation on the server.

        Sends a Role Request for selected Channel.

        invokeSendRoleRequest(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices in channel grid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "invokeSendRoleRequest", payload=payload, response_object=None
        )

    def PauseEchoReply(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the pauseEchoReply operation on the server.

        Pause Sending Echo Reply Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pauseEchoReply(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        pauseEchoReply(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        pauseEchoReply(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        pauseEchoReply(Arg2=list, async_operation=bool)list
        ---------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("pauseEchoReply", payload=payload, response_object=None)

    def PauseEchoRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the pauseEchoRequest operation on the server.

        Pause Sending Echo Request Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        pauseEchoRequest(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        pauseEchoRequest(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        pauseEchoRequest(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        pauseEchoRequest(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("pauseEchoRequest", payload=payload, response_object=None)

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

    def ResumeEchoReply(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumeEchoReply operation on the server.

        Resume Sending Echo Reply Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeEchoReply(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeEchoReply(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeEchoReply(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeEchoReply(Arg2=list, async_operation=bool)list
        ----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("resumeEchoReply", payload=payload, response_object=None)

    def ResumeEchoRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumeEchoRequest operation on the server.

        Resume Sending Echo Request Messages

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumeEchoRequest(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeEchoRequest(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeEchoRequest(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumeEchoRequest(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("resumeEchoRequest", payload=payload, response_object=None)

    def SendBarrierRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendBarrierRequest operation on the server.

        Send Barrier Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendBarrierRequest(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendBarrierRequest(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendBarrierRequest(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendBarrierRequest(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendBarrierRequest", payload=payload, response_object=None
        )

    def SendConfigRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendConfigRequest operation on the server.

        Send Config Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendConfigRequest(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendConfigRequest(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendConfigRequest(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendConfigRequest(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("sendConfigRequest", payload=payload, response_object=None)

    def SendDescriptionStatRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendDescriptionStatRequest operation on the server.

        Send Description Stat Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendDescriptionStatRequest(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendDescriptionStatRequest(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendDescriptionStatRequest(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendDescriptionStatRequest(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendDescriptionStatRequest", payload=payload, response_object=None
        )

    def SendEchoRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendEchoRequest operation on the server.

        Send Echo Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendEchoRequest(EnableEchoTimeout=bool, EchoTimeoutVal=number, async_operation=bool)
        ------------------------------------------------------------------------------------
        - EnableEchoTimeout (bool): This parameter requires a enableEchoTimeout of type kBool
        - EchoTimeoutVal (number): This parameter requires a echoTimeoutVal of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendEchoRequest(EnableEchoTimeout=bool, EchoTimeoutVal=number, SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------------------------------------
        - EnableEchoTimeout (bool): This parameter requires a enableEchoTimeout of type kBool
        - EchoTimeoutVal (number): This parameter requires a echoTimeoutVal of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendEchoRequest(SessionIndices=string, EnableEchoTimeout=bool, EchoTimeoutVal=number, async_operation=bool)
        -----------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a enableEchoTimeout of type kBool
        - EnableEchoTimeout (bool): This parameter requires a echoTimeoutVal of type kInteger
        - EchoTimeoutVal (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendEchoRequest(Arg2=list, Arg3=bool, Arg4=number, async_operation=bool)list
        ----------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (bool): Enable Echo Timeout
        - Arg4 (number): Echo Timeout Value
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("sendEchoRequest", payload=payload, response_object=None)

    def SendExperimenterMessage(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendExperimenterMessage operation on the server.

        Send Experimenter Message

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendExperimenterMessage(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, async_operation=bool)
        -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendExperimenterMessage(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendExperimenterMessage(SessionIndices=string, ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, async_operation=bool)
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a experimenterDataLength of type kInteger
        - ExperimenterDataLength (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a experimenterData of type kString
        - ExperimenterData (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendExperimenterMessage(Arg2=list, Arg3=number, Arg4=number, Arg5=number, Arg6=string, async_operation=bool)list
        ----------------------------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (number): Experimenter Data Length.
        - Arg4 (number): Experimenter ID.
        - Arg5 (number): Experimenter ID
        - Arg6 (str): Experimenter Data in Hex.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendExperimenterMessage", payload=payload, response_object=None
        )

    def SendExperimenterStatRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendExperimenterStatRequest operation on the server.

        Send Experimenter Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendExperimenterStatRequest(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, async_operation=bool)
        ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendExperimenterStatRequest(ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - ExperimenterDataLength (number): This parameter requires a experimenterDataLength of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ExperimenterData (str): This parameter requires a experimenterData of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendExperimenterStatRequest(SessionIndices=string, ExperimenterDataLength=number, ErrorUnsupportedTypeFormat=null, ErrorUnsupportedTypeFormat=null, ExperimenterData=string, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a experimenterDataLength of type kInteger
        - ExperimenterDataLength (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a experimenterData of type kString
        - ExperimenterData (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendExperimenterStatRequest(Arg2=list, Arg3=number, Arg4=number, Arg5=number, Arg6=string, async_operation=bool)list
        --------------------------------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (number): Experimenter Data Length.
        - Arg4 (number): Experimenter ID.
        - Arg5 (number): Experimenter ID
        - Arg6 (str): Experimenter Data in Hex.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendExperimenterStatRequest", payload=payload, response_object=None
        )

    def SendFeatureRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendFeatureRequest operation on the server.

        Send Feature Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendFeatureRequest(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendFeatureRequest(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendFeatureRequest(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendFeatureRequest(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendFeatureRequest", payload=payload, response_object=None
        )

    def SendGetQueueConfigRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendGetQueueConfigRequest operation on the server.

        Send Queue Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGetQueueConfigRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        -----------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGetQueueConfigRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGetQueueConfigRequest(SessionIndices=string, OutputPortType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        ----------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGetQueueConfigRequest(Arg2=list, Arg3=enum, Arg4=number, async_operation=bool)list
        --------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | mANUAL | oFPP_TABLE | oFPP_NONE | oFPP_ANY)): Output Port Type
        - Arg4 (number): Port ID
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendGetQueueConfigRequest", payload=payload, response_object=None
        )

    def SendGroupDescriptionRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendGroupDescriptionRequest operation on the server.

        Send Group Description Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGroupDescriptionRequest(async_operation=bool)
        -------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupDescriptionRequest(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupDescriptionRequest(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupDescriptionRequest(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendGroupDescriptionRequest", payload=payload, response_object=None
        )

    def SendGroupFeaturesRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendGroupFeaturesRequest operation on the server.

        Send Group Features Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGroupFeaturesRequest(async_operation=bool)
        ----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupFeaturesRequest(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupFeaturesRequest(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupFeaturesRequest(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendGroupFeaturesRequest", payload=payload, response_object=None
        )

    def SendGroupStatsRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendGroupStatsRequest operation on the server.

        Send Group Stats Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGroupStatsRequest(GroupIDType=enum, GroupID=number, async_operation=bool)
        -----------------------------------------------------------------------------
        - GroupIDType (str(enumOpt-Manual | enumOpt-OFPG_ALL | enumOpt-OFPG_ANY)): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
        - GroupID (number): This parameter requires a groupID of type kInteger
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupStatsRequest(GroupIDType=enum, GroupID=number, SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------------------------------
        - GroupIDType (str(enumOpt-Manual | enumOpt-OFPG_ALL | enumOpt-OFPG_ANY)): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
        - GroupID (number): This parameter requires a groupID of type kInteger
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupStatsRequest(SessionIndices=string, GroupIDType=enum, GroupID=number, async_operation=bool)
        ----------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a groupIDType of type kEnumValue=enumOpt-Manual,enumOpt-OFPG_ALL,enumOpt-OFPG_ANY
        - GroupIDType (str(enumOpt-Manual | enumOpt-OFPG_ALL | enumOpt-OFPG_ANY)): This parameter requires a groupID of type kInteger
        - GroupID (number): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendGroupStatsRequest(Arg2=list, Arg3=enum, Arg4=number, async_operation=bool)list
        ----------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPG_ALL | oFPG_ANY | manual)): Group ID Type
        - Arg4 (number): Group ID
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendGroupStatsRequest", payload=payload, response_object=None
        )

    def SendMeterConfigRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendMeterConfigRequest operation on the server.

        Send Meter Config Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendMeterConfigRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        -----------------------------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterConfigRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterConfigRequest(SessionIndices=string, MeterIDType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        ----------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterConfigRequest(Arg2=list, Arg3=enum, Arg4=number, async_operation=bool)list
        -----------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPM_SLOWPATH | oFPM_CONTROLLER | all | manual)): Meter ID Type
        - Arg4 (number): Meter ID
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendMeterConfigRequest", payload=payload, response_object=None
        )

    def SendMeterFeaturesRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendMeterFeaturesRequest operation on the server.

        Send Meter Features Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendMeterFeaturesRequest(async_operation=bool)
        ----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterFeaturesRequest(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterFeaturesRequest(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterFeaturesRequest(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendMeterFeaturesRequest", payload=payload, response_object=None
        )

    def SendMeterStatRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendMeterStatRequest operation on the server.

        Send Meter Stat Request to Switch.

        sendMeterStatRequest(Arg2=list, Arg3=enum, Arg4=number, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPM_SLOWPATH | oFPM_CONTROLLER | all | manual)): Meter ID Type
        - Arg4 (number): Meter ID
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "sendMeterStatRequest", payload=payload, response_object=None
        )

    def SendMeterStatsRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the sendMeterStatsRequest operation on the server.

        Send Meter Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendMeterStatsRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        ----------------------------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterStatsRequest(MeterIDType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------------------------------------------------
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendMeterStatsRequest(SessionIndices=string, MeterIDType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        ---------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a meterIDType of type kEnumValue=enumOpt-ALL,enumOpt-MANUAL,enumOpt-OFPM_CONTROLLER,enumOpt-OFPM_SLOWPATH
        - MeterIDType (str(enumOpt-ALL | enumOpt-MANUAL | enumOpt-OFPM_CONTROLLER | enumOpt-OFPM_SLOWPATH)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12
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
        return self._execute(
            "sendMeterStatsRequest", payload=payload, response_object=None
        )

    def SendPortDescription(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendPortDescription operation on the server.

        Send Port Description

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPortDescription(async_operation=bool)
        -----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendPortDescription(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendPortDescription(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendPortDescription(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendPortDescription", payload=payload, response_object=None
        )

    def SendPortStatsRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendPortStatsRequest operation on the server.

        Send Port Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPortStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        ------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY | enumOpt-OFPP_NONE)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendPortStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY | enumOpt-OFPP_NONE)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendPortStatsRequest(SessionIndices=string, OutputPortType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        -----------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY,enumOpt-OFPP_NONE
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY | enumOpt-OFPP_NONE)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendPortStatsRequest(Arg2=list, Arg3=enum, Arg4=number, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | mANUAL | oFPP_TABLE | oFPP_NONE | oFPP_ANY)): Output Port Type
        - Arg4 (number): Port ID
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendPortStatsRequest", payload=payload, response_object=None
        )

    def SendQueueStatsRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendQueueStatsRequest operation on the server.

        Send Queue Stats Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendQueueStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, QueueType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        --------------------------------------------------------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - QueueType (str(enumOpt-MANUAL | enumOpt-OFPQ_ALL)): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendQueueStatsRequest(OutputPortType=enum, ErrorUnsupportedTypeFormat=null, QueueType=enum, ErrorUnsupportedTypeFormat=null, SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - QueueType (str(enumOpt-MANUAL | enumOpt-OFPQ_ALL)): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendQueueStatsRequest(SessionIndices=string, OutputPortType=enum, ErrorUnsupportedTypeFormat=null, QueueType=enum, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a outputPortType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPP_ANY
        - OutputPortType (str(enumOpt-MANUAL | enumOpt-OFPP_ANY)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a queueType of type kEnumValue=enumOpt-MANUAL,enumOpt-OFPQ_ALL
        - QueueType (str(enumOpt-MANUAL | enumOpt-OFPQ_ALL)): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendQueueStatsRequest(Arg2=list, Arg3=enum, Arg4=number, Arg5=enum, Arg6=number, async_operation=bool)list
        ----------------------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(oFPP_IN_PORT | oFPP_NORMAL | oFPP_FLOOD | oFPP_ALL | oFPP_CONTROLLER | oFPP_LOCAL | mANUAL | oFPP_TABLE | oFPP_NONE | oFPP_ANY)): Output Port Type
        - Arg4 (number): Port ID
        - Arg5 (str(oFPQ_ALL | manual)): Queue Type
        - Arg6 (number): Queue ID
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendQueueStatsRequest", payload=payload, response_object=None
        )

    def SendTableModRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendTableModRequest operation on the server.

        Send Table Mod Request

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendTableModRequest(TableIdType=enum, TableId=number, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        ------------------------------------------------------------------------------------------------------------
        - TableIdType (str(enumOpt-ALL_TABLE | enumOpt-MANUAL)): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
        - TableId (number): This parameter requires a tableId of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendTableModRequest(TableIdType=enum, TableId=number, ErrorUnsupportedTypeFormat=null, SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------------------------------------------------------------
        - TableIdType (str(enumOpt-ALL_TABLE | enumOpt-MANUAL)): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
        - TableId (number): This parameter requires a tableId of type kInteger
        - ErrorUnsupportedTypeFormat (null): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendTableModRequest(SessionIndices=string, TableIdType=enum, TableId=number, ErrorUnsupportedTypeFormat=null, async_operation=bool)
        -----------------------------------------------------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a tableIdType of type kEnumValue=enumOpt-ALL_TABLE,enumOpt-MANUAL
        - TableIdType (str(enumOpt-ALL_TABLE | enumOpt-MANUAL)): This parameter requires a tableId of type kInteger
        - TableId (number): This parameter requires a errorUnsupportedTypeFormat of type kVoid
        - ErrorUnsupportedTypeFormat (null): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendTableModRequest(Arg2=list, Arg3=enum, Arg4=number, Arg5=number, async_operation=bool)list
        ---------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Arg3 (str(aLL_TABLE | manual)): Table ID Type
        - Arg4 (number): Table ID
        - Arg5 (number): Table Config
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendTableModRequest", payload=payload, response_object=None
        )

    def SendTableStatsRequest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendTableStatsRequest operation on the server.

        Send Table Stats Request to Switch

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendTableStatsRequest(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendTableStatsRequest(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendTableStatsRequest(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        sendTableStatsRequest(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute(
            "sendTableStatsRequest", payload=payload, response_object=None
        )

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

    def StartChannel(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the startChannel operation on the server.

        Start OpenFlow Channel

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startChannel(async_operation=bool)
        ----------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startChannel(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startChannel(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------
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
        return self._execute("startChannel", payload=payload, response_object=None)

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

    def StopChannel(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stopChannel operation on the server.

        Stop OpenFlow Channel

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopChannel(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopChannel(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopChannel(SessionIndices=string, async_operation=bool)
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
        return self._execute("stopChannel", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        CalcFlowRate=None,
        CalcFlowRateWithBarrier=None,
        DatapathId=None,
        DatapathIdHex=None,
        EnableHelloElement=None,
        FlowTxBurstSize=None,
        InterFlowBurstGap=None,
        MaxFlowsAtATime=None,
        RemoteIp=None,
        SendRoleRequest=None,
        StartupGenerationId=None,
        StartupRoleRequest=None,
        UseDatapathID=None,
    ):
        """Base class infrastructure that gets a list of openFlowChannel device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CalcFlowRate (str): optional regex of calcFlowRate
        - CalcFlowRateWithBarrier (str): optional regex of calcFlowRateWithBarrier
        - DatapathId (str): optional regex of datapathId
        - DatapathIdHex (str): optional regex of datapathIdHex
        - EnableHelloElement (str): optional regex of enableHelloElement
        - FlowTxBurstSize (str): optional regex of flowTxBurstSize
        - InterFlowBurstGap (str): optional regex of interFlowBurstGap
        - MaxFlowsAtATime (str): optional regex of maxFlowsAtATime
        - RemoteIp (str): optional regex of remoteIp
        - SendRoleRequest (str): optional regex of sendRoleRequest
        - StartupGenerationId (str): optional regex of startupGenerationId
        - StartupRoleRequest (str): optional regex of startupRoleRequest
        - UseDatapathID (str): optional regex of useDatapathID

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
