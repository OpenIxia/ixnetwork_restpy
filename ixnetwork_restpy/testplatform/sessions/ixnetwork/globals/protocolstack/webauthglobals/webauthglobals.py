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


class WebAuthGlobals(Base):
    """Web Authentication Global Options
    The WebAuthGlobals class encapsulates a list of webAuthGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the WebAuthGlobals.find() method.
    The list can be managed by the user by using the WebAuthGlobals.add() and WebAuthGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'webAuthGlobals'

    def __init__(self, parent):
        super(WebAuthGlobals, self).__init__(parent)

    @property
    def AuthFailure(self):
        """Text to match on web page to determine if authentication was unsuccessful

        Returns:
            str
        """
        return self._get_attribute('authFailure')
    @AuthFailure.setter
    def AuthFailure(self, value):
        self._set_attribute('authFailure', value)

    @property
    def AuthSuccess(self):
        """Text to match on web page to determine if authentication was successful

        Returns:
            str
        """
        return self._get_attribute('authSuccess')
    @AuthSuccess.setter
    def AuthSuccess(self, value):
        self._set_attribute('authSuccess', value)

    @property
    def AuthTimeout(self):
        """The amount of time to wait for the DUT to return a success or failure page

        Returns:
            number
        """
        return self._get_attribute('authTimeout')
    @AuthTimeout.setter
    def AuthTimeout(self, value):
        self._set_attribute('authTimeout', value)

    @property
    def DefaultFields(self):
        """Controls if we look up for default HTML tags

        Returns:
            bool
        """
        return self._get_attribute('defaultFields')
    @DefaultFields.setter
    def DefaultFields(self, value):
        self._set_attribute('defaultFields', value)

    @property
    def DelayDhcp(self):
        """DHCP delay

        Returns:
            number
        """
        return self._get_attribute('delayDhcp')
    @DelayDhcp.setter
    def DelayDhcp(self, value):
        self._set_attribute('delayDhcp', value)

    @property
    def DisableArpResponse(self):
        """If enabled, bla bla

        Returns:
            bool
        """
        return self._get_attribute('disableArpResponse')
    @DisableArpResponse.setter
    def DisableArpResponse(self, value):
        self._set_attribute('disableArpResponse', value)

    @property
    def EnableMaxOutstanding(self):
        """If set, maximum number of sessions will be enforced

        Returns:
            bool
        """
        return self._get_attribute('enableMaxOutstanding')
    @EnableMaxOutstanding.setter
    def EnableMaxOutstanding(self, value):
        self._set_attribute('enableMaxOutstanding', value)

    @property
    def InputField1(self):
        """The label on the first field of the web authentication form to be matched

        Returns:
            str
        """
        return self._get_attribute('inputField1')
    @InputField1.setter
    def InputField1(self, value):
        self._set_attribute('inputField1', value)

    @property
    def InputField2(self):
        """The label on the second field of the web authentication form to be matched

        Returns:
            str
        """
        return self._get_attribute('inputField2')
    @InputField2.setter
    def InputField2(self, value):
        self._set_attribute('inputField2', value)

    @property
    def InputField3(self):
        """The label on the third field of the web authentication form to be matched

        Returns:
            str
        """
        return self._get_attribute('inputField3')
    @InputField3.setter
    def InputField3(self, value):
        self._set_attribute('inputField3', value)

    @property
    def MaxClientsPerSecond(self):
        """The number of interfaces to setup per second

        Returns:
            number
        """
        return self._get_attribute('maxClientsPerSecond')
    @MaxClientsPerSecond.setter
    def MaxClientsPerSecond(self, value):
        self._set_attribute('maxClientsPerSecond', value)

    @property
    def MaxOutstandingRequests(self):
        """The maximum number of sessions that can be outstanding at any time

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingRequests')
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        self._set_attribute('maxOutstandingRequests', value)

    @property
    def NumRetry(self):
        """The number of times to attempt web authentication, including failures and timeouts.

        Returns:
            number
        """
        return self._get_attribute('numRetry')
    @NumRetry.setter
    def NumRetry(self, value):
        self._set_attribute('numRetry', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def PolicyEnable(self):
        """Attempt to read the Request URL after a successful authentication

        Returns:
            bool
        """
        return self._get_attribute('policyEnable')
    @PolicyEnable.setter
    def PolicyEnable(self, value):
        self._set_attribute('policyEnable', value)

    @property
    def PolicySuccess(self):
        """Text to match on web page to determine if policy enforcement was successful

        Returns:
            str
        """
        return self._get_attribute('policySuccess')
    @PolicySuccess.setter
    def PolicySuccess(self, value):
        self._set_attribute('policySuccess', value)

    @property
    def PolicyTimeout(self):
        """The amount of time to wait for the DUT to return the Request URL page

        Returns:
            number
        """
        return self._get_attribute('policyTimeout')
    @PolicyTimeout.setter
    def PolicyTimeout(self, value):
        self._set_attribute('policyTimeout', value)

    @property
    def Port(self):
        """TCP port number for the Protocol Type

        Returns:
            number
        """
        return self._get_attribute('port')
    @Port.setter
    def Port(self, value):
        self._set_attribute('port', value)

    @property
    def Protocol(self):
        """The protocol used by the supplicants

        Returns:
            str
        """
        return self._get_attribute('protocol')
    @Protocol.setter
    def Protocol(self, value):
        self._set_attribute('protocol', value)

    @property
    def RedirectFailureUrl(self):
        """URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself

        Returns:
            str
        """
        return self._get_attribute('redirectFailureUrl')
    @RedirectFailureUrl.setter
    def RedirectFailureUrl(self, value):
        self._set_attribute('redirectFailureUrl', value)

    @property
    def RedirectLoginUrl(self):
        """URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself

        Returns:
            str
        """
        return self._get_attribute('redirectLoginUrl')
    @RedirectLoginUrl.setter
    def RedirectLoginUrl(self, value):
        self._set_attribute('redirectLoginUrl', value)

    @property
    def RenewDhcp(self):
        """If set, a new DHCP request will be generated following a successful authentication

        Returns:
            bool
        """
        return self._get_attribute('renewDhcp')
    @RenewDhcp.setter
    def RenewDhcp(self, value):
        self._set_attribute('renewDhcp', value)

    @property
    def RequestUrl(self):
        """The URL that the emulated supplicants will request, also used to determine successful authentication

        Returns:
            str
        """
        return self._get_attribute('requestUrl')
    @RequestUrl.setter
    def RequestUrl(self, value):
        self._set_attribute('requestUrl', value)

    @property
    def ResponseDelay(self):
        """The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response

        Returns:
            number
        """
        return self._get_attribute('responseDelay')
    @ResponseDelay.setter
    def ResponseDelay(self, value):
        self._set_attribute('responseDelay', value)

    @property
    def WaitBeforeRun(self):
        """Wait before running this protocol

        Returns:
            number
        """
        return self._get_attribute('waitBeforeRun')
    @WaitBeforeRun.setter
    def WaitBeforeRun(self, value):
        self._set_attribute('waitBeforeRun', value)

    @property
    def WaitForCompletion(self):
        """If true the configuration will end after all interfaces are configured

        Returns:
            bool
        """
        return self._get_attribute('waitForCompletion')
    @WaitForCompletion.setter
    def WaitForCompletion(self, value):
        self._set_attribute('waitForCompletion', value)

    def update(self, AuthFailure=None, AuthSuccess=None, AuthTimeout=None, DefaultFields=None, DelayDhcp=None, DisableArpResponse=None, EnableMaxOutstanding=None, InputField1=None, InputField2=None, InputField3=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, NumRetry=None, PolicyEnable=None, PolicySuccess=None, PolicyTimeout=None, Port=None, Protocol=None, RedirectFailureUrl=None, RedirectLoginUrl=None, RenewDhcp=None, RequestUrl=None, ResponseDelay=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Updates a child instance of webAuthGlobals on the server.

        Args:
            AuthFailure (str): Text to match on web page to determine if authentication was unsuccessful
            AuthSuccess (str): Text to match on web page to determine if authentication was successful
            AuthTimeout (number): The amount of time to wait for the DUT to return a success or failure page
            DefaultFields (bool): Controls if we look up for default HTML tags
            DelayDhcp (number): DHCP delay
            DisableArpResponse (bool): If enabled, bla bla
            EnableMaxOutstanding (bool): If set, maximum number of sessions will be enforced
            InputField1 (str): The label on the first field of the web authentication form to be matched
            InputField2 (str): The label on the second field of the web authentication form to be matched
            InputField3 (str): The label on the third field of the web authentication form to be matched
            MaxClientsPerSecond (number): The number of interfaces to setup per second
            MaxOutstandingRequests (number): The maximum number of sessions that can be outstanding at any time
            NumRetry (number): The number of times to attempt web authentication, including failures and timeouts.
            PolicyEnable (bool): Attempt to read the Request URL after a successful authentication
            PolicySuccess (str): Text to match on web page to determine if policy enforcement was successful
            PolicyTimeout (number): The amount of time to wait for the DUT to return the Request URL page
            Port (number): TCP port number for the Protocol Type
            Protocol (str): The protocol used by the supplicants
            RedirectFailureUrl (str): URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself
            RedirectLoginUrl (str): URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself
            RenewDhcp (bool): If set, a new DHCP request will be generated following a successful authentication
            RequestUrl (str): The URL that the emulated supplicants will request, also used to determine successful authentication
            ResponseDelay (number): The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response
            WaitBeforeRun (number): Wait before running this protocol
            WaitForCompletion (bool): If true the configuration will end after all interfaces are configured

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AuthFailure=None, AuthSuccess=None, AuthTimeout=None, DefaultFields=None, DelayDhcp=None, DisableArpResponse=None, EnableMaxOutstanding=None, InputField1=None, InputField2=None, InputField3=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, NumRetry=None, PolicyEnable=None, PolicySuccess=None, PolicyTimeout=None, Port=None, Protocol=None, RedirectFailureUrl=None, RedirectLoginUrl=None, RenewDhcp=None, RequestUrl=None, ResponseDelay=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Adds a new webAuthGlobals node on the server and retrieves it in this instance.

        Args:
            AuthFailure (str): Text to match on web page to determine if authentication was unsuccessful
            AuthSuccess (str): Text to match on web page to determine if authentication was successful
            AuthTimeout (number): The amount of time to wait for the DUT to return a success or failure page
            DefaultFields (bool): Controls if we look up for default HTML tags
            DelayDhcp (number): DHCP delay
            DisableArpResponse (bool): If enabled, bla bla
            EnableMaxOutstanding (bool): If set, maximum number of sessions will be enforced
            InputField1 (str): The label on the first field of the web authentication form to be matched
            InputField2 (str): The label on the second field of the web authentication form to be matched
            InputField3 (str): The label on the third field of the web authentication form to be matched
            MaxClientsPerSecond (number): The number of interfaces to setup per second
            MaxOutstandingRequests (number): The maximum number of sessions that can be outstanding at any time
            NumRetry (number): The number of times to attempt web authentication, including failures and timeouts.
            PolicyEnable (bool): Attempt to read the Request URL after a successful authentication
            PolicySuccess (str): Text to match on web page to determine if policy enforcement was successful
            PolicyTimeout (number): The amount of time to wait for the DUT to return the Request URL page
            Port (number): TCP port number for the Protocol Type
            Protocol (str): The protocol used by the supplicants
            RedirectFailureUrl (str): URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself
            RedirectLoginUrl (str): URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself
            RenewDhcp (bool): If set, a new DHCP request will be generated following a successful authentication
            RequestUrl (str): The URL that the emulated supplicants will request, also used to determine successful authentication
            ResponseDelay (number): The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response
            WaitBeforeRun (number): Wait before running this protocol
            WaitForCompletion (bool): If true the configuration will end after all interfaces are configured

        Returns:
            self: This instance with all currently retrieved webAuthGlobals data using find and the newly added webAuthGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the webAuthGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AuthFailure=None, AuthSuccess=None, AuthTimeout=None, DefaultFields=None, DelayDhcp=None, DisableArpResponse=None, EnableMaxOutstanding=None, InputField1=None, InputField2=None, InputField3=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, NumRetry=None, ObjectId=None, PolicyEnable=None, PolicySuccess=None, PolicyTimeout=None, Port=None, Protocol=None, RedirectFailureUrl=None, RedirectLoginUrl=None, RenewDhcp=None, RequestUrl=None, ResponseDelay=None, WaitBeforeRun=None, WaitForCompletion=None):
        """Finds and retrieves webAuthGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve webAuthGlobals data from the server.
        By default the find method takes no parameters and will retrieve all webAuthGlobals data from the server.

        Args:
            AuthFailure (str): Text to match on web page to determine if authentication was unsuccessful
            AuthSuccess (str): Text to match on web page to determine if authentication was successful
            AuthTimeout (number): The amount of time to wait for the DUT to return a success or failure page
            DefaultFields (bool): Controls if we look up for default HTML tags
            DelayDhcp (number): DHCP delay
            DisableArpResponse (bool): If enabled, bla bla
            EnableMaxOutstanding (bool): If set, maximum number of sessions will be enforced
            InputField1 (str): The label on the first field of the web authentication form to be matched
            InputField2 (str): The label on the second field of the web authentication form to be matched
            InputField3 (str): The label on the third field of the web authentication form to be matched
            MaxClientsPerSecond (number): The number of interfaces to setup per second
            MaxOutstandingRequests (number): The maximum number of sessions that can be outstanding at any time
            NumRetry (number): The number of times to attempt web authentication, including failures and timeouts.
            ObjectId (str): Unique identifier for this object
            PolicyEnable (bool): Attempt to read the Request URL after a successful authentication
            PolicySuccess (str): Text to match on web page to determine if policy enforcement was successful
            PolicyTimeout (number): The amount of time to wait for the DUT to return the Request URL page
            Port (number): TCP port number for the Protocol Type
            Protocol (str): The protocol used by the supplicants
            RedirectFailureUrl (str): URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself
            RedirectLoginUrl (str): URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself
            RenewDhcp (bool): If set, a new DHCP request will be generated following a successful authentication
            RequestUrl (str): The URL that the emulated supplicants will request, also used to determine successful authentication
            ResponseDelay (number): The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response
            WaitBeforeRun (number): Wait before running this protocol
            WaitForCompletion (bool): If true the configuration will end after all interfaces are configured

        Returns:
            self: This instance with matching webAuthGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of webAuthGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the webAuthGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
