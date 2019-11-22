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


class DhcpGlobals(Base):
    """Global settings placeholder for DHCPPlugin.
    The DhcpGlobals class encapsulates a list of dhcpGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the DhcpGlobals.find() method.
    The list can be managed by the user by using the DhcpGlobals.add() and DhcpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpGlobals'

    def __init__(self, parent):
        super(DhcpGlobals, self).__init__(parent)

    @property
    def DhcpOptionSet(self):
        """An instance of the DhcpOptionSet class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpoptionset.dhcpoptionset.DhcpOptionSet)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpoptionset.dhcpoptionset import DhcpOptionSet
        return DhcpOptionSet(self)

    @property
    def AcceptPartialConfig(self):
        """This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.

        Returns:
            bool
        """
        return self._get_attribute('acceptPartialConfig')
    @AcceptPartialConfig.setter
    def AcceptPartialConfig(self, value):
        self._set_attribute('acceptPartialConfig', value)

    @property
    def Dhcp4AddrLeaseTime(self):
        """Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.

        Returns:
            number
        """
        return self._get_attribute('dhcp4AddrLeaseTime')
    @Dhcp4AddrLeaseTime.setter
    def Dhcp4AddrLeaseTime(self, value):
        self._set_attribute('dhcp4AddrLeaseTime', value)

    @property
    def Dhcp4ClientPort(self):
        """UDP port that the client listens on for DHCP and BOOTP responses.

        Returns:
            number
        """
        return self._get_attribute('dhcp4ClientPort')
    @Dhcp4ClientPort.setter
    def Dhcp4ClientPort(self, value):
        self._set_attribute('dhcp4ClientPort', value)

    @property
    def Dhcp4MaxMsgSize(self):
        """Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.

        Returns:
            number
        """
        return self._get_attribute('dhcp4MaxMsgSize')
    @Dhcp4MaxMsgSize.setter
    def Dhcp4MaxMsgSize(self, value):
        self._set_attribute('dhcp4MaxMsgSize', value)

    @property
    def Dhcp4NumRetry(self):
        """Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).

        Returns:
            number
        """
        return self._get_attribute('dhcp4NumRetry')
    @Dhcp4NumRetry.setter
    def Dhcp4NumRetry(self, value):
        self._set_attribute('dhcp4NumRetry', value)

    @property
    def Dhcp4ResponseTimeout(self):
        """The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.

        Returns:
            number
        """
        return self._get_attribute('dhcp4ResponseTimeout')
    @Dhcp4ResponseTimeout.setter
    def Dhcp4ResponseTimeout(self, value):
        self._set_attribute('dhcp4ResponseTimeout', value)

    @property
    def Dhcp4ResponseTimeoutFactor(self):
        """The factor by which the timeout will be multiplied each time the response timeout has been reached.

        Returns:
            number
        """
        return self._get_attribute('dhcp4ResponseTimeoutFactor')
    @Dhcp4ResponseTimeoutFactor.setter
    def Dhcp4ResponseTimeoutFactor(self, value):
        self._set_attribute('dhcp4ResponseTimeoutFactor', value)

    @property
    def Dhcp4ServerPort(self):
        """UDP port that the client addresses server requests to.

        Returns:
            number
        """
        return self._get_attribute('dhcp4ServerPort')
    @Dhcp4ServerPort.setter
    def Dhcp4ServerPort(self, value):
        self._set_attribute('dhcp4ServerPort', value)

    @property
    def Dhcp6EchoIaInfo(self):
        """If set, the DHCPv6 client will request the exact address as advertised by server.

        Returns:
            bool
        """
        return self._get_attribute('dhcp6EchoIaInfo')
    @Dhcp6EchoIaInfo.setter
    def Dhcp6EchoIaInfo(self, value):
        self._set_attribute('dhcp6EchoIaInfo', value)

    @property
    def Dhcp6RebMaxRt(self):
        """RFC 3315 Max Rebind timeout value in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6RebMaxRt')
    @Dhcp6RebMaxRt.setter
    def Dhcp6RebMaxRt(self, value):
        self._set_attribute('dhcp6RebMaxRt', value)

    @property
    def Dhcp6RebTimeout(self):
        """RFC 3315 Initial Rebind timeout seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6RebTimeout')
    @Dhcp6RebTimeout.setter
    def Dhcp6RebTimeout(self, value):
        self._set_attribute('dhcp6RebTimeout', value)

    @property
    def Dhcp6RelMaxRc(self):
        """RFC 3315 Release attempts

        Returns:
            number
        """
        return self._get_attribute('dhcp6RelMaxRc')
    @Dhcp6RelMaxRc.setter
    def Dhcp6RelMaxRc(self, value):
        self._set_attribute('dhcp6RelMaxRc', value)

    @property
    def Dhcp6RelTimeout(self):
        """RFC 3315 Initial Release timeout in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6RelTimeout')
    @Dhcp6RelTimeout.setter
    def Dhcp6RelTimeout(self, value):
        self._set_attribute('dhcp6RelTimeout', value)

    @property
    def Dhcp6RenMaxRt(self):
        """RFC 3315 Max Renew timeout value in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6RenMaxRt')
    @Dhcp6RenMaxRt.setter
    def Dhcp6RenMaxRt(self, value):
        self._set_attribute('dhcp6RenMaxRt', value)

    @property
    def Dhcp6RenTimeout(self):
        """RFC 3315 Initial Renew timeout in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6RenTimeout')
    @Dhcp6RenTimeout.setter
    def Dhcp6RenTimeout(self, value):
        self._set_attribute('dhcp6RenTimeout', value)

    @property
    def Dhcp6ReqMaxRc(self):
        """RFC 3315 Max Request retry attempts

        Returns:
            number
        """
        return self._get_attribute('dhcp6ReqMaxRc')
    @Dhcp6ReqMaxRc.setter
    def Dhcp6ReqMaxRc(self, value):
        self._set_attribute('dhcp6ReqMaxRc', value)

    @property
    def Dhcp6ReqMaxRt(self):
        """RFC 3315 Max Request timeout value in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6ReqMaxRt')
    @Dhcp6ReqMaxRt.setter
    def Dhcp6ReqMaxRt(self, value):
        self._set_attribute('dhcp6ReqMaxRt', value)

    @property
    def Dhcp6ReqTimeout(self):
        """RFC 3315 Initial Request timeout in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6ReqTimeout')
    @Dhcp6ReqTimeout.setter
    def Dhcp6ReqTimeout(self, value):
        self._set_attribute('dhcp6ReqTimeout', value)

    @property
    def Dhcp6SolMaxRc(self):
        """RFC 3315 Max Solicit retry attempts

        Returns:
            number
        """
        return self._get_attribute('dhcp6SolMaxRc')
    @Dhcp6SolMaxRc.setter
    def Dhcp6SolMaxRc(self, value):
        self._set_attribute('dhcp6SolMaxRc', value)

    @property
    def Dhcp6SolMaxRt(self):
        """RFC 3315 Max Solicit timeout value in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6SolMaxRt')
    @Dhcp6SolMaxRt.setter
    def Dhcp6SolMaxRt(self, value):
        self._set_attribute('dhcp6SolMaxRt', value)

    @property
    def Dhcp6SolTimeout(self):
        """RFC 3315 Initial Solicit timeout in seconds

        Returns:
            number
        """
        return self._get_attribute('dhcp6SolTimeout')
    @Dhcp6SolTimeout.setter
    def Dhcp6SolTimeout(self, value):
        self._set_attribute('dhcp6SolTimeout', value)

    @property
    def MaxOutstandingReleases(self):
        """This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingReleases')
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute('maxOutstandingReleases', value)

    @property
    def MaxOutstandingRequests(self):
        """This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingRequests')
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute('maxOutstandingRequests', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def RenewOnLinkUp(self):
        """Indicate to renew the active DHCP sessions after link status goes down and up.

        Returns:
            bool
        """
        return self._get_attribute('renewOnLinkUp')
    @RenewOnLinkUp.setter
    def RenewOnLinkUp(self, value):
        self._set_attribute('renewOnLinkUp', value)

    @property
    def SetupRateIncrement(self):
        """This value represents the increment value for setup rate.This value is applied every second and can be negative.

        Returns:
            number
        """
        return self._get_attribute('setupRateIncrement')
    @SetupRateIncrement.setter
    def SetupRateIncrement(self, value):
        self._set_attribute('setupRateIncrement', value)

    @property
    def SetupRateInitial(self):
        """Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.

        Returns:
            number
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def SetupRateMax(self):
        """This value represents the final value for setup rate.The setup rate will not change after this value is reached.

        Returns:
            number
        """
        return self._get_attribute('setupRateMax')
    @SetupRateMax.setter
    def SetupRateMax(self, value):
        self._set_attribute('setupRateMax', value)

    @property
    def SkipReleaseOnStop(self):
        """If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.

        Returns:
            bool
        """
        return self._get_attribute('skipReleaseOnStop')
    @SkipReleaseOnStop.setter
    def SkipReleaseOnStop(self, value):
        self._set_attribute('skipReleaseOnStop', value)

    @property
    def TeardownRateIncrement(self):
        """This value represents the increment value for teardown rate.This value is applied every second and can be negative.

        Returns:
            number
        """
        return self._get_attribute('teardownRateIncrement')
    @TeardownRateIncrement.setter
    def TeardownRateIncrement(self, value):
        self._set_attribute('teardownRateIncrement', value)

    @property
    def TeardownRateInitial(self):
        """Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.

        Returns:
            number
        """
        return self._get_attribute('teardownRateInitial')
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute('teardownRateInitial', value)

    @property
    def TeardownRateMax(self):
        """This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.

        Returns:
            number
        """
        return self._get_attribute('teardownRateMax')
    @TeardownRateMax.setter
    def TeardownRateMax(self, value):
        self._set_attribute('teardownRateMax', value)

    @property
    def WaitForCompletion(self):
        """If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Returns:
            bool
        """
        return self._get_attribute('waitForCompletion')
    @WaitForCompletion.setter
    def WaitForCompletion(self, value):
        self._set_attribute('waitForCompletion', value)

    def update(self, AcceptPartialConfig=None, Dhcp4AddrLeaseTime=None, Dhcp4ClientPort=None, Dhcp4MaxMsgSize=None, Dhcp4NumRetry=None, Dhcp4ResponseTimeout=None, Dhcp4ResponseTimeoutFactor=None, Dhcp4ServerPort=None, Dhcp6EchoIaInfo=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, SkipReleaseOnStop=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Updates a child instance of dhcpGlobals on the server.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
            Dhcp4AddrLeaseTime (number): Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.
            Dhcp4ClientPort (number): UDP port that the client listens on for DHCP and BOOTP responses.
            Dhcp4MaxMsgSize (number): Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.
            Dhcp4NumRetry (number): Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
            Dhcp4ResponseTimeout (number): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
            Dhcp4ResponseTimeoutFactor (number): The factor by which the timeout will be multiplied each time the response timeout has been reached.
            Dhcp4ServerPort (number): UDP port that the client addresses server requests to.
            Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
            Dhcp6RebMaxRt (number): RFC 3315 Max Rebind timeout value in seconds
            Dhcp6RebTimeout (number): RFC 3315 Initial Rebind timeout seconds
            Dhcp6RelMaxRc (number): RFC 3315 Release attempts
            Dhcp6RelTimeout (number): RFC 3315 Initial Release timeout in seconds
            Dhcp6RenMaxRt (number): RFC 3315 Max Renew timeout value in seconds
            Dhcp6RenTimeout (number): RFC 3315 Initial Renew timeout in seconds
            Dhcp6ReqMaxRc (number): RFC 3315 Max Request retry attempts
            Dhcp6ReqMaxRt (number): RFC 3315 Max Request timeout value in seconds
            Dhcp6ReqTimeout (number): RFC 3315 Initial Request timeout in seconds
            Dhcp6SolMaxRc (number): RFC 3315 Max Solicit retry attempts
            Dhcp6SolMaxRt (number): RFC 3315 Max Solicit timeout value in seconds
            Dhcp6SolTimeout (number): RFC 3315 Initial Solicit timeout in seconds
            MaxOutstandingReleases (number): This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.
            MaxOutstandingRequests (number): This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            RenewOnLinkUp (bool): Indicate to renew the active DHCP sessions after link status goes down and up.
            SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
            SkipReleaseOnStop (bool): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
            TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
            TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
            TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
            WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AcceptPartialConfig=None, Dhcp4AddrLeaseTime=None, Dhcp4ClientPort=None, Dhcp4MaxMsgSize=None, Dhcp4NumRetry=None, Dhcp4ResponseTimeout=None, Dhcp4ResponseTimeoutFactor=None, Dhcp4ServerPort=None, Dhcp6EchoIaInfo=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, SkipReleaseOnStop=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Adds a new dhcpGlobals node on the server and retrieves it in this instance.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
            Dhcp4AddrLeaseTime (number): Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.
            Dhcp4ClientPort (number): UDP port that the client listens on for DHCP and BOOTP responses.
            Dhcp4MaxMsgSize (number): Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.
            Dhcp4NumRetry (number): Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
            Dhcp4ResponseTimeout (number): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
            Dhcp4ResponseTimeoutFactor (number): The factor by which the timeout will be multiplied each time the response timeout has been reached.
            Dhcp4ServerPort (number): UDP port that the client addresses server requests to.
            Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
            Dhcp6RebMaxRt (number): RFC 3315 Max Rebind timeout value in seconds
            Dhcp6RebTimeout (number): RFC 3315 Initial Rebind timeout seconds
            Dhcp6RelMaxRc (number): RFC 3315 Release attempts
            Dhcp6RelTimeout (number): RFC 3315 Initial Release timeout in seconds
            Dhcp6RenMaxRt (number): RFC 3315 Max Renew timeout value in seconds
            Dhcp6RenTimeout (number): RFC 3315 Initial Renew timeout in seconds
            Dhcp6ReqMaxRc (number): RFC 3315 Max Request retry attempts
            Dhcp6ReqMaxRt (number): RFC 3315 Max Request timeout value in seconds
            Dhcp6ReqTimeout (number): RFC 3315 Initial Request timeout in seconds
            Dhcp6SolMaxRc (number): RFC 3315 Max Solicit retry attempts
            Dhcp6SolMaxRt (number): RFC 3315 Max Solicit timeout value in seconds
            Dhcp6SolTimeout (number): RFC 3315 Initial Solicit timeout in seconds
            MaxOutstandingReleases (number): This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.
            MaxOutstandingRequests (number): This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            RenewOnLinkUp (bool): Indicate to renew the active DHCP sessions after link status goes down and up.
            SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
            SkipReleaseOnStop (bool): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
            TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
            TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
            TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
            WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Returns:
            self: This instance with all currently retrieved dhcpGlobals data using find and the newly added dhcpGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dhcpGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, Dhcp4AddrLeaseTime=None, Dhcp4ClientPort=None, Dhcp4MaxMsgSize=None, Dhcp4NumRetry=None, Dhcp4ResponseTimeout=None, Dhcp4ResponseTimeoutFactor=None, Dhcp4ServerPort=None, Dhcp6EchoIaInfo=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, SkipReleaseOnStop=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Finds and retrieves dhcpGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve dhcpGlobals data from the server.
        By default the find method takes no parameters and will retrieve all dhcpGlobals data from the server.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
            Dhcp4AddrLeaseTime (number): Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.
            Dhcp4ClientPort (number): UDP port that the client listens on for DHCP and BOOTP responses.
            Dhcp4MaxMsgSize (number): Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.
            Dhcp4NumRetry (number): Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
            Dhcp4ResponseTimeout (number): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
            Dhcp4ResponseTimeoutFactor (number): The factor by which the timeout will be multiplied each time the response timeout has been reached.
            Dhcp4ServerPort (number): UDP port that the client addresses server requests to.
            Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
            Dhcp6RebMaxRt (number): RFC 3315 Max Rebind timeout value in seconds
            Dhcp6RebTimeout (number): RFC 3315 Initial Rebind timeout seconds
            Dhcp6RelMaxRc (number): RFC 3315 Release attempts
            Dhcp6RelTimeout (number): RFC 3315 Initial Release timeout in seconds
            Dhcp6RenMaxRt (number): RFC 3315 Max Renew timeout value in seconds
            Dhcp6RenTimeout (number): RFC 3315 Initial Renew timeout in seconds
            Dhcp6ReqMaxRc (number): RFC 3315 Max Request retry attempts
            Dhcp6ReqMaxRt (number): RFC 3315 Max Request timeout value in seconds
            Dhcp6ReqTimeout (number): RFC 3315 Initial Request timeout in seconds
            Dhcp6SolMaxRc (number): RFC 3315 Max Solicit retry attempts
            Dhcp6SolMaxRt (number): RFC 3315 Max Solicit timeout value in seconds
            Dhcp6SolTimeout (number): RFC 3315 Initial Solicit timeout in seconds
            MaxOutstandingReleases (number): This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.
            MaxOutstandingRequests (number): This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
            ObjectId (str): Unique identifier for this object
            RenewOnLinkUp (bool): Indicate to renew the active DHCP sessions after link status goes down and up.
            SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
            SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
            SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
            SkipReleaseOnStop (bool): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
            TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
            TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
            TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
            WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Returns:
            self: This instance with matching dhcpGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dhcpGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dhcpGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
