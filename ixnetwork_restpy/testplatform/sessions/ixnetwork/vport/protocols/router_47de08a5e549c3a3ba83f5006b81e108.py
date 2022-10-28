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
    """A container used to hold three lists associated with the router: route ranges, interfaces, and link state advertisements (LSAs).
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "router"
    _SDM_ATT_MAP = {
        "DisableAutoGenerateLinkLsa": "disableAutoGenerateLinkLsa",
        "DisableAutoGenerateRouterLsa": "disableAutoGenerateRouterLsa",
        "DiscardLearnedLsa": "discardLearnedLsa",
        "EnableGracefulRestartHelperMode": "enableGracefulRestartHelperMode",
        "EnableStrictLsaChecking": "enableStrictLsaChecking",
        "EnableSupportReasonSwReloadOrUpgrade": "enableSupportReasonSwReloadOrUpgrade",
        "EnableSupportReasonSwRestart": "enableSupportReasonSwRestart",
        "EnableSupportReasonSwitchToRedundantControlProcessor": "enableSupportReasonSwitchToRedundantControlProcessor",
        "EnableSupportReasonUnknown": "enableSupportReasonUnknown",
        "EnableSupportRfc5838": "enableSupportRfc5838",
        "Enabled": "enabled",
        "IsLearnedLsaRefreshed": "isLearnedLsaRefreshed",
        "LsaRefreshTime": "lsaRefreshTime",
        "LsaRetransmitTime": "lsaRetransmitTime",
        "MaxNumLsaPerSecond": "maxNumLsaPerSecond",
        "RouterId": "routerId",
        "TrafficGroupId": "trafficGroupId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Router, self).__init__(parent, list_op)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_05b544e75dae141da1eeb5726765435f.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_05b544e75dae141da1eeb5726765435f import (
            Interface,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Interface", None) is not None:
                return self._properties.get("Interface")
        return Interface(self)

    @property
    def LearnedLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_5a5a3bb7d08624879255d8188cb002d8.LearnedLsa): An instance of the LearnedLsa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_5a5a3bb7d08624879255d8188cb002d8 import (
            LearnedLsa,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedLsa", None) is not None:
                return self._properties.get("LearnedLsa")
        return LearnedLsa(self)

    @property
    def NetworkRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_5d63b4cd2c8ae562232173bdbadc81d3.NetworkRange): An instance of the NetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_5d63b4cd2c8ae562232173bdbadc81d3 import (
            NetworkRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NetworkRange", None) is not None:
                return self._properties.get("NetworkRange")
        return NetworkRange(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_2723793fa0b18ac84ab4fdc31f738a00.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_2723793fa0b18ac84ab4fdc31f738a00 import (
            RouteRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RouteRange", None) is not None:
                return self._properties.get("RouteRange")
        return RouteRange(self)

    @property
    def UserLsaGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_1240248adae59823c47663d14e20498e.UserLsaGroup): An instance of the UserLsaGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_1240248adae59823c47663d14e20498e import (
            UserLsaGroup,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UserLsaGroup", None) is not None:
                return self._properties.get("UserLsaGroup")
        return UserLsaGroup(self)

    @property
    def DisableAutoGenerateLinkLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableAutoGenerateLinkLsa"])

    @DisableAutoGenerateLinkLsa.setter
    def DisableAutoGenerateLinkLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableAutoGenerateLinkLsa"], value)

    @property
    def DisableAutoGenerateRouterLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DisableAutoGenerateRouterLsa"])

    @DisableAutoGenerateRouterLsa.setter
    def DisableAutoGenerateRouterLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DisableAutoGenerateRouterLsa"], value)

    @property
    def DiscardLearnedLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DiscardLearnedLsa"])

    @DiscardLearnedLsa.setter
    def DiscardLearnedLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DiscardLearnedLsa"], value)

    @property
    def EnableGracefulRestartHelperMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the OSPF Router to act as Helper during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableGracefulRestartHelperMode"])

    @EnableGracefulRestartHelperMode.setter
    def EnableGracefulRestartHelperMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableGracefulRestartHelperMode"], value)

    @property
    def EnableStrictLsaChecking(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables Strict LSA Checking during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableStrictLsaChecking"])

    @EnableStrictLsaChecking.setter
    def EnableStrictLsaChecking(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableStrictLsaChecking"], value)

    @property
    def EnableSupportReasonSwReloadOrUpgrade(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSupportReasonSwReloadOrUpgrade"]
        )

    @EnableSupportReasonSwReloadOrUpgrade.setter
    def EnableSupportReasonSwReloadOrUpgrade(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSupportReasonSwReloadOrUpgrade"], value
        )

    @property
    def EnableSupportReasonSwRestart(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the reason as Software Restart in Grace LSA during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSupportReasonSwRestart"])

    @EnableSupportReasonSwRestart.setter
    def EnableSupportReasonSwRestart(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSupportReasonSwRestart"], value)

    @property
    def EnableSupportReasonSwitchToRedundantControlProcessor(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableSupportReasonSwitchToRedundantControlProcessor"]
        )

    @EnableSupportReasonSwitchToRedundantControlProcessor.setter
    def EnableSupportReasonSwitchToRedundantControlProcessor(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableSupportReasonSwitchToRedundantControlProcessor"],
            value,
        )

    @property
    def EnableSupportReasonUnknown(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Sets the reason as Unknown in Grace LSA during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSupportReasonUnknown"])

    @EnableSupportReasonUnknown.setter
    def EnableSupportReasonUnknown(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSupportReasonUnknown"], value)

    @property
    def EnableSupportRfc5838(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables support for RFC5838
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSupportRfc5838"])

    @EnableSupportRfc5838.setter
    def EnableSupportRfc5838(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSupportRfc5838"], value)

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
    def IsLearnedLsaRefreshed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, learned OSPF LSA information is refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsLearnedLsaRefreshed"])

    @property
    def LsaRefreshTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsaRefreshTime"])

    @LsaRefreshTime.setter
    def LsaRefreshTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsaRefreshTime"], value)

    @property
    def LsaRetransmitTime(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
        """
        return self._get_attribute(self._SDM_ATT_MAP["LsaRetransmitTime"])

    @LsaRetransmitTime.setter
    def LsaRetransmitTime(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LsaRetransmitTime"], value)

    @property
    def MaxNumLsaPerSecond(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Limits the number of LSAs that will be sent per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxNumLsaPerSecond"])

    @MaxNumLsaPerSecond.setter
    def MaxNumLsaPerSecond(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxNumLsaPerSecond"], value)

    @property
    def RouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Used to set the ID of the router, expressed as an IPv4 address.
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
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficGroupId"])

    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficGroupId"], value)

    def update(
        self,
        DisableAutoGenerateLinkLsa=None,
        DisableAutoGenerateRouterLsa=None,
        DiscardLearnedLsa=None,
        EnableGracefulRestartHelperMode=None,
        EnableStrictLsaChecking=None,
        EnableSupportReasonSwReloadOrUpgrade=None,
        EnableSupportReasonSwRestart=None,
        EnableSupportReasonSwitchToRedundantControlProcessor=None,
        EnableSupportReasonUnknown=None,
        EnableSupportRfc5838=None,
        Enabled=None,
        LsaRefreshTime=None,
        LsaRetransmitTime=None,
        MaxNumLsaPerSecond=None,
        RouterId=None,
        TrafficGroupId=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str) -> Router
        """Updates router resource on the server.

        Args
        ----
        - DisableAutoGenerateLinkLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
        - DisableAutoGenerateRouterLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
        - DiscardLearnedLsa (bool): If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
        - EnableGracefulRestartHelperMode (bool): Enables the OSPF Router to act as Helper during Graceful Restart
        - EnableStrictLsaChecking (bool): Enables Strict LSA Checking during Graceful Restart
        - EnableSupportReasonSwReloadOrUpgrade (bool): Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
        - EnableSupportReasonSwRestart (bool): Sets the reason as Software Restart in Grace LSA during Graceful Restart
        - EnableSupportReasonSwitchToRedundantControlProcessor (bool): Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
        - EnableSupportReasonUnknown (bool): Sets the reason as Unknown in Grace LSA during Graceful Restart
        - EnableSupportRfc5838 (bool): Enables support for RFC5838
        - Enabled (bool): Enables or disables the simulated router.
        - LsaRefreshTime (number): Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
        - LsaRetransmitTime (number): Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
        - MaxNumLsaPerSecond (number): Limits the number of LSAs that will be sent per second.
        - RouterId (str): Used to set the ID of the router, expressed as an IPv4 address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        DisableAutoGenerateLinkLsa=None,
        DisableAutoGenerateRouterLsa=None,
        DiscardLearnedLsa=None,
        EnableGracefulRestartHelperMode=None,
        EnableStrictLsaChecking=None,
        EnableSupportReasonSwReloadOrUpgrade=None,
        EnableSupportReasonSwRestart=None,
        EnableSupportReasonSwitchToRedundantControlProcessor=None,
        EnableSupportReasonUnknown=None,
        EnableSupportRfc5838=None,
        Enabled=None,
        LsaRefreshTime=None,
        LsaRetransmitTime=None,
        MaxNumLsaPerSecond=None,
        RouterId=None,
        TrafficGroupId=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str) -> Router
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - DisableAutoGenerateLinkLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
        - DisableAutoGenerateRouterLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
        - DiscardLearnedLsa (bool): If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
        - EnableGracefulRestartHelperMode (bool): Enables the OSPF Router to act as Helper during Graceful Restart
        - EnableStrictLsaChecking (bool): Enables Strict LSA Checking during Graceful Restart
        - EnableSupportReasonSwReloadOrUpgrade (bool): Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
        - EnableSupportReasonSwRestart (bool): Sets the reason as Software Restart in Grace LSA during Graceful Restart
        - EnableSupportReasonSwitchToRedundantControlProcessor (bool): Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
        - EnableSupportReasonUnknown (bool): Sets the reason as Unknown in Grace LSA during Graceful Restart
        - EnableSupportRfc5838 (bool): Enables support for RFC5838
        - Enabled (bool): Enables or disables the simulated router.
        - LsaRefreshTime (number): Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
        - LsaRetransmitTime (number): Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
        - MaxNumLsaPerSecond (number): Limits the number of LSAs that will be sent per second.
        - RouterId (str): Used to set the ID of the router, expressed as an IPv4 address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

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
        DisableAutoGenerateLinkLsa=None,
        DisableAutoGenerateRouterLsa=None,
        DiscardLearnedLsa=None,
        EnableGracefulRestartHelperMode=None,
        EnableStrictLsaChecking=None,
        EnableSupportReasonSwReloadOrUpgrade=None,
        EnableSupportReasonSwRestart=None,
        EnableSupportReasonSwitchToRedundantControlProcessor=None,
        EnableSupportReasonUnknown=None,
        EnableSupportRfc5838=None,
        Enabled=None,
        IsLearnedLsaRefreshed=None,
        LsaRefreshTime=None,
        LsaRetransmitTime=None,
        MaxNumLsaPerSecond=None,
        RouterId=None,
        TrafficGroupId=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, int, int, int, str, str) -> Router
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - DisableAutoGenerateLinkLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
        - DisableAutoGenerateRouterLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
        - DiscardLearnedLsa (bool): If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
        - EnableGracefulRestartHelperMode (bool): Enables the OSPF Router to act as Helper during Graceful Restart
        - EnableStrictLsaChecking (bool): Enables Strict LSA Checking during Graceful Restart
        - EnableSupportReasonSwReloadOrUpgrade (bool): Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
        - EnableSupportReasonSwRestart (bool): Sets the reason as Software Restart in Grace LSA during Graceful Restart
        - EnableSupportReasonSwitchToRedundantControlProcessor (bool): Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
        - EnableSupportReasonUnknown (bool): Sets the reason as Unknown in Grace LSA during Graceful Restart
        - EnableSupportRfc5838 (bool): Enables support for RFC5838
        - Enabled (bool): Enables or disables the simulated router.
        - IsLearnedLsaRefreshed (bool): If true, learned OSPF LSA information is refreshed.
        - LsaRefreshTime (number): Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
        - LsaRetransmitTime (number): Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
        - MaxNumLsaPerSecond (number): Limits the number of LSAs that will be sent per second.
        - RouterId (str): Used to set the ID of the router, expressed as an IPv4 address.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

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

    def GracefulRouterRestart(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the gracefulRouterRestart operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        gracefulRouterRestart(async_operation=bool)string
        -------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

        gracefulRouterRestart(Arg2=number, Arg3=enum, Arg4=number, async_operation=bool)string
        --------------------------------------------------------------------------------------
        - Arg2 (number): NOT DEFINED
        - Arg3 (str(softwareReloadOrUpgrade | softwareRestart | switchToRedundantControlProcessor | unknown)): NOT DEFINED
        - Arg4 (number): NOT DEFINED
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
            "gracefulRouterRestart", payload=payload, response_object=None
        )

    def RefreshLearnedLsa(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshLearnedLsa operation on the server.

        This exec refreshes the learned OSPFv3 LSA from the DUT.

        refreshLearnedLsa(async_operation=bool)bool
        -------------------------------------------
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
        return self._execute("refreshLearnedLsa", payload=payload, response_object=None)
