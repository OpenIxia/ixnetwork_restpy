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


class Srv6Oam(Base):
    """
    The Srv6Oam class encapsulates a list of srv6Oam resources that are managed by the user.
    A list of resources can be retrieved from the server using the Srv6Oam.find() method.
    The list can be managed by using the Srv6Oam.add() and Srv6Oam.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "srv6Oam"
    _SDM_ATT_MAP = {
        "Active": "active",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableSBfdResponder": "enableSBfdResponder",
        "Errors": "errors",
        "LocalRouterId": "localRouterId",
        "LocatorBlkLen": "locatorBlkLen",
        "Multiplier": "multiplier",
        "Name": "name",
        "NumPingTraceRouteDest": "numPingTraceRouteDest",
        "NumReverseBsid": "numReverseBsid",
        "ReplyDestUnreachCode": "replyDestUnreachCode",
        "RxCfgSrcAddrFlag": "rxCfgSrcAddrFlag",
        "RxSrcAddr": "rxSrcAddr",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "TraceRouteRxPortEnd": "traceRouteRxPortEnd",
        "TraceRouteRxPortStart": "traceRouteRxPortStart",
        "TracerouteDstPort": "tracerouteDstPort",
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
        super(Srv6Oam, self).__init__(parent, list_op)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

    @property
    def LearnedInfoUpdate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_0f2cd377c44f7dfc2c15b68516dc2707.LearnedInfoUpdate): An instance of the LearnedInfoUpdate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_0f2cd377c44f7dfc2c15b68516dc2707 import (
            LearnedInfoUpdate,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfoUpdate", None) is not None:
                return self._properties.get("LearnedInfoUpdate")
        return LearnedInfoUpdate(self)

    @property
    def SbfdResponder(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sbfdresponder_e89a7c6cba0a1f66c71ecb217db4ccfd.SbfdResponder): An instance of the SbfdResponder class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.sbfdresponder_e89a7c6cba0a1f66c71ecb217db4ccfd import (
            SbfdResponder,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SbfdResponder", None) is not None:
                return self._properties.get("SbfdResponder")
        return SbfdResponder(self)._select()

    @property
    def Srv6OamDestination(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamdestination_4c1ece21781b682b07f8d26d61f2b8b6.Srv6OamDestination): An instance of the Srv6OamDestination class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamdestination_4c1ece21781b682b07f8d26d61f2b8b6 import (
            Srv6OamDestination,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Srv6OamDestination", None) is not None:
                return self._properties.get("Srv6OamDestination")
        return Srv6OamDestination(self)._select()

    @property
    def Srv6OamReverseBsid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamreversebsid_32c773aa5ec81fe48c4dde8135918746.Srv6OamReverseBsid): An instance of the Srv6OamReverseBsid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6oamreversebsid_32c773aa5ec81fe48c4dde8135918746 import (
            Srv6OamReverseBsid,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Srv6OamReverseBsid", None) is not None:
                return self._properties.get("Srv6OamReverseBsid")
        return Srv6OamReverseBsid(self)._select()

    @property
    def Srv6SbfdResponder(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6sbfdresponder_aeecc02f1736a0513600da92f49c6d9f.Srv6SbfdResponder): An instance of the Srv6SbfdResponder class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srv6sbfdresponder_aeecc02f1736a0513600da92f49c6d9f import (
            Srv6SbfdResponder,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Srv6SbfdResponder", None) is not None:
                return self._properties.get("Srv6SbfdResponder")
        return Srv6SbfdResponder(self)._select()

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
    def EnableSBfdResponder(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, it enables the S-BFD Responder.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSBfdResponder"])

    @EnableSBfdResponder.setter
    def EnableSBfdResponder(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSBfdResponder"], value)

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def LocalRouterId(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The MPLOAM Router ID value, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LocalRouterId"])

    @property
    def LocatorBlkLen(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the locator block length value in bits. It is useful while processing the Compressed SIDs in SRH. For example, SID (128 bits) = Locator Block Length + G-SID length + Arguments + G-sid index.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["LocatorBlkLen"]))

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
    def NumPingTraceRouteDest(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify number of destinations to be configured for Ping/Trace Route/SBFD Requests.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumPingTraceRouteDest"])

    @NumPingTraceRouteDest.setter
    def NumPingTraceRouteDest(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumPingTraceRouteDest"], value)

    @property
    def NumReverseBsid(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify number of Reverse Binding SIDs to be configured for backhaul detection.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumReverseBsid"])

    @NumReverseBsid.setter
    def NumReverseBsid(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumReverseBsid"], value)

    @property
    def ReplyDestUnreachCode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Options to select the Error Code while sending Destination Unreachable Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ReplyDestUnreachCode"])
        )

    @property
    def RxCfgSrcAddrFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, Source Address of IPv6 header in Response packets will be taken as per configuration. If Disabled, Source Address of IPv6 will be taken from the Interface on which the received destination (Egress) is configured (emulated/loopback interface).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RxCfgSrcAddrFlag"])
        )

    @property
    def RxSrcAddr(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Address of IPv6 header in Response packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RxSrcAddr"]))

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

    @property
    def TraceRouteRxPortEnd(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the End value of UDP port up to which Session will be listening for Trace Route Packets. Default End UDP port is 33634. Min value : 33434 - Max value : 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["TraceRouteRxPortEnd"])

    @TraceRouteRxPortEnd.setter
    def TraceRouteRxPortEnd(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TraceRouteRxPortEnd"], value)

    @property
    def TraceRouteRxPortStart(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Start value of UDP port from which Session will be listening for Trace Route Packets. Default Start UDP port is 33434. Min value : 33434 - Max value : 65535
        """
        return self._get_attribute(self._SDM_ATT_MAP["TraceRouteRxPortStart"])

    @TraceRouteRxPortStart.setter
    def TraceRouteRxPortStart(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TraceRouteRxPortStart"], value)

    @property
    def TracerouteDstPort(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Destination Port to be used for Trace Route
        """
        return self._get_attribute(self._SDM_ATT_MAP["TracerouteDstPort"])

    @TracerouteDstPort.setter
    def TracerouteDstPort(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TracerouteDstPort"], value)

    def update(
        self,
        ConnectedVia=None,
        EnableSBfdResponder=None,
        Multiplier=None,
        Name=None,
        NumPingTraceRouteDest=None,
        NumReverseBsid=None,
        StackedLayers=None,
        TraceRouteRxPortEnd=None,
        TraceRouteRxPortStart=None,
        TracerouteDstPort=None,
    ):
        # type: (List[str], bool, int, str, int, int, List[str], int, int, int) -> Srv6Oam
        """Updates srv6Oam resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableSBfdResponder (bool): If selected, it enables the S-BFD Responder.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumPingTraceRouteDest (number): Specify number of destinations to be configured for Ping/Trace Route/SBFD Requests.
        - NumReverseBsid (number): Specify number of Reverse Binding SIDs to be configured for backhaul detection.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - TraceRouteRxPortEnd (number): Specifies the End value of UDP port up to which Session will be listening for Trace Route Packets. Default End UDP port is 33634. Min value : 33434 - Max value : 65535
        - TraceRouteRxPortStart (number): Specifies the Start value of UDP port from which Session will be listening for Trace Route Packets. Default Start UDP port is 33434. Min value : 33434 - Max value : 65535
        - TracerouteDstPort (number): Destination Port to be used for Trace Route

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        EnableSBfdResponder=None,
        Multiplier=None,
        Name=None,
        NumPingTraceRouteDest=None,
        NumReverseBsid=None,
        StackedLayers=None,
        TraceRouteRxPortEnd=None,
        TraceRouteRxPortStart=None,
        TracerouteDstPort=None,
    ):
        # type: (List[str], bool, int, str, int, int, List[str], int, int, int) -> Srv6Oam
        """Adds a new srv6Oam resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - EnableSBfdResponder (bool): If selected, it enables the S-BFD Responder.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumPingTraceRouteDest (number): Specify number of destinations to be configured for Ping/Trace Route/SBFD Requests.
        - NumReverseBsid (number): Specify number of Reverse Binding SIDs to be configured for backhaul detection.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - TraceRouteRxPortEnd (number): Specifies the End value of UDP port up to which Session will be listening for Trace Route Packets. Default End UDP port is 33634. Min value : 33434 - Max value : 65535
        - TraceRouteRxPortStart (number): Specifies the Start value of UDP port from which Session will be listening for Trace Route Packets. Default Start UDP port is 33434. Min value : 33434 - Max value : 65535
        - TracerouteDstPort (number): Destination Port to be used for Trace Route

        Returns
        -------
        - self: This instance with all currently retrieved srv6Oam resources using find and the newly added srv6Oam resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained srv6Oam resources in this instance from the server.

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
        EnableSBfdResponder=None,
        Errors=None,
        LocalRouterId=None,
        Multiplier=None,
        Name=None,
        NumPingTraceRouteDest=None,
        NumReverseBsid=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        TraceRouteRxPortEnd=None,
        TraceRouteRxPortStart=None,
        TracerouteDstPort=None,
    ):
        """Finds and retrieves srv6Oam resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve srv6Oam resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all srv6Oam resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableSBfdResponder (bool): If selected, it enables the S-BFD Responder.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - LocalRouterId (list(str)): The MPLOAM Router ID value, in IPv4 format.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumPingTraceRouteDest (number): Specify number of destinations to be configured for Ping/Trace Route/SBFD Requests.
        - NumReverseBsid (number): Specify number of Reverse Binding SIDs to be configured for backhaul detection.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - TraceRouteRxPortEnd (number): Specifies the End value of UDP port up to which Session will be listening for Trace Route Packets. Default End UDP port is 33634. Min value : 33434 - Max value : 65535
        - TraceRouteRxPortStart (number): Specifies the Start value of UDP port from which Session will be listening for Trace Route Packets. Default Start UDP port is 33434. Min value : 33434 - Max value : 65535
        - TracerouteDstPort (number): Destination Port to be used for Trace Route

        Returns
        -------
        - self: This instance with matching srv6Oam resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of srv6Oam data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the srv6Oam resources from the server available through an iterator or index

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

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        LocatorBlkLen=None,
        ReplyDestUnreachCode=None,
        RxCfgSrcAddrFlag=None,
        RxSrcAddr=None,
    ):
        """Base class infrastructure that gets a list of srv6Oam device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - LocatorBlkLen (str): optional regex of locatorBlkLen
        - ReplyDestUnreachCode (str): optional regex of replyDestUnreachCode
        - RxCfgSrcAddrFlag (str): optional regex of rxCfgSrcAddrFlag
        - RxSrcAddr (str): optional regex of rxSrcAddr

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
