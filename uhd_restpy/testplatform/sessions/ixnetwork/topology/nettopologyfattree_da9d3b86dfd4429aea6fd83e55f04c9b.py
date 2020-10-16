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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class NetTopologyFatTree(Base):
    """Fat Tree topology
    The NetTopologyFatTree class encapsulates a list of netTopologyFatTree resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetTopologyFatTree.find() method.
    The list can be managed by using the NetTopologyFatTree.add() and NetTopologyFatTree.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'netTopologyFatTree'
    _SDM_ATT_MAP = {
        'IncludeEntryPoint': 'includeEntryPoint',
        'LevelCount': 'levelCount',
        'LinkMultiplier': 'linkMultiplier',
    }

    def __init__(self, parent):
        super(NetTopologyFatTree, self).__init__(parent)

    @property
    def Level(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.level_2d6a41b0a919905f176ad907ea4fdab6.Level): An instance of the Level class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.level_2d6a41b0a919905f176ad907ea4fdab6 import Level
        return Level(self)

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
    def LevelCount(self):
        """
        Returns
        -------
        - number: Number of Levels
        """
        return self._get_attribute(self._SDM_ATT_MAP['LevelCount'])
    @LevelCount.setter
    def LevelCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LevelCount'], value)

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

    def update(self, IncludeEntryPoint=None, LevelCount=None, LinkMultiplier=None):
        """Updates netTopologyFatTree resource on the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LevelCount (number): Number of Levels
        - LinkMultiplier (number): number of links between two nodes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeEntryPoint=None, LevelCount=None, LinkMultiplier=None):
        """Adds a new netTopologyFatTree resource on the server and adds it to the container.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LevelCount (number): Number of Levels
        - LinkMultiplier (number): number of links between two nodes

        Returns
        -------
        - self: This instance with all currently retrieved netTopologyFatTree resources using find and the newly added netTopologyFatTree resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained netTopologyFatTree resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeEntryPoint=None, LevelCount=None, LinkMultiplier=None):
        """Finds and retrieves netTopologyFatTree resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netTopologyFatTree resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netTopologyFatTree resources from the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LevelCount (number): Number of Levels
        - LinkMultiplier (number): number of links between two nodes

        Returns
        -------
        - self: This instance with matching netTopologyFatTree resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netTopologyFatTree data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netTopologyFatTree resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
