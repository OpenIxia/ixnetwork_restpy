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


class EapoUdpGlobals(Base):
    """
    The EapoUdpGlobals class encapsulates a list of eapoUdpGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the EapoUdpGlobals.find() method.
    The list can be managed by the user by using the EapoUdpGlobals.add() and EapoUdpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'eapoUdpGlobals'

    def __init__(self, parent):
        super(EapoUdpGlobals, self).__init__(parent)

    @property
    def CertInfo(self):
        """An instance of the CertInfo class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.certinfo.certinfo.CertInfo)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.certinfo.certinfo import CertInfo
        return CertInfo(self)._select()

    @property
    def NacSettings(self):
        """An instance of the NacSettings class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nacsettings.NacSettings)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.nacsettings.nacsettings import NacSettings
        return NacSettings(self)._select()

    @property
    def ChangeStatusQuery(self):
        """After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.

        Returns:
            number
        """
        return self._get_attribute('changeStatusQuery')
    @ChangeStatusQuery.setter
    def ChangeStatusQuery(self, value):
        self._set_attribute('changeStatusQuery', value)

    @property
    def CookieSize(self):
        """The size of the cookie we send.

        Returns:
            number
        """
        return self._get_attribute('cookieSize')
    @CookieSize.setter
    def CookieSize(self, value):
        self._set_attribute('cookieSize', value)

    @property
    def FragmentSize(self):
        """Size of the frame sent.

        Returns:
            number
        """
        return self._get_attribute('fragmentSize')
    @FragmentSize.setter
    def FragmentSize(self, value):
        self._set_attribute('fragmentSize', value)

    @property
    def MaxClientsPerSecond(self):
        """The number of interfaces to setup per second. Zero value means maximum with no limit.

        Returns:
            number
        """
        return self._get_attribute('maxClientsPerSecond')
    @MaxClientsPerSecond.setter
    def MaxClientsPerSecond(self, value):
        self._set_attribute('maxClientsPerSecond', value)

    @property
    def MaxOutstandingRequests(self):
        """The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.

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
    def Port(self):
        """Port on which we start listening for UDP messages for this plugin.

        Returns:
            number
        """
        return self._get_attribute('port')
    @Port.setter
    def Port(self, value):
        self._set_attribute('port', value)

    @property
    def Timeout(self):
        """After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.

        Returns:
            number
        """
        return self._get_attribute('timeout')
    @Timeout.setter
    def Timeout(self, value):
        self._set_attribute('timeout', value)

    @property
    def TriggerCount(self):
        """How many triggers are sent when a client is started.

        Returns:
            number
        """
        return self._get_attribute('triggerCount')
    @TriggerCount.setter
    def TriggerCount(self, value):
        self._set_attribute('triggerCount', value)

    @property
    def TriggerOrigin(self):
        """The trigger source can be external (outside port) or internal (another plugin or application).

        Returns:
            str
        """
        return self._get_attribute('triggerOrigin')
    @TriggerOrigin.setter
    def TriggerOrigin(self, value):
        self._set_attribute('triggerOrigin', value)

    @property
    def TriggerType(self):
        """Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).

        Returns:
            str
        """
        return self._get_attribute('triggerType')
    @TriggerType.setter
    def TriggerType(self, value):
        self._set_attribute('triggerType', value)

    @property
    def WaitBeforeRun(self):
        """Time to wait before running this protocol

        Returns:
            number
        """
        return self._get_attribute('waitBeforeRun')
    @WaitBeforeRun.setter
    def WaitBeforeRun(self, value):
        self._set_attribute('waitBeforeRun', value)

    @property
    def WaitForCompletion(self):
        """If true the configuration will end after all interfaces are configured.

        Returns:
            bool
        """
        return self._get_attribute('waitForCompletion')
    @WaitForCompletion.setter
    def WaitForCompletion(self, value):
        self._set_attribute('waitForCompletion', value)

    def update(self, ChangeStatusQuery=None, CookieSize=None, FragmentSize=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, Port=None, Timeout=None, TriggerCount=None, TriggerOrigin=None, TriggerType=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Updates a child instance of eapoUdpGlobals on the server.

        Args:
            ChangeStatusQuery (number): After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.
            CookieSize (number): The size of the cookie we send.
            FragmentSize (number): Size of the frame sent.
            MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
            MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
            Port (number): Port on which we start listening for UDP messages for this plugin.
            Timeout (number): After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.
            TriggerCount (number): How many triggers are sent when a client is started.
            TriggerOrigin (str): The trigger source can be external (outside port) or internal (another plugin or application).
            TriggerType (str): Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).
            WaitBeforeRun (number): Time to wait before running this protocol
            WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ChangeStatusQuery=None, CookieSize=None, FragmentSize=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, Port=None, Timeout=None, TriggerCount=None, TriggerOrigin=None, TriggerType=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Adds a new eapoUdpGlobals node on the server and retrieves it in this instance.

        Args:
            ChangeStatusQuery (number): After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.
            CookieSize (number): The size of the cookie we send.
            FragmentSize (number): Size of the frame sent.
            MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
            MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
            Port (number): Port on which we start listening for UDP messages for this plugin.
            Timeout (number): After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.
            TriggerCount (number): How many triggers are sent when a client is started.
            TriggerOrigin (str): The trigger source can be external (outside port) or internal (another plugin or application).
            TriggerType (str): Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).
            WaitBeforeRun (number): Time to wait before running this protocol
            WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Returns:
            self: This instance with all currently retrieved eapoUdpGlobals data using find and the newly added eapoUdpGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the eapoUdpGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ChangeStatusQuery=None, CookieSize=None, FragmentSize=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, ObjectId=None, Port=None, Timeout=None, TriggerCount=None, TriggerOrigin=None, TriggerType=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Finds and retrieves eapoUdpGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve eapoUdpGlobals data from the server.
        By default the find method takes no parameters and will retrieve all eapoUdpGlobals data from the server.

        Args:
            ChangeStatusQuery (number): After how many status query messages received from DUT, we announce we changed state, so DUT initiates a full re-authentication. Zero value means that we never announce a state change.
            CookieSize (number): The size of the cookie we send.
            FragmentSize (number): Size of the frame sent.
            MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
            MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
            ObjectId (str): Unique identifier for this object
            Port (number): Port on which we start listening for UDP messages for this plugin.
            Timeout (number): After how long we declare a failure due to timeout. In external trigger case, we enable the timer after the first seen message.
            TriggerCount (number): How many triggers are sent when a client is started.
            TriggerOrigin (str): The trigger source can be external (outside port) or internal (another plugin or application).
            TriggerType (str): Specify the trigger type when origin is internal. Any DHCP+ mean that after we are receiving the IPv4 address, we send the message (ARP, GratArp, ICMP).
            WaitBeforeRun (number): Time to wait before running this protocol
            WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Returns:
            self: This instance with matching eapoUdpGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of eapoUdpGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the eapoUdpGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
