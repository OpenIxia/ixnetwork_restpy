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


class FcoeFwdGlobals(Base):
    """StackManager FCoE Global Settings
    The FcoeFwdGlobals class encapsulates a list of fcoeFwdGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the FcoeFwdGlobals.find() method.
    The list can be managed by using the FcoeFwdGlobals.add() and FcoeFwdGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcoeFwdGlobals'
    _SDM_ATT_MAP = {
        'AcceptPartialConfig': 'acceptPartialConfig',
        'DcbxTimeout': 'dcbxTimeout',
        'FipClearVlinkWithPortIds': 'fipClearVlinkWithPortIds',
        'MaxPacketsPerSecond': 'maxPacketsPerSecond',
        'MaxRetries': 'maxRetries',
        'ObjectId': 'objectId',
        'RetryInterval': 'retryInterval',
    }

    def __init__(self, parent):
        super(FcoeFwdGlobals, self).__init__(parent)

    @property
    def AcceptPartialConfig(self):
        """
        Returns
        -------
        - bool: This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'])
    @AcceptPartialConfig.setter
    def AcceptPartialConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'], value)

    @property
    def DcbxTimeout(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for DCBX to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DcbxTimeout'])
    @DcbxTimeout.setter
    def DcbxTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DcbxTimeout'], value)

    @property
    def FipClearVlinkWithPortIds(self):
        """
        Returns
        -------
        - bool: Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FipClearVlinkWithPortIds'])
    @FipClearVlinkWithPortIds.setter
    def FipClearVlinkWithPortIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FipClearVlinkWithPortIds'], value)

    @property
    def MaxPacketsPerSecond(self):
        """
        Returns
        -------
        - number: The maximum number of requests transmitted in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'])
    @MaxPacketsPerSecond.setter
    def MaxPacketsPerSecond(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxPacketsPerSecond'], value)

    @property
    def MaxRetries(self):
        """
        Returns
        -------
        - number: The number of request retries for each negotiation stage in case of response timeout or error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxRetries'])
    @MaxRetries.setter
    def MaxRetries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxRetries'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def RetryInterval(self):
        """
        Returns
        -------
        - number: The number of seconds to wait for a response before sending a new request.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RetryInterval'])
    @RetryInterval.setter
    def RetryInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RetryInterval'], value)

    def update(self, AcceptPartialConfig=None, DcbxTimeout=None, FipClearVlinkWithPortIds=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None):
        """Updates fcoeFwdGlobals resource on the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - FipClearVlinkWithPortIds (bool): Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AcceptPartialConfig=None, DcbxTimeout=None, FipClearVlinkWithPortIds=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None):
        """Adds a new fcoeFwdGlobals resource on the server and adds it to the container.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - FipClearVlinkWithPortIds (bool): Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.

        Returns
        -------
        - self: This instance with all currently retrieved fcoeFwdGlobals resources using find and the newly added fcoeFwdGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fcoeFwdGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, DcbxTimeout=None, FipClearVlinkWithPortIds=None, MaxPacketsPerSecond=None, MaxRetries=None, ObjectId=None, RetryInterval=None):
        """Finds and retrieves fcoeFwdGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcoeFwdGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcoeFwdGlobals resources from the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure. When is true the plugin reports success if at least one session is established. When is false the plugin reports success only if all sessions are established.
        - DcbxTimeout (number): The number of seconds to wait for DCBX to negotiate.
        - FipClearVlinkWithPortIds (bool): Determines whether the FIP Clear Virtual Link requests sent by FCF contain Vx_Port Identification descriptors or not.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - ObjectId (str): Unique identifier for this object
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.

        Returns
        -------
        - self: This instance with matching fcoeFwdGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcoeFwdGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcoeFwdGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
