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


class ExternalLink(Base):
    """Links to NetTopologies with each other
    The ExternalLink class encapsulates a list of externalLink resources that are managed by the user.
    A list of resources can be retrieved from the server using the ExternalLink.find() method.
    The list can be managed by using the ExternalLink.add() and ExternalLink.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'externalLink'
    _SDM_ATT_MAP = {
        'FromNodeIndex': 'fromNodeIndex',
        'ToNetworkTopology': 'toNetworkTopology',
        'ToNodeIndex': 'toNodeIndex',
    }

    def __init__(self, parent):
        super(ExternalLink, self).__init__(parent)

    @property
    def FromNodeIndex(self):
        """
        Returns
        -------
        - number: Index of the originating node as defined in fromNetworkTopology
        """
        return self._get_attribute(self._SDM_ATT_MAP['FromNodeIndex'])
    @FromNodeIndex.setter
    def FromNodeIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FromNodeIndex'], value)

    @property
    def ToNetworkTopology(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/topology/.../*): Network Topology this link is pointing to
        """
        return self._get_attribute(self._SDM_ATT_MAP['ToNetworkTopology'])
    @ToNetworkTopology.setter
    def ToNetworkTopology(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ToNetworkTopology'], value)

    @property
    def ToNodeIndex(self):
        """
        Returns
        -------
        - number: Index of the target node as defined in toNetworkTopology
        """
        return self._get_attribute(self._SDM_ATT_MAP['ToNodeIndex'])
    @ToNodeIndex.setter
    def ToNodeIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ToNodeIndex'], value)

    def update(self, FromNodeIndex=None, ToNetworkTopology=None, ToNodeIndex=None):
        """Updates externalLink resource on the server.

        Args
        ----
        - FromNodeIndex (number): Index of the originating node as defined in fromNetworkTopology
        - ToNetworkTopology (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): Network Topology this link is pointing to
        - ToNodeIndex (number): Index of the target node as defined in toNetworkTopology

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, FromNodeIndex=None, ToNetworkTopology=None, ToNodeIndex=None):
        """Adds a new externalLink resource on the server and adds it to the container.

        Args
        ----
        - FromNodeIndex (number): Index of the originating node as defined in fromNetworkTopology
        - ToNetworkTopology (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): Network Topology this link is pointing to
        - ToNodeIndex (number): Index of the target node as defined in toNetworkTopology

        Returns
        -------
        - self: This instance with all currently retrieved externalLink resources using find and the newly added externalLink resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained externalLink resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, FromNodeIndex=None, ToNetworkTopology=None, ToNodeIndex=None):
        """Finds and retrieves externalLink resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve externalLink resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all externalLink resources from the server.

        Args
        ----
        - FromNodeIndex (number): Index of the originating node as defined in fromNetworkTopology
        - ToNetworkTopology (str(None | /api/v1/sessions/1/ixnetwork/topology/.../*)): Network Topology this link is pointing to
        - ToNodeIndex (number): Index of the target node as defined in toNetworkTopology

        Returns
        -------
        - self: This instance with matching externalLink resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of externalLink data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the externalLink resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
