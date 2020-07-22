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


class Router(Base):
    """A container used to hold three lists associated with the router: route ranges, interfaces, and link state advertisements (LSAs).
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'
    _SDM_ATT_MAP = {
        'DisableAutoGenerateLinkLsa': 'disableAutoGenerateLinkLsa',
        'DisableAutoGenerateRouterLsa': 'disableAutoGenerateRouterLsa',
        'DiscardLearnedLsa': 'discardLearnedLsa',
        'EnableGracefulRestartHelperMode': 'enableGracefulRestartHelperMode',
        'EnableStrictLsaChecking': 'enableStrictLsaChecking',
        'EnableSupportReasonSwReloadOrUpgrade': 'enableSupportReasonSwReloadOrUpgrade',
        'EnableSupportReasonSwRestart': 'enableSupportReasonSwRestart',
        'EnableSupportReasonSwitchToRedundantControlProcessor': 'enableSupportReasonSwitchToRedundantControlProcessor',
        'EnableSupportReasonUnknown': 'enableSupportReasonUnknown',
        'EnableSupportRfc5838': 'enableSupportRfc5838',
        'Enabled': 'enabled',
        'IsLearnedLsaRefreshed': 'isLearnedLsaRefreshed',
        'LsaRefreshTime': 'lsaRefreshTime',
        'LsaRetransmitTime': 'lsaRetransmitTime',
        'MaxNumLsaPerSecond': 'maxNumLsaPerSecond',
        'RouterId': 'routerId',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ee3b04c1da65cc99c5a7a503492ed84b.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_ee3b04c1da65cc99c5a7a503492ed84b import Interface
        return Interface(self)

    @property
    def LearnedLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_833c63bd6c25e1b5eae9fe3cf4256d16.LearnedLsa): An instance of the LearnedLsa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_833c63bd6c25e1b5eae9fe3cf4256d16 import LearnedLsa
        return LearnedLsa(self)

    @property
    def NetworkRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_c0c2b62f912fb146b24872fd01a280b9.NetworkRange): An instance of the NetworkRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_c0c2b62f912fb146b24872fd01a280b9 import NetworkRange
        return NetworkRange(self)

    @property
    def RouteRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_e8b63d512383712e41b15bd4c306347b.RouteRange): An instance of the RouteRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_e8b63d512383712e41b15bd4c306347b import RouteRange
        return RouteRange(self)

    @property
    def UserLsaGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_7795cb447526ddc4b75100787366e015.UserLsaGroup): An instance of the UserLsaGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_7795cb447526ddc4b75100787366e015 import UserLsaGroup
        return UserLsaGroup(self)

    @property
    def DisableAutoGenerateLinkLsa(self):
        """
        Returns
        -------
        - bool: If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableAutoGenerateLinkLsa'])
    @DisableAutoGenerateLinkLsa.setter
    def DisableAutoGenerateLinkLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableAutoGenerateLinkLsa'], value)

    @property
    def DisableAutoGenerateRouterLsa(self):
        """
        Returns
        -------
        - bool: If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableAutoGenerateRouterLsa'])
    @DisableAutoGenerateRouterLsa.setter
    def DisableAutoGenerateRouterLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DisableAutoGenerateRouterLsa'], value)

    @property
    def DiscardLearnedLsa(self):
        """
        Returns
        -------
        - bool: If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa'])
    @DiscardLearnedLsa.setter
    def DiscardLearnedLsa(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DiscardLearnedLsa'], value)

    @property
    def EnableGracefulRestartHelperMode(self):
        """
        Returns
        -------
        - bool: Enables the OSPF Router to act as Helper during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode'])
    @EnableGracefulRestartHelperMode.setter
    def EnableGracefulRestartHelperMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableGracefulRestartHelperMode'], value)

    @property
    def EnableStrictLsaChecking(self):
        """
        Returns
        -------
        - bool: Enables Strict LSA Checking during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStrictLsaChecking'])
    @EnableStrictLsaChecking.setter
    def EnableStrictLsaChecking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableStrictLsaChecking'], value)

    @property
    def EnableSupportReasonSwReloadOrUpgrade(self):
        """
        Returns
        -------
        - bool: Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwReloadOrUpgrade'])
    @EnableSupportReasonSwReloadOrUpgrade.setter
    def EnableSupportReasonSwReloadOrUpgrade(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwReloadOrUpgrade'], value)

    @property
    def EnableSupportReasonSwRestart(self):
        """
        Returns
        -------
        - bool: Sets the reason as Software Restart in Grace LSA during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwRestart'])
    @EnableSupportReasonSwRestart.setter
    def EnableSupportReasonSwRestart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwRestart'], value)

    @property
    def EnableSupportReasonSwitchToRedundantControlProcessor(self):
        """
        Returns
        -------
        - bool: Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwitchToRedundantControlProcessor'])
    @EnableSupportReasonSwitchToRedundantControlProcessor.setter
    def EnableSupportReasonSwitchToRedundantControlProcessor(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonSwitchToRedundantControlProcessor'], value)

    @property
    def EnableSupportReasonUnknown(self):
        """
        Returns
        -------
        - bool: Sets the reason as Unknown in Grace LSA during Graceful Restart
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportReasonUnknown'])
    @EnableSupportReasonUnknown.setter
    def EnableSupportReasonUnknown(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportReasonUnknown'], value)

    @property
    def EnableSupportRfc5838(self):
        """
        Returns
        -------
        - bool: Enables support for RFC5838
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSupportRfc5838'])
    @EnableSupportRfc5838.setter
    def EnableSupportRfc5838(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSupportRfc5838'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IsLearnedLsaRefreshed(self):
        """
        Returns
        -------
        - bool: If true, learned OSPF LSA information is refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsLearnedLsaRefreshed'])

    @property
    def LsaRefreshTime(self):
        """
        Returns
        -------
        - number: Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaRefreshTime'])
    @LsaRefreshTime.setter
    def LsaRefreshTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaRefreshTime'], value)

    @property
    def LsaRetransmitTime(self):
        """
        Returns
        -------
        - number: Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
        """
        return self._get_attribute(self._SDM_ATT_MAP['LsaRetransmitTime'])
    @LsaRetransmitTime.setter
    def LsaRetransmitTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LsaRetransmitTime'], value)

    @property
    def MaxNumLsaPerSecond(self):
        """
        Returns
        -------
        - number: Limits the number of LSAs that will be sent per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNumLsaPerSecond'])
    @MaxNumLsaPerSecond.setter
    def MaxNumLsaPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxNumLsaPerSecond'], value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: Used to set the ID of the router, expressed as an IPv4 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterId'])
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterId'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
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
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
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
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

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

    def find(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, IsLearnedLsaRefreshed=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
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
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

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
        """Executes the gracefulRouterRestart operation on the server.

        NOT DEFINED

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        gracefulRouterRestart(Arg2=number, Arg3=enum, Arg4=number)string
        ----------------------------------------------------------------
        - Arg2 (number): NOT DEFINED
        - Arg3 (str(softwareReloadOrUpgrade | softwareRestart | switchToRedundantControlProcessor | unknown)): NOT DEFINED
        - Arg4 (number): NOT DEFINED
        - Returns str: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('gracefulRouterRestart', payload=payload, response_object=None)

    def RefreshLearnedLsa(self):
        """Executes the refreshLearnedLsa operation on the server.

        This exec refreshes the learned OSPFv3 LSA from the DUT.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedLsa', payload=payload, response_object=None)
