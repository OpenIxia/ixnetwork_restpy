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


class Layer23TrafficItemFilter(Base):
    """Filters associated with layer23TrafficItem view.
    The Layer23TrafficItemFilter class encapsulates a list of layer23TrafficItemFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Layer23TrafficItemFilter.find() method.
    The list can be managed by using the Layer23TrafficItemFilter.add() and Layer23TrafficItemFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'layer23TrafficItemFilter'
    _SDM_ATT_MAP = {
        'TrafficItemFilterIds': 'trafficItemFilterIds',
    }

    def __init__(self, parent):
        super(Layer23TrafficItemFilter, self).__init__(parent)

    @property
    def TrafficItemFilterIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter]): Selected traffic item filters from the availableTrafficItemFilter list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemFilterIds'])
    @TrafficItemFilterIds.setter
    def TrafficItemFilterIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficItemFilterIds'], value)

    def update(self, TrafficItemFilterIds=None):
        """Updates layer23TrafficItemFilter resource on the server.

        Args
        ----
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, TrafficItemFilterIds=None):
        """Adds a new layer23TrafficItemFilter resource on the server and adds it to the container.

        Args
        ----
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Returns
        -------
        - self: This instance with all currently retrieved layer23TrafficItemFilter resources using find and the newly added layer23TrafficItemFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained layer23TrafficItemFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, TrafficItemFilterIds=None):
        """Finds and retrieves layer23TrafficItemFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer23TrafficItemFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer23TrafficItemFilter resources from the server.

        Args
        ----
        - TrafficItemFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableTrafficItemFilter])): Selected traffic item filters from the availableTrafficItemFilter list.

        Returns
        -------
        - self: This instance with matching layer23TrafficItemFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer23TrafficItemFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer23TrafficItemFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
