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


class NetTopologyHubNSpoke(Base):
    """hub-n-spoke topology
    The NetTopologyHubNSpoke class encapsulates a list of netTopologyHubNSpoke resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetTopologyHubNSpoke.find() method.
    The list can be managed by using the NetTopologyHubNSpoke.add() and NetTopologyHubNSpoke.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'netTopologyHubNSpoke'
    _SDM_ATT_MAP = {
        'EnableLevel2Spokes': 'enableLevel2Spokes',
        'IncludeEntryPoint': 'includeEntryPoint',
        'LinkMultiplier': 'linkMultiplier',
        'NumberOfFirstLevelSpokes': 'numberOfFirstLevelSpokes',
        'NumberOfSecondLevelSpokes': 'numberOfSecondLevelSpokes',
    }

    def __init__(self, parent):
        super(NetTopologyHubNSpoke, self).__init__(parent)

    @property
    def EnableLevel2Spokes(self):
        """
        Returns
        -------
        - bool: Enable Level 2 Spokes
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLevel2Spokes'])
    @EnableLevel2Spokes.setter
    def EnableLevel2Spokes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLevel2Spokes'], value)

    @property
    def IncludeEntryPoint(self):
        """
        Returns
        -------
        - bool: if true, entry node belongs to ring topology, otherwise it is outside of ring
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeEntryPoint'])
    @IncludeEntryPoint.setter
    def IncludeEntryPoint(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeEntryPoint'], value)

    @property
    def LinkMultiplier(self):
        """
        Returns
        -------
        - number: number of links between two nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMultiplier'])
    @LinkMultiplier.setter
    def LinkMultiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkMultiplier'], value)

    @property
    def NumberOfFirstLevelSpokes(self):
        """
        Returns
        -------
        - number: Number of First Level Spokes
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfFirstLevelSpokes'])
    @NumberOfFirstLevelSpokes.setter
    def NumberOfFirstLevelSpokes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfFirstLevelSpokes'], value)

    @property
    def NumberOfSecondLevelSpokes(self):
        """
        Returns
        -------
        - number: Number of Second Level Spokes
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfSecondLevelSpokes'])
    @NumberOfSecondLevelSpokes.setter
    def NumberOfSecondLevelSpokes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfSecondLevelSpokes'], value)

    def update(self, EnableLevel2Spokes=None, IncludeEntryPoint=None, LinkMultiplier=None, NumberOfFirstLevelSpokes=None, NumberOfSecondLevelSpokes=None):
        """Updates netTopologyHubNSpoke resource on the server.

        Args
        ----
        - EnableLevel2Spokes (bool): Enable Level 2 Spokes
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - NumberOfFirstLevelSpokes (number): Number of First Level Spokes
        - NumberOfSecondLevelSpokes (number): Number of Second Level Spokes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableLevel2Spokes=None, IncludeEntryPoint=None, LinkMultiplier=None, NumberOfFirstLevelSpokes=None, NumberOfSecondLevelSpokes=None):
        """Adds a new netTopologyHubNSpoke resource on the server and adds it to the container.

        Args
        ----
        - EnableLevel2Spokes (bool): Enable Level 2 Spokes
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - NumberOfFirstLevelSpokes (number): Number of First Level Spokes
        - NumberOfSecondLevelSpokes (number): Number of Second Level Spokes

        Returns
        -------
        - self: This instance with all currently retrieved netTopologyHubNSpoke resources using find and the newly added netTopologyHubNSpoke resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained netTopologyHubNSpoke resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableLevel2Spokes=None, IncludeEntryPoint=None, LinkMultiplier=None, NumberOfFirstLevelSpokes=None, NumberOfSecondLevelSpokes=None):
        """Finds and retrieves netTopologyHubNSpoke resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netTopologyHubNSpoke resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netTopologyHubNSpoke resources from the server.

        Args
        ----
        - EnableLevel2Spokes (bool): Enable Level 2 Spokes
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - NumberOfFirstLevelSpokes (number): Number of First Level Spokes
        - NumberOfSecondLevelSpokes (number): Number of Second Level Spokes

        Returns
        -------
        - self: This instance with matching netTopologyHubNSpoke resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netTopologyHubNSpoke data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netTopologyHubNSpoke resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
