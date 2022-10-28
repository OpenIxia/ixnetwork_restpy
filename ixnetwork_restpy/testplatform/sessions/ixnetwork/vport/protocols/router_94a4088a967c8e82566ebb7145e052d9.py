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


class Router(Base):
    """The router object represents a simulated router. In addition to some identifying options, it holds four lists for the router: (1) Advertise FEC Range-FECs to be advertised by the simulated router. (2)  Interfaces-router interface. (3) L2 VPN Interfaces-Layer 2 VPN interfaces used in establishing VPNs. (4) Explicit Include List-an optional list of IP FECs used to filter received FECs. This allows the simulated router to ignore all other FECs.
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "router"
    _SDM_ATT_MAP = {
        "EnableBfdMplsLearnedLsp": "enableBfdMplsLearnedLsp",
        "EnableFilterFec": "enableFilterFec",
        "EnableGracefulRestart": "enableGracefulRestart",
        "EnableLspPingLearnedLsp": "enableLspPingLearnedLsp",
        "EnableOverrideRbit": "enableOverrideRbit",
        "EnableP2mpCapabilty": "enableP2mpCapabilty",
        "EnablePduRateControl": "enablePduRateControl",
        "EnableVcFecs": "enableVcFecs",
        "EnableVcGroupMatch": "enableVcGroupMatch",
        "Enabled": "enabled",
        "InterPduGap": "interPduGap",
        "IsBgpAdVplsLearnedInfoRefreshed": "isBgpAdVplsLearnedInfoRefreshed",
        "ReconnectTime": "reconnectTime",
        "RecoveryTime": "recoveryTime",
        "RouterId": "routerId",
        "TrafficGroupId": "trafficGroupId",
        "TransportAddress": "transportAddress",
        "UseTransportAddress": "useTransportAddress",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Router, self).__init__(parent, list_op)

    @property
    def AdvFecRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advfecrange_f00588596498857b75d5d898ca2e9a6f.AdvFecRange): An instance of the AdvFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.advfecrange_f00588596498857b75d5d898ca2e9a6f import (
            AdvFecRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AdvFecRange", None) is not None:
                return self._properties.get("AdvFecRange")
        return AdvFecRange(self)

    @property
    def IncludeIpFecRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.includeipfecrange_373b75680a1f0ec85775f1ba1a1428c8.IncludeIpFecRange): An instance of the IncludeIpFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.includeipfecrange_373b75680a1f0ec85775f1ba1a1428c8 import (
            IncludeIpFecRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IncludeIpFecRange", None) is not None:
                return self._properties.get("IncludeIpFecRange")
        return IncludeIpFecRange(self)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_fe0b08fd21beb5f4d59f82e4c9b072a9.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_fe0b08fd21beb5f4d59f82e4c9b072a9 import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def L2Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2interface_3d1eb8aa91ce49d1264d0d3e9350426f.L2Interface): An instance of the L2Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2interface_3d1eb8aa91ce49d1264d0d3e9350426f import (
            L2Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L2Interface", None) is not None:
                return self._properties.get("L2Interface")
        return L2Interface(self)

    @property
    def LearnedBgpAdVplsLabels(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbgpadvplslabels_d636c7428c14c72b574463ac879c4b82.LearnedBgpAdVplsLabels): An instance of the LearnedBgpAdVplsLabels class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedbgpadvplslabels_d636c7428c14c72b574463ac879c4b82 import (
            LearnedBgpAdVplsLabels,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedBgpAdVplsLabels", None) is not None:
                return self._properties.get("LearnedBgpAdVplsLabels")
        return LearnedBgpAdVplsLabels(self)

    @property
    def MulticastLeafRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastleafrange_61982e4d7933d5db8e1c6734f344bc95.MulticastLeafRange): An instance of the MulticastLeafRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastleafrange_61982e4d7933d5db8e1c6734f344bc95 import (
            MulticastLeafRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastLeafRange", None) is not None:
                return self._properties.get("MulticastLeafRange")
        return MulticastLeafRange(self)

    @property
    def MulticastRootRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastrootrange_2ba3e3319b567aec9e33e2c02f700b75.MulticastRootRange): An instance of the MulticastRootRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.multicastrootrange_2ba3e3319b567aec9e33e2c02f700b75 import (
            MulticastRootRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MulticastRootRange", None) is not None:
                return self._properties.get("MulticastRootRange")
        return MulticastRootRange(self)

    @property
    def ReqFecRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.reqfecrange_c17e1dc9cea7640db4f5e99196ecfcff.ReqFecRange): An instance of the ReqFecRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.reqfecrange_c17e1dc9cea7640db4f5e99196ecfcff import (
            ReqFecRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ReqFecRange", None) is not None:
                return self._properties.get("ReqFecRange")
        return ReqFecRange(self)

    @property
    def EnableBfdMplsLearnedLsp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableBfdMplsLearnedLsp"])

    @EnableBfdMplsLearnedLsp.setter
    def EnableBfdMplsLearnedLsp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableBfdMplsLearnedLsp"], value)

    @property
    def EnableFilterFec(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFilterFec"])

    @EnableFilterFec.setter
    def EnableFilterFec(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFilterFec"], value)

    @property
    def EnableGracefulRestart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGracefulRestart"])

    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGracefulRestart"], value)

    @property
    def EnableLspPingLearnedLsp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLspPingLearnedLsp"])

    @EnableLspPingLearnedLsp.setter
    def EnableLspPingLearnedLsp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLspPingLearnedLsp"], value)

    @property
    def EnableOverrideRbit(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableOverrideRbit"])

    @EnableOverrideRbit.setter
    def EnableOverrideRbit(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableOverrideRbit"], value)

    @property
    def EnableP2mpCapabilty(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables P2MP capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableP2mpCapabilty"])

    @EnableP2mpCapabilty.setter
    def EnableP2mpCapabilty(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableP2mpCapabilty"], value)

    @property
    def EnablePduRateControl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the PDU Rate Control feature.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePduRateControl"])

    @EnablePduRateControl.setter
    def EnablePduRateControl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePduRateControl"], value)

    @property
    def EnableVcFecs(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of Layer 2 Virtual Circuit FECs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVcFecs"])

    @EnableVcFecs.setter
    def EnableVcFecs(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVcFecs"], value)

    @property
    def EnableVcGroupMatch(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableVcGroupMatch"])

    @EnableVcGroupMatch.setter
    def EnableVcGroupMatch(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableVcGroupMatch"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def InterPduGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The user-specified gap time between PDUs, in milliseconds (ms).
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterPduGap"])

    @InterPduGap.setter
    def InterPduGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterPduGap"], value)

    @property
    def IsBgpAdVplsLearnedInfoRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Refreshes the AD VPLS Learned Info.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsBgpAdVplsLearnedInfoRefreshed"])

    @property
    def ReconnectTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReconnectTime"])

    @ReconnectTime.setter
    def ReconnectTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReconnectTime"], value)

    @property
    def RecoveryTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RecoveryTime"])

    @RecoveryTime.setter
    def RecoveryTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RecoveryTime"], value)

    @property
    def RouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The ID of the simulated router, expressed as an IP address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterId"])

    @RouterId.setter
    def RouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RouterId"], value)

    @property
    def TrafficGroupId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    @property
    def TransportAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/interface): The string interface description for the transport address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransportAddress"])

    @TransportAddress.setter
    def TransportAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransportAddress"], value)

    @property
    def UseTransportAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: The boolean value for the transport address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseTransportAddress"])

    @UseTransportAddress.setter
    def UseTransportAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseTransportAddress"], value)

    def update(
        self,
        EnableBfdMplsLearnedLsp=None,
        EnableFilterFec=None,
        EnableGracefulRestart=None,
        EnableLspPingLearnedLsp=None,
        EnableOverrideRbit=None,
        EnableP2mpCapabilty=None,
        EnablePduRateControl=None,
        EnableVcFecs=None,
        EnableVcGroupMatch=None,
        Enabled=None,
        InterPduGap=None,
        ReconnectTime=None,
        RecoveryTime=None,
        RouterId=None,
        TrafficGroupId=None,
        TransportAddress=None,
        UseTransportAddress=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str, str, bool) -> Router
        """Updates router resource on the server.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): NOT DEFINED
        - EnableFilterFec (bool): Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        - EnableGracefulRestart (bool): If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        - EnableLspPingLearnedLsp (bool): NOT DEFINED
        - EnableOverrideRbit (bool): NOT DEFINED
        - EnableP2mpCapabilty (bool): If true, enables P2MP capability.
        - EnablePduRateControl (bool): Enables the PDU Rate Control feature.
        - EnableVcFecs (bool): Enables the use of Layer 2 Virtual Circuit FECs.
        - EnableVcGroupMatch (bool): If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        - Enabled (bool): Enables or disables the simulated router.
        - InterPduGap (number): The user-specified gap time between PDUs, in milliseconds (ms).
        - ReconnectTime (number): This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        - RecoveryTime (number): The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        - RouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The string interface description for the transport address.
        - UseTransportAddress (bool): The boolean value for the transport address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        EnableBfdMplsLearnedLsp=None,
        EnableFilterFec=None,
        EnableGracefulRestart=None,
        EnableLspPingLearnedLsp=None,
        EnableOverrideRbit=None,
        EnableP2mpCapabilty=None,
        EnablePduRateControl=None,
        EnableVcFecs=None,
        EnableVcGroupMatch=None,
        Enabled=None,
        InterPduGap=None,
        ReconnectTime=None,
        RecoveryTime=None,
        RouterId=None,
        TrafficGroupId=None,
        TransportAddress=None,
        UseTransportAddress=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str, str, bool) -> Router
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): NOT DEFINED
        - EnableFilterFec (bool): Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        - EnableGracefulRestart (bool): If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        - EnableLspPingLearnedLsp (bool): NOT DEFINED
        - EnableOverrideRbit (bool): NOT DEFINED
        - EnableP2mpCapabilty (bool): If true, enables P2MP capability.
        - EnablePduRateControl (bool): Enables the PDU Rate Control feature.
        - EnableVcFecs (bool): Enables the use of Layer 2 Virtual Circuit FECs.
        - EnableVcGroupMatch (bool): If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        - Enabled (bool): Enables or disables the simulated router.
        - InterPduGap (number): The user-specified gap time between PDUs, in milliseconds (ms).
        - ReconnectTime (number): This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        - RecoveryTime (number): The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        - RouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The string interface description for the transport address.
        - UseTransportAddress (bool): The boolean value for the transport address.

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        EnableBfdMplsLearnedLsp=None,
        EnableFilterFec=None,
        EnableGracefulRestart=None,
        EnableLspPingLearnedLsp=None,
        EnableOverrideRbit=None,
        EnableP2mpCapabilty=None,
        EnablePduRateControl=None,
        EnableVcFecs=None,
        EnableVcGroupMatch=None,
        Enabled=None,
        InterPduGap=None,
        IsBgpAdVplsLearnedInfoRefreshed=None,
        ReconnectTime=None,
        RecoveryTime=None,
        RouterId=None,
        TrafficGroupId=None,
        TransportAddress=None,
        UseTransportAddress=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, bool, int, int, str, str, str, bool) -> Router
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - EnableBfdMplsLearnedLsp (bool): NOT DEFINED
        - EnableFilterFec (bool): Enables Filter FEC, which allows the user to control which received FEC ranges will be stored in the state machine.
        - EnableGracefulRestart (bool): If enabled, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
        - EnableLspPingLearnedLsp (bool): NOT DEFINED
        - EnableOverrideRbit (bool): NOT DEFINED
        - EnableP2mpCapabilty (bool): If true, enables P2MP capability.
        - EnablePduRateControl (bool): Enables the PDU Rate Control feature.
        - EnableVcFecs (bool): Enables the use of Layer 2 Virtual Circuit FECs.
        - EnableVcGroupMatch (bool): If enabled, the VC Group ID must be matched in addition to the VC ID, VC Type, and Peer for the PseudoWire to be considered Up (Up status).
        - Enabled (bool): Enables or disables the simulated router.
        - InterPduGap (number): The user-specified gap time between PDUs, in milliseconds (ms).
        - IsBgpAdVplsLearnedInfoRefreshed (bool): Refreshes the AD VPLS Learned Info.
        - ReconnectTime (number): This Fault Tolerant (FT) Reconnect Timer value is advertised in the FT Session TLV in the Initialization message sent by a neighbor LSR. It is a request sent by an LSR to its neighbor(s) in the event that the receiving neighbor detects that the LDP session has failed, the receiver should maintain MPLS forwarding state and wait for the sender to perform a restart of the control plane and LDP protocol. If the value = 0, the sender is indicating that it will not preserve its MPLS forwarding state across the restart.
        - RecoveryTime (number): The restarting LSR is advertising the amount of time that it will retain its MPLS forwarding state. This time period begins when it sends the restart Initialization message, with the FT session TLV, to the neighbor LSRs (to re-establish the LDP session). This timer allows the neighbors some time to resync the LSPs in an orderly manner. If the value = 0, it means that the restarting LSR was not able to preserve the MPLS forwarding state.
        - RouterId (str): The ID of the simulated router, expressed as an IP address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - TransportAddress (str(None | /api/v1/sessions/1/ixnetwork/vport/interface)): The string interface description for the transport address.
        - UseTransportAddress (bool): The boolean value for the transport address.

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshBgpAdVplsLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshBgpAdVplsLearnedInfo operation on the server.

        If enabled, it refreshes BGP advanced LSP learned information.

        refreshBgpAdVplsLearnedInfo(async_operation=bool)bool
        -----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

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
            "refreshBgpAdVplsLearnedInfo", payload=payload, response_object=None
        )
