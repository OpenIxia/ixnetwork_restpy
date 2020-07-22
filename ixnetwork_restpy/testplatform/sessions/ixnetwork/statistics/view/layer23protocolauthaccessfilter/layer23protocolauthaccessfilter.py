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


class Layer23ProtocolAuthAccessFilter(Base):
    """Filters associated with layer23ProtocolAuthaccess view.
    The Layer23ProtocolAuthAccessFilter class encapsulates a list of layer23ProtocolAuthAccessFilter resources that are managed by the user.
    A list of resources can be retrieved from the server using the Layer23ProtocolAuthAccessFilter.find() method.
    The list can be managed by using the Layer23ProtocolAuthAccessFilter.add() and Layer23ProtocolAuthAccessFilter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'layer23ProtocolAuthAccessFilter'
    _SDM_ATT_MAP = {
        'PortFilterIds': 'portFilterIds',
        'ProtocolFilterIds': 'protocolFilterIds',
    }

    def __init__(self, parent):
        super(Layer23ProtocolAuthAccessFilter, self).__init__(parent)

    @property
    def PortFilterIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter]): Ports that have been filtered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortFilterIds'])
    @PortFilterIds.setter
    def PortFilterIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortFilterIds'], value)

    @property
    def ProtocolFilterIds(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter]): Protocols that have been filtered.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolFilterIds'])
    @ProtocolFilterIds.setter
    def ProtocolFilterIds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolFilterIds'], value)

    def update(self, PortFilterIds=None, ProtocolFilterIds=None):
        """Updates layer23ProtocolAuthAccessFilter resource on the server.

        Args
        ----
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Ports that have been filtered.
        - ProtocolFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter])): Protocols that have been filtered.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, PortFilterIds=None, ProtocolFilterIds=None):
        """Adds a new layer23ProtocolAuthAccessFilter resource on the server and adds it to the container.

        Args
        ----
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Ports that have been filtered.
        - ProtocolFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter])): Protocols that have been filtered.

        Returns
        -------
        - self: This instance with all currently retrieved layer23ProtocolAuthAccessFilter resources using find and the newly added layer23ProtocolAuthAccessFilter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained layer23ProtocolAuthAccessFilter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, PortFilterIds=None, ProtocolFilterIds=None):
        """Finds and retrieves layer23ProtocolAuthAccessFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve layer23ProtocolAuthAccessFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all layer23ProtocolAuthAccessFilter resources from the server.

        Args
        ----
        - PortFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availablePortFilter])): Ports that have been filtered.
        - ProtocolFilterIds (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../availableProtocolFilter])): Protocols that have been filtered.

        Returns
        -------
        - self: This instance with matching layer23ProtocolAuthAccessFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of layer23ProtocolAuthAccessFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the layer23ProtocolAuthAccessFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
