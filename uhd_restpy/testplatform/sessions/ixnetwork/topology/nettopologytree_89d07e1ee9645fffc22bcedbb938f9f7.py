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


class NetTopologyTree(Base):
    """tree topology
    The NetTopologyTree class encapsulates a list of netTopologyTree resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetTopologyTree.find() method.
    The list can be managed by using the NetTopologyTree.add() and NetTopologyTree.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'netTopologyTree'
    _SDM_ATT_MAP = {
        'IncludeEntryPoint': 'includeEntryPoint',
        'LinkMultiplier': 'linkMultiplier',
        'MaxChildPerNode': 'maxChildPerNode',
        'Nodes': 'nodes',
        'TreeDepth': 'treeDepth',
        'UseTreeDepth': 'useTreeDepth',
    }

    def __init__(self, parent):
        super(NetTopologyTree, self).__init__(parent)

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
    def MaxChildPerNode(self):
        """
        Returns
        -------
        - number: Maximum children per node
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxChildPerNode'])
    @MaxChildPerNode.setter
    def MaxChildPerNode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxChildPerNode'], value)

    @property
    def Nodes(self):
        """
        Returns
        -------
        - number: number of nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP['Nodes'])
    @Nodes.setter
    def Nodes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Nodes'], value)

    @property
    def TreeDepth(self):
        """
        Returns
        -------
        - number: Depth of the Tree, defined as length of path from root node to deepest node in the tree
        """
        return self._get_attribute(self._SDM_ATT_MAP['TreeDepth'])
    @TreeDepth.setter
    def TreeDepth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TreeDepth'], value)

    @property
    def UseTreeDepth(self):
        """
        Returns
        -------
        - bool: Use Tree Depth
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseTreeDepth'])
    @UseTreeDepth.setter
    def UseTreeDepth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseTreeDepth'], value)

    def update(self, IncludeEntryPoint=None, LinkMultiplier=None, MaxChildPerNode=None, Nodes=None, TreeDepth=None, UseTreeDepth=None):
        """Updates netTopologyTree resource on the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - MaxChildPerNode (number): Maximum children per node
        - Nodes (number): number of nodes
        - TreeDepth (number): Depth of the Tree, defined as length of path from root node to deepest node in the tree
        - UseTreeDepth (bool): Use Tree Depth

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeEntryPoint=None, LinkMultiplier=None, MaxChildPerNode=None, Nodes=None, TreeDepth=None, UseTreeDepth=None):
        """Adds a new netTopologyTree resource on the server and adds it to the container.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - MaxChildPerNode (number): Maximum children per node
        - Nodes (number): number of nodes
        - TreeDepth (number): Depth of the Tree, defined as length of path from root node to deepest node in the tree
        - UseTreeDepth (bool): Use Tree Depth

        Returns
        -------
        - self: This instance with all currently retrieved netTopologyTree resources using find and the newly added netTopologyTree resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained netTopologyTree resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeEntryPoint=None, LinkMultiplier=None, MaxChildPerNode=None, Nodes=None, TreeDepth=None, UseTreeDepth=None):
        """Finds and retrieves netTopologyTree resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netTopologyTree resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netTopologyTree resources from the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - MaxChildPerNode (number): Maximum children per node
        - Nodes (number): number of nodes
        - TreeDepth (number): Depth of the Tree, defined as length of path from root node to deepest node in the tree
        - UseTreeDepth (bool): Use Tree Depth

        Returns
        -------
        - self: This instance with matching netTopologyTree resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netTopologyTree data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netTopologyTree resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
