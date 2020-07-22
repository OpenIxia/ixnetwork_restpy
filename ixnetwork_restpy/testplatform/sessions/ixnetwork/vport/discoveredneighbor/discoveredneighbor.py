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


class DiscoveredNeighbor(Base):
    """This object holds the discoverd neighbor information for the virtual port.
    The DiscoveredNeighbor class encapsulates a list of discoveredNeighbor resources that are managed by the user.
    A list of resources can be retrieved from the server using the DiscoveredNeighbor.find() method.
    The list can be managed by using the DiscoveredNeighbor.add() and DiscoveredNeighbor.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'discoveredNeighbor'
    _SDM_ATT_MAP = {
        'IsRouter': 'isRouter',
        'LastUpdate': 'lastUpdate',
        'NeighborIp': 'neighborIp',
        'NeighborMac': 'neighborMac',
    }

    def __init__(self, parent):
        super(DiscoveredNeighbor, self).__init__(parent)

    @property
    def IsRouter(self):
        """
        Returns
        -------
        - str: (read only) Indicates if the neighbor is a router or not.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsRouter'])

    @property
    def LastUpdate(self):
        """
        Returns
        -------
        - str: (read only) Indicates when the last update for the neighbor happened.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastUpdate'])

    @property
    def NeighborIp(self):
        """
        Returns
        -------
        - str: (read only) The IP address of the neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NeighborIp'])

    @property
    def NeighborMac(self):
        """
        Returns
        -------
        - str: (read only) The MAC address of the neighbor.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NeighborMac'])

    def add(self):
        """Adds a new discoveredNeighbor resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved discoveredNeighbor resources using find and the newly added discoveredNeighbor resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained discoveredNeighbor resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IsRouter=None, LastUpdate=None, NeighborIp=None, NeighborMac=None):
        """Finds and retrieves discoveredNeighbor resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve discoveredNeighbor resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all discoveredNeighbor resources from the server.

        Args
        ----
        - IsRouter (str): (read only) Indicates if the neighbor is a router or not.
        - LastUpdate (str): (read only) Indicates when the last update for the neighbor happened.
        - NeighborIp (str): (read only) The IP address of the neighbor.
        - NeighborMac (str): (read only) The MAC address of the neighbor.

        Returns
        -------
        - self: This instance with matching discoveredNeighbor resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of discoveredNeighbor data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the discoveredNeighbor resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
