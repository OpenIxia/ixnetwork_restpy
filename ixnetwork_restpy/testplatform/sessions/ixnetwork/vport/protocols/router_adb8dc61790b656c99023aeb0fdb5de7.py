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


class Router(Base):
    """A container used to hold three lists associated with the router: route ranges, interfaces, and link state advertisements (LSAs).
    The Router class encapsulates a list of router resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by the user by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def Interface(self):
        """An instance of the Interface class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_dfe5c3eb4fd57765f405f17253549393.Interface)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_dfe5c3eb4fd57765f405f17253549393 import Interface
        return Interface(self)

    @property
    def LearnedLsa(self):
        """An instance of the LearnedLsa class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_0f677fe648c14477348cfc6613db77c5.LearnedLsa)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedlsa_0f677fe648c14477348cfc6613db77c5 import LearnedLsa
        return LearnedLsa(self)

    @property
    def NetworkRange(self):
        """An instance of the NetworkRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_1924c3e98184e589965f8510ef44cd40.NetworkRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.networkrange_1924c3e98184e589965f8510ef44cd40 import NetworkRange
        return NetworkRange(self)

    @property
    def RouteRange(self):
        """An instance of the RouteRange class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_ad07da82b6de7182c805e4f1d50d801e.RouteRange)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routerange_ad07da82b6de7182c805e4f1d50d801e import RouteRange
        return RouteRange(self)

    @property
    def UserLsaGroup(self):
        """An instance of the UserLsaGroup class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_3b8786ad2bb397cc30d956f08d4a4ded.UserLsaGroup)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsagroup_3b8786ad2bb397cc30d956f08d4a4ded import UserLsaGroup
        return UserLsaGroup(self)

    @property
    def DisableAutoGenerateLinkLsa(self):
        """If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.

        Returns:
            bool
        """
        return self._get_attribute('disableAutoGenerateLinkLsa')
    @DisableAutoGenerateLinkLsa.setter
    def DisableAutoGenerateLinkLsa(self, value):
        self._set_attribute('disableAutoGenerateLinkLsa', value)

    @property
    def DisableAutoGenerateRouterLsa(self):
        """If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.

        Returns:
            bool
        """
        return self._get_attribute('disableAutoGenerateRouterLsa')
    @DisableAutoGenerateRouterLsa.setter
    def DisableAutoGenerateRouterLsa(self, value):
        self._set_attribute('disableAutoGenerateRouterLsa', value)

    @property
    def DiscardLearnedLsa(self):
        """If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.

        Returns:
            bool
        """
        return self._get_attribute('discardLearnedLsa')
    @DiscardLearnedLsa.setter
    def DiscardLearnedLsa(self, value):
        self._set_attribute('discardLearnedLsa', value)

    @property
    def EnableGracefulRestartHelperMode(self):
        """Enables the OSPF Router to act as Helper during Graceful Restart

        Returns:
            bool
        """
        return self._get_attribute('enableGracefulRestartHelperMode')
    @EnableGracefulRestartHelperMode.setter
    def EnableGracefulRestartHelperMode(self, value):
        self._set_attribute('enableGracefulRestartHelperMode', value)

    @property
    def EnableStrictLsaChecking(self):
        """Enables Strict LSA Checking during Graceful Restart

        Returns:
            bool
        """
        return self._get_attribute('enableStrictLsaChecking')
    @EnableStrictLsaChecking.setter
    def EnableStrictLsaChecking(self, value):
        self._set_attribute('enableStrictLsaChecking', value)

    @property
    def EnableSupportReasonSwReloadOrUpgrade(self):
        """Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart

        Returns:
            bool
        """
        return self._get_attribute('enableSupportReasonSwReloadOrUpgrade')
    @EnableSupportReasonSwReloadOrUpgrade.setter
    def EnableSupportReasonSwReloadOrUpgrade(self, value):
        self._set_attribute('enableSupportReasonSwReloadOrUpgrade', value)

    @property
    def EnableSupportReasonSwRestart(self):
        """Sets the reason as Software Restart in Grace LSA during Graceful Restart

        Returns:
            bool
        """
        return self._get_attribute('enableSupportReasonSwRestart')
    @EnableSupportReasonSwRestart.setter
    def EnableSupportReasonSwRestart(self, value):
        self._set_attribute('enableSupportReasonSwRestart', value)

    @property
    def EnableSupportReasonSwitchToRedundantControlProcessor(self):
        """Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart

        Returns:
            bool
        """
        return self._get_attribute('enableSupportReasonSwitchToRedundantControlProcessor')
    @EnableSupportReasonSwitchToRedundantControlProcessor.setter
    def EnableSupportReasonSwitchToRedundantControlProcessor(self, value):
        self._set_attribute('enableSupportReasonSwitchToRedundantControlProcessor', value)

    @property
    def EnableSupportReasonUnknown(self):
        """Sets the reason as Unknown in Grace LSA during Graceful Restart

        Returns:
            bool
        """
        return self._get_attribute('enableSupportReasonUnknown')
    @EnableSupportReasonUnknown.setter
    def EnableSupportReasonUnknown(self, value):
        self._set_attribute('enableSupportReasonUnknown', value)

    @property
    def EnableSupportRfc5838(self):
        """Enables support for RFC5838

        Returns:
            bool
        """
        return self._get_attribute('enableSupportRfc5838')
    @EnableSupportRfc5838.setter
    def EnableSupportRfc5838(self, value):
        self._set_attribute('enableSupportRfc5838', value)

    @property
    def Enabled(self):
        """Enables or disables the simulated router.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IsLearnedLsaRefreshed(self):
        """If true, learned OSPF LSA information is refreshed.

        Returns:
            bool
        """
        return self._get_attribute('isLearnedLsaRefreshed')

    @property
    def LsaRefreshTime(self):
        """Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA

        Returns:
            number
        """
        return self._get_attribute('lsaRefreshTime')
    @LsaRefreshTime.setter
    def LsaRefreshTime(self, value):
        self._set_attribute('lsaRefreshTime', value)

    @property
    def LsaRetransmitTime(self):
        """Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received

        Returns:
            number
        """
        return self._get_attribute('lsaRetransmitTime')
    @LsaRetransmitTime.setter
    def LsaRetransmitTime(self, value):
        self._set_attribute('lsaRetransmitTime', value)

    @property
    def MaxNumLsaPerSecond(self):
        """Limits the number of LSAs that will be sent per second.

        Returns:
            number
        """
        return self._get_attribute('maxNumLsaPerSecond')
    @MaxNumLsaPerSecond.setter
    def MaxNumLsaPerSecond(self, value):
        self._set_attribute('maxNumLsaPerSecond', value)

    @property
    def RouterId(self):
        """Used to set the ID of the router, expressed as an IPv4 address.

        Returns:
            str
        """
        return self._get_attribute('routerId')
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute('routerId', value)

    @property
    def TrafficGroupId(self):
        """The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)
        """
        return self._get_attribute('trafficGroupId')
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute('trafficGroupId', value)

    def update(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
        """Updates a child instance of router on the server.

        Args:
            DisableAutoGenerateLinkLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
            DisableAutoGenerateRouterLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
            DiscardLearnedLsa (bool): If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
            EnableGracefulRestartHelperMode (bool): Enables the OSPF Router to act as Helper during Graceful Restart
            EnableStrictLsaChecking (bool): Enables Strict LSA Checking during Graceful Restart
            EnableSupportReasonSwReloadOrUpgrade (bool): Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
            EnableSupportReasonSwRestart (bool): Sets the reason as Software Restart in Grace LSA during Graceful Restart
            EnableSupportReasonSwitchToRedundantControlProcessor (bool): Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
            EnableSupportReasonUnknown (bool): Sets the reason as Unknown in Grace LSA during Graceful Restart
            EnableSupportRfc5838 (bool): Enables support for RFC5838
            Enabled (bool): Enables or disables the simulated router.
            LsaRefreshTime (number): Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
            LsaRetransmitTime (number): Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
            MaxNumLsaPerSecond (number): Limits the number of LSAs that will be sent per second.
            RouterId (str): Used to set the ID of the router, expressed as an IPv4 address.
            TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
        """Adds a new router node on the server and retrieves it in this instance.

        Args:
            DisableAutoGenerateLinkLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
            DisableAutoGenerateRouterLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
            DiscardLearnedLsa (bool): If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
            EnableGracefulRestartHelperMode (bool): Enables the OSPF Router to act as Helper during Graceful Restart
            EnableStrictLsaChecking (bool): Enables Strict LSA Checking during Graceful Restart
            EnableSupportReasonSwReloadOrUpgrade (bool): Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
            EnableSupportReasonSwRestart (bool): Sets the reason as Software Restart in Grace LSA during Graceful Restart
            EnableSupportReasonSwitchToRedundantControlProcessor (bool): Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
            EnableSupportReasonUnknown (bool): Sets the reason as Unknown in Grace LSA during Graceful Restart
            EnableSupportRfc5838 (bool): Enables support for RFC5838
            Enabled (bool): Enables or disables the simulated router.
            LsaRefreshTime (number): Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
            LsaRetransmitTime (number): Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
            MaxNumLsaPerSecond (number): Limits the number of LSAs that will be sent per second.
            RouterId (str): Used to set the ID of the router, expressed as an IPv4 address.
            TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns:
            self: This instance with all currently retrieved router data using find and the newly added router data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the router data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadOrUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, EnableSupportRfc5838=None, Enabled=None, IsLearnedLsaRefreshed=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, RouterId=None, TrafficGroupId=None):
        """Finds and retrieves router data from the server.

        All named parameters support regex and can be used to selectively retrieve router data from the server.
        By default the find method takes no parameters and will retrieve all router data from the server.

        Args:
            DisableAutoGenerateLinkLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Link LSAs. Custom Link LSAs may then be configured by the user or the Network Range LSAs may be generated.
            DisableAutoGenerateRouterLsa (bool): If enabled, the emulated OSPFv3 router will not automatically generate Router LSAs. Custom Router LSAs may then be configured by the user or the Network Range LSAs may be generated.
            DiscardLearnedLsa (bool): If enabled, the emulated OSPF router (RID) will not learn any LSAs from the neighbor and the Learned LSAs window will be empty, even when full adjacency has been established. A message will be displayed in the OSPF Learned LSAs window for each interface on the router, indicating that this option has been enabled.
            EnableGracefulRestartHelperMode (bool): Enables the OSPF Router to act as Helper during Graceful Restart
            EnableStrictLsaChecking (bool): Enables Strict LSA Checking during Graceful Restart
            EnableSupportReasonSwReloadOrUpgrade (bool): Sets restart reason as Software Reload-Upgrade in Grace LSA during Graceful Restart
            EnableSupportReasonSwRestart (bool): Sets the reason as Software Restart in Grace LSA during Graceful Restart
            EnableSupportReasonSwitchToRedundantControlProcessor (bool): Sets the reason as Switch to Redundant Control Processor in Grace LSA during Graceful Restart
            EnableSupportReasonUnknown (bool): Sets the reason as Unknown in Grace LSA during Graceful Restart
            EnableSupportRfc5838 (bool): Enables support for RFC5838
            Enabled (bool): Enables or disables the simulated router.
            IsLearnedLsaRefreshed (bool): If true, learned OSPF LSA information is refreshed.
            LsaRefreshTime (number): Indicates the time in seconds after which OSPF flushes out old LSA and advertises new LSA
            LsaRetransmitTime (number): Indicates the time in seconds after which OSPF retransmits LSA if LS Acknowledgement is not received
            MaxNumLsaPerSecond (number): Limits the number of LSAs that will be sent per second.
            RouterId (str): Used to set the ID of the router, expressed as an IPv4 address.
            TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): The name of the group to which this emulated OSPF router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns:
            self: This instance with matching router data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the router data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GracefulRouterRestart(self, *args, **kwargs):
        """Executes the gracefulRouterRestart operation on the server.

        NOT DEFINED

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        gracefulRouterRestart()string

            Returns:
                str: NOT DEFINED

        gracefulRouterRestart(Arg2:number, Arg3:enum, Arg4:number)string
            Args:
                args[0] is Arg2 (number): NOT DEFINED
                args[1] is Arg3 (str(softwareReloadOrUpgrade|softwareRestart|switchToRedundantControlProcessor|unknown)): NOT DEFINED
                args[2] is Arg4 (number): NOT DEFINED

            Returns:
                str: NOT DEFINED

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('gracefulRouterRestart', payload=payload, response_object=None)

    def RefreshLearnedLsa(self):
        """Executes the refreshLearnedLsa operation on the server.

        This exec refreshes the learned OSPFv3 LSA from the DUT.

            Returns:
                bool: NOT DEFINED

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedLsa', payload=payload, response_object=None)
