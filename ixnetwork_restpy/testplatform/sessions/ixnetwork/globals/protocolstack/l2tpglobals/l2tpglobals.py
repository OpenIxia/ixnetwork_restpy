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


class L2tpGlobals(Base):
    """L2tp session data class
    The L2tpGlobals class encapsulates a list of l2tpGlobals resources that is be managed by the user.
    A list of resources can be retrieved from the server using the L2tpGlobals.find() method.
    The list can be managed by the user by using the L2tpGlobals.add() and L2tpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2tpGlobals'

    def __init__(self, parent):
        super(L2tpGlobals, self).__init__(parent)

    @property
    def EnforcePerPortRates(self):
        """If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.

        Returns:
            bool
        """
        return self._get_attribute('enforcePerPortRates')
    @EnforcePerPortRates.setter
    def EnforcePerPortRates(self, value):
        self._set_attribute('enforcePerPortRates', value)

    @property
    def MaxOutstandingReleases(self):
        """The maximum number of PPP session releases opened at any time by the PPP plugin.

        Returns:
            number
        """
        return self._get_attribute('maxOutstandingReleases')
    @MaxOutstandingReleases.setter
    def MaxOutstandingReleases(self, value):
        self._set_attribute('maxOutstandingReleases', value)

    @property
    def MaxOutstandingRequests(self):
        """Threshold at which the plugin begins throttling back the number of new clients being set up.

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
    def SetupRateInitial(self):
        """Initial setup rate

        Returns:
            number
        """
        return self._get_attribute('setupRateInitial')
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute('setupRateInitial', value)

    @property
    def TeardownRateInitial(self):
        """Initial teardown rate

        Returns:
            number
        """
        return self._get_attribute('teardownRateInitial')
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute('teardownRateInitial', value)

    def update(self, EnforcePerPortRates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Updates a child instance of l2tpGlobals on the server.

        Args:
            EnforcePerPortRates (bool): If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.
            MaxOutstandingReleases (number): The maximum number of PPP session releases opened at any time by the PPP plugin.
            MaxOutstandingRequests (number): Threshold at which the plugin begins throttling back the number of new clients being set up.
            SetupRateInitial (number): Initial setup rate
            TeardownRateInitial (number): Initial teardown rate

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, EnforcePerPortRates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Adds a new l2tpGlobals node on the server and retrieves it in this instance.

        Args:
            EnforcePerPortRates (bool): If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.
            MaxOutstandingReleases (number): The maximum number of PPP session releases opened at any time by the PPP plugin.
            MaxOutstandingRequests (number): Threshold at which the plugin begins throttling back the number of new clients being set up.
            SetupRateInitial (number): Initial setup rate
            TeardownRateInitial (number): Initial teardown rate

        Returns:
            self: This instance with all currently retrieved l2tpGlobals data using find and the newly added l2tpGlobals data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the l2tpGlobals data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnforcePerPortRates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Finds and retrieves l2tpGlobals data from the server.

        All named parameters support regex and can be used to selectively retrieve l2tpGlobals data from the server.
        By default the find method takes no parameters and will retrieve all l2tpGlobals data from the server.

        Args:
            EnforcePerPortRates (bool): If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.
            MaxOutstandingReleases (number): The maximum number of PPP session releases opened at any time by the PPP plugin.
            MaxOutstandingRequests (number): Threshold at which the plugin begins throttling back the number of new clients being set up.
            ObjectId (str): Unique identifier for this object
            SetupRateInitial (number): Initial setup rate
            TeardownRateInitial (number): Initial teardown rate

        Returns:
            self: This instance with matching l2tpGlobals data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of l2tpGlobals data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the l2tpGlobals data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
