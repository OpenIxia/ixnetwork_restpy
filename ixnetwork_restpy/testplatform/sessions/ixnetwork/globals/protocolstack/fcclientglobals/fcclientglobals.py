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


class FcClientGlobals(Base):
    """StackManager FC Global Settings
    The FcClientGlobals class encapsulates a list of fcClientGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the FcClientGlobals.find() method.
    The list can be managed by using the FcClientGlobals.add() and FcClientGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fcClientGlobals'
    _SDM_ATT_MAP = {
        'AcceptPartialConfig': 'acceptPartialConfig',
        'MaxPacketsPerSecond': 'maxPacketsPerSecond',
        'MaxRetries': 'maxRetries',
        'ObjectId': 'objectId',
        'RetryInterval': 'retryInterval',
        'SetupRate': 'setupRate',
        'TeardownRate': 'teardownRate',
    }

    def __init__(self, parent):
        super(FcClientGlobals, self).__init__(parent)

    @property
    def AcceptPartialConfig(self):
        """
        Returns
        -------
        - bool: This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'])
    @AcceptPartialConfig.setter
    def AcceptPartialConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AcceptPartialConfig'], value)

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

    @property
    def SetupRate(self):
        """
        Returns
        -------
        - number: The number of interfaces scheduled to be configured in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRate'])
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRate'], value)

    @property
    def TeardownRate(self):
        """
        Returns
        -------
        - number: The number of interfaces scheduled to be deconfigured in each second.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRate'])
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRate'], value)

    def update(self, AcceptPartialConfig=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Updates fcClientGlobals resource on the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AcceptPartialConfig=None, MaxPacketsPerSecond=None, MaxRetries=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Adds a new fcClientGlobals resource on the server and adds it to the container.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Returns
        -------
        - self: This instance with all currently retrieved fcClientGlobals resources using find and the newly added fcClientGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fcClientGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcceptPartialConfig=None, MaxPacketsPerSecond=None, MaxRetries=None, ObjectId=None, RetryInterval=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves fcClientGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcClientGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcClientGlobals resources from the server.

        Args
        ----
        - AcceptPartialConfig (bool): This flag controls how the negotiation process reports success or failure.When is true the plugin reports success if at least one session is established.When is false the plugin reports success only if all sessions are established.
        - MaxPacketsPerSecond (number): The maximum number of requests transmitted in each second.
        - MaxRetries (number): The number of request retries for each negotiation stage in case of response timeout or error.
        - ObjectId (str): Unique identifier for this object
        - RetryInterval (number): The number of seconds to wait for a response before sending a new request.
        - SetupRate (number): The number of interfaces scheduled to be configured in each second.
        - TeardownRate (number): The number of interfaces scheduled to be deconfigured in each second.

        Returns
        -------
        - self: This instance with matching fcClientGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcClientGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcClientGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
