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


class DhcpGlobals(Base):
    """Global settings placeholder for DHCPPlugin.
    The DhcpGlobals class encapsulates a list of dhcpGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the DhcpGlobals.find() method.
    The list can be managed by using the DhcpGlobals.add() and DhcpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpGlobals'
    _SDM_ATT_MAP = {
        'AcceptPartialConfig': 'acceptPartialConfig',
        'Dhcp4AddrLeaseTime': 'dhcp4AddrLeaseTime',
        'Dhcp4ClientPort': 'dhcp4ClientPort',
        'Dhcp4MaxMsgSize': 'dhcp4MaxMsgSize',
        'Dhcp4NumRetry': 'dhcp4NumRetry',
        'Dhcp4ResponseTimeout': 'dhcp4ResponseTimeout',
        'Dhcp4ResponseTimeoutFactor': 'dhcp4ResponseTimeoutFactor',
        'Dhcp4ServerPort': 'dhcp4ServerPort',
        'Dhcp6EchoIaInfo': 'dhcp6EchoIaInfo',
        'Dhcp6RebMaxRt': 'dhcp6RebMaxRt',
        'Dhcp6RebTimeout': 'dhcp6RebTimeout',
        'Dhcp6RelMaxRc': 'dhcp6RelMaxRc',
        'Dhcp6RelTimeout': 'dhcp6RelTimeout',
        'Dhcp6RenMaxRt': 'dhcp6RenMaxRt',
        'Dhcp6RenTimeout': 'dhcp6RenTimeout',
        'Dhcp6ReqMaxRc': 'dhcp6ReqMaxRc',
        'Dhcp6ReqMaxRt': 'dhcp6ReqMaxRt',
        'Dhcp6ReqTimeout': 'dhcp6ReqTimeout',
        'Dhcp6SolMaxRc': 'dhcp6SolMaxRc',
        'Dhcp6SolMaxRt': 'dhcp6SolMaxRt',
        'Dhcp6SolTimeout': 'dhcp6SolTimeout',
        'MaxOutstandingReleases': 'maxOutstandingReleases',
        'MaxOutstandingRequests': 'maxOutstandingRequests',
        'ObjectId': 'objectId',
        'RenewOnLinkUp': 'renewOnLinkUp',
        'SetupRateIncrement': 'setupRateIncrement',
        'SetupRateInitial': 'setupRateInitial',
        'SetupRateMax': 'setupRateMax',
        'SkipReleaseOnStop': 'skipReleaseOnStop',
        'TeardownRateIncrement': 'teardownRateIncrement',
        'TeardownRateInitial': 'teardownRateInitial',
        'TeardownRateMax': 'teardownRateMax',
        'WaitForCompletion': 'waitForCompletion',
    }

    def __init__(self, parent):
        super(DhcpGlobals, self).__init__(parent)

    @property
    def DhcpOptionSet(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpoptionset.dhcpoptionset.DhcpOptionSet): An instance of the DhcpOptionSet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpoptionset.dhcpoptionset import DhcpOptionSet
        return DhcpOptionSet(self)

    @property
    def AcceptPartialConfig(self):
        """
        Returns
        -------
        - bool: This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'])
    @AcceptPartialConfig.setter
    def AcceptPartialConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'], value)

    @property
    def Dhcp4AddrLeaseTime(self):
        """
        Returns
        -------
        - number: Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp4AddrLeaseTime'])
    @Dhcp4AddrLeaseTime.setter
    def Dhcp4AddrLeaseTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp4AddrLeaseTime'], value)

    @property
    def Dhcp4ClientPort(self):
        """
        Returns
        -------
        - number: UDP port that the client listens on for DHCP and BOOTP responses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp4ClientPort'])
    @Dhcp4ClientPort.setter
    def Dhcp4ClientPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp4ClientPort'], value)

    @property
    def Dhcp4MaxMsgSize(self):
        """
        Returns
        -------
        - number: Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp4MaxMsgSize'])
    @Dhcp4MaxMsgSize.setter
    def Dhcp4MaxMsgSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp4MaxMsgSize'], value)

    @property
    def Dhcp4NumRetry(self):
        """
        Returns
        -------
        - number: Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp4NumRetry'])
    @Dhcp4NumRetry.setter
    def Dhcp4NumRetry(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp4NumRetry'], value)

    @property
    def Dhcp4ResponseTimeout(self):
        """
        Returns
        -------
        - number: The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp4ResponseTimeout'])
    @Dhcp4ResponseTimeout.setter
    def Dhcp4ResponseTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp4ResponseTimeout'], value)

    @property
    def Dhcp4ResponseTimeoutFactor(self):
        """
        Returns
        -------
        - number: The factor by which the timeout will be multiplied each time the response timeout has been reached.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp4ResponseTimeoutFactor'])
    @Dhcp4ResponseTimeoutFactor.setter
    def Dhcp4ResponseTimeoutFactor(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp4ResponseTimeoutFactor'], value)

    @property
    def Dhcp4ServerPort(self):
        """
        Returns
        -------
        - number: UDP port that the client addresses server requests to.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp4ServerPort'])
    @Dhcp4ServerPort.setter
    def Dhcp4ServerPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp4ServerPort'], value)

    @property
    def Dhcp6EchoIaInfo(self):
        """
        Returns
        -------
        - bool: If set, the DHCPv6 client will request the exact address as advertised by server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6EchoIaInfo'])
    @Dhcp6EchoIaInfo.setter
    def Dhcp6EchoIaInfo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6EchoIaInfo'], value)

    @property
    def Dhcp6RebMaxRt(self):
        """
        Returns
        -------
        - number: RFC 3315 Max Rebind timeout value in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6RebMaxRt'])
    @Dhcp6RebMaxRt.setter
    def Dhcp6RebMaxRt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6RebMaxRt'], value)

    @property
    def Dhcp6RebTimeout(self):
        """
        Returns
        -------
        - number: RFC 3315 Initial Rebind timeout seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6RebTimeout'])
    @Dhcp6RebTimeout.setter
    def Dhcp6RebTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6RebTimeout'], value)

    @property
    def Dhcp6RelMaxRc(self):
        """
        Returns
        -------
        - number: RFC 3315 Release attempts
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6RelMaxRc'])
    @Dhcp6RelMaxRc.setter
    def Dhcp6RelMaxRc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6RelMaxRc'], value)

    @property
    def Dhcp6RelTimeout(self):
        """
        Returns
        -------
        - number: RFC 3315 Initial Release timeout in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6RelTimeout'])
    @Dhcp6RelTimeout.setter
    def Dhcp6RelTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6RelTimeout'], value)

    @property
    def Dhcp6RenMaxRt(self):
        """
        Returns
        -------
        - number: RFC 3315 Max Renew timeout value in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6RenMaxRt'])
    @Dhcp6RenMaxRt.setter
    def Dhcp6RenMaxRt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6RenMaxRt'], value)

    @property
    def Dhcp6RenTimeout(self):
        """
        Returns
        -------
        - number: RFC 3315 Initial Renew timeout in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6RenTimeout'])
    @Dhcp6RenTimeout.setter
    def Dhcp6RenTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6RenTimeout'], value)

    @property
    def Dhcp6ReqMaxRc(self):
        """
        Returns
        -------
        - number: RFC 3315 Max Request retry attempts
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6ReqMaxRc'])
    @Dhcp6ReqMaxRc.setter
    def Dhcp6ReqMaxRc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6ReqMaxRc'], value)

    @property
    def Dhcp6ReqMaxRt(self):
        """
        Returns
        -------
        - number: RFC 3315 Max Request timeout value in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6ReqMaxRt'])
    @Dhcp6ReqMaxRt.setter
    def Dhcp6ReqMaxRt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6ReqMaxRt'], value)

    @property
    def Dhcp6ReqTimeout(self):
        """
        Returns
        -------
        - number: RFC 3315 Initial Request timeout in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6ReqTimeout'])
    @Dhcp6ReqTimeout.setter
    def Dhcp6ReqTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6ReqTimeout'], value)

    @property
    def Dhcp6SolMaxRc(self):
        """
        Returns
        -------
        - number: RFC 3315 Max Solicit retry attempts
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6SolMaxRc'])
    @Dhcp6SolMaxRc.setter
    def Dhcp6SolMaxRc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6SolMaxRc'], value)

    @property
    def Dhcp6SolMaxRt(self):
        """
        Returns
        -------
        - number: RFC 3315 Max Solicit timeout value in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6SolMaxRt'])
    @Dhcp6SolMaxRt.setter
    def Dhcp6SolMaxRt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6SolMaxRt'], value)

    @property
    def Dhcp6SolTimeout(self):
        """
        Returns
        -------
        - number: RFC 3315 Initial Solicit timeout in seconds
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6SolTimeout'])
    @Dhcp6SolTimeout.setter
    def Dhcp6SolTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6SolTimeout'], value)

    @property
    def MaxOutstandingReleases(self):
        """
        Returns
        -------
        - number: This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingReleases'])
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingReleases'], value)

    @property
    def MaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'])
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def RenewOnLinkUp(self):
        """
        Returns
        -------
        - bool: Indicate to renew the active DHCP sessions after link status goes down and up.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RenewOnLinkUp'])
    @RenewOnLinkUp.setter
    def RenewOnLinkUp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RenewOnLinkUp'], value)

    @property
    def SetupRateIncrement(self):
        """
        Returns
        -------
        - number: This value represents the increment value for setup rate.This value is applied every second and can be negative.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateIncrement'])
    @SetupRateIncrement.setter
    def SetupRateIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateIncrement'], value)

    @property
    def SetupRateInitial(self):
        """
        Returns
        -------
        - number: Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateInitial'])
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateInitial'], value)

    @property
    def SetupRateMax(self):
        """
        Returns
        -------
        - number: This value represents the final value for setup rate.The setup rate will not change after this value is reached.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateMax'])
    @SetupRateMax.setter
    def SetupRateMax(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateMax'], value)

    @property
    def SkipReleaseOnStop(self):
        """
        Returns
        -------
        - bool: If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SkipReleaseOnStop'])
    @SkipReleaseOnStop.setter
    def SkipReleaseOnStop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SkipReleaseOnStop'], value)

    @property
    def TeardownRateIncrement(self):
        """
        Returns
        -------
        - number: This value represents the increment value for teardown rate.This value is applied every second and can be negative.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRateIncrement'])
    @TeardownRateIncrement.setter
    def TeardownRateIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRateIncrement'], value)

    @property
    def TeardownRateInitial(self):
        """
        Returns
        -------
        - number: Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRateInitial'])
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRateInitial'], value)

    @property
    def TeardownRateMax(self):
        """
        Returns
        -------
        - number: This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRateMax'])
    @TeardownRateMax.setter
    def TeardownRateMax(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRateMax'], value)

    @property
    def WaitForCompletion(self):
        """
        Returns
        -------
        - bool: If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitForCompletion'])
    @WaitForCompletion.setter
    def WaitForCompletion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WaitForCompletion'], value)

    def update(self, AcceptPartialConfig=None, Dhcp4AddrLeaseTime=None, Dhcp4ClientPort=None, Dhcp4MaxMsgSize=None, Dhcp4NumRetry=None, Dhcp4ResponseTimeout=None, Dhcp4ResponseTimeoutFactor=None, Dhcp4ServerPort=None, Dhcp6EchoIaInfo=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, SkipReleaseOnStop=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Updates dhcpGlobals resource on the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
        - Dhcp4AddrLeaseTime (number): Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.
        - Dhcp4ClientPort (number): UDP port that the client listens on for DHCP and BOOTP responses.
        - Dhcp4MaxMsgSize (number): Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.
        - Dhcp4NumRetry (number): Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
        - Dhcp4ResponseTimeout (number): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
        - Dhcp4ResponseTimeoutFactor (number): The factor by which the timeout will be multiplied each time the response timeout has been reached.
        - Dhcp4ServerPort (number): UDP port that the client addresses server requests to.
        - Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
        - Dhcp6RebMaxRt (number): RFC 3315 Max Rebind timeout value in seconds
        - Dhcp6RebTimeout (number): RFC 3315 Initial Rebind timeout seconds
        - Dhcp6RelMaxRc (number): RFC 3315 Release attempts
        - Dhcp6RelTimeout (number): RFC 3315 Initial Release timeout in seconds
        - Dhcp6RenMaxRt (number): RFC 3315 Max Renew timeout value in seconds
        - Dhcp6RenTimeout (number): RFC 3315 Initial Renew timeout in seconds
        - Dhcp6ReqMaxRc (number): RFC 3315 Max Request retry attempts
        - Dhcp6ReqMaxRt (number): RFC 3315 Max Request timeout value in seconds
        - Dhcp6ReqTimeout (number): RFC 3315 Initial Request timeout in seconds
        - Dhcp6SolMaxRc (number): RFC 3315 Max Solicit retry attempts
        - Dhcp6SolMaxRt (number): RFC 3315 Max Solicit timeout value in seconds
        - Dhcp6SolTimeout (number): RFC 3315 Initial Solicit timeout in seconds
        - MaxOutstandingReleases (number): This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.
        - MaxOutstandingRequests (number): This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        - RenewOnLinkUp (bool): Indicate to renew the active DHCP sessions after link status goes down and up.
        - SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
        - SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
        - SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
        - SkipReleaseOnStop (bool): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
        - TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
        - TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
        - TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
        - WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AcceptPartialConfig=None, Dhcp4AddrLeaseTime=None, Dhcp4ClientPort=None, Dhcp4MaxMsgSize=None, Dhcp4NumRetry=None, Dhcp4ResponseTimeout=None, Dhcp4ResponseTimeoutFactor=None, Dhcp4ServerPort=None, Dhcp6EchoIaInfo=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, SkipReleaseOnStop=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Adds a new dhcpGlobals resource on the server and adds it to the container.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
        - Dhcp4AddrLeaseTime (number): Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.
        - Dhcp4ClientPort (number): UDP port that the client listens on for DHCP and BOOTP responses.
        - Dhcp4MaxMsgSize (number): Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.
        - Dhcp4NumRetry (number): Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
        - Dhcp4ResponseTimeout (number): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
        - Dhcp4ResponseTimeoutFactor (number): The factor by which the timeout will be multiplied each time the response timeout has been reached.
        - Dhcp4ServerPort (number): UDP port that the client addresses server requests to.
        - Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
        - Dhcp6RebMaxRt (number): RFC 3315 Max Rebind timeout value in seconds
        - Dhcp6RebTimeout (number): RFC 3315 Initial Rebind timeout seconds
        - Dhcp6RelMaxRc (number): RFC 3315 Release attempts
        - Dhcp6RelTimeout (number): RFC 3315 Initial Release timeout in seconds
        - Dhcp6RenMaxRt (number): RFC 3315 Max Renew timeout value in seconds
        - Dhcp6RenTimeout (number): RFC 3315 Initial Renew timeout in seconds
        - Dhcp6ReqMaxRc (number): RFC 3315 Max Request retry attempts
        - Dhcp6ReqMaxRt (number): RFC 3315 Max Request timeout value in seconds
        - Dhcp6ReqTimeout (number): RFC 3315 Initial Request timeout in seconds
        - Dhcp6SolMaxRc (number): RFC 3315 Max Solicit retry attempts
        - Dhcp6SolMaxRt (number): RFC 3315 Max Solicit timeout value in seconds
        - Dhcp6SolTimeout (number): RFC 3315 Initial Solicit timeout in seconds
        - MaxOutstandingReleases (number): This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.
        - MaxOutstandingRequests (number): This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        - RenewOnLinkUp (bool): Indicate to renew the active DHCP sessions after link status goes down and up.
        - SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
        - SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
        - SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
        - SkipReleaseOnStop (bool): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
        - TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
        - TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
        - TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
        - WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpGlobals resources using find and the newly added dhcpGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, Dhcp4AddrLeaseTime=None, Dhcp4ClientPort=None, Dhcp4MaxMsgSize=None, Dhcp4NumRetry=None, Dhcp4ResponseTimeout=None, Dhcp4ResponseTimeoutFactor=None, Dhcp4ServerPort=None, Dhcp6EchoIaInfo=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, SkipReleaseOnStop=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Finds and retrieves dhcpGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpGlobals resources from the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
        - Dhcp4AddrLeaseTime (number): Period of time (in seconds) for which an IP address is requested by DHCP client.The actual lease time is specified by the DUT in the DHCPACK message.
        - Dhcp4ClientPort (number): UDP port that the client listens on for DHCP and BOOTP responses.
        - Dhcp4MaxMsgSize (number): Maximum size of a DHCP packet that the client will send or accept, including IP and UDP headers.According to RFC 2131, the minimum message size that a client should accept is 576 octets.
        - Dhcp4NumRetry (number): Number of times that the client will retransmit a request for which it has not received a response.When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
        - Dhcp4ResponseTimeout (number): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
        - Dhcp4ResponseTimeoutFactor (number): The factor by which the timeout will be multiplied each time the response timeout has been reached.
        - Dhcp4ServerPort (number): UDP port that the client addresses server requests to.
        - Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
        - Dhcp6RebMaxRt (number): RFC 3315 Max Rebind timeout value in seconds
        - Dhcp6RebTimeout (number): RFC 3315 Initial Rebind timeout seconds
        - Dhcp6RelMaxRc (number): RFC 3315 Release attempts
        - Dhcp6RelTimeout (number): RFC 3315 Initial Release timeout in seconds
        - Dhcp6RenMaxRt (number): RFC 3315 Max Renew timeout value in seconds
        - Dhcp6RenTimeout (number): RFC 3315 Initial Renew timeout in seconds
        - Dhcp6ReqMaxRc (number): RFC 3315 Max Request retry attempts
        - Dhcp6ReqMaxRt (number): RFC 3315 Max Request timeout value in seconds
        - Dhcp6ReqTimeout (number): RFC 3315 Initial Request timeout in seconds
        - Dhcp6SolMaxRc (number): RFC 3315 Max Solicit retry attempts
        - Dhcp6SolMaxRt (number): RFC 3315 Max Solicit timeout value in seconds
        - Dhcp6SolTimeout (number): RFC 3315 Initial Solicit timeout in seconds
        - MaxOutstandingReleases (number): This is the point at which requests will be restricted. Interfaces are torn down at the configured speed until there are this number of requests in disconnecting stage, at which point additional interfaces are torn down only when others get fully disconnected.
        - MaxOutstandingRequests (number): This is the point at which interface setup will be restricted. Interfaces are setup at the configured speed until there are this number of requests in progress, at which point new requests are only added when others are completed.
        - ObjectId (str): Unique identifier for this object
        - RenewOnLinkUp (bool): Indicate to renew the active DHCP sessions after link status goes down and up.
        - SetupRateIncrement (number): This value represents the increment value for setup rate.This value is applied every second and can be negative.
        - SetupRateInitial (number): Setup rate is the number of clients to start in each second.This value represents the initial value for setup rate.
        - SetupRateMax (number): This value represents the final value for setup rate.The setup rate will not change after this value is reached.
        - SkipReleaseOnStop (bool): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
        - TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
        - TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
        - TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
        - WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Returns
        -------
        - self: This instance with matching dhcpGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
