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


class Connector(Base):
    """Connects scenario elements
    The Connector class encapsulates a list of connector resources that are managed by the user.
    A list of resources can be retrieved from the server using the Connector.find() method.
    The list can be managed by using the Connector.add() and Connector.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'connector'
    _SDM_ATT_MAP = {
        'ConnectedTo': 'connectedTo',
        'Count': 'count',
        'PropagateMultiplier': 'propagateMultiplier',
    }

    def __init__(self, parent):
        super(Connector, self).__init__(parent)

    @property
    def ConnectedTo(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/lag/.../*): Scenario element this connector is connecting to
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedTo'])
    @ConnectedTo.setter
    def ConnectedTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedTo'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def PropagateMultiplier(self):
        """
        Returns
        -------
        - bool: The Connector will propagate the multiplicity of destination back to the source and its parent NetworkElementSet
        """
        return self._get_attribute(self._SDM_ATT_MAP['PropagateMultiplier'])

    def update(self, ConnectedTo=None):
        """Updates connector resource on the server.

        Args
        ----
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/lag/.../*)): Scenario element this connector is connecting to

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedTo=None):
        """Adds a new connector resource on the server and adds it to the container.

        Args
        ----
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/lag/.../*)): Scenario element this connector is connecting to

        Returns
        -------
        - self: This instance with all currently retrieved connector resources using find and the newly added connector resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained connector resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedTo=None, Count=None, PropagateMultiplier=None):
        """Finds and retrieves connector resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve connector resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all connector resources from the server.

        Args
        ----
        - ConnectedTo (str(None | /api/v1/sessions/1/ixnetwork/lag/.../*)): Scenario element this connector is connecting to
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - PropagateMultiplier (bool): The Connector will propagate the multiplicity of destination back to the source and its parent NetworkElementSet

        Returns
        -------
        - self: This instance with matching connector resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of connector data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the connector resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
