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


class L2tpGlobals(Base):
    """L2tp session data class
    The L2tpGlobals class encapsulates a list of l2tpGlobals resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2tpGlobals.find() method.
    The list can be managed by using the L2tpGlobals.add() and L2tpGlobals.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2tpGlobals'
    _SDM_ATT_MAP = {
        'EnforcePerPortRates': 'enforcePerPortRates',
        'MaxOutstandingReleases': 'maxOutstandingReleases',
        'MaxOutstandingRequests': 'maxOutstandingRequests',
        'ObjectId': 'objectId',
        'SetupRateInitial': 'setupRateInitial',
        'TeardownRateInitial': 'teardownRateInitial',
    }

    def __init__(self, parent):
        super(L2tpGlobals, self).__init__(parent)

    @property
    def EnforcePerPortRates(self):
        """
        Returns
        -------
        - bool: If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnforcePerPortRates'])
    @EnforcePerPortRates.setter
    def EnforcePerPortRates(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnforcePerPortRates'], value)

    @property
    def MaxOutstandingReleases(self):
        """
        Returns
        -------
        - number: The maximum number of PPP session releases opened at any time by the PPP plugin.
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
        - number: Threshold at which the plugin begins throttling back the number of new clients being set up.
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
    def SetupRateInitial(self):
        """
        Returns
        -------
        - number: Initial setup rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetupRateInitial'])
    @SetupRateInitial.setter
    def SetupRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetupRateInitial'], value)

    @property
    def TeardownRateInitial(self):
        """
        Returns
        -------
        - number: Initial teardown rate
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeardownRateInitial'])
    @TeardownRateInitial.setter
    def TeardownRateInitial(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeardownRateInitial'], value)

    def update(self, EnforcePerPortRates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Updates l2tpGlobals resource on the server.

        Args
        ----
        - EnforcePerPortRates (bool): If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.
        - MaxOutstandingReleases (number): The maximum number of PPP session releases opened at any time by the PPP plugin.
        - MaxOutstandingRequests (number): Threshold at which the plugin begins throttling back the number of new clients being set up.
        - SetupRateInitial (number): Initial setup rate
        - TeardownRateInitial (number): Initial teardown rate

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnforcePerPortRates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Adds a new l2tpGlobals resource on the server and adds it to the container.

        Args
        ----
        - EnforcePerPortRates (bool): If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.
        - MaxOutstandingReleases (number): The maximum number of PPP session releases opened at any time by the PPP plugin.
        - MaxOutstandingRequests (number): Threshold at which the plugin begins throttling back the number of new clients being set up.
        - SetupRateInitial (number): Initial setup rate
        - TeardownRateInitial (number): Initial teardown rate

        Returns
        -------
        - self: This instance with all currently retrieved l2tpGlobals resources using find and the newly added l2tpGlobals resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained l2tpGlobals resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnforcePerPortRates=None, MaxOutstandingReleases=None, MaxOutstandingRequests=None, ObjectId=None, SetupRateInitial=None, TeardownRateInitial=None):
        """Finds and retrieves l2tpGlobals resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2tpGlobals resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2tpGlobals resources from the server.

        Args
        ----
        - EnforcePerPortRates (bool): If false, the setup rate at port group level gets divided by physical ports and then by range (default behavior). If true, we only configure a per-port setup rate that gets enforced, no matter how many ranges are running.
        - MaxOutstandingReleases (number): The maximum number of PPP session releases opened at any time by the PPP plugin.
        - MaxOutstandingRequests (number): Threshold at which the plugin begins throttling back the number of new clients being set up.
        - ObjectId (str): Unique identifier for this object
        - SetupRateInitial (number): Initial setup rate
        - TeardownRateInitial (number): Initial teardown rate

        Returns
        -------
        - self: This instance with matching l2tpGlobals resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l2tpGlobals data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2tpGlobals resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
