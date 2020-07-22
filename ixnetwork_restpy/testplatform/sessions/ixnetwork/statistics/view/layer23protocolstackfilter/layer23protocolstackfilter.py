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


class Layer23ProtocolStackFilter(Base):
    """Filters associated with layer23ProtocolStack view.
    The Layer23ProtocolStackFilter class encapsulates a list of layer23ProtocolStackFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Layer23ProtocolStackFilter.find() method.
    The list can be managed by using the Layer23ProtocolStackFilter.add() and Layer23ProtocolStackFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'layer23ProtocolStackFilter'
    _SDM_ATT_MAP = {
        'DrilldownType': 'drilldownType',
        'NumberOfResults': 'numberOfResults',
        'ProtocolStackFilterId': 'protocolStackFilterId',
        'SortAscending': 'sortAscending',
        'SortingStatistic': 'sortingStatistic',
    }

    def __init__(self, parent):
        super(Layer23ProtocolStackFilter, self).__init__(parent)

    @property
    def DrilldownType(self):
        """
        Returns
        -------
        - str(perRange | perSession): Emulates perRange or perSession view based on the option seleted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DrilldownType'])
    @DrilldownType.setter
    def DrilldownType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DrilldownType'], value)

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
    def ProtocolStackFilterId(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolStackFilter]): Selected protocol stack filters from the availableProtocolStackFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolStackFilterId'])
    @ProtocolStackFilterId.setter
    def ProtocolStackFilterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolStackFilterId'], value)

    @property
    def SortAscending(self):
        """
        Returns
        -------
        - bool: Sets the display order of the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SortAscending'])
    @SortAscending.setter
    def SortAscending(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SortAscending'], value)

    @property
    def SortingStatistic(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/statistics/.../statistic): The reference statistic by which the data will be sorted in created SV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SortingStatistic'])
    @SortingStatistic.setter
    def SortingStatistic(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SortingStatistic'], value)

    def update(self, DrilldownType=None, NumberOfResults=None, ProtocolStackFilterId=None, SortAscending=None, SortingStatistic=None):
        """Updates layer23ProtocolStackFilter resource on the server.

        Args
        ----
        - DrilldownType (str(perRange | perSession)): Emulates perRange or perSession view based on the option seleted.
        - NumberOfResults (number): Number of traffic flows to be displayed.
        - ProtocolStackFilterId (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolStackFilter])): Selected protocol stack filters from the availableProtocolStackFilter list.
        - SortAscending (bool): Sets the display order of the view.
        - SortingStatistic (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../statistic)): The reference statistic by which the data will be sorted in created SV.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DrilldownType=None, NumberOfResults=None, ProtocolStackFilterId=None, SortAscending=None, SortingStatistic=None):
        """Adds a new layer23ProtocolStackFilter resource on the server and adds it to the container.

        Args
        ----
        - DrilldownType (str(perRange | perSession)): Emulates perRange or perSession view based on the option seleted.
        - NumberOfResults (number): Number of traffic flows to be displayed.
        - ProtocolStackFilterId (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolStackFilter])): Selected protocol stack filters from the availableProtocolStackFilter list.
        - SortAscending (bool): Sets the display order of the view.
        - SortingStatistic (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../statistic)): The reference statistic by which the data will be sorted in created SV.

        Returns
        -------
        - self: This instance with all currently retrieved layer23ProtocolStackFilter resources using find and the newly added layer23ProtocolStackFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained layer23ProtocolStackFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DrilldownType=None, NumberOfResults=None, ProtocolStackFilterId=None, SortAscending=None, SortingStatistic=None):
        """Finds and retrieves layer23ProtocolStackFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer23ProtocolStackFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer23ProtocolStackFilter resources from the server.

        Args
        ----
        - DrilldownType (str(perRange | perSession)): Emulates perRange or perSession view based on the option seleted.
        - NumberOfResults (number): Number of traffic flows to be displayed.
        - ProtocolStackFilterId (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolStackFilter])): Selected protocol stack filters from the availableProtocolStackFilter list.
        - SortAscending (bool): Sets the display order of the view.
        - SortingStatistic (str(None | /api/v1/sessions/1/ixnetwork/statistics/.../statistic)): The reference statistic by which the data will be sorted in created SV.

        Returns
        -------
        - self: This instance with matching layer23ProtocolStackFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer23ProtocolStackFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer23ProtocolStackFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
