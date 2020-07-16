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


class StatisticFilter(Base):
    """Statistic filter specification.
    The StatisticFilter class encapsulates a list of statisticFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the StatisticFilter.find() method.
    The list can be managed by using the StatisticFilter.add() and StatisticFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'statisticFilter'
    _SDM_ATT_MAP = {
        'Operator': 'operator',
        'StatisticFilterId': 'statisticFilterId',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(StatisticFilter, self).__init__(parent)

    @property
    def Operator(self):
        """
        Returns
        -------
        - str(isAnyOf | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isLike | isNotLike | isSmaller): The logical operation to be performed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Operator'])
    @Operator.setter
    def Operator(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Operator'], value)

    @property
    def StatisticFilterId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter): Selected statistic filters from the availableStatisticFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StatisticFilterId'])
    @StatisticFilterId.setter
    def StatisticFilterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StatisticFilterId'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: Value of statistic to be matched based on operator.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Operator=None, StatisticFilterId=None, Value=None):
        """Updates statisticFilter resource on the server.

        Args
        ----
        - Operator (str(isAnyOf | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isLike | isNotLike | isSmaller)): The logical operation to be performed.
        - StatisticFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter)): Selected statistic filters from the availableStatisticFilter list.
        - Value (str): Value of statistic to be matched based on operator.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Operator=None, StatisticFilterId=None, Value=None):
        """Adds a new statisticFilter resource on the server and adds it to the container.

        Args
        ----
        - Operator (str(isAnyOf | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isLike | isNotLike | isSmaller)): The logical operation to be performed.
        - StatisticFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter)): Selected statistic filters from the availableStatisticFilter list.
        - Value (str): Value of statistic to be matched based on operator.

        Returns
        -------
        - self: This instance with all currently retrieved statisticFilter resources using find and the newly added statisticFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained statisticFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Operator=None, StatisticFilterId=None, Value=None):
        """Finds and retrieves statisticFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve statisticFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all statisticFilter resources from the server.

        Args
        ----
        - Operator (str(isAnyOf | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isLike | isNotLike | isSmaller)): The logical operation to be performed.
        - StatisticFilterId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter)): Selected statistic filters from the availableStatisticFilter list.
        - Value (str): Value of statistic to be matched based on operator.

        Returns
        -------
        - self: This instance with matching statisticFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of statisticFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the statisticFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
