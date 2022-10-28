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


class Host(Base):
    """This object represents the emulated IGMP host for which the group ranges are created.
    The Host class encapsulates a list of host resources that are managed by the user.
    A list of resources can be retrieved from the server using the Host.find() method.
    The list can be managed by using the Host.add() and Host.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "host"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "GqResponseMode": "gqResponseMode",
        "InterfaceId": "interfaceId",
        "InterfaceIndex": "interfaceIndex",
        "InterfaceType": "interfaceType",
        "Interfaces": "interfaces",
        "ReportFreq": "reportFreq",
        "RespToQueryImmediately": "respToQueryImmediately",
        "RobustnessVariable": "robustnessVariable",
        "RouterAlert": "routerAlert",
        "SqResponseMode": "sqResponseMode",
        "SuppressReports": "suppressReports",
        "TrafficGroupId": "trafficGroupId",
        "UpResponseMode": "upResponseMode",
        "Version": "version",
    }
    _SDM_ENUM_MAP = {
        "version": ["igmpv1", "igmpv2", "igmpv3"],
    }

    def __init__(self, parent, list_op=False):
        super(Host, self).__init__(parent, list_op)

    @property
    def Group(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.group_b8eef8cdbd0da12e3fdb6e5fa5a6ef91.Group): An instance of the Group class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.group_b8eef8cdbd0da12e3fdb6e5fa5a6ef91 import (
            Group,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Group", None) is not None:
                return self._properties.get("Group")
        return Group(self)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of the host in the IGMP simulation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def GqResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, responds to General Query messages (where the Group Address field and Number of Sources Field = 0). This query message is sent by a multicast router so it can learn about the complete multicast reception state for each of the neighboring interfaces. interfaces.
        """
        return self._get_attribute(self._SDM_ATT_MAP["GqResponseMode"])

    @GqResponseMode.setter
    def GqResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["GqResponseMode"], value)

    @property
    def InterfaceId(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): This is a local ID and is unique per router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceId"])

    @InterfaceId.setter
    def InterfaceId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceId"], value)

    @property
    def InterfaceIndex(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this IGMP interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceIndex"])

    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceIndex"], value)

    @property
    def InterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The type of interface to be selected for this IGMP interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceType"])

    @InterfaceType.setter
    def InterfaceType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceType"], value)

    @property
    def Interfaces(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Interfaces"])

    @Interfaces.setter
    def Interfaces(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Interfaces"], value)

    @property
    def ReportFreq(self):
        # type: () -> int
        """
        Returns
        -------
        - number: When the mode is report to all unsolicited, this is the frequency in seconds with unsolicited messages are generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportFreq"])

    @ReportFreq.setter
    def ReportFreq(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportFreq"], value)

    @property
    def RespToQueryImmediately(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the state machine will ignore the value specified in the maximum response delay in the membership query message, assume that the delay is always 0 seconds, and immediately responds to the query by sending a report.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RespToQueryImmediately"])

    @RespToQueryImmediately.setter
    def RespToQueryImmediately(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RespToQueryImmediately"], value)

    @property
    def RobustnessVariable(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["RobustnessVariable"])

    @RobustnessVariable.setter
    def RobustnessVariable(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RobustnessVariable"], value)

    @property
    def RouterAlert(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the IP header Send Router Alert bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterAlert"])

    @RouterAlert.setter
    def RouterAlert(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterAlert"], value)

    @property
    def SqResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, responds to Group-Specific Query messages. This query message is sent by a multicast router so it can learn about the multicast reception state, concerning one multicast address, for each of the neighboring interfaces; for example, when member leaves a group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SqResponseMode"])

    @SqResponseMode.setter
    def SqResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SqResponseMode"], value)

    @property
    def SuppressReports(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Suppress generation of V3 reports on receipt of v1/v2 reports having common groups. If enabled, it indicates that a host/group member will allow its IGMPv3 Membership Record to be suppressed by a membership report for Version 1 or 2. The suppression will only be for group reports received from another port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SuppressReports"])

    @SuppressReports.setter
    def SuppressReports(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SuppressReports"], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): This object contains the traffic group information configured in the trafficGroup object.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    @property
    def UpResponseMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Report to all unsolicited-causes each simulated host to automatically send full memberships messages at regular intervals.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UpResponseMode"])

    @UpResponseMode.setter
    def UpResponseMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UpResponseMode"], value)

    @property
    def Version(self):
        # type: () -> str
        """
        Returns
        -------
        - str(igmpv1 | igmpv2 | igmpv3): Sets the IGMP version number that is to be simulated on the host: 1, 2, or 3.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Version"])

    @Version.setter
    def Version(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Version"], value)

    def update(
        self,
        Enabled=None,
        GqResponseMode=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        ReportFreq=None,
        RespToQueryImmediately=None,
        RobustnessVariable=None,
        RouterAlert=None,
        SqResponseMode=None,
        SuppressReports=None,
        TrafficGroupId=None,
        UpResponseMode=None,
        Version=None,
    ):
        # type: (bool, bool, str, int, str, str, int, bool, int, bool, bool, bool, str, bool, str) -> Host
        """Updates host resource on the server.

        Args
        ----
        - Enabled (bool): Enables the use of the host in the IGMP simulation.
        - GqResponseMode (bool): If enabled, responds to General Query messages (where the Group Address field and Number of Sources Field = 0). This query message is sent by a multicast router so it can learn about the complete multicast reception state for each of the neighboring interfaces. interfaces.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This is a local ID and is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this IGMP interface.
        - InterfaceType (str): The type of interface to be selected for this IGMP interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - ReportFreq (number): When the mode is report to all unsolicited, this is the frequency in seconds with unsolicited messages are generated.
        - RespToQueryImmediately (bool): If enabled, the state machine will ignore the value specified in the maximum response delay in the membership query message, assume that the delay is always 0 seconds, and immediately responds to the query by sending a report.
        - RobustnessVariable (number): NOT DEFINED
        - RouterAlert (bool): Sets the IP header Send Router Alert bit.
        - SqResponseMode (bool): If enabled, responds to Group-Specific Query messages. This query message is sent by a multicast router so it can learn about the multicast reception state, concerning one multicast address, for each of the neighboring interfaces; for example, when member leaves a group.
        - SuppressReports (bool): Suppress generation of V3 reports on receipt of v1/v2 reports having common groups. If enabled, it indicates that a host/group member will allow its IGMPv3 Membership Record to be suppressed by a membership report for Version 1 or 2. The suppression will only be for group reports received from another port.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): This object contains the traffic group information configured in the trafficGroup object.
        - UpResponseMode (bool): Report to all unsolicited-causes each simulated host to automatically send full memberships messages at regular intervals.
        - Version (str(igmpv1 | igmpv2 | igmpv3)): Sets the IGMP version number that is to be simulated on the host: 1, 2, or 3.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        GqResponseMode=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        ReportFreq=None,
        RespToQueryImmediately=None,
        RobustnessVariable=None,
        RouterAlert=None,
        SqResponseMode=None,
        SuppressReports=None,
        TrafficGroupId=None,
        UpResponseMode=None,
        Version=None,
    ):
        # type: (bool, bool, str, int, str, str, int, bool, int, bool, bool, bool, str, bool, str) -> Host
        """Adds a new host resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the use of the host in the IGMP simulation.
        - GqResponseMode (bool): If enabled, responds to General Query messages (where the Group Address field and Number of Sources Field = 0). This query message is sent by a multicast router so it can learn about the complete multicast reception state for each of the neighboring interfaces. interfaces.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This is a local ID and is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this IGMP interface.
        - InterfaceType (str): The type of interface to be selected for this IGMP interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - ReportFreq (number): When the mode is report to all unsolicited, this is the frequency in seconds with unsolicited messages are generated.
        - RespToQueryImmediately (bool): If enabled, the state machine will ignore the value specified in the maximum response delay in the membership query message, assume that the delay is always 0 seconds, and immediately responds to the query by sending a report.
        - RobustnessVariable (number): NOT DEFINED
        - RouterAlert (bool): Sets the IP header Send Router Alert bit.
        - SqResponseMode (bool): If enabled, responds to Group-Specific Query messages. This query message is sent by a multicast router so it can learn about the multicast reception state, concerning one multicast address, for each of the neighboring interfaces; for example, when member leaves a group.
        - SuppressReports (bool): Suppress generation of V3 reports on receipt of v1/v2 reports having common groups. If enabled, it indicates that a host/group member will allow its IGMPv3 Membership Record to be suppressed by a membership report for Version 1 or 2. The suppression will only be for group reports received from another port.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): This object contains the traffic group information configured in the trafficGroup object.
        - UpResponseMode (bool): Report to all unsolicited-causes each simulated host to automatically send full memberships messages at regular intervals.
        - Version (str(igmpv1 | igmpv2 | igmpv3)): Sets the IGMP version number that is to be simulated on the host: 1, 2, or 3.

        Returns
        -------
        - self: This instance with all currently retrieved host resources using find and the newly added host resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained host resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        GqResponseMode=None,
        InterfaceId=None,
        InterfaceIndex=None,
        InterfaceType=None,
        Interfaces=None,
        ReportFreq=None,
        RespToQueryImmediately=None,
        RobustnessVariable=None,
        RouterAlert=None,
        SqResponseMode=None,
        SuppressReports=None,
        TrafficGroupId=None,
        UpResponseMode=None,
        Version=None,
    ):
        # type: (bool, bool, str, int, str, str, int, bool, int, bool, bool, bool, str, bool, str) -> Host
        """Finds and retrieves host resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve host resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all host resources from the server.

        Args
        ----
        - Enabled (bool): Enables the use of the host in the IGMP simulation.
        - GqResponseMode (bool): If enabled, responds to General Query messages (where the Group Address field and Number of Sources Field = 0). This query message is sent by a multicast router so it can learn about the complete multicast reception state for each of the neighboring interfaces. interfaces.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): This is a local ID and is unique per router.
        - InterfaceIndex (number): The assigned protocol interface ID for this IGMP interface.
        - InterfaceType (str): The type of interface to be selected for this IGMP interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/interface | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/atm/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/dhcpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ip/l2tpEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/ipEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernet/pppoxEndpoint/range | /api/v1/sessions/1/ixnetwork/vport/protocolStack/ethernetEndpoint/range)): The interfaces that are associated with the selected interface type.
        - ReportFreq (number): When the mode is report to all unsolicited, this is the frequency in seconds with unsolicited messages are generated.
        - RespToQueryImmediately (bool): If enabled, the state machine will ignore the value specified in the maximum response delay in the membership query message, assume that the delay is always 0 seconds, and immediately responds to the query by sending a report.
        - RobustnessVariable (number): NOT DEFINED
        - RouterAlert (bool): Sets the IP header Send Router Alert bit.
        - SqResponseMode (bool): If enabled, responds to Group-Specific Query messages. This query message is sent by a multicast router so it can learn about the multicast reception state, concerning one multicast address, for each of the neighboring interfaces; for example, when member leaves a group.
        - SuppressReports (bool): Suppress generation of V3 reports on receipt of v1/v2 reports having common groups. If enabled, it indicates that a host/group member will allow its IGMPv3 Membership Record to be suppressed by a membership report for Version 1 or 2. The suppression will only be for group reports received from another port.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): This object contains the traffic group information configured in the trafficGroup object.
        - UpResponseMode (bool): Report to all unsolicited-causes each simulated host to automatically send full memberships messages at regular intervals.
        - Version (str(igmpv1 | igmpv2 | igmpv3)): Sets the IGMP version number that is to be simulated on the host: 1, 2, or 3.

        Returns
        -------
        - self: This instance with matching host resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of host data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the host resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Fetches interface accessor Iface list.

        getInterfaceAccessorIfaceList(async_operation=bool)string
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

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
            "getInterfaceAccessorIfaceList", payload=payload, response_object=None
        )
