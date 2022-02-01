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


class FlowCondition(Base):
    """
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
    _SDM_ENUM_MAP = {
        'operator': ['isBetween', 'isDifferent', 'isEqual', 'isEqualOrGreater', 'isEqualOrSmaller', 'isGreater', 'isSmaller'],
    }

    def __init__(self, parent, list_op=False):
        super(FlowCondition, self).__init__(parent, list_op)

    @property
    def Operator(self):
        # type: () -> str
        """
        Returns
        -------
        - str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Operator'])
    @Operator.setter
    def Operator(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Operator'], value)

    @property
    def ShowFirstMatchingSet(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShowFirstMatchingSet'])
    @ShowFirstMatchingSet.setter
    def ShowFirstMatchingSet(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ShowFirstMatchingSet'], value)

    @property
    def TrackingFilterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackingFilterId'])
    @TrackingFilterId.setter
    def TrackingFilterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TrackingFilterId'], value)

    @property
    def Values(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Values'])
    @Values.setter
    def Values(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP['Values'], value)

    def update(self, Operator=None, ShowFirstMatchingSet=None, TrackingFilterId=None, Values=None):
        # type: (str, bool, str, List[int]) -> FlowCondition
        """Updates flowCondition resource on the server.

        Args
        ----
        - Operator (str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller)): 
        - ShowFirstMatchingSet (bool): 
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): 
        - Values (list(number)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Operator=None, ShowFirstMatchingSet=None, TrackingFilterId=None, Values=None):
        # type: (str, bool, str, List[int]) -> FlowCondition
        """Adds a new flowCondition resource on the server and adds it to the container.

        Args
        ----
        - Operator (str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller)): 
        - ShowFirstMatchingSet (bool): 
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): 
        - Values (list(number)): 

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
        # type: (str, bool, str, List[int]) -> FlowCondition
        """Finds and retrieves flowCondition resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowCondition resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowCondition resources from the server.

        Args
        ----
        - Operator (str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller)): 
        - ShowFirstMatchingSet (bool): 
        - TrackingFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrackingFilter)): 
        - Values (list(number)): 

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
