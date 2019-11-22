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


class FcoeFwdGlobals(Base):
    """StackManager FCoE Global Settings
    The FcoeFwdGlobals class encapsulates a list of fcoeFwdGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the FcoeFwdGlobals.find() method.
    The list can be managed by the user by using the FcoeFwdGlobals.add() and FcoeFwdGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcoeFwdGlobals'

    def __init__(self, parent):
        super(FcoeFwdGlobals, self).__init__(parent)

    @property
    def AcceptPartialConfig(self):
        """This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.

        Returns:
            bool
        """
        return self._get_attribute('acceptPartialConfig')
    @AcceptPartialConfig.setter
    def AcceptPartialConfig(self, value):
        self._set_attribute('acceptPartialConfig', value)

    @property
    def DcbxTimeout(self):
        """The number of seconds to wait for DCBX to negotiate.

        Returns:
            number
        """
        return self._get_attribute('dcbxTimeout')
    @DcbxTimeout.setter
    def DcbxTimeout(self, value):
        self._set_attribute('dcbxTimeout', value)

    @property
    def FipClearVlinkWithPortIds(self):
        """Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.

        Returns:
            bool
        """
        return self._get_attribute('fipClearVlinkWithPortIds')
    @FipClearVlinkWithPortIds.setter
    def FipClearVlinkWithPortIds(self, value):
        self._set_attribute('fipClearVlinkWithPortIds', value)

    @property
    def MaxPacketsPerSecond(self):
        """The maximum number of requests transmitted in each second.

        Returns:
            number
        """
        return self._get_attribute('maxPacketsPerSecond')
    @MaxPacketsPerSecond.setter
    def MaxPacketsPerSecond(self, value):
        self._set_attribute('maxPacketsPerSecond', value)

    @property
    def MaxRetries(self):
        """The number of request retries for each negotiation stage in case of response timeout or error.

        Returns:
            number
        """
        return self._get_attribute('maxRetries')
    @MaxRetries.setter
    def MaxRetries(self, value):
        self._set_attribute('maxRetries', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def RetryInterval(self):
        """The number of seconds to wait for a response before sending a new request.

        Returns:
            number
        """
        return self._get_attribute('retryInterval')
    @RetryInterval.setter
    def RetryInterval(self, value):
        self._set_attribute('retryInterval', value)

    def update(self, AcceptPartialConfig=None, DcbxTimeout=None, FipClearVlinkWithPortIds=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None):
        """Updates a child instance of fcoeFwdGlobals on the server.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            FipClearVlinkWithPortIds (bool): Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
            MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
            RetryInterval (number): The number of seconds to wait for a response before sending a new request.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AcceptPartialConfig=None, DcbxTimeout=None, FipClearVlinkWithPortIds=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None):
        """Adds a new fcoeFwdGlobals node on the server and retrieves it in this instance.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            FipClearVlinkWithPortIds (bool): Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
            MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
            RetryInterval (number): The number of seconds to wait for a response before sending a new request.

        Returns:
            self: This instance with all currently retrieved fcoeFwdGlobals data using find and the newly added fcoeFwdGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the fcoeFwdGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, DcbxTimeout=None, FipClearVlinkWithPortIds=None, MaxPacketsPerSecond=None, MaxRetries=None, ObjectId=None, RetryInterval=None):
        """Finds and retrieves fcoeFwdGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve fcoeFwdGlobals data from the server.
        By default the find method takes no parameters and will retrieve all fcoeFwdGlobals data from the server.

        Args:
            AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.
            DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
            FipClearVlinkWithPortIds (bool): Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.
            MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
            MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
            ObjectId (str): Unique identifier for this object
            RetryInterval (number): The number of seconds to wait for a response before sending a new request.

        Returns:
            self: This instance with matching fcoeFwdGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of fcoeFwdGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the fcoeFwdGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
