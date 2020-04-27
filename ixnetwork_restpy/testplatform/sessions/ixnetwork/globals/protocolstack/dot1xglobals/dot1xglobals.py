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


class Dot1xGlobals(Base):
    """Global settings placeholder for Dot1x
    The Dot1xGlobals class encapsulates a list of dot1xGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the Dot1xGlobals.find() method.
    The list can be managed by using the Dot1xGlobals.add() and Dot1xGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dot1xGlobals'

    def __init__(self, parent):
        super(Dot1xGlobals, self).__init__(parent)

    @property
    def CertInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.certinfo.certinfo.CertInfo): An instance of the CertInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.certinfo.certinfo import CertInfo
        return CertInfo(self)._select()

    @property
    def NacSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nacsettings.NacSettings): An instance of the NacSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.nacsettings.nacsettings import NacSettings
        return NacSettings(self)._select()

    @property
    def AuthOnNoResponse(self):
        """
        Returns
        -------
        - bool: If the DUT is not responding to EAPoL Start after configured number of retries, declare the session a success.
        """
        return self._get_attribute('authOnNoResponse')
    @AuthOnNoResponse.setter
    def AuthOnNoResponse(self, value):
        self._set_attribute('authOnNoResponse', value)

    @property
    def AuthPeriod(self):
        """
        Returns
        -------
        - number: Time to wait for Authentication request
        """
        return self._get_attribute('authPeriod')
    @AuthPeriod.setter
    def AuthPeriod(self, value):
        self._set_attribute('authPeriod', value)

    @property
    def Authenticator(self):
        """
        Returns
        -------
        - str: Mac address used to send frames if multicast is used.
        """
        return self._get_attribute('authenticator')
    @Authenticator.setter
    def Authenticator(self, value):
        self._set_attribute('authenticator', value)

    @property
    def AuthenticatorMulticast(self):
        """
        Returns
        -------
        - bool: When using vlan and multicast, this value need to be true.
        """
        return self._get_attribute('authenticatorMulticast')
    @AuthenticatorMulticast.setter
    def AuthenticatorMulticast(self, value):
        self._set_attribute('authenticatorMulticast', value)

    @property
    def DisableLogoff(self):
        """
        Returns
        -------
        - bool: Do not send Logoff message when closing a session.
        """
        return self._get_attribute('disableLogoff')
    @DisableLogoff.setter
    def DisableLogoff(self, value):
        self._set_attribute('disableLogoff', value)

    @property
    def DutTestMode(self):
        """
        Returns
        -------
        - str: Specify what is the dut port mode.
        """
        return self._get_attribute('dutTestMode')
    @DutTestMode.setter
    def DutTestMode(self, value):
        self._set_attribute('dutTestMode', value)

    @property
    def FragmentSize(self):
        """
        Returns
        -------
        - number: Size of the frame sent.
        """
        return self._get_attribute('fragmentSize')
    @FragmentSize.setter
    def FragmentSize(self, value):
        self._set_attribute('fragmentSize', value)

    @property
    def HeldPeriod(self):
        """
        Returns
        -------
        - number: Time to wait before sending new authentication requests after a failure
        """
        return self._get_attribute('heldPeriod')
    @HeldPeriod.setter
    def HeldPeriod(self, value):
        self._set_attribute('heldPeriod', value)

    @property
    def LogoffMaxClientsPerSecond(self):
        """
        Returns
        -------
        - number: The number of interfaces to logoff per second. Zero value means maximum with no limit.
        """
        return self._get_attribute('logoffMaxClientsPerSecond')
    @LogoffMaxClientsPerSecond.setter
    def LogoffMaxClientsPerSecond(self, value):
        self._set_attribute('logoffMaxClientsPerSecond', value)

    @property
    def LogoffMaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: The maximum number of logoff sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        """
        return self._get_attribute('logoffMaxOutstandingRequests')
    @LogoffMaxOutstandingRequests.setter
    def LogoffMaxOutstandingRequests(self, value):
        self._set_attribute('logoffMaxOutstandingRequests', value)

    @property
    def MacAuthPrefix(self):
        """
        Returns
        -------
        - str: When using machine authentication, a prefix is needed to differentiate between users and machines.
        """
        return self._get_attribute('macAuthPrefix')
    @MacAuthPrefix.setter
    def MacAuthPrefix(self, value):
        self._set_attribute('macAuthPrefix', value)

    @property
    def MaxClientsPerSecond(self):
        """
        Returns
        -------
        - number: The number of interfaces to setup per second. Zero value means maximum with no limit.
        """
        return self._get_attribute('maxClientsPerSecond')
    @MaxClientsPerSecond.setter
    def MaxClientsPerSecond(self, value):
        self._set_attribute('maxClientsPerSecond', value)

    @property
    def MaxOutstandingRequests(self):
        """
        Returns
        -------
        - number: The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        """
        return self._get_attribute('maxOutstandingRequests')
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute('maxOutstandingRequests', value)

    @property
    def MaxStart(self):
        """
        Returns
        -------
        - number: Number of times to send EAPoL Start frames before assuming sessions are considered timeout if no frame is received from authenticator. If Authorized on no response global option is checked, sessions will be declared a success
        """
        return self._get_attribute('maxStart')
    @MaxStart.setter
    def MaxStart(self, value):
        self._set_attribute('maxStart', value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

    @property
    def OnlyMulticast(self):
        """
        Returns
        -------
        - bool: Specify if destination MAC address can be multicast.
        """
        return self._get_attribute('onlyMulticast')
    @OnlyMulticast.setter
    def OnlyMulticast(self, value):
        self._set_attribute('onlyMulticast', value)

    @property
    def StartPeriod(self):
        """
        Returns
        -------
        - number: Time to wait for ID request
        """
        return self._get_attribute('startPeriod')
    @StartPeriod.setter
    def StartPeriod(self, value):
        self._set_attribute('startPeriod', value)

    @property
    def StatsPeriod(self):
        """
        Returns
        -------
        - number: Protocol option.
        """
        return self._get_attribute('statsPeriod')
    @StatsPeriod.setter
    def StatsPeriod(self, value):
        self._set_attribute('statsPeriod', value)

    @property
    def SuccessiveStart(self):
        """
        Returns
        -------
        - number: Number of EAPoL Start messages that are sent when a client is started.
        """
        return self._get_attribute('successiveStart')
    @SuccessiveStart.setter
    def SuccessiveStart(self, value):
        self._set_attribute('successiveStart', value)

    @property
    def WaitBeforeRun(self):
        """
        Returns
        -------
        - number: Time to wait before running this protocol
        """
        return self._get_attribute('waitBeforeRun')
    @WaitBeforeRun.setter
    def WaitBeforeRun(self, value):
        self._set_attribute('waitBeforeRun', value)

    @property
    def WaitForCompletion(self):
        """
        Returns
        -------
        - bool: If true the configuration will end after all interfaces are configured.
        """
        return self._get_attribute('waitForCompletion')
    @WaitForCompletion.setter
    def WaitForCompletion(self, value):
        self._set_attribute('waitForCompletion', value)

    def update(self, AuthOnNoResponse=None, AuthPeriod=None, Authenticator=None, AuthenticatorMulticast=None, DisableLogoff=None, DutTestMode=None, FragmentSize=None, HeldPeriod=None, LogoffMaxClientsPerSecond=None, LogoffMaxOutstandingRequests=None, MacAuthPrefix=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, MaxStart=None, OnlyMulticast=None, StartPeriod=None, StatsPeriod=None, SuccessiveStart=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Updates dot1xGlobals resource on the server.

        Args
        ----
        - AuthOnNoResponse (bool): If the DUT is not responding to EAPoL Start after configured number of retries, declare the session a success.
        - AuthPeriod (number): Time to wait for Authentication request
        - Authenticator (str): Mac address used to send frames if multicast is used.
        - AuthenticatorMulticast (bool): When using vlan and multicast, this value need to be true.
        - DisableLogoff (bool): Do not send Logoff message when closing a session.
        - DutTestMode (str): Specify what is the dut port mode.
        - FragmentSize (number): Size of the frame sent.
        - HeldPeriod (number): Time to wait before sending new authentication requests after a failure
        - LogoffMaxClientsPerSecond (number): The number of interfaces to logoff per second. Zero value means maximum with no limit.
        - LogoffMaxOutstandingRequests (number): The maximum number of logoff sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - MacAuthPrefix (str): When using machine authentication, a prefix is needed to differentiate between users and machines.
        - MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - MaxStart (number): Number of times to send EAPoL Start frames before assuming sessions are considered timeout if no frame is received from authenticator. If Authorized on no response global option is checked, sessions will be declared a success
        - OnlyMulticast (bool): Specify if destination MAC address can be multicast.
        - StartPeriod (number): Time to wait for ID request
        - StatsPeriod (number): Protocol option.
        - SuccessiveStart (number): Number of EAPoL Start messages that are sent when a client is started.
        - WaitBeforeRun (number): Time to wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AuthOnNoResponse=None, AuthPeriod=None, Authenticator=None, AuthenticatorMulticast=None, DisableLogoff=None, DutTestMode=None, FragmentSize=None, HeldPeriod=None, LogoffMaxClientsPerSecond=None, LogoffMaxOutstandingRequests=None, MacAuthPrefix=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, MaxStart=None, OnlyMulticast=None, StartPeriod=None, StatsPeriod=None, SuccessiveStart=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Adds a new dot1xGlobals resource on the server and adds it to the container.

        Args
        ----
        - AuthOnNoResponse (bool): If the DUT is not responding to EAPoL Start after configured number of retries, declare the session a success.
        - AuthPeriod (number): Time to wait for Authentication request
        - Authenticator (str): Mac address used to send frames if multicast is used.
        - AuthenticatorMulticast (bool): When using vlan and multicast, this value need to be true.
        - DisableLogoff (bool): Do not send Logoff message when closing a session.
        - DutTestMode (str): Specify what is the dut port mode.
        - FragmentSize (number): Size of the frame sent.
        - HeldPeriod (number): Time to wait before sending new authentication requests after a failure
        - LogoffMaxClientsPerSecond (number): The number of interfaces to logoff per second. Zero value means maximum with no limit.
        - LogoffMaxOutstandingRequests (number): The maximum number of logoff sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - MacAuthPrefix (str): When using machine authentication, a prefix is needed to differentiate between users and machines.
        - MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - MaxStart (number): Number of times to send EAPoL Start frames before assuming sessions are considered timeout if no frame is received from authenticator. If Authorized on no response global option is checked, sessions will be declared a success
        - OnlyMulticast (bool): Specify if destination MAC address can be multicast.
        - StartPeriod (number): Time to wait for ID request
        - StatsPeriod (number): Protocol option.
        - SuccessiveStart (number): Number of EAPoL Start messages that are sent when a client is started.
        - WaitBeforeRun (number): Time to wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Returns
        -------
        - self: This instance with all currently retrieved dot1xGlobals resources using find and the newly added dot1xGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained dot1xGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AuthOnNoResponse=None, AuthPeriod=None, Authenticator=None, AuthenticatorMulticast=None, DisableLogoff=None, DutTestMode=None, FragmentSize=None, HeldPeriod=None, LogoffMaxClientsPerSecond=None, LogoffMaxOutstandingRequests=None, MacAuthPrefix=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, MaxStart=None, ObjectId=None, OnlyMulticast=None, StartPeriod=None, StatsPeriod=None, SuccessiveStart=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Finds and retrieves dot1xGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dot1xGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dot1xGlobals resources from the server.

        Args
        ----
        - AuthOnNoResponse (bool): If the DUT is not responding to EAPoL Start after configured number of retries, declare the session a success.
        - AuthPeriod (number): Time to wait for Authentication request
        - Authenticator (str): Mac address used to send frames if multicast is used.
        - AuthenticatorMulticast (bool): When using vlan and multicast, this value need to be true.
        - DisableLogoff (bool): Do not send Logoff message when closing a session.
        - DutTestMode (str): Specify what is the dut port mode.
        - FragmentSize (number): Size of the frame sent.
        - HeldPeriod (number): Time to wait before sending new authentication requests after a failure
        - LogoffMaxClientsPerSecond (number): The number of interfaces to logoff per second. Zero value means maximum with no limit.
        - LogoffMaxOutstandingRequests (number): The maximum number of logoff sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - MacAuthPrefix (str): When using machine authentication, a prefix is needed to differentiate between users and machines.
        - MaxClientsPerSecond (number): The number of interfaces to setup per second. Zero value means maximum with no limit.
        - MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment. Zero value means maximum with no limit.
        - MaxStart (number): Number of times to send EAPoL Start frames before assuming sessions are considered timeout if no frame is received from authenticator. If Authorized on no response global option is checked, sessions will be declared a success
        - ObjectId (str): Unique identifier for this object
        - OnlyMulticast (bool): Specify if destination MAC address can be multicast.
        - StartPeriod (number): Time to wait for ID request
        - StatsPeriod (number): Protocol option.
        - SuccessiveStart (number): Number of EAPoL Start messages that are sent when a client is started.
        - WaitBeforeRun (number): Time to wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured.

        Returns
        -------
        - self: This instance with matching dot1xGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dot1xGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dot1xGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
