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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class WebAuthGlobals(Base):
    """Web Authentication Global Options
    The WebAuthGlobals class encapsulates a list of webAuthGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the WebAuthGlobals.find() method.
    The list can be managed by using the WebAuthGlobals.add() and WebAuthGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'webAuthGlobals'
    _SDM_ATT_MAP = {
        'AuthFailure': 'authFailure',
        'AuthSuccess': 'authSuccess',
        'AuthTimeout': 'authTimeout',
        'DefaultFields': 'defaultFields',
        'DelayDhcp': 'delayDhcp',
        'DisableArpResponse': 'disableArpResponse',
        'EnableMaxOutstanding': 'enableMaxOutstanding',
        'InputField1': 'inputField1',
        'InputField2': 'inputField2',
        'InputField3': 'inputField3',
        'MaxClientsPerSecond': 'maxClientsPerSecond',
        'MaxOutstandingRequests': 'maxOutstandingRequests',
        'NumRetry': 'numRetry',
        'ObjectId': 'objectId',
        'PolicyEnable': 'policyEnable',
        'PolicySuccess': 'policySuccess',
        'PolicyTimeout': 'policyTimeout',
        'Port': 'port',
        'Protocol': 'protocol',
        'RedirectFailureUrl': 'redirectFailureUrl',
        'RedirectLoginUrl': 'redirectLoginUrl',
        'RenewDhcp': 'renewDhcp',
        'RequestUrl': 'requestUrl',
        'ResponseDelay': 'responseDelay',
        'WaitBeforeRun': 'waitBeforeRun',
        'WaitForCompletion': 'waitForCompletion',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(WebAuthGlobals, self).__init__(parent, list_op)

    @property
    def AuthFailure(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Text to match on web page to determine if authentication was unsuccessful
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthFailure'])
    @AuthFailure.setter
    def AuthFailure(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AuthFailure'], value)

    @property
    def AuthSuccess(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Text to match on web page to determine if authentication was successful
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthSuccess'])
    @AuthSuccess.setter
    def AuthSuccess(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AuthSuccess'], value)

    @property
    def AuthTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The amount of time to wait for the DUT to return a success or failure page
        """
        return self._get_attribute(self._SDM_ATT_MAP['AuthTimeout'])
    @AuthTimeout.setter
    def AuthTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['AuthTimeout'], value)

    @property
    def DefaultFields(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls if we look up for default HTML tags
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultFields'])
    @DefaultFields.setter
    def DefaultFields(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DefaultFields'], value)

    @property
    def DelayDhcp(self):
        # type: () -> int
        """
        Returns
        -------
        - number: DHCP delay
        """
        return self._get_attribute(self._SDM_ATT_MAP['DelayDhcp'])
    @DelayDhcp.setter
    def DelayDhcp(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['DelayDhcp'], value)

    @property
    def DisableArpResponse(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, bla bla
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisableArpResponse'])
    @DisableArpResponse.setter
    def DisableArpResponse(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['DisableArpResponse'], value)

    @property
    def EnableMaxOutstanding(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If set, maximum number of sessions will be enforced
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMaxOutstanding'])
    @EnableMaxOutstanding.setter
    def EnableMaxOutstanding(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableMaxOutstanding'], value)

    @property
    def InputField1(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The label on the first field of the web authentication form to be matched
        """
        return self._get_attribute(self._SDM_ATT_MAP['InputField1'])
    @InputField1.setter
    def InputField1(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['InputField1'], value)

    @property
    def InputField2(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The label on the second field of the web authentication form to be matched
        """
        return self._get_attribute(self._SDM_ATT_MAP['InputField2'])
    @InputField2.setter
    def InputField2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['InputField2'], value)

    @property
    def InputField3(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The label on the third field of the web authentication form to be matched
        """
        return self._get_attribute(self._SDM_ATT_MAP['InputField3'])
    @InputField3.setter
    def InputField3(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['InputField3'], value)

    @property
    def MaxClientsPerSecond(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of interfaces to setup per second
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxClientsPerSecond'])
    @MaxClientsPerSecond.setter
    def MaxClientsPerSecond(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxClientsPerSecond'], value)

    @property
    def MaxOutstandingRequests(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The maximum number of sessions that can be outstanding at any time
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'])
    @MaxOutstandingRequests.setter
    def MaxOutstandingRequests(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxOutstandingRequests'], value)

    @property
    def NumRetry(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of times to attempt web authentication, including failures and timeouts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumRetry'])
    @NumRetry.setter
    def NumRetry(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumRetry'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def PolicyEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Attempt to read the Request URL after a successful authentication
        """
        return self._get_attribute(self._SDM_ATT_MAP['PolicyEnable'])
    @PolicyEnable.setter
    def PolicyEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['PolicyEnable'], value)

    @property
    def PolicySuccess(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Text to match on web page to determine if policy enforcement was successful
        """
        return self._get_attribute(self._SDM_ATT_MAP['PolicySuccess'])
    @PolicySuccess.setter
    def PolicySuccess(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PolicySuccess'], value)

    @property
    def PolicyTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The amount of time to wait for the DUT to return the Request URL page
        """
        return self._get_attribute(self._SDM_ATT_MAP['PolicyTimeout'])
    @PolicyTimeout.setter
    def PolicyTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PolicyTimeout'], value)

    @property
    def Port(self):
        # type: () -> int
        """
        Returns
        -------
        - number: TCP port number for the Protocol Type
        """
        return self._get_attribute(self._SDM_ATT_MAP['Port'])
    @Port.setter
    def Port(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Port'], value)

    @property
    def Protocol(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The protocol used by the supplicants
        """
        return self._get_attribute(self._SDM_ATT_MAP['Protocol'])
    @Protocol.setter
    def Protocol(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Protocol'], value)

    @property
    def RedirectFailureUrl(self):
        # type: () -> str
        """
        Returns
        -------
        - str: URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself
        """
        return self._get_attribute(self._SDM_ATT_MAP['RedirectFailureUrl'])
    @RedirectFailureUrl.setter
    def RedirectFailureUrl(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RedirectFailureUrl'], value)

    @property
    def RedirectLoginUrl(self):
        # type: () -> str
        """
        Returns
        -------
        - str: URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself
        """
        return self._get_attribute(self._SDM_ATT_MAP['RedirectLoginUrl'])
    @RedirectLoginUrl.setter
    def RedirectLoginUrl(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RedirectLoginUrl'], value)

    @property
    def RenewDhcp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If set, a new DHCP request will be generated following a successful authentication
        """
        return self._get_attribute(self._SDM_ATT_MAP['RenewDhcp'])
    @RenewDhcp.setter
    def RenewDhcp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['RenewDhcp'], value)

    @property
    def RequestUrl(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The URL that the emulated supplicants will request, also used to determine successful authentication
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequestUrl'])
    @RequestUrl.setter
    def RequestUrl(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RequestUrl'], value)

    @property
    def ResponseDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResponseDelay'])
    @ResponseDelay.setter
    def ResponseDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['ResponseDelay'], value)

    @property
    def WaitBeforeRun(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Wait before running this protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitBeforeRun'])
    @WaitBeforeRun.setter
    def WaitBeforeRun(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['WaitBeforeRun'], value)

    @property
    def WaitForCompletion(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true the configuration will end after all interfaces are configured
        """
        return self._get_attribute(self._SDM_ATT_MAP['WaitForCompletion'])
    @WaitForCompletion.setter
    def WaitForCompletion(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['WaitForCompletion'], value)

    def update(self, AuthFailure=None, AuthSuccess=None, AuthTimeout=None, DefaultFields=None, DelayDhcp=None, DisableArpResponse=None, EnableMaxOutstanding=None, InputField1=None, InputField2=None, InputField3=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, NumRetry=None, PolicyEnable=None, PolicySuccess=None, PolicyTimeout=None, Port=None, Protocol=None, RedirectFailureUrl=None, RedirectLoginUrl=None, RenewDhcp=None, RequestUrl=None, ResponseDelay=None, WaitBeforeRun=None, WaitForCompletion=None):
        # type: (str, str, int, bool, int, bool, bool, str, str, str, int, int, int, bool, str, int, int, str, str, str, bool, str, int, int, bool) -> WebAuthGlobals
        """Updates webAuthGlobals resource on the server.

        Args
        ----
        - AuthFailure (str): Text to match on web page to determine if authentication was unsuccessful
        - AuthSuccess (str): Text to match on web page to determine if authentication was successful
        - AuthTimeout (number): The amount of time to wait for the DUT to return a success or failure page
        - DefaultFields (bool): Controls if we look up for default HTML tags
        - DelayDhcp (number): DHCP delay
        - DisableArpResponse (bool): If enabled, bla bla
        - EnableMaxOutstanding (bool): If set, maximum number of sessions will be enforced
        - InputField1 (str): The label on the first field of the web authentication form to be matched
        - InputField2 (str): The label on the second field of the web authentication form to be matched
        - InputField3 (str): The label on the third field of the web authentication form to be matched
        - MaxClientsPerSecond (number): The number of interfaces to setup per second
        - MaxOutstandingRequests (number): The maximum number of sessions that can be outstanding at any time
        - NumRetry (number): The number of times to attempt web authentication, including failures and timeouts.
        - PolicyEnable (bool): Attempt to read the Request URL after a successful authentication
        - PolicySuccess (str): Text to match on web page to determine if policy enforcement was successful
        - PolicyTimeout (number): The amount of time to wait for the DUT to return the Request URL page
        - Port (number): TCP port number for the Protocol Type
        - Protocol (str): The protocol used by the supplicants
        - RedirectFailureUrl (str): URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself
        - RedirectLoginUrl (str): URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself
        - RenewDhcp (bool): If set, a new DHCP request will be generated following a successful authentication
        - RequestUrl (str): The URL that the emulated supplicants will request, also used to determine successful authentication
        - ResponseDelay (number): The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response
        - WaitBeforeRun (number): Wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AuthFailure=None, AuthSuccess=None, AuthTimeout=None, DefaultFields=None, DelayDhcp=None, DisableArpResponse=None, EnableMaxOutstanding=None, InputField1=None, InputField2=None, InputField3=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, NumRetry=None, PolicyEnable=None, PolicySuccess=None, PolicyTimeout=None, Port=None, Protocol=None, RedirectFailureUrl=None, RedirectLoginUrl=None, RenewDhcp=None, RequestUrl=None, ResponseDelay=None, WaitBeforeRun=None, WaitForCompletion=None):
        # type: (str, str, int, bool, int, bool, bool, str, str, str, int, int, int, bool, str, int, int, str, str, str, bool, str, int, int, bool) -> WebAuthGlobals
        """Adds a new webAuthGlobals resource on the server and adds it to the container.

        Args
        ----
        - AuthFailure (str): Text to match on web page to determine if authentication was unsuccessful
        - AuthSuccess (str): Text to match on web page to determine if authentication was successful
        - AuthTimeout (number): The amount of time to wait for the DUT to return a success or failure page
        - DefaultFields (bool): Controls if we look up for default HTML tags
        - DelayDhcp (number): DHCP delay
        - DisableArpResponse (bool): If enabled, bla bla
        - EnableMaxOutstanding (bool): If set, maximum number of sessions will be enforced
        - InputField1 (str): The label on the first field of the web authentication form to be matched
        - InputField2 (str): The label on the second field of the web authentication form to be matched
        - InputField3 (str): The label on the third field of the web authentication form to be matched
        - MaxClientsPerSecond (number): The number of interfaces to setup per second
        - MaxOutstandingRequests (number): The maximum number of sessions that can be outstanding at any time
        - NumRetry (number): The number of times to attempt web authentication, including failures and timeouts.
        - PolicyEnable (bool): Attempt to read the Request URL after a successful authentication
        - PolicySuccess (str): Text to match on web page to determine if policy enforcement was successful
        - PolicyTimeout (number): The amount of time to wait for the DUT to return the Request URL page
        - Port (number): TCP port number for the Protocol Type
        - Protocol (str): The protocol used by the supplicants
        - RedirectFailureUrl (str): URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself
        - RedirectLoginUrl (str): URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself
        - RenewDhcp (bool): If set, a new DHCP request will be generated following a successful authentication
        - RequestUrl (str): The URL that the emulated supplicants will request, also used to determine successful authentication
        - ResponseDelay (number): The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response
        - WaitBeforeRun (number): Wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured

        Returns
        -------
        - self: This instance with all currently retrieved webAuthGlobals resources using find and the newly added webAuthGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained webAuthGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AuthFailure=None, AuthSuccess=None, AuthTimeout=None, DefaultFields=None, DelayDhcp=None, DisableArpResponse=None, EnableMaxOutstanding=None, InputField1=None, InputField2=None, InputField3=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, NumRetry=None, ObjectId=None, PolicyEnable=None, PolicySuccess=None, PolicyTimeout=None, Port=None, Protocol=None, RedirectFailureUrl=None, RedirectLoginUrl=None, RenewDhcp=None, RequestUrl=None, ResponseDelay=None, WaitBeforeRun=None, WaitForCompletion=None):
        # type: (str, str, int, bool, int, bool, bool, str, str, str, int, int, int, str, bool, str, int, int, str, str, str, bool, str, int, int, bool) -> WebAuthGlobals
        """Finds and retrieves webAuthGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve webAuthGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all webAuthGlobals resources from the server.

        Args
        ----
        - AuthFailure (str): Text to match on web page to determine if authentication was unsuccessful
        - AuthSuccess (str): Text to match on web page to determine if authentication was successful
        - AuthTimeout (number): The amount of time to wait for the DUT to return a success or failure page
        - DefaultFields (bool): Controls if we look up for default HTML tags
        - DelayDhcp (number): DHCP delay
        - DisableArpResponse (bool): If enabled, bla bla
        - EnableMaxOutstanding (bool): If set, maximum number of sessions will be enforced
        - InputField1 (str): The label on the first field of the web authentication form to be matched
        - InputField2 (str): The label on the second field of the web authentication form to be matched
        - InputField3 (str): The label on the third field of the web authentication form to be matched
        - MaxClientsPerSecond (number): The number of interfaces to setup per second
        - MaxOutstandingRequests (number): The maximum number of sessions that can be outstanding at any time
        - NumRetry (number): The number of times to attempt web authentication, including failures and timeouts.
        - ObjectId (str): Unique identifier for this object
        - PolicyEnable (bool): Attempt to read the Request URL after a successful authentication
        - PolicySuccess (str): Text to match on web page to determine if policy enforcement was successful
        - PolicyTimeout (number): The amount of time to wait for the DUT to return the Request URL page
        - Port (number): TCP port number for the Protocol Type
        - Protocol (str): The protocol used by the supplicants
        - RedirectFailureUrl (str): URL that the DUT will redirect a failed supplicant to if the DUT does not generate the page itself
        - RedirectLoginUrl (str): URL that the DUT will redirect the supplicant to if the DUT does not generate the page itself
        - RenewDhcp (bool): If set, a new DHCP request will be generated following a successful authentication
        - RequestUrl (str): The URL that the emulated supplicants will request, also used to determine successful authentication
        - ResponseDelay (number): The amount of time that the supplicant will wait after receiving the WebAuth credential request page before sending a response
        - WaitBeforeRun (number): Wait before running this protocol
        - WaitForCompletion (bool): If true the configuration will end after all interfaces are configured

        Returns
        -------
        - self: This instance with matching webAuthGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of webAuthGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the webAuthGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
