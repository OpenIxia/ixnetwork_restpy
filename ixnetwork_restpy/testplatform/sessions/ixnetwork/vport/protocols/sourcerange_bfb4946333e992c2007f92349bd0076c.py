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


class SourceRange(Base):
    """This object holds a list of source IPv4 addresses that multicast traffic should be included from or excluded from.
    The SourceRange class encapsulates a list of sourceRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SourceRange.find() method.
    The list can be managed by using the SourceRange.add() and SourceRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'sourceRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'IpFrom': 'ipFrom',
    }

    def __init__(self, parent):
        super(SourceRange, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The number of IP addresses in the source range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def IpFrom(self):
        """
        Returns
        -------
        - str: The first IP address in the source range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IpFrom'])
    @IpFrom.setter
    def IpFrom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IpFrom'], value)

    def update(self, Count=None, IpFrom=None):
        """Updates sourceRange resource on the server.

        Args
        ----
        - Count (number): The number of IP addresses in the source range.
        - IpFrom (str): The first IP address in the source range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, IpFrom=None):
        """Adds a new sourceRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The number of IP addresses in the source range.
        - IpFrom (str): The first IP address in the source range.

        Returns
        -------
        - self: This instance with all currently retrieved sourceRange resources using find and the newly added sourceRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained sourceRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, IpFrom=None):
        """Finds and retrieves sourceRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve sourceRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all sourceRange resources from the server.

        Args
        ----
        - Count (number): The number of IP addresses in the source range.
        - IpFrom (str): The first IP address in the source range.

        Returns
        -------
        - self: This instance with matching sourceRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of sourceRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the sourceRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
