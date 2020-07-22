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


class FlowCondition(Base):
    """Flow condition for displaying egress/ingress statistics.
    The FlowCondition class encapsulates a list of flowCondition resources that are managed by the user.
    A list of resources can be retrieved from the server using the FlowCondition.find() method.
    The list can be managed by using the FlowCondition.add() and FlowCondition.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'flowCondition'
    _SDM_ATT_MAP = {
        'Operator': 'operator',
        'ShowFirstMatchingSet': 'showFirstMatchingSet',
        'TrackingFilterId': 'trackingFilterId',
        'Values': 'values',
    }

    def __init__(self, parent):
        super(FlowCondition, self).__init__(parent)

    @property
    def Operator(self):
        """
        Returns
        -------
        - str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller): The logical operation to be performed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Operator'])
    @Operator.setter
    def Operator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Operator'], value)

    @property
    def ShowFirstMatchingSet(self):
        """
        Returns
        -------
        - bool: If true, displays the first matching set.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowFirstMatchingSet'])
    @ShowFirstMatchingSet.setter
    def ShowFirstMatchingSet(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ShowFirstMatchingSet'], value)

    @property
    def TrackingFilterId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter): Selected tracking filters from the availableTrackingFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackingFilterId'])
    @TrackingFilterId.setter
    def TrackingFilterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackingFilterId'], value)

    @property
    def Values(self):
        """
        Returns
        -------
        - list(number): Value to be matched for the condition.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Values'])
    @Values.setter
    def Values(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Values'], value)

    def update(self, Operator=None, ShowFirstMatchingSet=None, TrackingFilterId=None, Values=None):
        """Updates flowCondition resource on the server.

        Args
        ----
        - Operator (str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller)): The logical operation to be performed.
        - ShowFirstMatchingSet (bool): If true, displays the first matching set.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.
        - Values (list(number)): Value to be matched for the condition.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Operator=None, ShowFirstMatchingSet=None, TrackingFilterId=None, Values=None):
        """Adds a new flowCondition resource on the server and adds it to the container.

        Args
        ----
        - Operator (str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller)): The logical operation to be performed.
        - ShowFirstMatchingSet (bool): If true, displays the first matching set.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.
        - Values (list(number)): Value to be matched for the condition.

        Returns
        -------
        - self: This instance with all currently retrieved flowCondition resources using find and the newly added flowCondition resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained flowCondition resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Operator=None, ShowFirstMatchingSet=None, TrackingFilterId=None, Values=None):
        """Finds and retrieves flowCondition resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowCondition resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowCondition resources from the server.

        Args
        ----
        - Operator (str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller)): The logical operation to be performed.
        - ShowFirstMatchingSet (bool): If true, displays the first matching set.
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.
        - Values (list(number)): Value to be matched for the condition.

        Returns
        -------
        - self: This instance with matching flowCondition resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of flowCondition data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowCondition resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
