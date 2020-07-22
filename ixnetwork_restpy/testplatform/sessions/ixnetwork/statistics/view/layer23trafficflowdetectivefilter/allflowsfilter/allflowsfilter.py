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


class AllFlowsFilter(Base):
    """All flows filter specification.
    The AllFlowsFilter class encapsulates a list of allFlowsFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the AllFlowsFilter.find() method.
    The list can be managed by using the AllFlowsFilter.add() and AllFlowsFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'allFlowsFilter'
    _SDM_ATT_MAP = {
        'NumberOfResults': 'numberOfResults',
        'SortByStatisticId': 'sortByStatisticId',
        'SortingCondition': 'sortingCondition',
    }

    def __init__(self, parent):
        super(AllFlowsFilter, self).__init__(parent)

    @property
    def NumberOfResults(self):
        """
        Returns
        -------
        - number: Number of traffic flows to be displayed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfResults'])
    @NumberOfResults.setter
    def NumberOfResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfResults'], value)

    @property
    def SortByStatisticId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter): The reference statistic by which the data will be sorted in created SV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SortByStatisticId'])
    @SortByStatisticId.setter
    def SortByStatisticId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SortByStatisticId'], value)

    @property
    def SortingCondition(self):
        """
        Returns
        -------
        - str(bestPerformers | worstPerformers): Sets the display order of the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SortingCondition'])
    @SortingCondition.setter
    def SortingCondition(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SortingCondition'], value)

    def update(self, NumberOfResults=None, SortByStatisticId=None, SortingCondition=None):
        """Updates allFlowsFilter resource on the server.

        Args
        ----
        - NumberOfResults (number): Number of traffic flows to be displayed.
        - SortByStatisticId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter)): The reference statistic by which the data will be sorted in created SV.
        - SortingCondition (str(bestPerformers | worstPerformers)): Sets the display order of the view.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, NumberOfResults=None, SortByStatisticId=None, SortingCondition=None):
        """Adds a new allFlowsFilter resource on the server and adds it to the container.

        Args
        ----
        - NumberOfResults (number): Number of traffic flows to be displayed.
        - SortByStatisticId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter)): The reference statistic by which the data will be sorted in created SV.
        - SortingCondition (str(bestPerformers | worstPerformers)): Sets the display order of the view.

        Returns
        -------
        - self: This instance with all currently retrieved allFlowsFilter resources using find and the newly added allFlowsFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained allFlowsFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, NumberOfResults=None, SortByStatisticId=None, SortingCondition=None):
        """Finds and retrieves allFlowsFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve allFlowsFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all allFlowsFilter resources from the server.

        Args
        ----
        - NumberOfResults (number): Number of traffic flows to be displayed.
        - SortByStatisticId (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../availableStatisticFilter)): The reference statistic by which the data will be sorted in created SV.
        - SortingCondition (str(bestPerformers | worstPerformers)): Sets the display order of the view.

        Returns
        -------
        - self: This instance with matching allFlowsFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of allFlowsFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the allFlowsFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
