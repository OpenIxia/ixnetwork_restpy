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


class Dhcpv6PdClientGlobals(Base):
    """Global settings placeholder for DHCPPlugin.
    The Dhcpv6PdClientGlobals class encapsulates a list of dhcpv6PdClientGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the Dhcpv6PdClientGlobals.find() method.
    The list can be managed by using the Dhcpv6PdClientGlobals.add() and Dhcpv6PdClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv6PdClientGlobals'
    _SDM_ATT_MAP = {
        'AcceptPartialConfig': 'acceptPartialConfig',
        'Dhcp6EchoIaInfo': 'dhcp6EchoIaInfo',
        'Dhcp6InfMaxRc': 'dhcp6InfMaxRc',
        'Dhcp6InfMaxRt': 'dhcp6InfMaxRt',
        'Dhcp6InfTimeout': 'dhcp6InfTimeout',
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
        'TeardownRateIncrement': 'teardownRateIncrement',
        'TeardownRateInitial': 'teardownRateInitial',
        'TeardownRateMax': 'teardownRateMax',
        'WaitForCompletion': 'waitForCompletion',
    }

    def __init__(self, parent):
        super(Dhcpv6PdClientGlobals, self).__init__(parent)

    @property
    def Dhcpv6PdOptionSet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdoptionset.dhcpv6pdoptionset.Dhcpv6PdOptionSet): An instance of the Dhcpv6PdOptionSet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdoptionset.dhcpv6pdoptionset import Dhcpv6PdOptionSet
        return Dhcpv6PdOptionSet(self)

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
    def Dhcp6InfMaxRc(self):
        """
        Returns
        -------
        - number: The maximum information-request retry attempts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRc'])
    @Dhcp6InfMaxRc.setter
    def Dhcp6InfMaxRc(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRc'], value)

    @property
    def Dhcp6InfMaxRt(self):
        """
        Returns
        -------
        - number: RFC 3315 maximum information-request timeout value, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRt'])
    @Dhcp6InfMaxRt.setter
    def Dhcp6InfMaxRt(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6InfMaxRt'], value)

    @property
    def Dhcp6InfTimeout(self):
        """
        Returns
        -------
        - number: RFC 3315 Initial information-request timeout, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dhcp6InfTimeout'])
    @Dhcp6InfTimeout.setter
    def Dhcp6InfTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dhcp6InfTimeout'], value)

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

    def update(self, AcceptPartialConfig=None, Dhcp6EchoIaInfo=None, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Updates dhcpv6PdClientGlobals resource on the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
        - Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
        - Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
        - Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
        - Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
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
        - TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
        - TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
        - TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
        - WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AcceptPartialConfig=None, Dhcp6EchoIaInfo=None, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Adds a new dhcpv6PdClientGlobals resource on the server and adds it to the container.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
        - Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
        - Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
        - Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
        - Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
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
        - TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
        - TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
        - TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
        - WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Returns
        -------
        - self: This instance with all currently retrieved dhcpv6PdClientGlobals resources using find and the newly added dhcpv6PdClientGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dhcpv6PdClientGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, Dhcp6EchoIaInfo=None, Dhcp6InfMaxRc=None, Dhcp6InfMaxRt=None, Dhcp6InfTimeout=None, Dhcp6RebMaxRt=None, Dhcp6RebTimeout=None, Dhcp6RelMaxRc=None, Dhcp6RelTimeout=None, Dhcp6RenMaxRt=None, Dhcp6RenTimeout=None, Dhcp6ReqMaxRc=None, Dhcp6ReqMaxRt=None, Dhcp6ReqTimeout=None, Dhcp6SolMaxRc=None, Dhcp6SolMaxRt=None, Dhcp6SolTimeout=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, RenewOnLinkUp=None, SetupRateIncrement=None, SetupRateInitial=None, SetupRateMax=None, TeardownRateIncrement=None, TeardownRateInitial=None, TeardownRateMax=None, WaitForCompletion=None):
        """Finds and retrieves dhcpv6PdClientGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dhcpv6PdClientGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dhcpv6PdClientGlobals resources from the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one address is configured.When is false the plugin reports success only if all address are configured.
        - Dhcp6EchoIaInfo (bool): If set, the DHCPv6 client will request the exact address as advertised by server.
        - Dhcp6InfMaxRc (number): The maximum information-request retry attempts.
        - Dhcp6InfMaxRt (number): RFC 3315 maximum information-request timeout value, in seconds.
        - Dhcp6InfTimeout (number): RFC 3315 Initial information-request timeout, in seconds.
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
        - TeardownRateIncrement (number): This value represents the increment value for teardown rate.This value is applied every second and can be negative.
        - TeardownRateInitial (number): Teardown rate is the number of clients to stop in each second.This value represents the initial value for teardown rate.
        - TeardownRateMax (number): This value represents the final value for teardown rate.The teardown rate will not change after this value is reached.
        - WaitForCompletion (bool): If true the DHCP plugin is waiting until all DHCP interfaces are configured using DHCP discovery.If is false the configuration will return as soon that the configuration is sent to port.The discovery information can be queried at a later time when is needed.

        Returns
        -------
        - self: This instance with matching dhcpv6PdClientGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dhcpv6PdClientGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dhcpv6PdClientGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
